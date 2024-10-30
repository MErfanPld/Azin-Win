# Generated by Django 4.1.7 on 2024-10-30 07:46

from django.db import migrations, models
import top_projects.utils


class Migration(migrations.Migration):

    dependencies = [
        ('top_projects', '0002_remove_topproject_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topproject',
            name='images_1',
            field=models.ImageField(upload_to=top_projects.utils.upload_image_top_project, verbose_name='تصویر شماره 1'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_2',
            field=models.ImageField(upload_to=top_projects.utils.upload_image_top_project, verbose_name='تصویر شماره 2'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_3',
            field=models.ImageField(upload_to=top_projects.utils.upload_image_top_project, verbose_name='تصویر شماره 3'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_4',
            field=models.ImageField(upload_to=top_projects.utils.upload_image_top_project, verbose_name='تصویر شماره 4'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_5',
            field=models.ImageField(upload_to=top_projects.utils.upload_image_top_project, verbose_name='تصویر شماره 5'),
        ),
    ]
