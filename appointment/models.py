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

    EMPPOINTMENT_DURATION_IN_MINUTES = [
        (30, "30 minutes"),
        (45, "45 minutes"),
        (60, "60 minutes"), # 1h
        (75, "75 minutes"), # 1h15mn
        (90, "90 minutes"), # 1h30mn
        (105, "105 minutes"), # 1h45mn
        (120, "120 minutes"), # 2h
        (135, "135 minutes"), # 2h15mn
        (150, "150 minutes"), # 2h30mn
        (165, "165 minutes"), # 2h45mn
        (180, "180 minutes"), # 3h
    ]
    enppointment_duration_in_minutes = models.IntegerField(
        choices=EMPPOINTMENT_DURATION_IN_MINUTES,
        default=30,
        null=False,
        blank=False,
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


class AvailabilityInterval(models.Model):

    availibility = models.ForeignKey(
        to=Availability,
        on_delete=models.CASCADE,
        related_name="intervals",
        null=False,
        blank=False,
    )

    start_time = models.TimeField(
        null=False,
        blank=False,
    )

    end_time = models.TimeField(
        null=False,
        blank=False,
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