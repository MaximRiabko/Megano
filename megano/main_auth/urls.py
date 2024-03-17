from django.contrib import admin
from django.urls import path
from .views import register, RecoveryPassword, Login, logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('recovery/e-mail', RecoveryPassword.as_view(), name='recovery_password')
]