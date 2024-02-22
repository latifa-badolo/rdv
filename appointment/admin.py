from django.contrib import admin
from .models import Appointment, Availability, Calendar

class AvailabilityInline(admin.TabularInline):
    model = Availability
    fields = ["day_of_week", "start_time", "end_time"]

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ["owner", "active", "updated_at"]
    inlines = [AvailabilityInline]

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ["calendar", "start_time", "end_time", "day_of_week", "updated_at"]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["date", "start_time", "end_time", "status", "updated_at"]
