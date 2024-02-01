# date : 20240201
# file : test25_web.py
# desc : urllib 모듈 사용법

# from urllib.request import *  # request 모듈 안의 모든 함수를 사용하고 싶을 때 -> *
from urllib.request import Request, urlopen # request 모듈 안의 Request 클래스와 urlopen만 사용하겠다

req = Request('https://www.naver.com/') # 네이버 웹주소(url)
res = urlopen(req) # url 주소로 웹사이트를 열어달라고 요청

print(f'응답 코드 : {res.status}') # url로 요청된 웹사이트의 응답 확인
print(res.read())

# urllib.request보다 성능이 조금 더 나은 모듈
import requests

res2 = requests.get('https://www.naver.com/')

print(res2.status_code)
print(res2.text)