#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.desktop = QApplication.desktop()

        # 获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        print(self.height)
        print(self.width)

        # 显示窗口
        self.show()

def get_screen_rect():
    import sys
    desktop = QApplication.desktop()
    return desktop.height(), desktop,widget
    # rect = desktop.screenGeometry()
    # height = rect.height()
    # widget = rect.width()
    # return height, widget

if __name__ == '__main__':
    # 创建应用程序和对象
    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())

    print(get_screen_rect())
