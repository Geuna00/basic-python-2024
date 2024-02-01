# file : test27_eh.py
# desc : 예외발생 처리

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    try:
        return x / y # 0 을 넣었을 때 예외 발생 : ZeroDivisionError
    except ZeroDivisionError as e:
        # print(e)
        print('[오류] 제수는 0이 될 수 없습니다.')
        return 0

def getOperands(): # 계산할 수를 입력받는 함수
    try:
        a, b = map(int, input('두 수 입력(구분자 공백) > ').split()) # 34. 을 넣었을 때 예외발생 : ValueError
        return a, b
    except ValueError as e:
        # print(e) # 정확한 예외 메시지 출력
        print('[오류] 정수만 입력하세요.')
        return 1, 1

while True:
    mnu = input('메뉴 입력(p[덧셈], m[뺄셈], t[곱셈], d[나눗셈], x[종료]) > ')

    if mnu == 'p':
        a, b = getOperands()
        print(f'덧셈 결과 : {a} + {b} = {add(a, b)}')
    elif mnu == 'm':
        a, b = getOperands()
        print(f'뺄셈 결과 : {a} - {b} = {minus(a, b)}')
    elif mnu == 't':
        a, b = getOperands()
        print(f'곱셈 결과 : {a} x {b} = {multi(a, b)}')
    elif mnu == 'd':
        a, b = getOperands()
        print(f'나눗셈 결과 : {a} ÷ {b} = {div(a, b)}')
    elif mnu == 'x':
        print('종료')
        break
    else:
        continue # 다시 메뉴 선택으로 올라감

    


