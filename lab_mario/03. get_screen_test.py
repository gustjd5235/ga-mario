# 02. pyqt_widget.py
# pyqt 위젯 배치 (QLabel, QPushButton)
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np
import retro
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 조정
        self.setFixedSize(300, 300)
        #창 제목 설정
        self.setWindowTitle('GA-Mario')

        # 게임 환경 생성
        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        env.reset()

        # 화면 가져오기
        screen = env.get_screen()

        print(screen.shape)
        print(screen)

        self.screenLabel = QLabel(self)


        #창 띄우기
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
