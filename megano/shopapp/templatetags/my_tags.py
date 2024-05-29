from django import template
from django.urls import reverse

from shopapp.models import Categories, Banner


register = template.Library()


@register.simple_tag
def reference_to_products():
    return Categories.objects.filter(parent__isnull=True)


@register.simple_tag
def reference_to_banners():
    return Banner.objects.all()
