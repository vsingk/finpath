# Generated migration file for goals app

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingsGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('goal_type', models.CharField(choices=[('purchase', 'Major Purchase'), ('emergency', 'Emergency Fund'), ('401k', '401(k) Retirement'), ('roth_ira', 'Roth IRA'), ('traditional_ira', 'Traditional IRA'), ('vacation', 'Vacation/Travel'), ('education', 'Education'), ('house', 'House Down Payment'), ('car', 'Car Purchase'), ('debt', 'Debt Payoff'), ('custom', 'Custom Goal')], default='custom', max_length=20)),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('current_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('monthly_contribution', models.DecimalField(decimal_places=2, default=0, help_text='How much you plan to contribute each month', max_digits=12)),
                ('target_date', models.DateField(blank=True, help_text='When do you want to reach this goal?', null=True)),
                ('priority', models.IntegerField(choices=[(1, 'High Priority'), (2, 'Medium Priority'), (3, 'Low Priority')], default=2)),
                ('is_active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savings_goals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'savings goals',
                'ordering': ['priority', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MonthlyAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField(help_text='First day of the allocation month')),
                ('remaining_budget', models.DecimalField(decimal_places=2, help_text='Remaining after expenses', max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_allocations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'monthly allocations',
                'ordering': ['-month'],
                'unique_together': {('user', 'month')},
            },
        ),
        migrations.CreateModel(
            name='GoalContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateField()),
                ('note', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='goals.savingsgoal')),
            ],
            options={
                'verbose_name_plural': 'goal contributions',
                'ordering': ['-date', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GoalAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('notes', models.TextField(blank=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='goals.savingsgoal')),
                ('monthly_allocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_allocations', to='goals.monthlyallocation')),
            ],
            options={
                'verbose_name_plural': 'goal allocations',
                'unique_together': {('monthly_allocation', 'goal')},
            },
        ),
    ]
