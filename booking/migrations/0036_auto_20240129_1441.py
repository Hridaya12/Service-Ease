# Generated by Django 3.0.5 on 2024-01-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0035_auto_20240129_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='default_image.png', null=True, upload_to='images'),
        ),
    ]