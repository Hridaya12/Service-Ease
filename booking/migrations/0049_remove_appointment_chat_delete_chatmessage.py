# Generated by Django 5.0.2 on 2024-02-09 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0048_chatmessage_appointment_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='chat',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
