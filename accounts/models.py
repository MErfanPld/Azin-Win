from datetime import datetime, timedelta
from django.contrib.auth import login, get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin


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
    REQUIRED_FIELDS = ['email']

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


class OtpCodeManager(models.Manager):
    def create_new_code(self, user):
        from accounts.helpers import create_code

        user.codes.all().update(is_used=True)
        return OtpCode.objects.create(code=create_code(), user=user)


class OtpCode(models.Model):
    code = models.CharField(verbose_name='کد', max_length=6)
    user = models.ForeignKey(verbose_name='کاربر', to=User, on_delete=models.CASCADE, related_name='codes', null=True)
    is_used = models.BooleanField(verbose_name='آیا استفاده شده است', default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True,
        verbose_name="تاریخ ثبت"
    )

    class Meta:
        verbose_name = 'کد یکبار مصرف'
        verbose_name_plural = 'کد ها یکبار مصرف'

    EXPIRE_TIME = 2

    objects = OtpCodeManager()

    def __str__(self):
        return f"{self.user}-{self.code}"

    def check_expire(self):
        expire_time = self.created_at.now() + timedelta(minutes=self.EXPIRE_TIME)
        if datetime.now() > expire_time:
            self.is_used = True
            self.save()
            return False
        return True

    def verify_code(self, request, is_login=False):
        self.is_used = True
        self.user.is_active = True
        self.user.save()
        self.save()

        if is_login:
            login(request, self.user)
            try:
                del request.session['verify_phone']
            except:
                pass
