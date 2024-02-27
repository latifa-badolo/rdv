from django.shortcuts import render, redirect
from django.contrib.auth import login as dj_login, authenticate, logout

from .models import User, ServiceProvider

from .forms import RegisterForm, EditServiceProviderForm

def login(request):

    context = {"errors": []}

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if not user:
            context["errors"].append("Cet utilisateur n'existe pas.")

        user = authenticate(request=request, username=username, password=password)

        if not user:
            context["errors"].append("Vos identifiant sont incorect")
        else:
            dj_login(request=request, user=user)
            return redirect("home")

    return render(request=request, template_name="account/login.html", context=context)


def register(request):

    context = {"errors": []}

    if request.method == "POST":

        register_form = RegisterForm(request.POST)
        service_provider_form = EditServiceProviderForm(request.POST)

        context["register_form"] = register_form
        context["service_provider_form"] = service_provider_form

        if register_form.is_valid():
            user = User.objects.filter(username=register_form.username).first()

            if user:
                context["errors"].append("Cet utilisateur existe déja")
                return render(request=request, template_name="account/register.html", context=context)
            
            if not register_form.password == register_form.confirm_password:
                context["errors"].append("Les mots de passe ne corresponde pas")
                return render(request=request, template_name="account/register.html", context=context)

            user = User.objects.create(username=register_form.username, password=register_form.password)
            user.phone_number = register_form.phone_number
            user.email = register_form.email
            user.phone_number = register_form.phone_number
            user.phone_number = register_form.phone_number
            user.phone_number = register_form.phone_number
            user.phone_number = register_form.phone_number
        

        register_form = register_form
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

    context["register_form"] = RegisterForm()
    context["service_provider_form"] = EditServiceProviderForm()

    return render(request=request, template_name="account/register.html", context=context)
