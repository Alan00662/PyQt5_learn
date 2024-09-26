import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class PrintThread(QThread):
    text_signal = pyqtSignal(str)  # 创建信号槽

    def run(self):
        while True:
            line = "这是来自print的内容：" + str(print())  # 模拟print输出
            self.text_signal.emit(line)  # 发送信号到主线程

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.setCentralWidget(self.text_edit)

        self.print_thread = PrintThread()
        self.print_thread.text_signal.connect(self.update_text)  # 连接信号到槽
        self.print_thread.start()

    def update_text(self, text):  # 更新文本的方法
        self.text_edit.append(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())