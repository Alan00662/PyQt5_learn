import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt


class DrawShapesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.initUI()

    def initUI(self):
        self.resize(850, 500)
        self.setWindowTitle('Draw Shapes with PyQt')

        # 创建滑块
        self.slider_x1 = self.create_slider()
        self.slider_y1 = self.create_slider()
        self.slider_x2 = self.create_slider()
        self.slider_y2 = self.create_slider()

        # 连接滑块值变化信号
        self.slider_x1.valueChanged.connect(self.update_x1)
        self.slider_y1.valueChanged.connect(self.update_y1)
        self.slider_x2.valueChanged.connect(self.update_x2)
        self.slider_y2.valueChanged.connect(self.update_y2)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(QLabel('x1 Slider:'))
        layout.addWidget(self.slider_x1)
        layout.addWidget(QLabel('y1 Slider:'))
        layout.addWidget(self.slider_y1)
        layout.addWidget(QLabel('x2 Slider:'))
        layout.addWidget(self.slider_x2)
        layout.addWidget(QLabel('y2 Slider:'))
        layout.addWidget(self.slider_y2)

        self.setLayout(layout)
        self.show()

    def create_slider(self):
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 210)
        slider.setValue(0)  # 默认值
        return slider

    def update_x1(self, value):
        self.x1 = value
        self.update()  # 更新界面

    def update_y1(self, value):
        self.y1 = value
        self.update()  # 更新界面

    def update_x2(self, value):
        self.x2 = value
        self.update()  # 更新界面

    def update_y2(self, value):
        self.y2 = value
        self.update()  # 更新界面

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rectangle(qp)
        self.draw_txt(qp)
        self.draw_point(qp)
        qp.end()

    def draw_rectangle(self, qp):
        # 绘制两个矩形
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        qp.drawRect(105, 105, 210, 210)  # 第一个矩形
        qp.drawRect(535, 105, 210, 210)  # 第二个矩形
        
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)
        # 绘制十字交叉虚线
        pen.setStyle(Qt.DashLine)  
        qp.drawLine(105, 210, 315, 210)  # 横线
        qp.drawLine(210 , 105, 210 , 315)  # 竖线
        qp.drawLine(535, 210, 745, 210)  # 横线
        qp.drawLine(640, 105, 640, 315)  # 竖线

    def draw_txt(self, qp):
        qp.setFont(QFont('Arial', 14))
        qp.drawText(315, 210 + 7, f'x1: {self.x1}')  # 右侧边长
        qp.drawText(210 - 14, 315 + 14, f'y1: {self.y1}')  # 右侧边长
        qp.drawText(535 - 35, 210 + 7, f'x2: {self.x2}')  # 右侧边长
        qp.drawText(640 - 14, 315 + 14, f'y2: {self.y2}')  # 右侧边长

    def draw_point(self, qp):
        pen = QPen(Qt.black, 10)  # 将点的大小放大5倍
        qp.setPen(pen)
        qp.drawPoint(105 + self.x1, 105 + self.y1)  # 第一个矩形内的点
        qp.drawPoint(535 + self.x2, 105 + self.y2)  # 第二个矩形内的点


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawShapesWidget()
    sys.exit(app.exec_())
