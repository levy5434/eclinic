# Generated by Django 3.0.5 on 2020-10-05 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20201002_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='appointments',
        ),
    ]
