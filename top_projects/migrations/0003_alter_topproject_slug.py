# Generated by Django 4.1.7 on 2023-03-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_projects', '0002_topproject_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topproject',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='ادرس'),
        ),
    ]
