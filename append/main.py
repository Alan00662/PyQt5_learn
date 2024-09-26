
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import threading


class MyThread(QtCore.QThread):
    # 定义一个信号
    updated_text = QtCore.pyqtSignal(str)

    def run( self ):
        # do some work here
        self.updated_text.emit('job finished')

class Windows(QWidget):
    def __init__( self, parent = None ):
        super(Windows, self).__init__(parent)
        layout = QVBoxLayout()
        self._thread = MyThread(self)
        # 关联工作线程中的信号到此处的槽函数updateText，在updateText中完成ui的更新
        self._thread.updated_text.connect(self.updateText)

        self.browse_button = QPushButton('浏览')
        # 点击按钮，开始执行任务
        self.browse_button.clicked.connect(self._thread.start)
        layout.addWidget(self.browse_button)  # 确认升级

    def updateText( self, text ):
        # 这里对UI进行更新
        self.widget_ui.text_browser.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Windows()
    w.show()
    sys.exit(app.exec_())