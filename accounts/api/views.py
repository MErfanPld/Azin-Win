from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from accounts.api.serializers import *
from django.contrib.auth import get_user_model

from accounts.helpers import create_code
from accounts.models import OtpCode

User = get_user_model()


class UserAuthVS(GenericViewSet):
    @action(
        methods=["get", "post"],
        detail=False,
        url_path="code/send",
        serializer_class=OtpCodeSerializer,
    )
    def code_send(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        phone_number = serializer.data['phone_number']
        user = User.objects.filter(phone_number=phone_number).first()

        if user:
            try:
                return Response({'message': 'پیامک حاوی کد تایید با موفقیت ارسال شد.', 'phone_number': user.phone_number}, 200)
            except:
                return Response(
                    {'error': 'خطایی هنگام ارسال پیامک حاوی کد یکبار مصرف پیش آمده است! لطفا دوباره امتحان کنید.'}, 400)

        return Response({'error': 'کاربری با این شماره موبایل وجود ندارد!'}, 404)
