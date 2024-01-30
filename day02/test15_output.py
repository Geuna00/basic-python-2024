# file : test15_output.py
# desc : 콘솔 출력 포맷방식 String Format

print(10)
print('10')

string_1 = '{}'.format(10) # {}위치에 format 함수뒤에 들어있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name = '김근아' # input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000, '만', '빌려주세요')
print(string_3)
print()

# 정수 문자열포맷 d
string_4 = '_____{:d}_____'.format(100) # 정수
print(string_4)
string_4 = '_____{:5d}_____'.format(100) # 다섯자리
print(string_4)
string_4 = '_____{:05d}_____'.format(100) # 다섯자리를 만들 때 빈자리 0으로 표기
print(string_4)
string_4 = '_____{:+5d}_____'.format(100) # 양수 표현
print(string_4)
string_4 = '_____{:05d}_____'.format(-100) # 음수 표현
print(string_4)
string_4 = '_____{:=010d}_____'.format(-100) # 기호와 숫자를 분리
print(string_4)
print()

# 실수 문자열포맷 f(기본 소수점 6자리)
string_5 = '_____{:.2f}_____'.format(78.33333333333) # .숫자 : 소수점 몇째자리까지 자름
print(string_5)

val = 78.33333333333
string_5 = '_____{:7.2f}_____'.format(val) # 전체자리수 : 7자리 / 소수점 : 2자리
print(string_5)
print()
# 파이썬 3.6이후 도입. format() 함수를 사용하지 않음
string_6 = f'_____{val:7.2f}_____'
print(string_6)
print()

string_7 = 'hello, world!'
print(string_7.upper()) # upper case : 글자를 모두 대문자로 변환
print(string_7.lower()) # lower case : 글자를 모두 소문자로 변환
print(string_7.lower().capitalize()) # 맨앞 글자만 대문자로 

print(string_7.split(' ')) # 특정한 단어로 자르는 함수.      split(' ')랑 split()이 같나?

string_8 = 'Hello, I am GA Kim. I am a student. Good Luck for your day.'
words = string_8.split()
print(words)
print(f'string_8 문장 단어 갯수는 {len(words)}개 입니다.')
print()

string_9 = 'A10'
print(string_9.isalnum()) # True        isalnum() : 알파벳과 숫자
print(string_9.isnumeric()) # False     isnumeric() : 숫자
string_10 = '10.5' # 소수점은 함수를 만들어서 처리해야함
print(string_10.isdecimal()) # False    isdecimal() : 정수
print()

print('안냥' in '안녕하세요')