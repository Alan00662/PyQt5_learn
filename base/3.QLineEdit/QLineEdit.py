import sys

# PyQt5
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit

# 创建一个应用对象
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(800, 600)
    window.setWindowTitle('QLineEdit Example')

    label = QLabel("账号", window)
    label.setGeometry(20, 20, 30, 30)

    lineEdit = QLineEdit(window)
    lineEdit.setPlaceholderText("请输入账号")
    lineEdit.setGeometry(55, 20, 200, 30)

    button = QPushButton("登录", window)
    button.setGeometry(50, 80, 70, 30)

    window.show()
    app.exec_()