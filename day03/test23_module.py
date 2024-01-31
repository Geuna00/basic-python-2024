# file : test23_module.py
# desc : 모듈 사용

import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')
# print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2 ** 10)
print(math.pow(2, 10)) # 제승
print(math.ceil(3.1)) # ceil() : 올림
print(math.floor(3.6)) # floor() : 내림
print(round(4.7)) # round() : 반올림(기본함수. 자주 사용하기 때문에 math에 없음)

import math as m # 별명짓기(간소화)
print(m.sin(2))

from math import pi, pow # from은 조심해서 사용해야 함 / 다른 모듈에도 같은 이름이 있을 수 있음(충돌발생가능)

print(pi)
print(pow(2, 10))