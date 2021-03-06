# 01.pyqt_basic.py
# 창 띄우는 기본 코드 (모든 코드에서 기본적으로 사용)
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 조정
        self.setFixedSize(400, 300)
        #창 제목 설정
        self.setWindowTitle('MyApp')
        #창 띄우기
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())