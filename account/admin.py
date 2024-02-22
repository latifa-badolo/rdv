from django.contrib import admin

from .models import User, ServiceProvider, Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", ]

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ["user", "work", "town", "level_of_education"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["value"]