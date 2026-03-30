from django import forms
from .models import SavingsEntry


class SavingsEntryForm(forms.ModelForm):
    class Meta:
        model = SavingsEntry
        fields = ('amount', 'date', 'note')
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. 150.00',
                'min': '0.01',
                'step': '0.01',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'note': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Optional: what was this for?',
            }),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise forms.ValidationError('Amount must be greater than zero.')
        return amount
