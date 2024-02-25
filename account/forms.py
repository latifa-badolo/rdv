from django import forms
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm, UserCreationForm as BaseUserCreationForm

from .models import User, ServiceProvider, Category

class RegisterForm(BaseUserCreationForm):

    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput()
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput()
    )

    avatar = forms.FileField(
        required=True,
        widget=forms.FileField()
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "phone_number","email", "avatar", "first_name", "last_name"]


class EditServiceProviderForm(forms.ModelForm):

    work = forms.CharField(
        required=True,
        label="Métier",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    town = forms.ChoiceField(
        choices=ServiceProvider.TOWNS,
        required=True,  
        label="Ville",
        widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"})
    )

    level_of_education = forms.ChoiceField(
        choices=ServiceProvider.LEVEL_OF_EDUCATION,
        required=True,
        label="Niveau d'éducation",
        widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        label="Categorie de métier",
        widget=forms.Select(attrs={"class": "form-select", "style": "width: 200px"})
    )

    description = forms.CharField(
        required=True,
        label="Description",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "6"})
    )

    class Meta:
        model = ServiceProvider
        fields = ["work", "category", "town", "level_of_education", "description"]