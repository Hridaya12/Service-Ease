# Generated by Django 3.0.5 on 2024-01-31 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0040_appointment_invoice_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='invoice_id',
            new_name='invoice_number',
        ),
    ]