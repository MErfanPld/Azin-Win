from django.db import models


class CustomModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ ویرایش"
    )

    # created_at = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name="تاریخ ثبت"
    # )
    # updated_at = models.DateTimeField(
    #     auto_now=True,
    #     verbose_name="تاریخ ویرایش"
    # )

    class Meta:
        abstract = True
        ordering = ['-created_at']
