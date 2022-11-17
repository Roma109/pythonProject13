import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

SCREEN_SIZE = [500, 500]


class Interface:

    def loadUI(self, qwidget):
        qwidget.setGeometry(500, 500, SCREEN_SIZE[0], SCREEN_SIZE[1])
        qwidget.button = QPushButton('Кнопка', qwidget)
        qwidget.button.move(20, 20)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        Interface().loadUI(self)
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
        heigh, width = randint(0, 500 - d), randint(0, 500 - d)
        qp.setPen(QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 4))
        qp.drawEllipse(heigh, width, d, d)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
