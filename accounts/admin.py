from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'occupation', 'employment_status', 'annual_income', 'login_streak', 'last_visit_date')
    list_filter = ('employment_status',)
    search_fields = ('user__username', 'user__email', 'occupation')
