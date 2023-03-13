# Generated by Django 4.1.7 on 2023-03-13 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otpcode',
            options={'verbose_name': 'کد یکبار مصرف', 'verbose_name_plural': 'کد ها یکبار مصرف'},
        ),
        migrations.RemoveField(
            model_name='otpcode',
            name='created',
        ),
        migrations.RemoveField(
            model_name='otpcode',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='otpcode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AddField(
            model_name='otpcode',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='آیا استفاده شده است'),
        ),
        migrations.AddField(
            model_name='otpcode',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codes', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.CharField(max_length=6, verbose_name='کد'),
        ),
    ]
