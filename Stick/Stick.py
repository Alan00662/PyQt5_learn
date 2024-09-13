from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class JoystickWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.radius = 100
        self.center = self.rect().center()
        self.position = self.center

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制操纵杆
        joystick_rect = QRectF(
            self.center.x() - self.radius,
            self.center.y() - self.radius,
            2 * self.radius,
            2 * self.radius
        )
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 255, 128))
        painter.drawEllipse(joystick_rect)

        # 绘制操纵杆当前位置
        painter.setBrush(QColor(255, 0, 0, 128))
        painter.drawEllipse(self.position.x() - 10, self.position.y() - 10, 20, 20)

    def mousePressEvent(self, event):
        # 处理鼠标按下事件
        if event.button() == Qt.LeftButton:
            self.move_joystick(event.pos())

    def mouseMoveEvent(self, event):
        # 处理鼠标移动事件
        if event.buttons() & Qt.LeftButton:
            self.move_joystick(event.pos())

    def mouseReleaseEvent(self, event):
        # 处理鼠标释放事件
        if event.button() == Qt.LeftButton:
            self.move_joystick(self.center)

    def move_joystick(self, position):
        # 更新操纵杆的位置
        vec = position - self.center
        length = vec.manhattanLength()
        if length <= self.radius:
            self.position = position
        # else:
        #     self.position = self.center + vec.normalized() * self.radius

        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Joystick Demo')
        self.resize(800, 600)

        joystick_widget = JoystickWidget()

        # 将小部件添加到主窗口的布局中
        layout = QVBoxLayout()
        layout.addWidget(joystick_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
