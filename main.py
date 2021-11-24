import random
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

SCREEN_SIZE = [600, 650]


class RandomYellowCircles(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.resize(*SCREEN_SIZE)
        self.flag = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.draw_random_yellow_circles)
        self.flag = True
        self.update()
    def draw_random_yellow_circles(self):
        if self.flag:
            painter = QPainter(self)
            painter.begin(self)
            painter.setBrush(QColor(250, 255, 0))
            x, y = random.randint(0, SCREEN_SIZE[0]),\
                    random.randint(0, SCREEN_SIZE[0])
            w = h = random.randint(10, 70)

            painter.drawEllipse(x, y, w, h)
            painter.end()
            self.flag = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sq = RandomYellowCircles()
    sq.show()
    sys.exit(app.exec())

