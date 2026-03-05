from django.contrib import admin
from .models import Budget, BudgetCategory, Expense


class BudgetCategoryInline(admin.TabularInline):
    model = BudgetCategory
    extra = 1


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'total_income', 'created_at')
    list_filter = ('month', 'user')
    search_fields = ('user__username',)
    date_hierarchy = 'month'
    inlines = [BudgetCategoryInline]


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'description', 'created_at')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'description', 'category__name')
    date_hierarchy = 'date'
