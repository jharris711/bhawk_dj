# Generated by Django 2.2.12 on 2020-06-04 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_presskitimgs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PressKitImgs',
            new_name='PressKitImg',
        ),
    ]