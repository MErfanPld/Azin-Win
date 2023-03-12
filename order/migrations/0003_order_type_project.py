# Generated by Django 4.1.7 on 2023-03-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_remove_order_name_user_order_full_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="type_project",
            field=models.CharField(
                blank=True,
                choices=[("A", "نوساز"), ("B", "بازسازی")],
                max_length=2,
                null=True,
                verbose_name="نوع پروژه",
            ),
        ),
    ]