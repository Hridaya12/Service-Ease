# Generated by Django 3.0.5 on 2024-02-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0043_auto_20240205_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='staff',
            field=models.CharField(default='Not assigned', max_length=50),
        ),
    ]
