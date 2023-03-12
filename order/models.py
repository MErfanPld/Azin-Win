from django.db import models
from accounts.models import User

# Create your models here.


class TypeWindow(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام پنجره")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "نوع پنجره"
        verbose_name_plural = "نوع پنجره ها"


class Order(models.Model):
    type_project_CHOICES = (
        ('A', 'نوساز'),
        ('B', 'بازسازی'),
    )
    status_CHOICES = (
        ('A', 'پیگیری شده'),
        ('B', 'پیگیره نشده'),
    )
    type_window = models.ForeignKey(
        to=TypeWindow, on_delete=models.CASCADE, related_name="orders", verbose_name="نوع پنجره"
    )
    type_project = models.CharField(
        max_length=2, choices=type_project_CHOICES, blank=True, null=True, verbose_name="نوع پروژه")
    number = models.FloatField(verbose_name="تعداد واحد")
    number_units = models.FloatField(verbose_name=" units تعداد")
    addr = models.TextField(verbose_name="ادرس محل")
    phone_number = models.CharField(
        max_length=11, unique=True, null=True, blank=True, verbose_name="شماره تماس")
    full_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    status = models.CharField(
        max_length=2, choices=status_CHOICES, blank=True, null=True, verbose_name="وضعیت درخواست")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.full_name} | {self.phone_number} | {self.type_window} | {self.created}"

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست ها"
