import requests
from django.conf import settings
from kavenegar import *


def send_sms(receiver, body_id):
    data = {
        'username': settings.SMS_USERNAME,
        'password': settings.SMS_PASSWORD,
        'text': f'{receiver}',
        'to': receiver,
        'bodyId': body_id,
    }
    response = requests.post(settings.SMS_WEB_SERVICE_URL, data)

    # api_key = '6A7A663139434F576369452F385972337444784A637A505374637147524C396F6F7A6B4338614333414F453D'
    # response = requests.get(f'https://api.kavenegar.com/v1/{api_key}/sms/send.json?receptor=09396988720&message=salam')

    if response.status_code and response.json().get('RetStatus') == 1:
        return False

    return True
