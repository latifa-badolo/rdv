# Generated by Django 5.0.1 on 2024-02-17 18:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_remove_calendar_enppointment_duration_in_minutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='availability',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AvailabilityInterval',
        ),
    ]
