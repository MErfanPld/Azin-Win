from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.contrib import messages
from django.urls import resolve

from accounts.helpers import create_code
from accounts.models import OtpCode
from sms.helpers import send_sms
from sms.sms_texts import SMS_TEXTS
from utils.validator import mobile_regex

User = get_user_model()


class UserForm(forms.ModelForm):
    password = forms.CharField(label='رمز عبور', required=True)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'full_name', 'is_admin', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id:
            self.fields.pop('password')

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.pop('password', None)
        if password:
            user.set_password(password)
        user.is_active = True
        if commit:
            user.save()
        return user


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(), label='تکرار رمز عبور')

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError('رمز عبور با تکرار آن مغایرت دارد!')

        return password2

    def save(self, commit=True):
        password = self.cleaned_data.pop('password', None)
        user = super().save(False)

        if password:
            user.set_password(password)
        user.save()

        code = OtpCode.objects.create_new_code(user)
        self.request.session['verify_phone_number'] = user.phone_number
        messages.success(self.request, 'ثبت نام شما با موفقیت انجام شد. کد تایید حساب کاربری برای شما پیامک شد.')

        sms_text = SMS_TEXTS['verify_code'].format(code.code)
        send_sms(user.phone_number, sms_text)
        return user


class PasswordResetForm(forms.ModelForm):
    phone_number = forms.CharField(label='شماره موبایل کاربر', required=True, min_length=11,
                                   max_length=11, validators=[mobile_regex])

    class Meta:
        model = OtpCode
        fields = ['phone_number']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean_phone_number(self):
        if not User.objects.filter(phone_number=self.cleaned_data.get('phone_number')).exists():
            raise forms.ValidationError('کاربری با این شماره موبایل وجود ندارد!', code='phone_number')

        return self.cleaned_data['phone_number']

    def save(self, commit=True):
        phone_number = self.cleaned_data.pop('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()

        code = OtpCode.objects.create_new_code(user)
        self.request.session['verify_phone_number'] = phone_number
        messages.success(self.request, 'کد تایید حساب کاربری به شماره موبایل شما پیامک شد.')
        sms_text = SMS_TEXTS['verify_code'].format(code.code)
        send_sms(phone_number, sms_text)
        return code


class OtpCodeForm(forms.Form):
    code = forms.CharField(label='کد تایید', required=True, min_length=6, max_length=6, validators=[RegexValidator(
        regex=r'^-?\d+\Z',
        message="کد تایید باید عددی باشد.",
    )])
    phone_number = forms.CharField(label='شماره موبایل کاربر', required=True, widget=forms.HiddenInput, min_length=11,
                                   max_length=11, validators=[mobile_regex])

    class Meta:
        model = OtpCode
        fields = ['code', 'phone_number']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        code = self.cleaned_data.get('code')

        code = OtpCode.objects.filter(user__phone_number=phone_number, code=code, is_used=False).first()
        if not code or not code.check_expire():
            raise forms.ValidationError('کد وارد شده معتبر نیست یا منقضی شده است!', code='code')

        return super().clean()

    def save(self, commit=True):
        code = OtpCode.objects.filter(user__phone_number=self.cleaned_data['phone_number'],
                                      code=self.cleaned_data['code']).first()

        if resolve(self.request.path_info).url_name == 'password-reset-confirm':
            code.verify_code(self.request, False)
            self.request.session['reset_password_code'] = code.code
            messages.success(self.request, 'رمز عبور جدید خود را وارد کنید.')
        else:
            messages.success(self.request, 'کاربر گرامی خوش آمدید')
            code.verify_code(self.request, True)

        return code
