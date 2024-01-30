# file : test12_dictionary.py
# desc : 복합자료형 딕셔너리

## 사전형 - key와 value쌍을 나열해 놓은 자료형
## {key:value, key:value, key:value, ... }
dict_movie = {'name':'어벤져스 엔드게임', 'type':'히어로 무비', 'year':2019, 
              'director':['안소니 루소', '조 루소'], 'cast':['아이언맨', '타노스', '헐크', '토르', '닥터스트레인지']}
# 조회
print(dict_movie['name'])
print(dict_movie['year'])
# 추가, 수정
dict_movie['year'] = 2020 # 입력한 key의 value값 수정
print(dict_movie)

dict_movie['producer'] = '케빈 파이기' # key와 value값 리스트에 추가
print(dict_movie)

if 'musician' in dict_movie: # 딕셔너리에 키가 있는지 확인할 때
    print(dict_movie['musician'])
else:
    print('음악감독 없음')

musician = dict_movie.get('musician') # 오류(예외) 발생X
print(musician)
# print(dict_movie['musician']) # 오류(예외) 발생
print()

# 반복문으로 출력
print('< 반복문 방법1 >')
for key in dict_movie:
    print(key, ':',dict_movie[key])
print()

print('< 반복문 방법2 >')
for key, value in dict_movie.items():
    print(key, ':', value)

