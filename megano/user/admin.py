from django.contrib import admin

from .models import Role
from shopapp.models import Profile

admin.site.register(Role)
admin.site.register(Profile)
