from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib.pyplot as plt
import numpy as np


# class JoystickWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setMinimumSize(200, 200)
#         self.radius = 100
#         self.center = self.rect().center()
#         self.position = self.center

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # 绘制操纵杆
#         joystick_rect = QRectF(
#             self.center.x() - self.radius,
#             self.center.y() - self.radius,
#             2 * self.radius,
#             2 * self.radius
#         )
#         painter.setPen(Qt.NoPen)
#         painter.setBrush(QColor(0, 0, 255, 128))
#         painter.drawEllipse(joystick_rect)

#         # 绘制操纵杆当前位置
#         painter.setBrush(QColor(255, 0, 0, 128))
#         painter.drawEllipse(self.position.x() - 10, self.position.y() - 10, 20, 20)

#     def mousePressEvent(self, event):
#         # 处理鼠标按下事件
#         if event.button() == Qt.LeftButton:
#             self.move_joystick(event.pos())

#     def mouseMoveEvent(self, event):
#         # 处理鼠标移动事件
#         if event.buttons() & Qt.LeftButton:
#             self.move_joystick(event.pos())

#     def mouseReleaseEvent(self, event):
#         # 处理鼠标释放事件
#         if event.button() == Qt.LeftButton:
#             self.move_joystick(self.center)

#     def move_joystick(self, position):
#         # 更新操纵杆的位置
#         vec = position - self.center
#         length = vec.manhattanLength()
#         if length <= self.radius:
#             self.position = position
#         else:
#             self.position = self.center + vec.normalized() * self.radius

#         self.update()

    


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Joystick Demo')
#         self.resize(800, 600)

#         joystick_widget = JoystickWidget()

#         # 将小部件添加到主窗口的布局中
#         layout = QVBoxLayout()
#         layout.addWidget(joystick_widget)

#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

def draw_joystick(left_x, left_y, right_x, right_y):
    fig, ax = plt.subplots()
    fig, bx = plt.subplots()
    c1_x = 3
    c1_y = 3
    r1 = 3
    
    c2_x = 15
    c2_y = 3
    r2 = 3
    # 绘制背景
    # 绘制左摇杆
    left_circle = plt.Circle((c1_x, c1_y), r1, color='blue', alpha=0.5)
    ax.add_artist(left_circle)
    ax.plot([c1_x, c1_x + left_x], [c1_y, c1_y + left_y], color='blue', lw=2)  # 左摇杆指向
    # 绘制右摇杆
    right_circle = plt.Circle((c2_x, c2_y), 3, color='red', alpha=0.5)
    bx.add_artist(right_circle)
    bx.plot([c2_x, c2_x + right_x ], [c2_y, c2_y + right_y ], color='red', lw=2)  # 右摇杆指向
    # 设置坐标轴
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    #     # 设置坐标轴
    # bx.set_xlim(20, 20)
    # bx.set_ylim(20, 20)
    # bx.set_xticks([])
    # bx.set_yticks([])
    # bx.set_aspect('equal')

    plt.title('Joystick Representation')
    plt.grid(False)
    plt.show()


if __name__ == '__main__':
    draw_joystick(1,1,2,2)  # 左摇杆指向(1,1) 右摇杆指向(2,2)
