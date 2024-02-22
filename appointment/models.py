from typing import Any
from django.db import models
from django.contrib.auth import get_user_model

from account.models import ServiceProvider

User = get_user_model()

class Calendar(models.Model):
    owner = models.OneToOneField(
        to=ServiceProvider,
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
        ("MONDAY", "Lundi"),
        ("TUESDAY", "Mardi"),
        ("WEDNESDAY", "Mercredi"),
        ("THURSDAY", "Jeudi"),
        ("FRIDAY", "Vendredi"),
        ("SATURDAY", "Samedi"),
        ("SUNDAY", "Dimanche"),
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

    calendar = models.ForeignKey(
        to=Calendar,
        on_delete=models.CASCADE,
        related_name="appointments",
        null=False,
        blank=False,
    )

    attende = models.ForeignKey(
        to=User,
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
        default="PENDING",
        null=False,
        blank=False,
    )

    message = models.TextField(
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
