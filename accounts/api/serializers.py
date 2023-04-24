from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from accounts.helpers import create_code
from accounts.models import OtpCode
from sms.helpers import send_sms
from sms.sms_texts import SMS_TEXTS
from utils.validator import mobile_regex

User = get_user_model()


class OtpCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6, required=False, validators=[RegexValidator(
        regex=r'^-?\d+\Z',
        message="کد تایید باید عددی باشد",
    )])
    phone_number = serializers.CharField(max_length=11, min_length=11, required=True, validators=[mobile_regex])

    def save(self, **kwargs):
        phone_number = self.validated_data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            raise serializers.ValidationError('کاربری با این شماره موبایل وجود ندارد!', code='phone_number')

        code = OtpCode.objects.create_new_code(user)
        sms_text = SMS_TEXTS['verify_code'].format(code.code)
        send_sms(user.phone_number, sms_text, code.code)
        return code


class OtpCodeConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6, required=True, validators=[RegexValidator(
        regex=r'^-?\d+\Z',
        message="کد تایید باید عددی باشد",
    )])
    phone_number = serializers.CharField(max_length=11, min_length=11, required=True, validators=[mobile_regex])

    def save(self, **kwargs):
        phone_number = self.validated_data.get('phone_number')
        code = create_code()

        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            raise serializers.ValidationError('کاربری با این شماره موبایل وجود ندارد!', code='phone_number')

        code = OtpCode.objects.create(code=code, user=user)
        # TODO send code with sms
        return code
