import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_button = QPushButton("OK", self)
        ok_button.setGeometry(20, 100, 50, 25)
        cancel_button = QPushButton("Cancel", self)
        cancel_button.setGeometry(100, 100, 50, 25)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.resize(400, 300)
    dialog.show()
    sys.exit(app.exec_())   