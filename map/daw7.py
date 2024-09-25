import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint

class ArrowWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw Arrow')

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 5, Qt.SolidLine)
        painter.setPen(pen)

        # 画箭头
        painter.drawLine(20, 30, 150, 30)  # 画线
        
        # 定义箭头的尖端为一个多边形
        arrow_head = QPolygon([
            QPoint(140, 20),
            QPoint(150, 30),
            QPoint(140, 40),
        ])
        
        painter.drawPolygon(arrow_head)  # 画箭头部分

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArrowWidget()
    ex.show()
    sys.exit(app.exec_())
