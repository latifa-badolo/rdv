from django import forms
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm, UserCreationForm as BaseUserCreationForm

from .models import User, Service

class AuthenticationForm(BaseAuthenticationForm):

    class Meta:
        model = User
