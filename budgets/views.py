import json
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone

from .models import Budget, BudgetCategory, Expense, DEFAULT_CATEGORIES
from .forms import BudgetForm, BudgetCategoryFormSet, ExpenseForm


@login_required
def budget_overview(request):
    today = timezone.now().date()
    current_month = today.replace(day=1)

    budget = Budget.objects.filter(user=request.user, month=current_month).first()

    if not budget:
        return render(request, 'budgets/overview.html', {
            'has_budget': False,
            'current_month': current_month,
        })

    categories = budget.categories.all()
    expenses = Expense.objects.filter(user=request.user, category__budget=budget)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.fields['category'].queryset = categories
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, f'Expense of ${expense.amount} added to {expense.category.name}!')
            return redirect('budget_overview')
    else:
        form = ExpenseForm()
        form.fields['category'].queryset = categories

    total_income = budget.total_income
    total_allocated = categories.aggregate(total=Sum('allocated'))['total'] or Decimal('0.00')
    total_spent = expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
    remaining = total_income - total_spent
    unallocated = total_income - total_allocated

    category_data = _build_category_data(categories)
    sankey_data = _build_sankey_data(budget, categories, total_income)
    recent_expenses = expenses[:20]

    context = {
        'has_budget': True,
        'budget': budget,
        'current_month': current_month,
        'form': form,
        'total_income': total_income,
        'total_allocated': total_allocated,
        'total_spent': total_spent,
        'remaining': remaining,
        'unallocated': unallocated,
        'category_data': category_data,
        'sankey_json': json.dumps(sankey_data),
        'recent_expenses': recent_expenses,
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
        spent = cat.expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
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
        spent = cat.expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        if spent > 0:
            rows.append(['Total Spent', cat.name, float(spent)])

    return rows
