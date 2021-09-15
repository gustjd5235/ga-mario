import sys
import retro
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #창 제목 설정
        self.setWindowTitle('GA-Mario')

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        screen = self.env.reset()

        self.screen_width = screen.shape[0] * 2
        self.screen_height = screem.shape[1] *2

        #창 크기 조정
        self.setFixedSize(self.screen_width + 500, self.screen_height + 100)

        self.screen_label = QLabel(self)
        self.screem_label.setGeometry(0,0,)
        #창 띄우기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())