from django.contrib import admin
from .models import ( Appointment, Attendee, Availability, Calendar)

class AvailabilityInline(admin.TabularInline):
    model = Availability
    fields = ["day_of_week", "start_time", "end_time"]


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ["user", "active", "updated_at"]
    inlines = [AvailabilityInline]

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ["calendar", "start_time", "end_time", "day_of_week", "updated_at"]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["date", "start_time", "end_time", "service", "status", "updated_at"]

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ["appointment", "first_name", "last_name", "email", "phone_number", "updated_at"]
