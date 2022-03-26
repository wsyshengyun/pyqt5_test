# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/03/26 10:53:05

'''

from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit, QPushButton, 
        QListWidget, QTextEdit)
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from .ui.some import Ui_Form
from .pack.log import logger
import time


class TestObject(QObject):

    num = 0
    objSignal = pyqtSignal(int)

    def __init__(self):

        super(TestObject, self).__init__()
        self.flg = True
        pass

    
    def run(self):
        while self.flg:
            self.num += 1
            self.objSignal.emit(self.num)
            time.sleep(0.5)
            if self.num>10:
                self.flg = False
                break
        
    
    def run_stop(self):
        self.flg = False

    def run_start(self):
        self.flg = True
    

class MyClass(QWidget, Ui_Form):

    def __init__(self):

        super(MyClass, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):

        self.thread = QThread()
        self.worker = TestObject()

        self.worker.moveToThread(self.thread)
        self.worker.objSignal[int].connect(self.flush)
        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.finished)

        
        self.pushButton_start.clicked.connect(self.work_start)
        self.pushButton_stop.clicked.connect(self.work_stop)


        
    
    def finished(self):
        
        logger.info("finished")
        self.pushButton_start.setEnabled(True)
        
        get_thread_info(self.thread)

    


    def work_start(self, a:int):

        logger.info("wrok_start")
        self.worker.run_start()
        self.pushButton_start.setEnabled(False)
        self.thread.start()
        get_thread_info(self.thread)

        pass

    
    def work_stop(self):
        self.pushButton_start.setEnabled(True) 
        self.worker.run_stop()
        self.thread.quit()
        get_thread_info(self.thread)
        pass
        
        
    
    def flush(self, count):
        logger.info("flush , count = {}".format(count))
        self.plainTextEdit.setPlainText(str(count))
        pass
        

 
def get_thread_info(th:QThread):
    # logger.info("isRunning = {}".format(th.isRunning()))   
    # logger.info("th.isFinished() = {}".format(th.isFinished()))
    logger.info("th.currentThread() = {}".format(th.currentThread()))
    logger.info("th.currentThreadId() = {}".format(th.currentThreadId()))
    
    






def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())



