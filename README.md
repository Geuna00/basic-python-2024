# 파이썬 기초 2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
    - 코딩폰트 : 나눔고딕코딩   https://github.com/naver/nanumfont
    - Notepad++ 설치            https://notepad-plus-plus.org/downloads/
    - Python 설치               https://www.python.org/downloads/release/python-3115/
    - Visual Studio Code 설치   https://code.visualstudio.com/
    - Git 설치                  https://git-scm.com/
        - TortoiseGit 설치      https://tortoisegit.org/download/
        - Github 가입           https://github.com/
        - Github Desktop 설치   https://desktop.github.com/

- 파이썬 기초(개발자 : 귀도 반 로썸)
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01)) # <class of 'int'>

    print(5 + 4 / 2) # 7.0
    print(5 == 4) # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참/거짓으로 조건 분기 (다른언어 switch)
        - for : 반복문 기본 (다른언어 foreach)
        - while : 반복문 변형 (다른언어 do~while)
    - 복합자료형 + 연산자(연산함수)
        - 리스트[], 튜플(), 딕셔너리{}
    - 출력 포맷
    - 구구단 + 디버깅

    ```python
    # debugging
    # F9(중단점 토글), F5(디버그 시작), F10(한줄씩 실행), F11(함수안으로 진입)
    # Shift + F5(디버깅 종료)
    print('구구단 시작!')
    for x in range(2, 9+1):# 2부터 9까지 반복
        print(f'{x}단 ----->')
        for y in range(1, 9+1): # 1부터 9까지 반복
            print(f'{x} x {y} = {x*y:2d}', end='\t') # end= : 엔터 대신 공백으로 변경
        print() # 안쪽 for문이 끝나면 마지막 엔터를 하나 추가    
    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기(피라미드 만들기)
    - 함수, 람다함수는 나중에
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 되는 것 : 객체(object)
        - 캡슐화(__plateNumber)
    - 패키지, 묘듈
    - 로또

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        - pip 사용

        ```shell
        > pip --version # 버전확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지를 삭제
        ```
    - 예외처리 : 비정상적인 프로그램 종료 막기
        - 오류(Error) : 코딩 중 발생할 수 있는 '문법적' 실수(실행 자체가 안됨)
        - 예외(Exception) : 실행 중 발생할 수 있는 '로직적' 실수(실행 잘되다가 갑자기 문제발생)

        ```python
        def div(x, y):
        try:
            return x / y # 0 을 넣었을 때 예외 발생 : ZeroDivisionError
        except ZeroDivisionError as e:
            # print(e)
            print('[오류] 제수는 0이 될 수 없습니다.')
            return 0
        ```
    - 텍스트 파일 입출력

    ```python
    f = open('파일명', mode='r|w|a', encoding='cp949|utf-8')
    f.read()
    f.readline() # 읽기
    f.wrtie('text') # 쓰기
    f.close() # 반드시 파일을 닫을 것
    ```
- 파이썬 응용
    - 주피터 노트북
        - Ctrl + Shift + P(명령팔레트)로 시작
        - 사용방법 (test31_jupyternb.ipynb) 참조
    - folium 기본 사용
    ![folium사용법](https://raw.githubusercontent.com/HyungJuu/basic-python-2024/main/images/python_001.png)

## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(Colab)
    - folium 계속
    - json 입출력
    - 응용예제 연습
        - IP주소 확인
        - QR코드 생성

## 6일차
- Python 라이브러리 경로 : C:\DEV\Langs\Python311\Lib\site-packages
 - 파이썬 응용
    - Window App(PyQt) 만들기

    ```shell
    > pip install PyQt5
    > pip install PyQt5Designer
    ```

    - PyQt5 기본실행
    - QtDesigner 사용법
    - 🌟스레드 학습 : UI스레드와 Background스레드 분리
        - [ ] GIL, 병렬프로세싱 더 학습할 것

    ![스레드예제](https://raw.githubusercontent.com/HyungJuu/basic-python-2024/main/images/python_003.gif)

    ```python
    # 스레드 클래스에서 시그널 선언
    class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기 위한 변수객체
        # ...

        def run(self) -> None: # 스레드 실행
            # 스레드로 동작할 내용
            maxVal = 100001
            self.initSignal.emit(maxVal) # emit() : UI 스레드로 보내기
            # ...

    class qtwin_exam(QWidget): # UI 스레드
        # ...
        def btnStartClicked(self):
            th = BackWorker(self)
            th.start() # BackWorker 내의 self.run() 실행
            th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
            # ...

        # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 = 슬롯함수
        @pyqtSlot(int) # BackWorkder 스레드에서 self.initSignal.emit() 이 동작해서 실행
        def initPgbTask(self, maxVal):
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal-1)
    ```

## 7일차
- 파이썬 응용
    - 객체지향
        - 상속, 오버라이딩(재정의), 오버로딩만 공부하면 됨!
            - 오버로딩 : 같은 이름의 함수를 골라 사용하는 것(매개변수가 다르면 다양하게 사용 가능)
            
            ```python
            class qtwin_exam(QWidget): # 상속
                # ...

                # QWidget에 있는 closeEvent를 그대로 쓰면 그냥 닫힘
                # 닫을지 말지 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
                def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인 (재정의)
                    re = QMessageBox.question(self, '종료확인','종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
                    if re == QMessageBox.Yes: # 닫기
                        QCloseEvent.accept()           
                    else:
                        QCloseEvent.ignore() 
            ```
    - 가상환경 Virtualenv
        - 다른버전의 파이썬도 설치해야 사용 가능
        - 3.11에서 3.9 가상환경을 만들려면 3.9 파이썬 설치필요
    - PyQt5와 응용예제 연습
        - 이미지 뷰어
        - 이미지 에디터
    ![PyQt예제](https://raw.githubusercontent.com/HyungJuu/basic-python-2024/main/images/python_004.png)

## 8일차
- 파이썬 응용
    - PyQt5 응용예제 계속

- 파이썬 기본 코딩테스트



    - 객체지향(나중에...)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중상속
        - 추상클래스, 인터페이스...

