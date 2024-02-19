from django.contrib import admin

from .models import User, Service

@admin.register(User)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ["username", "email", ]

@admin.register(Service)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ["name", "enppointment_duration_in_minutes", ]