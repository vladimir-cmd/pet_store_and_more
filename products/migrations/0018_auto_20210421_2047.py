# Generated by Django 3.1.5 on 2021-04-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_size_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='l_price',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='m_price',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='s_price',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='x_price',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
