# file : test14_while.py
# desc : while 문

## while 참이 조건:
## 공통점 if 조건: elif 조건:, else:, for in range():, while 조건: => 콜론(:)
count = 0

# while count < 10: # count 변수값이 10보다 작거나 같은 동안 반복

# 무한루프 : Window OS, 모바일 OS, 자동차네비게이션, 라프베리파이, 아두이노, 게임, Winform개발, 웹개발, ...
while True: # 참인 동안, True는 항상 참임. 무한루프(Infinite Loop)
    count = count + 1
    print('나무찍기 ',count)
    if count == 10:
        break # 이 반복문을 빠져나가라
print()

number = 0
while True:
    number += 1
    if str(number).count('3') == 1 or \
        str(number).count('6') == 1 or \
        str(number).count('9') == 1: # 숫자를 문자열로 바꾼 값 안에 '3', '6', '9'가 있으면
        print('짝!') 
    else:
        print(number)

    if number == 30:
        break
print()

# 짝! 대신 countinue로 변경
number = 0
while True:
    number += 1
    if str(number).count('3') >= 1 or \
        str(number).count('6') >= 1 or \
        str(number).count('9') >= 1: # 숫자를 문자열로 바꾼 값 안에 '3', '6', '9'가 있으면
        continue # 반복에서 제외하는 것
    else:
        print(number)

    if number > 31:
        break # 반복문에서 빠져나가는 것
