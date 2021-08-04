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

        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        env.reset()

        screen = env.get_screen()
        screen_width = screen.shape[0]
        screen_height = screen.shape[1]

        #이미지
        label_image = QLabel(self)
        image = np.array()
        qimage = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage) # QImage를 QPixmap으로 전환
        pixmap = pixmap.scaled(screen.shape[0], screen.shape[1], Qt.IgnoreAspectRatio) # Ignore은 원본비율 무시한단 의미

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0, 0, screen.shape[0], screen.shape[1]) # x좌표, y좌표, 가로면적, 세로면적

        #창 띄우기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
