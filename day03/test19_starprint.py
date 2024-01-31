# file : test19_starprint.py
# desc : 별찍기 또는 피라미드 만들기
# *
# **
# ***
# ****
# *****

for i in range(1,5+1):
    # i = 1 -> range(1,2) 1번 반복
    # i = 2 -> range(1,3) 2번 반복
    for j in range(1, i+1): 
        print('*', end='') # 여백없이
    print() # 안쪽 for문이 끝나면 엔터
print()

for i in range(1,5+1):
    for j in range(1, 6-i+1): 
        print('*', end='') 
    print()
print()

for i in range(1,5+1):
    for j in range(1, 5-i+1): 
        print(' ', end='') 
    
    for j in range(1, i+1):
        print('*',end='')
    print()
print()

