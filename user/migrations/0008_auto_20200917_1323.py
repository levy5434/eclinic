# Generated by Django 3.0.5 on 2020-09-17 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200828_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
    ]
