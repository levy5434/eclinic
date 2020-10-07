# Generated by Django 3.0.5 on 2020-09-20 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200917_1701'),
        ('user', '0013_auto_20200919_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Animal', verbose_name='animal')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Doctor')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Service', verbose_name='service')),
            ],
        ),
    ]
