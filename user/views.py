from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from django.views import View
from .models import CustomUser
# Create your views here.

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Email: ", email)
            print("Password: ", password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('chatbot-view')  # Replace 'dashboard' with your desired redirect URL name
            else:
                messages.error(request, 'Invalid email or password.')
                return redirect('user-login')
        else:
            messages.error(request, 'Please correct the errors below.')
            return redirect('user-login')


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('user-login')  # Replace 'login' with your login URL name
        else:
            messages.error(request, 'Please correct the errors below.')
            redirect('user-register')

        return render(request, 'register.html', {'form': form})


class LogoutView(View):

    def post(self, request):
        logout(request)
        return redirect('user-login')  # Replace 'login' with your login URL name