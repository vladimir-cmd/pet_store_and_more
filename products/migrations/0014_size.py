# Generated by Django 3.1.5 on 2021-04-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210420_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], default='s', max_length=254)),
                ('price', models.FloatField()),
            ],
        ),
    ]
