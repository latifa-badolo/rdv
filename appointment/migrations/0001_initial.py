# Generated by Django 5.0.1 on 2024-02-20 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointments_limit_per_day', models.IntegerField(blank=True, default=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.serviceprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wensday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday')], max_length=100)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='appointment.calendar')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('PENDING', 'pending'), ('ACCEPTED', 'accepted'), ('REJECTED', 'rejected'), ('CANCELLED', 'cancelled')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('attende', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='appointment.calendar')),
            ],
        ),
    ]
