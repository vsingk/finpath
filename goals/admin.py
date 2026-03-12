from django.contrib import admin
from .models import SavingsGoal, GoalContribution, MonthlyAllocation, GoalAllocation


class GoalContributionInline(admin.TabularInline):
    model = GoalContribution
    extra = 0


@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'goal_type', 'target_amount', 'current_amount', 
                   'progress_percent', 'monthly_contribution', 'priority', 'is_active')
    list_filter = ('goal_type', 'priority', 'is_active', 'user')
    search_fields = ('user__username', 'name', 'notes')
    inlines = [GoalContributionInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(GoalContribution)
class GoalContributionAdmin(admin.ModelAdmin):
    list_display = ('goal', 'amount', 'date', 'note', 'created_at')
    list_filter = ('date', 'goal__user')
    search_fields = ('goal__name', 'note')
    date_hierarchy = 'date'


class GoalAllocationInline(admin.TabularInline):
    model = GoalAllocation
    extra = 0


@admin.register(MonthlyAllocation)
class MonthlyAllocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'remaining_budget', 'total_allocated', 'unallocated_amount')
    list_filter = ('month', 'user')
    search_fields = ('user__username',)
    date_hierarchy = 'month'
    inlines = [GoalAllocationInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(GoalAllocation)
class GoalAllocationAdmin(admin.ModelAdmin):
    list_display = ('monthly_allocation', 'goal', 'amount', 'notes')
    list_filter = ('monthly_allocation__month', 'goal__user')
    search_fields = ('goal__name', 'notes')
