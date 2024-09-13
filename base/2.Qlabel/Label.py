import sys

# PyQt5
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel

# 创建一个应用对象
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(400, 300)
    window.setWindowTitle('QLabel Example')

    label = QLabel("账号", window)
    label.setGeometry(200, 20, 30, 30)
    button = QPushButton("登录")
    button.clicked.connect(lambda: print("按钮被点击了"))
    button.setParent(window)

    window.show()
    app.exec_()