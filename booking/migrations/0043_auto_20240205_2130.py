# Generated by Django 3.0.5 on 2024-02-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0042_auto_20240205_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedappointment',
            name='staff',
            field=models.CharField(default='Not assigned', max_length=50),
        ),
    ]
