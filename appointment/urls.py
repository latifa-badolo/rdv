from django.urls import path

from .views import (
    see_calendar,
    edit_calendar,
    search_service_provider,
    my_appointments,
    accept_appointment,
    cancel_appointment,
    reject_appointment,
    see_service,
)

urlpatterns = [
    path("see_calendar/<int:service_provider_id>", see_calendar, name="see_calendar"),
    path("edit_calendar/", edit_calendar, name="edit_calendar"),
    path("see_service/", see_service, name="see_service"),
    path("search_service_provider/", search_service_provider, name="search_service_provider"),
    path("my_appointments/", my_appointments, name="my_appointments"),
    path("accept_appointment/<int:appointment_id>", accept_appointment, name="accept_appointment"),
    path("cancel_appointment/<int:appointment_id>", cancel_appointment, name="cancel_appointment"),
    path("reject_appointment/<int:appointment_id>", reject_appointment, name="reject_appointment"),
]
