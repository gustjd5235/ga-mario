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


        #print(self.screen)

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
        #self.i = full_screen_tiles.shape

        # print(full_screen_tiles.shape)
        #print(full_screen_tiles)

        full_screen_tile_count = full_screen_tiles.shape[0]

        # 정수여야 해서 / 2개
        full_screen_page1_tile = full_screen_tiles[0:full_screen_tile_count // 2].reshape((13, 16))
        full_screen_page2_tile = full_screen_tiles[full_screen_tile_count // 2:].reshape((13, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

        #print(type(full_screen_tiles[4][0]))

        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        #print(self.full_screen_tiles.shape)
        c = full_screen_tiles.shape[0]
        # for i in range(0, c):
        #print(full_screen_tiles.size)
        cnt = 0
        a = 0
        b = 0
        #print(full_screen_tiles)

        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.white))
        # 직사각형 (왼쪽 위, 오른쪽 아래)

        t = 0

        #print(full_screen_tiles[0][0])

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
            #print(cnt)
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
        self.env.step(self.press_buttons)
        self.update_screen()
        self.update()
        #print(self.screen)

    def keyPressEvent(self, event):
        key = event.key()
        if key == 16777235:
            self.press_buttons[4] = 1
        elif key == 16777237:
            self.press_buttons[5] = 1
        elif key == 16777234:
            self.press_buttons[6] = 1
        elif key == 16777236:
            self.press_buttons[7] = 1
        elif key == 65:
            self.press_buttons[8] = 1
        elif key == 66:
            self.press_buttons[0] = 1


    def keyReleaseEvent(self, event):
        key = event.key()
        if key == 16777235:
            self.press_buttons[4] = 0
        elif key == 16777237:
            self.press_buttons[5] = 0
        elif key == 16777234:
            self.press_buttons[6] = 0
        elif key == 16777236:
            self.press_buttons[7] = 0
        elif key == 65:
            self.press_buttons[8] = 0
        elif key == 66:
            self.press_buttons[0] = 0

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())