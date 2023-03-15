import requests
from django.conf import settings


def send_sms(receiver, msg):
    # response = requests.get(
    #     f'{settings.SMS_WEB_SERVICE_URL}username={settings.SMS_USERNAME}&password={settings.SMS_PASSWORD}&from={settings.SMS_FROM_NUMBER}&to={receiver}&text={msg}'
    # )

    response = requests.get(
        f'https://api.kavenegar.com/v1/{settings.SMS_WEB_SERVICE_TOKEN}/sms/send.json?receptor={receiver}&message={msg}')

    print('dddddddddddddddddddd')
    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        return False
    return True
