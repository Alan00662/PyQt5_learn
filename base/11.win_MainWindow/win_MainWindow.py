import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("这是文字~~")
        label.setStyleSheet("font-size:30px;color:red")

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        
        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")
        file_menu.addAction("另存为")
        file_menu.addAction("退出")
        

        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("撤销")
        edit_menu.addAction("恢复")
        edit_menu.addAction("复制")
        edit_menu.addAction("粘贴")
        edit_menu.addAction("查找")
        edit_menu.addAction("替换")

        view_menu = menu.addMenu("视图")
        view_menu.addAction("显示工具栏")
        view_menu.addAction("显示状态栏")

        help_menu = menu.addMenu("帮助")
        help_menu.addAction("关于") 

        # 设置中心内容显示
        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 设置窗口标题
    w.setWindowTitle("我是窗口标题....")
    w.resize(400, 300)
    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()
