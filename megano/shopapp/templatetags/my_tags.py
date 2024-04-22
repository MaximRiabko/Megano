from django import template
from django.urls import reverse

from shopapp.models import Categories

register = template.Library()


@register.simple_tag
def reference_to_products():
    return Categories.objects.filter(parent__isnull=True)
