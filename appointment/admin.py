from django.contrib import admin
from .models import ( Appointment, Attendee, Availability, AvailabilityInterval, Calendar)


class AvailabilityIntervalInlineInline(admin.TabularInline):
    model = AvailabilityInterval

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ["user", "enppointment_duration_in_minutes", "active", "updated_at"]

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ["calendar", "day_of_week", "updated_at"]
    inlines = [AvailabilityIntervalInlineInline]

@admin.register(AvailabilityInterval)
class AvailabilityIntervalAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time",]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["date", "start_time", "end_time", "service", "status", "updated_at"]

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ["appointment", "first_name", "last_name", "email", "phone_number", "updated_at"]
