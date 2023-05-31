import requests
from django.conf import settings
from django.core.mail import send_mail
import datetime


class WeatherWarningChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnList"

    def check_weather_warnings(self, warning_type):
        today = datetime.date.today().strftime("%Y%m%d")
        params = {
            "serviceKey": self.api_key,
            "pageNo": "1",
            "numOfRows": "10",
            "dataType": "json",
            "fromTmFc": today,
            "toTmFc": today,
            "areaCode": "L1030200",
            "warningType": warning_type,
            "stnId": "232",
        }

        response = requests.get(self.url, params=params)
        data = response.json()

        warning_types = data["response"]["body"]["items"]["item"]["warningType"]
        if "9" in warning_types or "7" in warning_types or "8" in warning_types:
            if "9" in warning_types:
                send_mail(
                    "폭우 발생 알림",
                    "폭우가 발생했습니다.",
                    settings.EMAIL_HOST_USER,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            if "7" in warning_types:
                send_mail(
                    "태풍 발생 알림",
                    "태풍이 발생했습니다.",
                    settings.EMAIL_HOST_USER,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            if "8" in warning_types:
                send_mail(
                    "대설 발생 알림",
                    "대설이 발생했습니다.",
                    settings.EMAIL_HOST_USER,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
        else:
            print("No weather warnings for the given types")
