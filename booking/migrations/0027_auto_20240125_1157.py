# Generated by Django 3.0.5 on 2024-01-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_auto_20240123_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]