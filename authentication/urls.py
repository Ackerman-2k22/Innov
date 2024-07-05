from .views import RegistrationView
from django.urls import path
from .views import NameValidationView, EmailValidationView, LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('validate-username', csrf_exempt(NameValidationView.as_view()),
         name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),
         name='validate-email')
]
