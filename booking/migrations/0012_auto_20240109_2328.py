# Generated by Django 3.0.5 on 2024-01-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20240109_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
