from django.db import models


# Create your models here.

class About_us(models.Model):
    image = models.ImageField(upload_to='1.png', verbose_name="تصویر")
    addr = models.TextField(verbose_name="ادرس")
    tel = models.CharField(max_length=150, verbose_name="تلفن")
    desc = models.TextField(verbose_name="توضیحات")

    def __str__(self):
        return f"{self.tel}"

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
