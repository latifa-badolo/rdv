# Generated by Django 5.0.1 on 2024-02-17 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='enppointment_duration_in_minutes',
        ),
    ]
