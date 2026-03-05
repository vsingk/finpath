from django.db import models
from django.contrib.auth.models import User


class SavingsEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_entries')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name_plural = 'savings entries'

    def __str__(self):
        return f"${self.amount} on {self.date} ({self.user.username})"
