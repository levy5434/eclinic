# Generated by Django 3.0.5 on 2020-09-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_appointment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='animal',
        ),
    ]
