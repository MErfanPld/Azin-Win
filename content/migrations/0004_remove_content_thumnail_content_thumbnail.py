# Generated by Django 4.1.7 on 2024-10-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_category_content_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='thumnail',
        ),
        migrations.AddField(
            model_name='content',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
