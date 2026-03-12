from django.contrib import admin
from .models import SavingsEntry


@admin.register(SavingsEntry)
class SavingsEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'note', 'created_at')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'note')
    date_hierarchy = 'date'
