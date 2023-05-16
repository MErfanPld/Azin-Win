from django.db import models

# Create your models here.

class FAQ(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان سوال")
    body = models.TextField(verbose_name="متن سوال")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"
      