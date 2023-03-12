# Generated by Django 4.1.7 on 2023-03-11 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_order_type_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.BooleanField(default=True, verbose_name="وضعیت درخواست"),
        ),
        migrations.AlterField(
            model_name="order",
            name="type_window",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="order.typewindow",
                verbose_name="نوع پنجره",
            ),
        ),
    ]