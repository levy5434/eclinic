# Generated by Django 3.0.5 on 2020-09-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200928_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
