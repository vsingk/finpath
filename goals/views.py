import json
from decimal import Decimal
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from django.db import transaction
from django import forms

from .models import SavingsGoal, GoalContribution, MonthlyAllocation, GoalAllocation
from .forms import SavingsGoalForm, GoalContributionForm, BulkAllocationForm


@login_required
def goals_overview(request):
    """Main dashboard for all savings goals"""
    goals = SavingsGoal.objects.filter(user=request.user, is_active=True)
    
    # Calculate totals
    total_target = goals.aggregate(total=Sum('target_amount'))['total'] or Decimal('0.00')
    total_saved = goals.aggregate(total=Sum('current_amount'))['total'] or Decimal('0.00')
    total_monthly = goals.aggregate(total=Sum('monthly_contribution'))['total'] or Decimal('0.00')
    
    # Overall progress
    overall_progress = round((total_saved / total_target * 100), 1) if total_target > 0 else 0
    
    # Categorize goals
    retirement_goals = goals.filter(goal_type__in=['401k', 'roth_ira', 'traditional_ira'])
    purchase_goals = goals.exclude(goal_type__in=['401k', 'roth_ira', 'traditional_ira'])
    
    # Recent contributions
    recent_contributions = GoalContribution.objects.filter(
        goal__user=request.user
    )[:10]
    
    # Get current month allocation if exists
    today = timezone.now().date()
    current_month = today.replace(day=1)
    current_allocation = MonthlyAllocation.objects.filter(
        user=request.user,
        month=current_month
    ).first()
    
    context = {
        'goals': goals,
        'retirement_goals': retirement_goals,
        'purchase_goals': purchase_goals,
        'total_target': total_target,
        'total_saved': total_saved,
        'total_monthly': total_monthly,
        'overall_progress': overall_progress,
        'recent_contributions': recent_contributions,
        'current_allocation': current_allocation,
    }
    return render(request, 'goals/overview.html', context)


@login_required
def create_goal(request):
    """Create a new savings goal"""
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, f'Goal "{goal.name}" created successfully!')
            return redirect('goals_overview')
    else:
        form = SavingsGoalForm()
    
    return render(request, 'goals/create_goal.html', {'form': form})


@login_required
def edit_goal(request, pk):
    """Edit an existing goal"""
    goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, f'Goal "{goal.name}" updated successfully!')
            return redirect('goals_overview')
    else:
        form = SavingsGoalForm(instance=goal)
    
    return render(request, 'goals/edit_goal.html', {'form': form, 'goal': goal})


@login_required
def delete_goal(request, pk):
    """Delete a goal"""
    goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    
    if request.method == 'POST':
        goal_name = goal.name
        goal.delete()
        messages.success(request, f'Goal "{goal_name}" deleted.')
    
    return redirect('goals_overview')


@login_required
def goal_detail(request, pk):
    """Detailed view of a single goal with contribution history"""
    goal = get_object_or_404(SavingsGoal, pk=pk, user=request.user)
    contributions = goal.contributions.all()
    
    # Handle contribution form
    if request.method == 'POST':
        form = GoalContributionForm(request.POST)
        if form.is_valid():
            contribution = form.save(commit=False)
            # Update goal's current amount
            goal.current_amount += contribution.amount
            goal.save()
            contribution.save()
            messages.success(request, f'Added ${contribution.amount} to {goal.name}!')
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalContributionForm(initial={'goal': goal, 'date': timezone.now().date()})
        form.fields['goal'].widget = forms.HiddenInput()
    
    # Build chart data for progress over time
    chart_data = _build_goal_progress_chart(contributions, goal.target_amount)
    
    context = {
        'goal': goal,
        'contributions': contributions,
        'form': form,
        'chart_data': json.dumps(chart_data),
    }
    return render(request, 'goals/detail.html', context)


@login_required
def delete_contribution(request, pk):
    """
    Delete a contribution.
    Note: Signals automatically handle:
    - Updating goal's current amount
    - Deleting corresponding budget expense
    """
    contribution = get_object_or_404(GoalContribution, pk=pk, goal__user=request.user)
    goal = contribution.goal
    
    if request.method == 'POST':
        contribution.delete()
        messages.success(
            request,
            f'Contribution of ${contribution.amount} deleted. Goal balance and budget updated automatically.'
        )
    
    return redirect('goal_detail', pk=goal.pk)


@login_required
@transaction.atomic
def allocate_budget(request):
    """
    Allocate remaining budget from current month to savings goals.
    Creates actual budget expenses and goal contributions.
    
    Features:
    - Creates category based on goal type (401k, Emergency Fund, etc.)
    - Prevents duplicate allocations for same goal in same month
    """
    from budgets.models import Budget, BudgetCategory, Expense
    
    today = timezone.now().date()
    current_month = today.replace(day=1)
    
    # Get current month's budget
    budget = Budget.objects.filter(user=request.user, month=current_month).first()
    
    if not budget:
        messages.warning(request, 'Please create a budget for this month first.')
        return redirect('budget_setup')
    
    # Calculate remaining budget
    expenses = Expense.objects.filter(user=request.user, category__budget=budget)
    total_spent = expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    remaining = budget.total_income - total_spent
    
    if remaining <= 0:
        messages.info(request, 'No remaining budget to allocate this month.')
        return redirect('goals_overview')
    
    # Get or create monthly allocation
    allocation, created = MonthlyAllocation.objects.get_or_create(
        user=request.user,
        month=current_month,
        defaults={'remaining_budget': remaining}
    )
    
    # Update remaining budget if it changed
    if not created and allocation.remaining_budget != remaining:
        allocation.remaining_budget = remaining
        allocation.save()
    
    # Get active goals
    goals = SavingsGoal.objects.filter(user=request.user, is_active=True)
    
    # Check which goals already have allocations this month
    already_allocated_goal_ids = set(
        allocation.goal_allocations.values_list('goal_id', flat=True)
    )
    
    if request.method == 'POST':
        form = BulkAllocationForm(
            request.POST,
            goals=goals,
            remaining_budget=remaining
        )
        
        if form.is_valid():
            # Validate: Check for duplicate allocations
            errors = []
            for field_name, amount in form.cleaned_data.items():
                if field_name.startswith('goal_') and amount and amount > 0:
                    goal_id = int(field_name.split('_')[1])
                    if goal_id in already_allocated_goal_ids:
                        goal = goals.get(id=goal_id)
                        errors.append(
                            f'"{goal.name}" already has an allocation for {current_month.strftime("%B %Y")}. '
                            f'Delete the existing allocation first if you want to change it.'
                        )
            
            if errors:
                for error in errors:
                    messages.error(request, error)
                # Return form with data
                context = {
                    'form': form,
                    'budget': budget,
                    'remaining': remaining,
                    'allocation': allocation,
                    'goals': goals,
                    'current_month': current_month,
                    'already_allocated_goal_ids': already_allocated_goal_ids,
                }
                return render(request, 'goals/allocate.html', context)
            
            # Create allocations and transactions
            total_allocated = Decimal('0')
            contributions_created = 0
            categories_created = []
            
            for field_name, amount in form.cleaned_data.items():
                if field_name.startswith('goal_') and amount and amount > 0:
                    goal_id = int(field_name.split('_')[1])
                    goal = goals.get(id=goal_id)
                    
                    # Determine category name based on goal type
                    category_name = _get_category_name_for_goal_type(goal.goal_type)
                    
                    # Get or create category for this goal type
                    category, cat_created = BudgetCategory.objects.get_or_create(
                        budget=budget,
                        name=category_name,
                        defaults={'allocated': Decimal('0.00')}
                    )
                    
                    if cat_created:
                        categories_created.append(category_name)
                    
                    # 1. Record the allocation (planning record)
                    GoalAllocation.objects.create(
                        monthly_allocation=allocation,
                        goal=goal,
                        amount=amount
                    )
                    
                    # 2. Create budget expense (actual expense in budget)
                    Expense.objects.create(
                        user=request.user,
                        category=category,
                        amount=amount,
                        date=today,
                        description=f'Allocation to {goal.name}',
                    )
                    
                    # 3. Create goal contribution (increase goal balance)
                    GoalContribution.objects.create(
                        goal=goal,
                        amount=amount,
                        date=today,
                        note=f'Monthly allocation for {current_month.strftime("%B %Y")}'
                    )
                    
                    # 4. Update goal's current amount
                    goal.current_amount += amount
                    goal.save()
                    
                    total_allocated += amount
                    contributions_created += 1
            
            # Build success message
            success_msg = f'Successfully allocated ${total_allocated:.2f} to {contributions_created} goal(s)!'
            if categories_created:
                success_msg += f' Created budget categories: {", ".join(categories_created)}.'
            
            messages.success(request, success_msg)
            return redirect('goals_overview')
    else:
        form = BulkAllocationForm(goals=goals, remaining_budget=remaining)
    
    context = {
        'form': form,
        'budget': budget,
        'remaining': remaining,
        'allocation': allocation,
        'goals': goals,
        'current_month': current_month,
        'already_allocated_goal_ids': already_allocated_goal_ids,
    }
    return render(request, 'goals/allocate.html', context)


@login_required
def allocation_history(request):
    """View history of monthly allocations"""
    allocations = MonthlyAllocation.objects.filter(user=request.user)
    
    context = {
        'allocations': allocations,
    }
    return render(request, 'goals/allocation_history.html', context)


def _get_category_name_for_goal_type(goal_type):
    """
    Map goal types to budget category names.
    Groups similar goals into logical categories.
    """
    category_mapping = {
        # Retirement accounts
        '401k': '401(k) Contributions',
        'roth_ira': 'Roth IRA',
        'traditional_ira': 'Traditional IRA',
        
        # Emergency & savings
        'emergency': 'Emergency Fund',
        'custom': 'Savings Goals',
        
        # Major purchases
        'house': 'House Down Payment',
        'car': 'Car Purchase',
        'purchase': 'Major Purchases',
        
        # Specific goals
        'vacation': 'Vacation/Travel',
        'education': 'Education',
        'debt': 'Debt Payoff',
    }
    
    return category_mapping.get(goal_type, 'Savings Goals')


def _build_goal_progress_chart(contributions, target_amount):
    """Build chart data showing progress toward goal over time"""
    if not contributions:
        return {'labels': [], 'data': [], 'target': float(target_amount)}
    
    ordered = contributions.order_by('date', 'created_at')
    labels = []
    data = []
    running_total = Decimal('0.00')
    
    for contrib in ordered:
        running_total += contrib.amount
        date_str = contrib.date.isoformat()
        
        if labels and labels[-1] == date_str:
            # Multiple contributions same day - update last point
            data[-1] = float(running_total)
        else:
            labels.append(date_str)
            data.append(float(running_total))
    
    return {
        'labels': labels,
        'data': data,
        'target': float(target_amount),
    }
