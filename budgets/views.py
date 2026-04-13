import json
from decimal import Decimal, InvalidOperation
import math
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime as Date
from django.utils.dateparse import parse_date
from .models import Budget, BudgetCategory, Expense, DEFAULT_CATEGORIES
from .forms import BudgetForm, BudgetCategoryFormSet, ExpenseForm
from django.http import JsonResponse, HttpResponse
from datetime import date
from django.urls import reverse
@login_required
def projected_Budget(request, n, i, a):
    try:
        savingsGoal = Decimal(n)
        year, month = map(int, a.split("-"))
        target_date = date(year, month, 1)
    except (ValueError, InvalidOperation):
        return JsonResponse({'error': 'Invalid input values.'}, status=400)

    today = timezone.localdate().replace(day=1)

    if target_date <= today:
        return JsonResponse({'error': 'Target date must be in the future.'}, status=400)

    differenceInDays = (target_date - today).days
    difasMonths = math.ceil(differenceInDays / 30)

    try:
        interestRate = (Decimal(i) / Decimal(100)) / Decimal(12)
        if interestRate == 0:
            proj = savingsGoal / Decimal(difasMonths)
            denominator = Decimal(difasMonths)
        else:
            denominator = ((1 + interestRate) ** difasMonths) - 1
            division = interestRate / denominator
            proj = savingsGoal * division
    except (InvalidOperation, ZeroDivisionError):
        return JsonResponse({'error': 'Invalid interest rate.'}, status=400)

    labels = []
    monthlyRepresentation = []
    running = float(proj)
    ir = float(interestRate)
    for m in range(difasMonths):
        labels.append(m + 1)
        if m == 0:
            monthlyRepresentation.append(round(running, 2))
        else:
            running = monthlyRepresentation[m - 1] * (1 + ir) + float(proj)
            monthlyRepresentation.append(round(running, 2))

    return JsonResponse({'projected amount per month': math.ceil(float(proj)), 'labels': labels, 'data': monthlyRepresentation})

@login_required
def monthlyDepositProject(request, monthlyDeposit, goalAmount, interestRate):
    try:
        monthly = float(monthlyDeposit)
        goal = float(goalAmount)
        ir_annual = float(interestRate)
    except (ValueError, InvalidOperation):
        return JsonResponse({'error': 'Invalid input values.'}, status=400)

    if monthly <= 0 or goal <= 0:
        return JsonResponse({'error': 'Monthly deposit and goal must be positive.'}, status=400)

    ir = (ir_annual / 100) / 12

    try:
        if ir == 0:
            months = goal / monthly
        else:
            Axi = ((goal * ir) / monthly) + 1
            if Axi <= 0:
                return JsonResponse({'error': 'Goal is not reachable with these inputs.'}, status=400)
            b = math.log(Axi, 10)
            c = math.log(1 + ir, 10)
            if c == 0:
                return JsonResponse({'error': 'Invalid interest rate.'}, status=400)
            months = b / c
    except (ValueError, ZeroDivisionError):
        return JsonResponse({'error': 'Invalid inputs for calculation.'}, status=400)

    labels = []
    monthlyProjection = []
    running = 0.0
    for m in range(math.ceil(months)):
        labels.append(m + 1)
        running = running * (1 + ir) + monthly
        monthlyProjection.append(round(running, 2))

    return JsonResponse({'months': math.ceil(months), 'labels': labels, 'data': monthlyProjection})

    

@login_required
def budget_overview(request):
    today = timezone.now().date()
    default_month = today.replace(day=1)

    month_param = request.GET.get('month') or request.POST.get('_month')
    current_month = default_month
    if month_param:
        try:
            year, month_num = map(int, month_param.split('-'))
            parsed = date(year, month_num, 1)
            if parsed <= default_month:
                current_month = parsed
        except (ValueError, AttributeError):
            pass

    month_str = current_month.strftime('%Y-%m')
    is_current_month = current_month == default_month

    if current_month.month == 1:
        prev_month = date(current_month.year - 1, 12, 1)
    else:
        prev_month = date(current_month.year, current_month.month - 1, 1)

    if current_month.month == 12:
        next_month = date(current_month.year + 1, 1, 1)
    else:
        next_month = date(current_month.year, current_month.month + 1, 1)

    nav_context = {
        'current_month': current_month,
        'month_str': month_str,
        'prev_month_str': prev_month.strftime('%Y-%m'),
        'next_month_str': next_month.strftime('%Y-%m'),
        'is_current_month': is_current_month,
    }

    budget = Budget.objects.filter(user=request.user, month=current_month).first()

    if not budget:
        return render(request, 'budgets/overview.html', {
            'has_budget': False,
            **nav_context,
        })

    categories = budget.categories.annotate(total_spent=Sum('expenses__amount'))
    expenses = Expense.objects.filter(user=request.user, category__budget=budget)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.fields['category'].queryset = categories
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, f'Expense of ${expense.amount} added to {expense.category.name}!')
            redirect_url = reverse('budget_overview')
            if not is_current_month:
                redirect_url += f'?month={month_str}'
            return redirect(redirect_url)
    else:
        form = ExpenseForm()
        form.fields['category'].queryset = categories

    total_income = budget.total_income
    total_allocated = categories.aggregate(total=Sum('allocated'))['total'] or Decimal('0.00')
    total_spent = expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    remaining = total_income - total_spent
    unallocated = total_income - total_allocated
    monthly_income = total_income / 12
    category_data = _build_category_data(categories)
    sankey_data = _build_sankey_data(budget, categories, total_income)
    recent_expenses = expenses[:20]

    context = {
        'has_budget': True,
        'budget': budget,
        'form': form,
        'total_income': total_income,
        'monthly_income': monthly_income,
        'total_allocated': total_allocated,
        'total_spent': total_spent,
        'remaining': remaining,
        'unallocated': unallocated,
        'category_data': category_data,
        'sankey_json': json.dumps(sankey_data),
        'recent_expenses': recent_expenses,
        **nav_context,
    }
    return render(request, 'budgets/overview.html', context)


@login_required
def budget_setup(request):
    today = timezone.now().date()
    current_month = today.replace(day=1)

    budget = Budget.objects.filter(user=request.user, month=current_month).first()
    is_new = budget is None

    if request.method == 'POST':
        budget_form = BudgetForm(request.POST, instance=budget)
        if budget_form.is_valid():
            budget_obj = budget_form.save(commit=False)
            budget_obj.user = request.user
            budget_obj.save()

            formset = BudgetCategoryFormSet(request.POST, instance=budget_obj)
            if formset.is_valid():  
                formset.save()
                messages.success(request, f'Budget for {budget_obj.month.strftime("%B %Y")} saved!')
                return redirect('budget_overview')
        else:
            if budget:
                formset = BudgetCategoryFormSet(request.POST, instance=budget)
            else:
                formset = BudgetCategoryFormSet(request.POST)
    else:
        budget_form = BudgetForm(instance=budget)
        if is_new:
            formset = BudgetCategoryFormSet(
                instance=Budget(),
                initial=[{'name': cat, 'allocated': Decimal('0.00')} for cat in DEFAULT_CATEGORIES],
            )
            formset.extra = len(DEFAULT_CATEGORIES)
        else:
            formset = BudgetCategoryFormSet(instance=budget)

    context = {
        'budget_form': budget_form,
        'formset': formset,
        'is_new': is_new,
        'current_month': current_month,
    }
    return render(request, 'budgets/setup.html', context)


@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted.')
    return redirect('budget_overview')


def _build_category_data(categories):
    result = []
    for cat in categories:
        if cat.allocated <= 0:
            continue
        spent = cat.total_spent or Decimal('0.00')
        percent = min(float(spent / cat.allocated * 100), 100) if cat.allocated > 0 else 0
        result.append({
            'name': cat.name,
            'allocated': cat.allocated,
            'spent': spent,
            'remaining': cat.allocated - spent,
            'percent': round(percent, 1),
            'over_budget': spent > cat.allocated,
        })
    return result


def _build_sankey_data(budget, categories, total_income):
    """Build Sankey data showing only how money spent is distributed across categories."""
    rows = []

    for cat in categories:
        spent = cat.total_spent or Decimal('0.00')
        if spent > 0:
            rows.append(['Total Spent', cat.name, float(spent)])

    return rows

