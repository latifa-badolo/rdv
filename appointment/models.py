from typing import Any
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Calendar(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )

    appointments_limit_per_day = models.IntegerField(
        default=10,
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    require_confirmation = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )


class Availability(models.Model):

    DAYS_OF_WEEK = [
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wensday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
    ]
    day_of_week = models.CharField(
        max_length=100,
        choices=DAYS_OF_WEEK,
        null=False,
        blank=False,
    )

    start_time = models.TimeField(
        null=True,
        blank=True,
    )

    end_time = models.TimeField(
        null=True,
        blank=True,
    )

    calendar = models.ForeignKey(
        to=Calendar,
        on_delete=models.CASCADE,
        related_name="availabilities",
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )


class Appointment(models.Model):
    start_time = models.TimeField(
        null=False,
        blank=False,
    )

    end_time = models.TimeField(
        null=False,
        blank=False,
    )

    date = models.DateField(
        null=False,
        blank=False,
    )

    service = models.ForeignKey(
        to="account.Service",
        on_delete=models.CASCADE,
        related_name="appointments",
        null=False,
        blank=False,
    )

    calendar = models.ForeignKey(
        to=Calendar,
        on_delete=models.CASCADE,
        related_name="appointments",
        null=False,
        blank=False,
    )

    APPOINTMENT_STATUS = [
        ("PENDING", "pending"),
        ("ACCEPTED", "accepted"),
        ("REJECTED", "rejected"),
        ("CANCELLED", "cancelled"),
    ]
    status = models.CharField(
        max_length=100,
        choices=APPOINTMENT_STATUS,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )


class Attendee(models.Model):

    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        max_length=255,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name="attendees",
        null=True,
        blank=True,
    )

    appointment = models.ForeignKey(
        to=Appointment,
        on_delete=models.SET_NULL,
        related_name="attendees",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
