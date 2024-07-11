from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth

# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, this email is already taken. Please select another one'},
                                status=409)
        return JsonResponse({'email_valid': True})


class NameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        surname = data['surname']
        if not name.isalpha() or not surname.isalpha():
            return JsonResponse({'name_error': 'Name should only contain alphabetic characters'}, status=400)
        if User.objects.filter(username=f"{name} {surname}").exists():
            return JsonResponse({'name_error': 'Sorry, this account already exists. Please just sign in again'}, status=409)
        return JsonResponse({'name_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        # GET USER DATA
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context = {
            'fieldValues': request.POST,
        }

        # Vérifiez que tous les champs sont présents
        if not name or not surname or not email or not password:
            messages.error(request, 'Please fill all fields')
            return render(request, 'authentication/register.html', context)

        if len(password) < 6:
            messages.error(request, 'Password too short')
            return render(request, 'authentication/register.html', context)

        username = f"{name}{surname}".lower()

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, first_name=name, last_name=surname, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                messages.success(request, 'Congratulations! You have successfully registered')
                return render(request, 'authentication/register.html')
        else:
            messages.error(request, 'User with this name already exists')
        return render(request, 'authentication/register.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                # Vérifie si le mot de passe correspond
                if user.check_password(password):
                    if not user.is_active:
                        messages.error(request, 'Account is not active, please contact your administrator')
                        return render(request, 'authentication/login.html')
                    # Connecte l'utilisateur
                    auth.login(request, user)
                    messages.success(request, f'Welcome {user.last_name}, you are now logged in')
                    return redirect('signalization')
                else:
                    messages.error(request, 'Invalid credentials, try again')
            except User.DoesNotExist:
                messages.error(request, 'Invalid credentials, try again')
        else:
            messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')