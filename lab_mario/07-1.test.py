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
        #self.full_screen_tiles = np.array([0])
        #self.i = 0

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

        # 타이머 생성
        self.qtimer = QTimer(self)
        # 타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.game_timer)
        # 1초(1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(1000 / 60)

        self.show()

    def paintEvent(self, event):
        self.ram = self.env.get_ram()

        full_screen_tiles = self.ram[0x0500:0x069F + 1]

        full_screen_tile_count = full_screen_tiles.shape[0]

        full_screen_page1_tile = full_screen_tiles[0:full_screen_tile_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)
        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        c = full_screen_tiles.shape[0]
        # for i in range(0, c):
        # print(full_screen_tiles.size)
        cnt = 0
        a = 0
        b = 0
        # print(full_screen_tiles)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.white))
        t = 0

        # print(full_screen_tiles[0][0])

        for i in range(416):
            print(t, i)
            cnt += 1
            if full_screen_tiles[t][i % 32] == 0:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.gray))
                painter.drawRect(480 + a, 0 + b, 10, 10)
            else:
                painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
                # 브러쉬 설정 (채우기)
                painter.setBrush(QBrush(Qt.blue))
                painter.drawRect(480 + a, 0 + b, 10, 10)
            a += 10
            # print(cnt)
            if cnt % 32 == 0:
                a = 0
                b += 10
                t += 1

    def update_screen(self):
        # 화면 가져오기
        self.screen = self.env.get_screen()

        screen_qimage = QImage(self.screen, self.screen.shape[1], self.screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(screen_qimage)
        pixmap = pixmap.scaled(480, 448, Qt.IgnoreAspectRatio)
        #pixmap = pixmap.scaled(self.screen_width, self.screen_height, Qt.IgnoreAspectRatio)
        self.label_image.setPixmap(pixmap)

    def game_timer(self):
        # 키 배열: B, NULL, SELECT, START, U, D, L, R, A
        # b = 66, u = 16777235, d = 16777237, l = 16777234, r = 16777236, a = 65
        # self.env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.env.step(self.press_buttons)
        self.update_screen()
        self.update()