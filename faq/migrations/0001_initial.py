# Generated by Django 4.1.7 on 2023-05-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان سوال')),
                ('body', models.TextField(verbose_name='متن سوال')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوال ها',
            },
        ),
    ]
