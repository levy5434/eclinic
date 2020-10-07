# Generated by Django 3.0.5 on 2020-09-28 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0018_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='owner',
        ),
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='client'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='information',
            field=models.TextField(blank=True, null=True, verbose_name='information'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='start time'),
        ),
    ]