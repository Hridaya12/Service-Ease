# Generated by Django 3.0.5 on 2024-01-12 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_vendorrequest_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorrequest',
            old_name='photo',
            new_name='image',
        ),
    ]