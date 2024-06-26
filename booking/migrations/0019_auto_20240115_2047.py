# Generated by Django 3.0.5 on 2024-01-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_feedback_acknowledged'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
    ]
