import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QFormLayout


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QFormLayout')
        # 设定当前Widget的宽高(可以拉伸大小)
        # self.resize(300, 200)
        # 禁止改变宽高（不可以拉伸）
        self.setFixedSize(300, 150)

        container = QVBoxLayout()
        form_layout = QFormLayout()

        edit1 = QLineEdit()
        edit1.setPlaceholderText('请输入用户名')
        form_layout.addRow('用户名', edit1)

        edit2 = QLineEdit()
        edit2.setPlaceholderText('请输入密码')
        form_layout.addRow('密码', edit2)

        container.addLayout(form_layout)

        button_login = QPushButton('登录')
        button_login.setFixedSize(100, 30)

        container.addWidget(button_login, alignment=Qt.AlignRight)

        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec()
