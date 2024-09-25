import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QFont, QPolygonF
from PyQt5.QtCore import Qt, QPoint, QPointF, QRect


class DrawShapesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(850, 500)
        self.setWindowTitle('Draw Shapes with PyQt')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rectangle(qp)

        # self.draw_ellipse(qp)
        # self.draw_text(qp)
        qp.end()

    def draw_rectangle(self, qp):
        # 绘制一个矩形
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        qp.drawRect(105, 105, 210, 210)  # 矩形的左上角坐标和宽度、高度
        qp.drawRect(535, 105, 210, 210)  # 矩形的左上角坐标和宽度、高度
        
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)
        # 绘制十字交叉虚线
        pen.setStyle(Qt.DashLine)  # 设置为虚线
        qp.drawLine(105, 210, 315, 210)  # 横线
        qp.drawLine(210 , 105, 210 , 315)  # 竖线

        qp.drawLine(535, 210, 745, 210)  # 横线
        qp.drawLine(640, 105, 640, 315)  # 竖线

    def draw_ellipse(self, qp):
        # 绘制一个椭圆
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)
        qp.setBrush(QBrush(QColor(200, 200, 255, 100)))  # 设置填充颜色和透明度
        qp.drawEllipse(180, 50, 100, 50)  # 椭圆的左上角坐标和宽度、高度

    def draw_text(self, qp):
        # 绘制文本
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        font = QFont("Arial", 12)  # 设置字体
        qp.setFont(font)
        qp.drawText(50, 170, "Hello, PyQt!")  # 文本的起始位置和文本内容


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawShapesWidget()
    sys.exit(app.exec_())
