import json
from decimal import Decimal
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
@login_required
def projected_Budget(request, n, i, a):
    #print(a)
    targetDate = parse_date(a)
    today = timezone.now().month
    savingsGoal = Decimal(n)
    
    year, month = map(int, a.split("-"))
    target_date = date(year, month, 1)

    today = timezone.localdate().replace(day=1)

    if (target_date < today):
        return JsonResponse({'error': 'Target date must be in the future.'}, status = 400)
    
    differenceInDays = (target_date - today).days
    difasMonths = math.ceil(differenceInDays / 30)
    print("differeence in months: ", difasMonths)

    interestRate = (Decimal(i) / Decimal(100)) / Decimal(12)
    print("IR: ", interestRate)
    print("goal savings: ", n)
    denomenator = ((1+interestRate) ** difasMonths) - 1
    division = interestRate / denomenator
    proj = savingsGoal * division
    labels = []
    monthlyRepresentation = []
    for month in range(difasMonths):
        labels.append(month + 1)
        if month == 0:
            monthlyRepresentation.append(round(Decimal(proj),2))
        else:
            lastMonth = monthlyRepresentation[month-1]
            monthlyRepresentation.append(round((Decimal(lastMonth) * (1 + interestRate)) + Decimal(proj), 2))
            
        
        
    #print(labels )
    #print(monthlyRepresentation)
    return JsonResponse({'projected amount per month': math.ceil(proj), 'labels': labels, 'data':monthlyRepresentation})

@login_required
def monthlyDepositProject(request, monthlyDeposit, goalAmount, interestRate):
    print(interestRate, type(interestRate))
    monthly = Decimal(monthlyDeposit)
    goal = Decimal(goalAmount)
    ir = ((Decimal(interestRate))/Decimal(100)) / Decimal(12)
    print("monthly: ", monthly, "goal: ", goal, "IR: ", ir)
    Axi = ((goal * ir) / monthly) + 1
    b = math.log(Axi, 10)
    c = math.log(1+ir, 10)
    months = b/c
    print("months: ", months)

    labels = []
    monthlyProjection = []
    for month in range(math.ceil(months)):
        labels.append(month + 1)
        if month == 0:
            monthlyProjection.append(round(monthly,2))
        else:
            lastMonth = monthlyProjection[month-1]
            monthlyProjection.append(round((Decimal(lastMonth) * (1 + ir) + Decimal(monthly)), 2))

    return JsonResponse({'months': math.ceil(months), 'labels': labels, 'data': monthlyProjection})

    

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
            return redirect('budget_overview')
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
        'current_month': current_month,
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

