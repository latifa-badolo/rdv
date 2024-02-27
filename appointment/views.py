from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import EditAvailabilityFormSet, CreateAppointmentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

from django.utils.dateparse import parse_time

from .models import Calendar, Appointment, Availability

from account.models import ServiceProvider, Category
from account.forms import EditServiceProviderForm

User = get_user_model()

"""
    - send notification
    - research service provider +
    - edit calendar availabilities +
    - login and signin +
"""

def see_calendar(request, service_provider_id, *args, **kwargs):

    context = {}

    user = request.user

    # calendar = Calendar.objects.select_related("availabilities").get(pk=service_provider_id)

    # availabilities = calendar.availabilities.all()

    # appointment = calendar.appointments.all()


    # for avalability in availabilities:
    #     start = (6, 15)
    #     end = (7, 00)


    # context = {
    #     "calendar": calendar,
    #     "availabilities": availabilities,
    # }

    return render(request=request, template_name="base.html", context=context)


def search_service_provider(request):

    context = {}

    service_providers = ServiceProvider.objects.all() 

    category = request.GET.get("category")
    search = request.GET.get("search")
    start_time = request.GET.get("start_time")
    end_time = request.GET.get("end_time")

    if category :
        service_providers = service_providers.filter(category__value=category)
        context["category"] = category

    if start_time :
        service_providers = service_providers.filter(calendar__appointments__start_time__lte=parse_time(start_time))
        context["start_time"] = start_time


    if end_time :
        service_providers = service_providers.filter(calendar__appointments__end_time__gte=parse_time(end_time))
        context["end_time"] = end_time


    if search :
        service_providers = service_providers.filter(
            Q(description__icontains=search) |
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search) |
            Q(town__icontains=search) |
            Q(work__icontains=search)
        )
        context["search"] = search

    context["categories"] = Category.objects.all()


    context["service_providers"] = service_providers

    return render(request=request, template_name="appointment/search_service_provider.html", context=context)

def service_provider_detail(request, service_provider_id):
    context = {}

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        appointment = CreateAppointmentForm(request.POST)

        if appointment.is_valid():
            service_provider = ServiceProvider.objects.get(pk=service_provider_id)
            owner = User.objects.get(pk=service_provider.user.pk)
            calendar = Calendar.objects.get(owner=service_provider.pk)
            availabilities = Availability.objects.filter(calendar=calendar)
            appointments = Appointment.objects.filter(calendar=calendar.pk)

            appointment = appointment.save(commit=False)



            appointment.attende = request.user
            appointment.calendar = calendar

            appointment.save()

            return redirect("home")

    appointment_form = CreateAppointmentForm()
    context["appointment_form"] = appointment_form

    service_provider = ServiceProvider.objects.get(pk=service_provider_id)
    owner = User.objects.get(pk=service_provider.user.pk)
    calendar = Calendar.objects.get(owner=service_provider.pk)
    availabilities = Availability.objects.filter(calendar=calendar)

    context["owner"] = owner
    context["service_provider"] = service_provider
    context["calendar"] = calendar
    context["availabilities"] = availabilities

    return render(request=request, template_name="appointment/service_provider_detail.html", context=context)

def my_appointments(request):

    context = {}

    if not request.user.is_authenticated:
        return redirect("login")

    service_provider = ServiceProvider.objects.filter(user=request.user).first()

    if not service_provider:
        return redirect("create_service_provider")

    pending_appointments = Appointment.objects.filter(status="PENDING", calendar__owner=service_provider.pk)
    accepted_appointments = Appointment.objects.filter(status="ACCEPTED", calendar__owner=service_provider.pk)

    context["pending_appointments"] = pending_appointments
    context["accepted_appointments"] = accepted_appointments

    return render(request=request, template_name="appointment/my_appointments.html", context=context)


def accept_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect("login")

    service_provider = ServiceProvider.objects.filter(user=request.user).first()
    if not service_provider:
        return redirect("create_service_provider")

    user = User.objects.get(pk=request.user.pk)
    pending_appointments = Appointment.objects.get(pk=appointment_id, calendar__owner=service_provider)
    pending_appointments.status = "ACCEPTED"
    pending_appointments.save()

    return redirect("my_appointments")

def cancel_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect("login")

    service_provider = ServiceProvider.objects.filter(user=request.user).first()
    if not service_provider:
        return redirect("create_service_provider")

    pending_appointments = Appointment.objects.get(pk=appointment_id)
    pending_appointments.status = "CANCELLED"
    pending_appointments.save()

    return redirect("my_appointments")

def reject_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect("login")

    service_provider = ServiceProvider.objects.filter(user=request.user).first()
    if not service_provider:
        return redirect("create_service_provider")

    pending_appointments = Appointment.objects.get(pk=appointment_id)
    pending_appointments.status = "REJECTED"
    pending_appointments.save()

    return redirect("my_appointments")


def edit_calendar(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.method == "POST":
        user = request.user

        _service_provider = ServiceProvider.objects.get(user=user)
        _calendar = Calendar.objects.get(owner=_service_provider.pk)

        edit_service_srovider_form = EditServiceProviderForm(data=request.POST, instance=_service_provider)

        if edit_service_srovider_form.is_valid():
            service_provider = edit_service_srovider_form.save(commit=False)
            service_provider.save()

        DAYS_OF_WEEK = [
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]

        for i in range(0, 7):
            day_of_week = DAYS_OF_WEEK[i]
            start_time = request.POST.get(f"form-{i}-start_time")
            end_time = request.POST.get(f"form-{i}-end_time")

            availability = Availability.objects.filter(calendar=_calendar.pk, day_of_week=day_of_week).first()
            availability.start_time = parse_time(start_time)
            availability.end_time = parse_time(end_time)
            availability.save()

    user = request.user

    service_provider = ServiceProvider.objects.get(user=user)
    calendar = Calendar.objects.get(owner=service_provider.pk)

    edit_availability_formset = EditAvailabilityFormSet(calendar_id=calendar.pk)
    edit_service_srovider_form = EditServiceProviderForm(instance=service_provider)

    context["edit_availability_formset"] = edit_availability_formset
    context["edit_service_srovider_form"] = edit_service_srovider_form

    return render(request=request, template_name="appointment/edit_calendar.html", context=context)


DAY_HOURS_15 = [
    (0, 00),
    (0, 15),
    (0, 30),
    (0, 45),
    (1, 00),
    (1, 15),
    (1, 30),
    (1, 45),
    (2, 00),
    (2, 15),
    (2, 30),
    (2, 45),
    (3, 00),
    (3, 15),
    (3, 30),
    (3, 45),
    (4, 00),
    (4, 15),
    (4, 30),
    (4, 45),
    (5, 00),
    (5, 15),
    (5, 30),
    (5, 45),
    (6, 00),
    (6, 15),
    (6, 30),
    (6, 45),
    (7, 00),
    (7, 15),
    (7, 30),
    (7, 45),
    (8, 00),
    (8, 15),
    (8, 30),
    (8, 45),
    (9, 00),
    (9, 15),
    (9, 30),
    (9, 45),
    (10, 00),
    (10, 15),
    (10, 30),
    (10, 45),
    (11, 00),
    (11, 15),
    (11, 30),
    (11, 45),
    (12, 00),
    (12, 15),
    (12, 30),
    (12, 45),
    (13, 00),
    (13, 15),
    (13, 30),
    (13, 45),
    (14, 00),
    (14, 15),
    (14, 30),
    (14, 45),
    (15, 00),
    (15, 15),
    (15, 30),
    (15, 45),
    (16, 00),
    (16, 15),
    (16, 30),
    (16, 45),
    (17, 00),
    (17, 15),
    (17, 30),
    (17, 45),
    (18, 00),
    (18, 15),
    (18, 30),
    (18, 45),
    (19, 00),
    (19, 15),
    (19, 30),
    (19, 45),
    (20, 00),
    (20, 15),
    (20, 30),
    (20, 45),
    (21, 00),
    (21, 15),
    (21, 30),
    (21, 45),
    (22, 00),
    (22, 15),
    (22, 30),
    (22, 45),
    (23, 00),
    (23, 15),
    (23, 30),
    (23, 45),
]

DAY_HOURS_30 = [
    (0, 00),
    (0, 30),
    (1, 00),
    (1, 30),
    (2, 00),
    (2, 30),
    (3, 00),
    (3, 30),
    (4, 00),
    (4, 30),
    (5, 00),
    (5, 30),
    (6, 00),
    (6, 30),
    (7, 00),
    (7, 30),
    (8, 00),
    (8, 30),
    (9, 00),
    (9, 30),
    (10, 00),
    (10, 30),
    (11, 00),
    (11, 30),
    (12, 00),
    (12, 30),
    (13, 00),
    (13, 30),
    (14, 00),
    (14, 30),
    (15, 00),
    (15, 30),
    (16, 00),
    (16, 30),
    (17, 00),
    (17, 30),
    (18, 00),
    (18, 30),
    (19, 00),
    (19, 30),
    (20, 00),
    (20, 30),
    (21, 00),
    (21, 30),
    (22, 00),
    (22, 30),
    (23, 00),
    (23, 30),
]
