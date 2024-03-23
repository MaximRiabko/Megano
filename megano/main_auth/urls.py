from django.contrib import admin
from django.urls import path
from .views import register, Reset_Password, Login, logout_view, Reset_Password_Done, Reset_Password_Confirm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('recovery/e-mail', Reset_Password.as_view(), name='recovery_password'),
    path('recovery/e-mail/done', Reset_Password_Done.as_view(), name='password_reset_done'),
    path('recovery/e-mail/confirm/<uidb64>/<token>/', Reset_Password_Confirm.as_view(), name='password_reset_confirm'),
]