import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtGui import QPainter, QPen, QFont, QPolygon
from PyQt5.QtCore import Qt, QPoint
import math  

class DrawShapesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        self.l_x = 0
        self.l_y = 0
        self.r_x = 0
        self.r_y = 0

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
        slider.setRange(-3500, 3500)
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
        self.draw_arrows(qp)
        qp.end()

    def draw_rectangle(self, qp):
        # 绘制两个矩形
        pen = QPen(Qt.black, 2)
        qp.setPen(pen)
        qp.drawRect(105, 105, 210, 210)  # 第一个矩形
        qp.drawRect(535, 105, 210, 210)  # 第二个矩形
        
        pen = QPen(Qt.red, 2)
        pen.setStyle(Qt.DashLine)  
        qp.setPen(pen)
        qp.drawLine(105, 210, 315, 210)  # 横线
        qp.drawLine(210 , 105, 210 , 315)  # 竖线
        qp.drawLine(535, 210, 745, 210)  # 横线
        qp.drawLine(640, 105, 640, 315)  # 竖线

    def draw_txt(self, qp):
        qp.setFont(QFont('Arial', 14))
        qp.drawText(315, 217, f'x1: {self.x1}') 
        qp.drawText(210 - 14, 315 + 14, f'y1: {self.y1}')  
        qp.drawText(535 - 35, 217, f'x2: {self.x2}') 
        qp.drawText(640 - 14, 315 + 14, f'y2: {self.y2}')  
    def draw_point(self, qp):
        pen = QPen(Qt.black, 4)  # 圆边的宽度
        qp.setPen(pen)
        radius = 4  # 圆的半径

        self.l_x = int(self.x1 * 0.03 + 210)
        self.l_y = int(-self.y1 * 0.03 + 210)
        self.r_x = int(self.x2 * 0.03 + 640)
        self.r_y = int(-self.y2 * 0.03 + 210)
         
        # 绘制第一个矩形内的圆形
        qp.drawEllipse(self.l_x - radius // 2, self.l_y - radius // 2, radius, radius)
        # # 绘制第二个矩形内的圆形
        qp.drawEllipse(self.r_x - radius // 2, self.r_y - radius // 2, radius, radius)

    def draw_arrows(self, qp):
        pen = QPen(Qt.blue, 2)
        qp.setPen(pen)

        # 第一个矩形的中心
        center_x1 = 210
        center_y1 = 210

        # 第二个矩形的中心
        center_x2 = 640
        center_y2 = 210

        # 箭头长度
        pian = 25
        len = 47
        ad =4
        # 绘制第一个矩形的箭头
        # 向右
        arrow_head_r = QPolygon([
            QPoint(center_x1 + pian, center_y1-ad),  # A
            QPoint(center_x1 + pian+len, center_y1-ad), # B
            QPoint(center_x1 + pian+len, center_y1-2*ad), # C
            QPoint(center_x1 + pian+len+4*ad, center_y1), # D
            QPoint(center_x1 + pian+len, center_y1+2*ad), # E
            QPoint(center_x1 + pian+len, center_y1+ad), 
            QPoint(center_x1 + pian, center_y1+ad),
        ])
        qp.drawPolygon(arrow_head_r)  # 画箭头头部
        # 向左
        arrow_head_l = QPolygon([
            QPoint(center_x1 - pian, center_y1-ad),  # A
            QPoint(center_x1 - pian-len, center_y1-ad), # B
            QPoint(center_x1 - pian-len, center_y1-2*ad), # C
            QPoint(center_x1 - pian-len-4*ad, center_y1), # D
            QPoint(center_x1 - pian-len, center_y1+2*ad), # E
            QPoint(center_x1 - pian-len, center_y1+ad), 
            QPoint(center_x1 - pian, center_y1+ad),
        ])
        qp.drawPolygon(arrow_head_l)  # 画箭头头部
        # 向上
        arrow_head_u = QPolygon([
            QPoint(center_x1-ad, center_y1-pian),  # A
            QPoint(center_x1-2*ad, center_y1-pian), # B
            QPoint(center_x1, center_y1-pian-len), # C
            QPoint(center_x1+2*ad, center_y1-pian), # D
            QPoint(center_x1, center_y1-pian+len), # E
            QPoint(center_x1, center_y1-pian), 
            QPoint(center_x1-ad, center_y1-pian),
        ])
        qp.drawPolygon(arrow_head_u)  # 画箭头头部
        # 向下
        arrow_head_d = QPolygon([
            QPoint(center_x1-ad, center_y1+pian),  # A
            QPoint(center_x1-2*ad, center_y1+pian), # B
            QPoint(center_x1, center_y1+pian+len), # C
            QPoint(center_x1+2*ad, center_y1+pian), # D
            QPoint(center_x1, center_y1+pian-len), # E
            QPoint(center_x1, center_y1+pian), 
            QPoint(center_x1-ad, center_y1+pian),
        ])
        qp.drawPolygon(arrow_head_d)  # 画箭头头部

        # 绘制第二个矩形的箭头
        # 向右
        arrow_head_r = QPolygon([
            QPoint(center_x2 + pian, center_y2-ad),  # A
            QPoint(center_x2 + pian+len, center_y2-ad), # B
            QPoint(center_x2 + pian+len, center_y2-2*ad), # C
            QPoint(center_x2 + pian+len+4*ad, center_y2), # D
            QPoint(center_x2 + pian+len, center_y2+2*ad), # E            
            QPoint(center_x2 + pian+len, center_y2+ad), 
            QPoint(center_x2 + pian, center_y2+ad),
        ])
        qp.drawPolygon(arrow_head_r)  # 画箭头头部
        # 向左
        arrow_head_l = QPolygon([
            QPoint(center_x2 - pian, center_y2-ad),  # A
            QPoint(center_x2 - pian-len, center_y2-ad), # B
            QPoint(center_x2 - pian-len, center_y2-2*ad), # C
            QPoint(center_x2 - pian-len-4*ad, center_y2), # D
            QPoint(center_x2 - pian-len, center_y2+2*ad), # E
            QPoint(center_x2 - pian-len, center_y2+ad), 
            QPoint(center_x2 - pian, center_y2+ad),
        ])
        qp.drawPolygon(arrow_head_l)  # 画箭头头部
        # 向上
        arrow_head_u = QPolygon([
            QPoint(center_x2-ad, center_y2-pian),  # A
            QPoint(center_x2-2*ad, center_y2-pian), # B
            QPoint(center_x2, center_y2-pian-len), # C
            QPoint(center_x2+2*ad, center_y2-pian), # D
            QPoint(center_x2, center_y2-pian+len), # E
            QPoint(center_x2, center_y2-pian), 
            QPoint(center_x2-ad, center_y2-pian),
        ])
        qp.drawPolygon(arrow_head_u)  # 画箭头头部
        # 向下
        arrow_head_d = QPolygon([
            QPoint(center_x2-ad, center_y2+pian),  # A
            QPoint(center_x2-2*ad, center_y2+pian), # B
            QPoint(center_x2, center_y2+pian+len), # C
            QPoint(center_x2+2*ad, center_y2+pian), # D
            QPoint(center_x2, center_y2+pian-len), # E
            QPoint(center_x2, center_y2+pian), 
            QPoint(center_x2-ad, center_y2+pian),
        ])
        qp.drawPolygon(arrow_head_d)  # 画箭头头部



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawShapesWidget()
    sys.exit(app.exec_())