import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout,QWidget,QPushButton, QGroupBox, QMainWindow

from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 400)

        self.setWindowTitle("PyQt5 布局管理")

        layout = QVBoxLayout()
        layout.addStretch(1)

        button1 = QPushButton("按钮1")
        layout.addWidget(button1)
        layout.addStretch(1)

        button2 = QPushButton("按钮2")
        layout.addWidget(button2)
        layout.addStretch(1)

        button3 = QPushButton("按钮3")
        layout.addWidget(button3)
        layout.addStretch(2)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
