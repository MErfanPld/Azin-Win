from django.db import models
from django.utils import timezone

# Create your models here.
from content.helpers import type_content_CHOICES, status_content_CHOICES
from content.utils import upload_image_content
from extenstions.utils import jalali_converter
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=225, blank=False,
                             null=True, verbose_name="نام دسته بندی")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, verbose_name="ادرس")
    status = models.CharField(
        max_length=2, choices=status_content_CHOICES, blank=True, null=True, verbose_name="ضعیت")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def jcreated(self):
        return jalali_converter(self.created)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Content(models.Model):
    # type_content = models.CharField(
    #     max_length=2, choices=type_content_CHOICES, blank=True, null=True, verbose_name="نوع محتوا")
    title = models.CharField(max_length=225,verbose_name="عنوان محتوا")
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, verbose_name="ادرس")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name="content", verbose_name="دسته بندی")
    body = models.TextField(verbose_name="متن")
    cover = models.ImageField(upload_to=upload_image_content, verbose_name="تصویر بزرگ")
    thumbnail = models.ImageField(
        upload_to=upload_image_content, verbose_name="تصویر بندانگشتی")
    status = models.CharField(
        max_length=2, choices=status_content_CHOICES, verbose_name="ضعیت")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f"{self.title} | {self.slug} | {self.created}"

    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا ها"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    def jcreated(self):
        return jalali_converter(self.created)

    
    # @property
    # def get_type_content(self):
    #     return dict(type_content_CHOICES).get(self.type_content, '')

    @property
    def get_status(self):
        return dict(status_content_CHOICES).get(self.status, '')
