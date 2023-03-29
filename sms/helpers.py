import requests
from django.conf import settings
from kavenegar import *


def send_sms(receiver, msg):
    # response = requests.get(
    #     f'{settings.SMS_WEB_SERVICE_URL}username={settings.SMS_USERNAME}&password={settings.SMS_PASSWORD}&from={settings.SMS_FROM_NUMBER}&to={receiver}&text={msg}'
    # )

    api_key = '6A7A663139434F576369452F385972337444784A637A505374637147524C396F6F7A6B4338614333414F453D'

    response = requests.get(f'https://api.kavenegar.com/v1/{api_key}/sms/send.json?receptor=09396988720&message=salam')
    print('wwwwwwwwwwwwwwwwwwww')
    print(response.status_code)
    print(response.text)

    return True
