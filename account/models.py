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
