from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, LoginForm, UserProfileForm


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

    context = {
        'profile': profile,
        'completion_percent': profile.profile_completion_percent(),
        'milestones': milestones,
        'achieved_count': achieved_count,
        'streak': profile.login_streak,
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
                'status': 'Coming Soon',
            },
        ],
    }
    return render(request, 'accounts/dashboard.html', context)
