from django import forms


class PaymentForm(forms.Form):
    card_number = forms.CharField(
        label='Номер карты',
        max_length=9,
        widget=forms.TextInput(attrs={'class': 'form-input Payment-bill', 'placeholder': '9999 9999', 'data-mask': '9999 9999', 'data-validate': 'require pay'}))