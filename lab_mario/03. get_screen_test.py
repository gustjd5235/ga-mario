import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.QtCore import QTimer


# print(screen.shape[0], screen.shape[1])
# print(screen)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        a = 2

        self.press_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        self.env.reset()

        self.screen = self.env.get_screen()

        # 창크기 조절
        self.setFixedSize(int(self.screen.shape[0] * a), int(a * self.screen.shape[1]))
        # 창제목 설정
        self.setWindowTitle('GA Mario')

        self.label_image = QLabel(self)

        self.image = self.env.get_screen()
        qimage = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(int(self.screen.shape[0] * a), int(a * self.screen.shape[1]), Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)
        self.label_image.setGeometry(0, 0, int(self.screen.shape[0] * a), int(a * self.screen.shape[1]))

        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        # 1초마다 연결된 함수를 실행
        self.qtimer.start(1000 // 60)

        # 이미지

        # 창 띄우기
        self.show()

    def timer(self):
        self.env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))

    def keyPressEvent(self, event):
        key = event.key()
        if key == event.key_Up:
            self.press_buttons[4] = 1
        elif key == event.key_Down:
            self.press_buttons[5] = 1
        elif key == event.key_Left:
            self.press_buttons[6] = 1
        elif key == event.key_Right:
            self.press_buttons[7] = 1
        elif key == event.key_A:
            self.press_buttons[0] = 1
        elif key == event.key_B:
            self.press_buttons[8] = 1

    def keyReleasevent(self, event):
        key = event.key()
        if key == event.key_Up:
            self.press_buttons[4] = 0
        elif key == event.key_Down:
            self.press_buttons[5] = 0
        elif key == event.key_Left:
            self.press_buttons[6] = 0
        elif key == event.key_Right:
            self.press_buttons[7] = 0
        elif key == event.key_A:
            self.press_buttons[0] = 0
        elif key == event.key_B:
            self.press_buttons[8] = 0

    def keyReleaseEvent(self, event):
        key = event.key()
        print(str(key) + 'release')


# 직접 실행할때만 실행되는 코드
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())