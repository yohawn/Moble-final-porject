import requests
import json


def send_api(API_HOST, path, method, headers, body):
    url = API_HOST + path

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)

        elif method == "POST":
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(body, ensure_ascii=False).encode("utf8"),
            )

        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)


# 호출 예시
API_HOST = "http://192.168.0.19:9000/"
headers = {
    "Authorization": "ToKen 04abf8e01bd6c4bfddf03b25c13c169894aa0430",  # 토큰값
    "Content-Type": "application/json",
    "charset": "UTF-8",
    "Accept": "*/*",
}
body = {
    "residents_number": 7,
    "ressident_name": "오요환",
    "resident_dong": 101,
    "resident_ho": 1104,
    "residents_doorpasswd": 6201,
    "resident_homephonenumber": "02-0201-1520",
    "resident_phone": "010-6454-1541",
    "resident_carnumber": "12나1234",
    "resident_typeofcar": "휘발유",
    "resident_residency": "거주중",
    "resident_movedate": None,
}
send_api(
    API_HOST,
    "/residents_information/",
    # "POST",
    "GET",
    headers,
    body,
)  # POST : 데이터 추가, GET  : 전체리스트
