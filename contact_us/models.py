from django.db import models

from content.helpers import status_content_CHOICES
from extenstions.utils import jalali_converter


# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره موبایل")
    body = models.TextField(verbose_name="متن")
    status = models.CharField(
        max_length=2, choices=status_content_CHOICES, blank=True, default="B", null=True, verbose_name="ضعیت")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.full_name} | {self.email} | {self.phone_number} | {self.created}"

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

    def jcreated(self):
        return jalali_converter(self.created)

    @property
    def get_status(self):
        return dict(status_content_CHOICES).get(self.status, '')
