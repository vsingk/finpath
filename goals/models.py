from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class SavingsGoal(models.Model):
    GOAL_TYPE_CHOICES = [
        ('purchase', 'Major Purchase'),
        ('emergency', 'Emergency Fund'),
        ('401k', '401(k) Retirement'),
        ('roth_ira', 'Roth IRA'),
        ('traditional_ira', 'Traditional IRA'),
        ('vacation', 'Vacation/Travel'),
        ('education', 'Education'),
        ('house', 'House Down Payment'),
        ('car', 'Car Purchase'),
        ('debt', 'Debt Payoff'),
        ('custom', 'Custom Goal'),
    ]

    PRIORITY_CHOICES = [
        (1, 'High Priority'),
        (2, 'Medium Priority'),
        (3, 'Low Priority'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_goals')
    name = models.CharField(max_length=200)
    goal_type = models.CharField(max_length=20, choices=GOAL_TYPE_CHOICES, default='custom')
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    monthly_contribution = models.DecimalField(max_digits=12, decimal_places=2, default=0, 
                                              help_text='How much you plan to contribute each month')
    target_date = models.DateField(null=True, blank=True, help_text='When do you want to reach this goal?')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['priority', '-created_at']
        verbose_name_plural = 'savings goals'

    def __str__(self):
        return f"{self.name} - ${self.current_amount} / ${self.target_amount}"

    def progress_percent(self):
        if self.target_amount <= 0:
            return 0
        percent = (self.current_amount / self.target_amount) * 100
        return min(round(percent, 1), 100)

    def remaining_amount(self):
        return max(self.target_amount - self.current_amount, Decimal('0.00'))

    def months_to_goal(self):
        if self.monthly_contribution <= 0:
            return None
        remaining = self.remaining_amount()
        if remaining <= 0:
            return 0
        return int((remaining / self.monthly_contribution)) + 1

    def is_retirement_account(self):
        return self.goal_type in ['401k', 'roth_ira', 'traditional_ira']

    def get_annual_limit(self):
        limits = {
            '401k': 23000,
            'roth_ira': 7000,
            'traditional_ira': 7000,
        }
        return limits.get(self.goal_type, None)


class GoalContribution(models.Model):
    goal = models.ForeignKey(SavingsGoal, on_delete=models.CASCADE, related_name='contributions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'goal contributions'

    def __str__(self):
        return f"${self.amount} to {self.goal.name} on {self.date}"


class MonthlyAllocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monthly_allocations')
    month = models.DateField(help_text='First day of the allocation month')
    remaining_budget = models.DecimalField(max_digits=12, decimal_places=2, 
                                          help_text='Remaining after expenses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-month']
        unique_together = ['user', 'month']
        verbose_name_plural = 'monthly allocations'

    def __str__(self):
        return f"{self.user.username} - {self.month.strftime('%B %Y')} - ${self.remaining_budget}"

    def get_allocations(self):
        return self.goal_allocations.all()

    def total_allocated(self):
        return self.goal_allocations.aggregate(
            total=models.Sum('amount')
        )['total'] or Decimal('0.00')

    def unallocated_amount(self):
        return self.remaining_budget - self.total_allocated()


class GoalAllocation(models.Model):
    monthly_allocation = models.ForeignKey(MonthlyAllocation, on_delete=models.CASCADE, 
                                          related_name='goal_allocations')
    goal = models.ForeignKey(SavingsGoal, on_delete=models.CASCADE, related_name='allocations')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'goal allocations'
        unique_together = ['monthly_allocation', 'goal']

    def __str__(self):
        return f"${self.amount} to {self.goal.name}"
