#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from .mainwindow import MainWindow
from ..ipOnline.main_check_ip_online import MyClass
from ..Broadcast.mainConfigPcIp import UI_pc_ip
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDockWidget

class MainMainwindow(MainWindow):
    def __init__(self):
        
        super(MainMainwindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.actionSetConfig.triggered.connect(self.on_actionSetConfig_changed)
        self.actionSetIp.triggered.connect(self.on_actionSetIp_changed)
        self.online_wiget = MyClass()
        self.setCentralWidget(self.online_wiget)
        
        # dockwidget
        # setip_widget = UI_pc_ip()
        # self.items = QDockWidget("setip", self)
        # self.items.setWidget(setip_widget)
        # self.items.setFloating(False)
        #
        # self.addDockWidget(Qt.RightDockWidgetArea, self.items)

    def on_actionSetConfig_changed(self):
        return super().on_actionSetConfig_changed()

    def on_actionSetIp_changed(self):
        self.setip_widget = UI_pc_ip()
        self.setip_widget.show()
        
    def closeEvent(self, a0) -> None:
        self.online_wiget.closeEvent(a0)
        # super(MainMainwindow, self).closeEvent(a0)

def main():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainMainwindow()
    win.show()
    app.exec_()


main()
