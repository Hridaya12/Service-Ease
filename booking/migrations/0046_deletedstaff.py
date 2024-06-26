# Generated by Django 3.0.5 on 2024-02-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0045_auto_20240206_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=255, unique=True, verbose_name='email address')),
            ],
        ),
    ]
