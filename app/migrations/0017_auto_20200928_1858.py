# Generated by Django 3.0.5 on 2020-09-28 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_appointment_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='text',
            new_name='information',
        ),
    ]
