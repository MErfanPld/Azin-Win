# Generated by Django 4.1.7 on 2023-04-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل'),
        ),
    ]
