from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .forms import RegistrationForm
from django.contrib import messages

from django.http import JsonResponse

User = get_user_model()

class LoginView(View):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        page_title = _('Login Form')
        return render(request, self.template_name, {'form': form, 'page_title': page_title})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('books_list')
        return render(request, self.template_name, {'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('login')

class RegistrationView(View):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, f'Обліковий запис користувача "{user.username}" успішно створено. Увійдіть зараз!')
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    
class CheckUserExistsView(View):
    def get(self, request, *args, **kwargs):
        username_exists = False
        user_email_exists = False

        username = request.GET.get('username')
        email = request.GET.get('email')

        if username:
            username_exists = User.objects.filter(username=username).exists()

        if email:
            user_email_exists = User.objects.filter(email=email).exists()

        data = {
            'user_check_errors': username_exists or user_email_exists,
            'email_exists': user_email_exists,
            'username_exists': username_exists
        }

        return JsonResponse(data)