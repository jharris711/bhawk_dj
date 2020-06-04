# Generated by Django 2.2.12 on 2020-06-04 08:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200604_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingshow',
            name='image',
            field=cloudinary.models.CloudinaryField(default='img', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
