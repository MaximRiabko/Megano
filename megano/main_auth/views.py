from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth import logout

class Login(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    next_page='index.html'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        errors = form.errors
        return JsonResponse({'errors': errors}, status=400)


def logout_view(request):
    logout(request)
    return redirect('/')


def register(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            redirect('index.html')
        return render(request, "register.html")

    elif request.method == 'POST':
        name, email, password = request.POST['name'], request.POST['login'], request.POST['pass']
        if name or email or password:
            exist = User.objects.filter(email=email).exists()
            if exist:
                return render(request, "login.html")
            user = User.objects.create_user(username=email, first_name=name, email=email, password=password)
            user.save()
            user = authenticate(request=request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('index.html')
        return render(request, "register.html")



class Reset_Password(PasswordResetView):
    template_name = 'e-mail.html'

class Reset_Password_Done(PasswordResetDoneView):
    template_name='e-mail-done.html'

class Reset_Password_Confirm(PasswordResetConfirmView):
    template_name = 'e-mail-confirm.html'