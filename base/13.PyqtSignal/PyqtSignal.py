import sys
import time
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

class MyWindow(Qwidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(400, 300)
        ok_button = QPushButton("OK", self)
        ok_button.setGeometry(20, 100, 50, 25)
        cancel_button = QPushButton("Cancel", self)
        cancel_button.setGeometry(100, 100, 50, 25)

    def my_slot(self,msg):

    def check_msg(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyWindow()
    dialog.resize(400, 300)
    dialog.show()
    sys.exit(app.exec_())   