# Generated by Django 3.0.5 on 2020-09-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_appointment_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Animal', verbose_name='animal'),
        ),
    ]
