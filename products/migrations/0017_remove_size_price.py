# Generated by Django 3.1.5 on 2021-04-21 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210421_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='price',
        ),
    ]
