from django.db import models
from accounts.models import User
from common.models import City
from extenstions.utils import jalali_converter

# Create your models here.
from order.helpers import type_project_CHOICES, status_CHOICES


class TypeWindow(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام پنجره")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "نوع پنجره"
        verbose_name_plural = "نوع پنجره ها"


class Order(models.Model):
    type_window = models.ForeignKey(
        to=TypeWindow, on_delete=models.CASCADE, related_name="orders", verbose_name="نوع پنجره"
    )
    type_project = models.CharField(
        max_length=2, choices=type_project_CHOICES, null=True, verbose_name="نوع پروژه ")
    number = models.FloatField(max_length=1000, null=True, verbose_name="تعداد واحد ")
    # city = models.CharField(max_length=100, null=True, verbose_name="شهر ")
    # addr = models.TextField(null=True, blank=True, verbose_name="ادرس محل ")
    phone_number = models.CharField(
        max_length=11, unique=True, null=True, verbose_name="شماره تماس")
    full_name = models.CharField(
        max_length=100, null=True, verbose_name="نام و نام خانوادگی ")
    # lat = models.TextField(null=True, blank=True, verbose_name='latitude')
    # long = models.TextField(null=True, blank=True, verbose_name='longitude')
    city = models.ForeignKey(
        to=City, on_delete=models.CASCADE, related_name="orders", null=True, verbose_name="شهر"
    )
    status = models.CharField(
        max_length=2, choices=status_CHOICES, blank=True, null=True, default='B', verbose_name="وضعیت درخواست")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.full_name} | {self.phone_number} | {self.type_window} | {self.created}"

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست ها"

    def jcreated(self):
        return jalali_converter(self.created)

    @property
    def get_type_project(self):
        return dict(type_project_CHOICES).get(self.type_project, '')

    @property
    def get_status(self):
        return dict(status_CHOICES).get(self.status, '')
