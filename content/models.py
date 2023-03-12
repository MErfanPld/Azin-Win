from django.db import models

# Create your models here.


class Content(models.Model):
    type_content_CHOICES = (
        ('A', 'UPVC (یو پی وی سی)'),
        ('B', ' آلومینیوم ترمال بریک'),
    )
    status_content_CHOICES = (
        ('A', 'نشان داده شود'),
        ('B', 'نشان داده نشود'),
    )
    type_content = models.CharField(
        max_length=2, choices=type_content_CHOICES, blank=True, null=True, verbose_name="نوع محتوا")
    title = models.CharField(max_length=225, blank=True,
                             null=True, verbose_name="عنوان محتوا")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="ادرس")
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
