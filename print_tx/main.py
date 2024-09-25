from PyQt5.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject
import sys
import io
import time
import threading

# 重定向标准输出
class TextRedirector(io.StringIO):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.append(message)  # 将输出追加到文本框

    def flush(self):  # 避免警告
        pass

class Worker(QObject):
    # 定义信号用于传递文本
    print_signal = pyqtSignal(str)

    def run(self):
        # 测试输出
        time.sleep(1)  # 模拟一些处理时间
        self.print_signal.emit("Hello, World!")  # 通过信号发送文本

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Print to Text Box Example')
        self.resize(400, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.display_button = QPushButton('显示')
        self.display_button.setFixedSize(100, 30)  # 设置按键的大小
        self.display_button.setStyleSheet("""
            QPushButton {
                background-color: blue;  /* 按键背景色为蓝色 */
                color: white;  /* 按键字体颜色为白色 */
                border-radius: 15px;  /* 设置为椭圆形 */
            }
            QPushButton:hover {
                background-color: gray;  /* 鼠标悬停时改为灰色 */
            }
        """)
        self.display_button.clicked.connect(self.start_thread)

        self.text_edit = QTextEdit()
        layout.addWidget(self.display_button)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

        # 重定向标准输出
        sys.stdout = TextRedirector(self.text_edit)

        # 创建工作线程
        self.worker = Worker()
        self.worker.print_signal.connect(self.update_text)  # 连接信号到槽

    def start_thread(self):
        # 改变按钮颜色为红色
        self.display_button.setStyleSheet("""
            QPushButton {
                background-color: red;  /* 按键背景色变为红色 */
                color: white;  /* 按键字体颜色为白色 */
                border-radius: 15px;  /* 设置为椭圆形 */
            }
            QPushButton:hover {
                background-color: gray;  /* 鼠标悬停时改为灰色 */
            }
        """)
        # 启动一个新的线程来发送命令
        threading.Thread(target=self.worker.run).start()

    def update_text(self, message):
        # 更新文本框
        self.text_edit.append(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()

    sys.exit(app.exec_())
