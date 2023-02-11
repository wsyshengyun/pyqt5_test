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


def main( ):
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()