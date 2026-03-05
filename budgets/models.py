from django.db import models
from django.contrib.auth.models import User


DEFAULT_CATEGORIES = [
    'Housing',
    'Food & Groceries',
    'Transportation',
    'Utilities',
    'Entertainment',
    'Health & Fitness',
    'Shopping',
    'Savings & Investments',
]


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    month = models.DateField(help_text='First day of the budget month')
    total_income = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-month']
        verbose_name_plural = 'budgets'
        unique_together = ['user', 'month']

    def __str__(self):
        return f"{self.user.username} - {self.month.strftime('%B %Y')}"


class BudgetCategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    allocated = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'budget categories'

    def __str__(self):
        return f"{self.name} (${self.allocated})"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'expenses'

    def __str__(self):
        return f"${self.amount} - {self.category.name} on {self.date} ({self.user.username})"
