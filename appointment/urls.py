from django.urls import path

from .views import (
    see_calendar,
)

urlpatterns = [
    path("see_calendar/<int:service_provider_id>", see_calendar, name="see_calendar")
]
