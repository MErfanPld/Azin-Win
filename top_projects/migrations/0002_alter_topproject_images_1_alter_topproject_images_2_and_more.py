# Generated by Django 4.1.7 on 2024-10-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topproject',
            name='images_1',
            field=models.ImageField(default='1.png', upload_to='', verbose_name='تصویر شماره 1'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_2',
            field=models.ImageField(default='1.png', upload_to='', verbose_name='تصویر شماره 2'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_3',
            field=models.ImageField(default='1.png', upload_to='', verbose_name='تصویر شماره 3'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_4',
            field=models.ImageField(default='1.png', upload_to='', verbose_name='تصویر شماره 4'),
        ),
        migrations.AlterField(
            model_name='topproject',
            name='images_5',
            field=models.ImageField(default='1.png', upload_to='', verbose_name='تصویر شماره 5'),
        ),
    ]
