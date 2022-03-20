# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton ,QLabel, QGridLayout
from .pack.log import logger 
from .ui.ip_online import Ui_Form

class MyClass(Ui_Form, QWidget):

    def __init__(self):
        super(MyClass, self).__init__()
        self.initUI()
        self.setupUi(self)

    def initUI(self):
        
        pass

    
def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())


