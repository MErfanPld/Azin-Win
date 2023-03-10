from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255, unique=True, verbose_name="ایمیل")
    phone_number = models.CharField(
        max_length=11, unique=True, verbose_name="شماره تماس")
    full_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    is_active = models.BooleanField(
        default=True, verbose_name="فعال / غیرفعال")
    is_admin = models.BooleanField(
        default=False, verbose_name="ادمین هست / ادمین نیست")

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'


class OtpCode(models.Model):
    phone_number = models.CharField(
        max_length=11, unique=True, verbose_name="شماره تماس")
    code = models.PositiveSmallIntegerField(verbose_name="کد")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ساخت")

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'

    class Meta:
        verbose_name = 'کد اعتبارسنجی'
        verbose_name_plural = 'کدهای اعتبارسنجی'
