from django import forms
from decimal import Decimal
from .models import SavingsGoal, GoalContribution, GoalAllocation


class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ('name', 'goal_type', 'target_amount', 'current_amount', 
                 'monthly_contribution', 'target_date', 'priority', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., Emergency Fund, New Laptop, Vacation to Hawaii'
            }),
            'goal_type': forms.Select(attrs={'class': 'form-input'}),
            'target_amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., 10000.00',
                'min': '0.01',
                'step': '0.01',
            }),
            'current_amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'min': '0',
                'step': '0.01',
            }),
            'monthly_contribution': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., 500.00',
                'min': '0',
                'step': '0.01',
            }),
            'target_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'priority': forms.Select(attrs={'class': 'form-input'}),
            'notes': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'Any additional notes about this goal...'
            }),
        }

    def clean_target_amount(self):
        amount = self.cleaned_data.get('target_amount')
        if amount is not None and amount <= 0:
            raise forms.ValidationError('Target amount must be greater than zero.')
        return amount

    def clean_current_amount(self):
        amount = self.cleaned_data.get('current_amount')
        if amount is not None and amount < 0:
            raise forms.ValidationError('Current amount cannot be negative.')
        return amount

    def clean(self):
        cleaned_data = super().clean()
        current = cleaned_data.get('current_amount') or Decimal('0')
        target = cleaned_data.get('target_amount')
        
        if current and target and current > target:
            raise forms.ValidationError('Current amount cannot exceed target amount.')
        
        return cleaned_data


class GoalContributionForm(forms.ModelForm):
    class Meta:
        model = GoalContribution
        fields = ('goal', 'amount', 'date', 'note')
        widgets = {
            'goal': forms.Select(attrs={'class': 'form-input'}),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g., 150.00',
                'min': '0.01',
                'step': '0.01',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'note': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Optional: note about this contribution'
            }),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise forms.ValidationError('Amount must be greater than zero.')
        return amount


class GoalAllocationForm(forms.ModelForm):
    class Meta:
        model = GoalAllocation
        fields = ('goal', 'amount', 'notes')
        widgets = {
            'goal': forms.Select(attrs={'class': 'form-input'}),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'min': '0',
                'step': '0.01',
            }),
            'notes': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Optional notes'
            }),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount < 0:
            raise forms.ValidationError('Amount cannot be negative.')
        return amount


class BulkAllocationForm(forms.Form):
    def __init__(self, *args, goals=None, remaining_budget=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if goals:
            for goal in goals:
                field_name = f'goal_{goal.id}'
                
                initial_value = Decimal('0.00')
                
                if goal.monthly_contribution and goal.monthly_contribution > 0:
                    initial_value = goal.monthly_contribution
                
                if remaining_budget is not None and remaining_budget > 0:
                    if initial_value > remaining_budget:
                        initial_value = remaining_budget
                
                self.fields[field_name] = forms.DecimalField(
                    label=goal.name,
                    required=False,
                    min_value=Decimal('0'),
                    max_value=remaining_budget if remaining_budget and remaining_budget > 0 else Decimal('999999.99'),
                    decimal_places=2,
                    initial=initial_value,
                    widget=forms.NumberInput(attrs={
                        'class': 'form-input',
                        'placeholder': '0.00',
                        'step': '0.01',
                        'min': '0',
                        'value': str(initial_value),
                    })
                )
        
        self.remaining_budget = remaining_budget

    def clean(self):
        cleaned_data = super().clean()
        total_allocated = Decimal('0')
        
        for field_name, value in cleaned_data.items():
            if field_name.startswith('goal_') and value:
                total_allocated += value
        
        if self.remaining_budget and total_allocated > self.remaining_budget:
            raise forms.ValidationError(
                f'Total allocation (${total_allocated}) exceeds remaining budget (${self.remaining_budget}).'
            )
        
        return cleaned_data
