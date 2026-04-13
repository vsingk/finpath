from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from .forms import SignupForm, LoginForm, UserProfileForm
from budgets.models import Budget, Expense
from savings.models import SavingsEntry
from goals.models import SavingsGoal


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Complete your profile below.')
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Welcome back!')
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})


@login_required
def dashboard_view(request):
    profile = request.user.profile
    profile.update_streak()

    milestones = profile.get_milestones()
    achieved_count = sum(1 for m in milestones if m['achieved'])

    today = timezone.now().date()
    current_month = today.replace(day=1)

    # Financial snapshot
    budget = Budget.objects.filter(user=request.user, month=current_month).first()
    snapshot_budget = None
    if budget:
        total_spent = Expense.objects.filter(
            user=request.user, category__budget=budget
        ).aggregate(total=Sum('amount'))['total'] or 0
        income_f = float(budget.total_income)
        spent_f = float(total_spent)
        pct = min(round(spent_f / income_f * 100, 1), 100) if income_f > 0 else 0
        snapshot_budget = {
            'income': budget.total_income,
            'spent': total_spent,
            'percent': pct,
            'over': spent_f > income_f,
        }

    total_savings = SavingsEntry.objects.filter(
        user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    active_goals = list(SavingsGoal.objects.filter(user=request.user, is_active=True))
    goals_count = len(active_goals)
    avg_goal_progress = round(
        sum(g.progress_percent() for g in active_goals) / goals_count, 1
    ) if goals_count else 0

    # First-run checklist
    profile_complete = profile.profile_completion_percent() == 100
    has_budget = budget is not None
    has_savings = SavingsEntry.objects.filter(user=request.user).exists()
    has_goal = goals_count > 0
    show_checklist = not (profile_complete and has_budget and has_savings and has_goal)

    completion_percent = profile.profile_completion_percent()
    context = {
        'profile': profile,
        'completion_percent': completion_percent,
        'milestones': milestones,
        'achieved_count': achieved_count,
        'streak': profile.login_streak,
        'snapshot_budget': snapshot_budget,
        'total_savings': total_savings,
        'goals_count': goals_count,
        'avg_goal_progress': avg_goal_progress,
        'show_checklist': show_checklist,
        'profile_complete': profile_complete,
        'has_budget': has_budget,
        'has_savings': has_savings,
        'has_goal': has_goal,
        'placeholder_features': [
            {
                'icon': '\U0001f4ca',
                'title': 'Budget Tracking',
                'description': 'Set up your monthly budget and track spending by category.',
                'status': 'Active',
                'url': 'budget_overview',
            },
            {
                'icon': '\U0001f3af',
                'title': 'Savings Progress',
                'description': 'Track your savings and project your growth over time.',
                'status': 'Active',
                'url': 'savings_progress',
            },
            {
                'icon': '\U0001f3c6',
                'title': 'Savings Goals',
                'description': 'Set goals for purchases, retirement accounts, and emergency funds.',
                'status': 'Active',
                'url': 'goals_overview',
            },
            {
                'icon': '\U0001f4d6',
                'title': 'Learning Center',
                'description': 'Bite-sized lessons on taxes, credit, and investing.',
                'status': 'Active',
                'url': 'learn',
            },
        ],
    }
    return render(request, 'accounts/dashboard.html', context)
