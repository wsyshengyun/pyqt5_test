# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionSetConfig.triggered.connect(self.on_actionSetConfig_changed)
        self.actionSetIp.triggered.connect(self.on_actionSetIp_changed)

        
    
    @pyqtSlot()
    def on_actionSetIp_changed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("on set ip")
        # raise NotImplementedError
    
    @pyqtSlot()
    def on_actionSetConfig_changed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("on set config")
        # raise NotImplementedError
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()