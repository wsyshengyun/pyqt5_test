# -*- coding: utf-8 -*-
'''
@File    :   learn_signal_map.py
@Time    :   2022/03/27 23:49:12

'''

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton
from PyQt5.QtCore import QSignalMapper


from pack.log import logger
from .ui.ui_learn_signal_map import Ui_Form

class MyClass(QWidget, Ui_Form):

    def __init__(self):
        super(MyClass, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setLayout(self.verticalLayout)

        self.mapper = QSignalMapper(self)
        
        self.create_btns()
        
        pass

    
    def create_btns(self):
        self.btns = []
        for i in range(5):
            btn = QPushButton(str(i), self)
            self.verticalLayout.addWidget(btn)
            self.btns.append(btn)

            btn.clicked.connect(self.mapper.map) 

            if i%2 ==0:
                self.mapper.setMapping(btn, str(i))
            else:
                self.mapper.setMapping(btn, int(i))

        self.mapper.mapped[str].connect(self.string_mapped)
        self.mapper.mapped[int].connect(self.int_mapped)
            

    
    def string_mapped(self, value):

        logger.info("stringMapped, {}".format(value))
        pass
        
    
    def int_mapped(self,value):
        
        logger.info("intMapped, {}".format(value))
        pass
        
        
        
            
        
        
    


def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())