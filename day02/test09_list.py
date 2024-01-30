# date : 20240130
# desc : 복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60 # 학생수만큼 변수를 생성

# 총 갯수 : (n) 이면 인덱스의 마지막 값은 (n-1)
#index=   0,  1,   2,  3,  4,  5,  6,  7,  8,   9
#index= -10, -9,  -8, -7, -6, -5, -4, -3, -2,  -1
std =   [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]

# 리스트 요소 접근
print(std[9]) # IndexError : 범위를 벗어남

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3, 4), std]
print(list_1)
print(list_1[5])
list_1[6] = '바꾼값' # 인덱스[6]의 std(리스트)가 '바꾼값'(문자열)로 변경
print(list_1)

## 리스트 연산
print(list_1[2:4]) # 인덱스[2]부터 인덱스[4-1]까지 / 즉, 오른쪽 값은 출력하고자 하는 인덱스(+1)
## 마이너스 연산
print(list_1[-5:-3]) # 리스트 오른쪽부터 -1, -2...  왠만해서는 -인덱스는 사용하지 않도록.. 헷갈림
## 이중 리스트
print(list_1[4][3]) # [1,2,3,4]에서 인덱스[3] 가져오기  # 4

list_2 = [[1,2,3], [4,5,6], [7,8,9]]
print(list_2[1][2]) # [4,5,6]에서 인덱스[2]  # 6

list_4 = [1,2,3]
list_5 = [7,8,9]
# list_3 = list_4 + list_5
## 리스트 연산 (+ , *)만 사용 가능
print(list_4 + list_5) # + 는 리스트를 연결 [1,2,3,7,8,9]
print(list_5 * 2) # 리스트를 반복 [7,8,9,7,8,9]
list_6 = list_5 * 2

## 리스트 길이함수 len()
print(len(list_4))

## append() : 리스트 마지막에 하나 추가
## insert(index, val) : 리스트의 index 자리에 val 추가 
print(list_1)
list_1.append('Hello!!')
print(list_1)

list_1.insert(2,100)
print(list_1)

## extend() : 기존 리스트 확장, +와 거의 유사
list_4.extend(list_5)
print(list_4)
print(list_5)

## 리스트 삭제
del list_4[3] # 리스트의 인덱스 하나를 삭제
print(list_4)
del list_4 # 리스트 자체를 삭제

# pop() : 마지막 값 출력
val = list_5.pop() # 마지막 값을 꺼내오기
print(val) # 9
print(list_5) # [7, 8]

print(std)
val = std.pop(2) # 리스트에서 마지막값이 아닌 두번째 인덱스 값을 꺼내오기
print(val)
print(std)

# clear() : 리스트 내용 삭제
list_5.clear() # del()은 완전삭제. print 안됨 / clear() 내용만 삭제(리스트는 남아있음)
print(list_5)

# sort() : 리스트 정렬
# 문자열, 숫자, 불 섞여있는 리스트는 정렬안됨
std.sort() # 항상 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not in : 리스트 안에 찾고자하는 값이 있을 때
print(99 in std) # True
print(98 in std) # False

# reverse(), copy(), count() ...

# *리스트 : 전개연산자 - 몰라도됨
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b] # 1차원 리스트 생성 [1,3,5,2,4,8]
print(list_c)

list_d = [list_a, list_b] # 2차원 리스트 생성 [[1,3,5], [2,4,8]]
print(list_d)