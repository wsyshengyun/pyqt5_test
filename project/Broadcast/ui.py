# coding:utf8

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
                             QApplication)
from PyQt5.QtCore import  pyqtSignal
from project.Broadcast.ui.widget import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        """ """
        # super.__init__(self)   # error
        # super.__init__()   # error
        super(MyWidget, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wid = MyWidget()
    wid.show()
    sys.exit(app.exec_())


