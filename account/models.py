from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    avatar = models.ImageField(
        upload_to="user/avatat",
        height_field=100,
        width_field=100,
        max_length=150,
        null=True,
        blank=True,
    )

    is_service_provider = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.username


class Service(models.Model):

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    thumbnail = models.ImageField(
        upload_to="service/img/",
        height_field=100,
        width_field=100,
        max_length=150,
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

    message_template = models.TextField(
        null=True,
        blank=True,
    )

    email_template = models.TextField(
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
        return self.name