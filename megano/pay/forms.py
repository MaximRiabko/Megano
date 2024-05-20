from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from shopapp.models import Profile


class UserRegistrationForm(forms.Form):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    username = forms.CharField(label="Full name", widget=forms.TextInput)
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    phone = forms.CharField(
        label="Phone number",
        empty_value="",
        widget=forms.TextInput,
    )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match")
        else:
            return cd["password2"]


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


class DeliveryForm(forms.Form):
    delivery_options = [
        ("ordinary", "Обычная доставка"),
        ("express", "Экспресс доставка"),
    ]

    delivery = forms.ChoiceField(
        label="Способ доставки", choices=delivery_options, widget=forms.RadioSelect()
    )
    city = forms.CharField(
        label="Город", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    address = forms.CharField(
        label="Адрес", widget=forms.Textarea(attrs={"class": "form-textarea"})
    )


class PaymentTypeForm(forms.Form):
    payment_options = [
        ("online", "Онлайн картой"),
        ("someone", "Онлайн со случайного чужого счета"),
    ]

    type = forms.ChoiceField(
        label="Способ доставки", choices=payment_options, widget=forms.RadioSelect()
    )
