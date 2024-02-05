# file : test39_nothread.py
# desc : Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner 에서 만든 ui를 로드
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui 파일내에 있는 위젯 접근은 VSCode 상에서 색상으로 표시X

    def btnStartClicked(self):
        maxVal = 101
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) # 프로그레스바 0부터 시작
        self.pgbTask.setRange(0, maxVal-1) # 0부터 100까지 / maxVal만 입력했을 때 프로그레스바가 99까지만 감 / for문의 입력방식과 좀 다름
        for i in range(maxVal): # 0 ~ 100까지
            print_str = f'노스레드 출력 >> {i}'
            print(print_str)
            self.txbLog.append(print_str)
            self.pgbTask.setValue(i)


    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인
        re = QMessageBox.question(self, '종료확인','종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()           
        else:
            QCloseEvent.ignore() 

if __name__ == '__main__':
    loop = QApplication(sys.argv)
    isinstance = qtwin_exam()
    isinstance.show()
    loop.exec_()

