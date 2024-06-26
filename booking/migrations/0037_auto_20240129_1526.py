# Generated by Django 3.0.5 on 2024-01-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0036_auto_20240129_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='images/default_image.png', null=True, upload_to='images'),
        ),
    ]
