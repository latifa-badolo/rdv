from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import EditCalendarForm, EditAvailabilityFormSet, CreateAppointmentForm

from datetime import datetime

from .models import Calendar, Appointment, Availability
from account.models import ServiceProvider

User = get_user_model()


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

    return render(request=request, template_name="appointment/search_service_provider.html", context={})

def service_provider_detail(request, service_provider_id):
    context = {}

    if not request.user.is_authenticated:
        return redirect("/admin/login")

    if request.method == "POST":
        appointment = CreateAppointmentForm(request.POST)

        if appointment.is_valid():
            service_provider = ServiceProvider.objects.get(pk=service_provider_id)
            owner = User.objects.get(pk=service_provider.user.pk)
            calendar = Calendar.objects.get(owner=service_provider.pk)
            availabilities = Availability.objects.filter(calendar=calendar)

            appointment = appointment.save(commit=False)

            appointment.attende = request.user
            appointment.calendar = calendar

            appointment.save()

            return redirect("/")

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
        return redirect("/admin/login")

    service_provider = ServiceProvider.objects.get(user=request.user)

    pending_appointments = Appointment.objects.filter(status="PENDING", calendar__owner=service_provider.pk)
    accepted_appointments = Appointment.objects.filter(status="ACCEPTED", calendar__owner=service_provider.pk)

    context["pending_appointments"] = pending_appointments
    context["accepted_appointments"] = accepted_appointments

    return render(request=request, template_name="appointment/my_appointments.html", context=context)

def accept_appointment(request, appointment_id):
    pending_appointments = Appointment.objects.get(pk=appointment_id)
    pending_appointments.status = "ACCEPTED"
    pending_appointments.save()

    return redirect("my_appointments")

def cancel_appointment(request, appointment_id):
    pending_appointments = Appointment.objects.get(pk=appointment_id)
    pending_appointments.status = "CANCELLED"
    pending_appointments.save()

    return redirect("my_appointments")

def reject_appointment(request, appointment_id):
    pending_appointments = Appointment.objects.get(pk=appointment_id)
    pending_appointments.status = "REJECTED"
    pending_appointments.save()

    return redirect("my_appointments")


def edit_calendar(request):

    if request.method == "POST":
        user = request.user
        context = {}

        # calendar = Calendar.objects.filter(user=user.pk).first()
        # availlabilities = Availability.objects.filter(calendar=calendar.pk)

        service_provider = ServiceProvider.objects.get(user=user)

        _calendar = Calendar.objects.get(owner=service_provider.pk)
        _availlabilities = Availability.objects.filter(calendar=_calendar.pk)

        calendar = EditCalendarForm(data=request.POST, instance=_calendar)
        availabilities = EditAvailabilityFormSet(data=request.POST, calendar_id=_calendar.pk)
        # availabilities = EditAvailabilityFormSet(data=request.POST, queryset=Availability.objects.filter(calendar=_calendar.pk))

        if calendar.is_valid():
            calendar = calendar.save(commit=False)
            calendar.save()



        # instances = availabilities.save(commit=False)
        print(availabilities    )
        # if availabilities.is_valid():

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
            availability.start_time = datetime.strptime(start_time, "%H:%M:%S").time()
            availability.end_time = datetime.strptime(end_time, "%H:%M:%S").time()
            availability.save()


        # for instance in availabilities:
        #     availability = instance.save()
        #     Availability.objects.filter(day_of_week=instance.day_of_week).update(
        #         start_time=instance.start_time,
        #         end_time=instance.end_time,
        #     )
        #     # instance.calendar = calendar_pk
        #     instance.save()


    user = request.user
    context = {}

    service_provider = ServiceProvider.objects.get(user=user)
    calendar = Calendar.objects.get(owner=service_provider.pk)
    availlabilities = Availability.objects.filter(calendar=calendar.pk)

    edit_calendar_form = EditCalendarForm(instance=calendar)
    edit_availability_formset = EditAvailabilityFormSet(calendar_id=calendar.pk)
    # edit_availability_formset = EditAvailabilityFormSet(initial=availlabilities.values())

    context = {"edit_calendar_form": edit_calendar_form, "edit_availability_formset": edit_availability_formset}

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