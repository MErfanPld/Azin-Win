# Generated by Django 4.1.7 on 2023-04-18 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topproject',
            name='slug',
        ),
    ]