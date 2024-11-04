from django.db import models


# Create your models here.

class About_us(models.Model):
    body = models.TextField(verbose_name="متن")

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"
