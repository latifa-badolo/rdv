# Generated by Django 5.0.1 on 2024-02-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_availability_end_time_availability_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
