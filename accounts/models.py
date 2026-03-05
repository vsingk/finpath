from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class UserProfile(models.Model):
    EMPLOYMENT_CHOICES = [
        ('student', 'Student'),
        ('intern', 'Intern'),
        ('employed_full', 'Employed Full-Time'),
        ('employed_part', 'Employed Part-Time'),
        ('freelance', 'Freelancer / Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    annual_income = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    occupation = models.CharField(max_length=120, blank=True)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    financial_goal = models.TextField(blank=True)
    login_streak = models.PositiveIntegerField(default=0)
    last_visit_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    def update_streak(self):
        today = timezone.now().date()
        if self.last_visit_date is None:
            self.login_streak = 1
            self.last_visit_date = today
            self.save(update_fields=['login_streak', 'last_visit_date'])
            return
        delta = (today - self.last_visit_date).days
        if delta == 0:
            return
        elif delta == 1:
            self.login_streak += 1
        else:
            self.login_streak = 1
        self.last_visit_date = today
        self.save(update_fields=['login_streak', 'last_visit_date'])

    def profile_completion_percent(self):
        fields = ['annual_income', 'occupation', 'employment_status', 'date_of_birth', 'financial_goal']
        filled = sum(1 for f in fields if getattr(self, f))
        return int((filled / len(fields)) * 100)

    def get_milestones(self):
        return [
            {
                'name': 'Profile Created',
                'achieved': True,
                'icon': '\u2705',
                'description': 'You created your FinPath account!',
            },
            {
                'name': 'Profile Completed',
                'achieved': self.profile_completion_percent() == 100,
                'icon': '\U0001f4cb',
                'description': 'Fill in all your financial details.',
            },
            {
                'name': '3-Day Streak',
                'achieved': self.login_streak >= 3,
                'icon': '\U0001f525',
                'description': 'Visit FinPath 3 days in a row.',
            },
            {
                'name': '7-Day Streak',
                'achieved': self.login_streak >= 7,
                'icon': '\u2b50',
                'description': 'Visit FinPath 7 days in a row.',
            },
            {
                'name': 'Goal Setter',
                'achieved': bool(self.financial_goal),
                'icon': '\U0001f3af',
                'description': 'Write down your financial goals.',
            },
        ]


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()
