# Generated by Django 2.2.12 on 2020-06-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200604_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandcamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('embed_url', models.CharField(max_length=10000)),
            ],
        ),
    ]
