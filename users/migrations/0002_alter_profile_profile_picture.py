# Generated by Django 5.2.1 on 2025-06-24 20:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='kvtec0mqxawgxmhsaamd', max_length=255, verbose_name='image'),
        ),
    ]
