from django import forms
from django.contrib.auth.models import User
from shopapp.models import Profile

class UserRegistrationForm(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    username = forms.CharField(label='Full name', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    phone = forms.CharField(label='Phone number', widget=forms.TextInput)
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        else:
            return cd['password2']


class PaymentForm(forms.Form):
    card_number = forms.CharField(
        label="Номер карты",
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "class": "form-input Payment-bill",
                "placeholder": "9999 9999",
                "data-mask": "9999 9999",
                "data-validate": "require pay",
            }
        ),
    )
