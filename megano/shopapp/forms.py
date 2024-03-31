from .models import Review
from django.forms import ModelForm, Textarea


class ReviewForm(ModelForm):
    """Модель ReviewForm предоставляет форму для отзывов
    на странице с товарами"""
    class Meta:
        model = Review
        fields = [
            'content',
        ]

        widgets = {
            'content': Textarea(attrs={
                'class': 'form-textarea',
                'id': 'reviwed',
                'name': 'reviwed',
                'placeholder': 'Отзыв',
            })
        }