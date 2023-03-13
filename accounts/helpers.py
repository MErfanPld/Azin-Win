import random

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone

from accounts.models import OtpCode

User = get_user_model()


def check_user_exist(new_phone):
    if User.objects.filter(phone_number=new_phone).exists():
        raise ValidationError([
            ValidationError('این شماره موبایل قبلا ثبت شده است!', code='phone_number'),
        ])


def check_reset_password_sent(user):
    reset_password = user.password_resets.last()
    if reset_password:
        today = timezone.now()
        expiration = reset_password.created_at + timedelta(minutes=1)

        if today > expiration:
            return True

        return False

    return True


def check_login_code_sent(user):
    login_code = user.login_codes.last()
    if login_code:
        today = timezone.now()
        expiration = login_code.created_at + timedelta(minutes=1)

        if today > expiration:
            return True

        return False

    return True


def check_code_expiration(code):
    code = OtpCode.objects.filter(code=code).first()
    if code and not code.is_used:
        today = timezone.now()
        expiration = code.created_at + timedelta(minutes=1)

        if today > expiration:
            return False

        return True

    return False


def create_code():
    return ''.join([str(random.randint(0, 9)) for item in range(6)])
