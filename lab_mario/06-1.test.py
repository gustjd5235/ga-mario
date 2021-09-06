import retro
import sys
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication,\
    QWidget, QLabel, QPushButton
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # 창 크기 고정
        self.setFixedSize(820, 448)
        # 창 제목 설정
        self.setWindowTitle('GA Mario')

        self.press_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # 이미지
        self.label_image = QLabel(self)

        # 게임 환경 생성
        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        # 새 게임 시작
        self.env.reset()
        # 화면 가져오기
        self.screen = self.env.get_screen()
        self.ram = self.env.get_ram()

        qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

        env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        env.reset()

        ram = env.get_ram()

        full_screen_tiles = ram[0x0500:0x069F + 1]

        print(full_screen_tiles.shape)
        print(full_screen_tiles)

        full_screen_tile_count = full_screen_tiles.shape[0]

        full_screen_page1_tile = full_screen_tiles[:full_screen_tile_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

        print(full_screen_tiles)

    def update_screen(self):
        # 화면 가져오기
        self.screen = self.env.get_screen()
        self.show()
        screen_qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(screen_qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)