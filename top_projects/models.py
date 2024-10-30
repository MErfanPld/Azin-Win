from django.db import models

from extenstions.utils import jalali_converter
from order.helpers import status_CHOICES
from top_projects.utils import upload_image_top_project


# Create your models here.


class TopProject(models.Model):
    eng_name = models.CharField(max_length=255, verbose_name="نام مهندس")
    project_name = models.CharField(max_length=255, verbose_name="نام پروژه")
    body = models.TextField(verbose_name="توضیحاتی درباره پروژه")
    images_1 = models.ImageField(upload_to=upload_image_top_project, verbose_name="تصویر شماره 1")
    images_2 = models.ImageField(upload_to=upload_image_top_project, verbose_name="تصویر شماره 2")
    images_3 = models.ImageField(upload_to=upload_image_top_project, verbose_name="تصویر شماره 3")
    images_4 = models.ImageField(upload_to=upload_image_top_project, verbose_name="تصویر شماره 4")
    images_5 = models.ImageField(upload_to=upload_image_top_project, verbose_name="تصویر شماره 5")
    status = models.CharField(
        max_length=2, choices=status_CHOICES, blank=True, null=True, default='B', verbose_name="وضعیت درخواست")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.eng_name} | {self.project_name} | {self.status} | {self.created}"

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه های برتر"

    def jcreated(self):
        return jalali_converter(self.created)

    @property
    def get_status(self):
        return dict(status_CHOICES).get(self.status, '')

    @property
    def get_images_1(self):
        return self.images_1.url if self.images_1 else ''

    @property
    def get_images_2(self):
        return self.images_2.url if self.images_2 else ''

    @property
    def get_images_3(self):
        return self.images_3.url if self.images_3 else ''

    @property
    def get_images_4(self):
        return self.images_4.url if self.images_4 else ''

    @property
    def get_images_5(self):
        return self.images_5.url if self.images_5 else ''
