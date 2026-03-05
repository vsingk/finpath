from django import forms
from django.forms import inlineformset_factory
from .models import Budget, BudgetCategory, Expense


class BudgetForm(forms.ModelForm):
    month = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-input',
            'type': 'date',
        }),
        help_text='Pick any date in the month you want to budget for.',
    )

    class Meta:
        model = Budget
        fields = ('month', 'total_income')
        widgets = {
            'total_income': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 4000.00',
                'min': '0.01',
                'step': '0.01',
            }),
        }

    def clean_month(self):
        month_val = self.cleaned_data.get('month')
        if month_val:
            return month_val.replace(day=1)
        return month_val

    def clean_total_income(self):
        income = self.cleaned_data.get('total_income')
        if income is not None and income <= 0:
            raise forms.ValidationError('Income must be greater than zero.')
        return income


class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ('name', 'allocated')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Category name',
            }),
            'allocated': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00',
                'min': '0',
                'step': '0.01',
            }),
        }


BudgetCategoryFormSet = inlineformset_factory(
    Budget,
    BudgetCategory,
    form=BudgetCategoryForm,
    extra=0,
    can_delete=True,
)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('category', 'amount', 'date', 'description')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 45.00',
                'min': '0.01',
                'step': '0.01',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Optional: what was this for?',
            }),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise forms.ValidationError('Amount must be greater than zero.')
        return amount
