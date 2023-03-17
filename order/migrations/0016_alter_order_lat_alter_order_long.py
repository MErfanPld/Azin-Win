# Generated by Django 4.1.7 on 2023-03-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_order_addr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lat',
            field=models.TextField(blank=True, null=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='order',
            name='long',
            field=models.TextField(blank=True, null=True, verbose_name='longitude'),
        ),
    ]
