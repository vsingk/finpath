from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email address'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Confirm password'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Password'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('annual_income', 'occupation', 'employment_status', 'date_of_birth', 'financial_goal')
        widgets = {
            'annual_income': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 50000'}),
            'occupation': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Software Intern'}),
            'employment_status': forms.Select(attrs={'class': 'form-input'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'financial_goal': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'What are your financial goals?'}),
        }
