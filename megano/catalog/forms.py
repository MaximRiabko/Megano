from .models import Review
from django.forms import ModelForm, Textarea


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'description',
        ]

        widgets = {
            'description': Textarea(attrs={
                'class': 'form-textarea',
                'id': 'reviwed',
                'name': 'reviwed',
                'placeholder': 'Отзыв',
            })
        }