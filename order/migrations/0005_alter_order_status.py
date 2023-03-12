# Generated by Django 4.1.7 on 2023-03-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_order_status_alter_order_type_window"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("A", "نوساز"), ("B", "بازسازی")],
                max_length=2,
                null=True,
                verbose_name="وضعیت درخواست",
            ),
        ),
    ]
