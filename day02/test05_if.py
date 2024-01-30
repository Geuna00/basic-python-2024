# date : 20240130
# desc : 흐름제어 if

## 조건이 참일 때와 거짓일 때로 나누어서 어떤 일을 처리하는 것 if
# 콜론(:) 입력후 엔터누르면 자동으로 들여쓰기  
# IndentationError : 들여쓰기 오류
number = int(input()) ## 입력함수 int(input()) - 문자로 된 입력값을 정수로 변경

if number > 0: ## if 조건: - 참인 조건
    print('양수입니다')
elif number == 0: ## 양수x 음수x
    print('0 입니다')
elif number < 0:
    print('음수입니다')
else: ## else: - 거짓인 조건
    print('정의할 수 없습니다')