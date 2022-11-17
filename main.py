import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic

SCREEN_SIZE = [500, 500]


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_star(qp)
            qp.end()

    def draw_star(self, qp):
        d = randint(3, 200)
        heigh, width = randint(0, 300 - d), randint(0, 300 - d)
        qp.setPen(QPen(QColor(255, 255, 0), 4))
        qp.drawEllipse(heigh, width, d, d)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
