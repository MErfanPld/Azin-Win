# Generated by Django 4.1.7 on 2023-03-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='1.png', verbose_name='تصویر')),
                ('addr', models.TextField(verbose_name='ادرس')),
                ('tel', models.CharField(max_length=150, verbose_name='تلفن')),
                ('desc', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]
