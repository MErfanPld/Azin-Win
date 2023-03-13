from django.db import models

# Create your models here.
from content.helpers import type_content_CHOICES, status_content_CHOICES


class Content(models.Model):
    type_content = models.CharField(
        max_length=2, choices=type_content_CHOICES, blank=True, null=True, verbose_name="نوع محتوا")
    title = models.CharField(max_length=225, blank=False,
                             null=True, verbose_name="عنوان محتوا")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="ادرس")
    body = models.TextField(verbose_name="متن")
    cover = models.ImageField(default="1.png", verbose_name="تصویر بزرگ")
    thumnail = models.ImageField(
        default="1.png", verbose_name="تصویر بندانگشتی")
    status = models.CharField(
        max_length=2, choices=status_content_CHOICES, blank=True, null=True, verbose_name="ضعیت")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.title} | {self.slug} | {self.created}"

    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا ها"

    @property
    def get_type_content(self):
        return dict(type_content_CHOICES).get(self.type_content, '')

    @property
    def get_status(self):
        return dict(status_content_CHOICES).get(self.status, '')
