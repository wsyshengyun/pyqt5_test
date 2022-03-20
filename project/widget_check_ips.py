# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton , \
    QLabel, QGridLayout
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QThread
from .pack.log import logger 
from .ui.ip_online import Ui_Form
from .pack.ping_ip import checking_ips, on_line_ips, q_ips
import time 
from .pack import currency


class Notify(QThread):
       
    signal = PQC.pyqtSignal(str)

    def __init__(self , signal=None):
        super(Notify, self).__init__()
        self.flg = True 
        # self.signal = signal
        pass 

    def stop(self):
        self.flg = False
    
    def set_flg(self):
        self.flg = True

    # def start(self, *args, **kwargs):
    #     self.flg = True
    #     logger.info("线程开启")
    #     super().start(*args, **kwargs)

    def run(self):
        while self.flg:
            ip = q_ips.get() 
            if ip != '':
                logger.info("发射信号ip = {}".format(ip))
                self.signal.emit(ip)
        else:
            logger.info("线程已经停止")
            

           
        
    

class MyClass(Ui_Form, QWidget):

    # signal = PQC.pyqtSignal(str)

    def __init__(self):

        super(MyClass, self).__init__()
        self.setupUi(self)
        self.initUI()

        # self.thread = Notify(self.signal)
        # self.signal[str].connect(self.on_receive_ip)

        self.thread = Notify()
        self.thread.signal[str].connect(self.on_receive_ip)

    def initUI(self):

        self.pushCheckOneLine.clicked.connect(self.on_clicked_check)
        self.pushConfigIp.clicked.connect(self.on_clicked_modify)
        self.btns = []
        self.onLineIps = []


        # grid 
        ips = [str(i) for i in range(2, 255)]

        positions = [(i,j) for i in range(16) for j in range(16)]

        # logger.info("ips = {}".format(ips))
        # logger.info("len(ips) = {}".format(len(ips)))
        # logger.info("list(zip(positions, ips)) = {}".format(list(zip(positions, ips))))

        for position, name in zip(positions, ips):
            button = QPushButton(name, self)
            button.clicked.connect(self.on_clicked_ips)
            self.btns.append(button)
            self.gridLayout.addWidget(button, *position)

    def on_receive_ip(self, ip):
        logger.info(" 接收到ip = {}".format(ip))
        if ip!= '0':
            self.onLineIps.append(ip)
            rection, tail = currency.split_ip(ip)
            for pushbutton in self.btns:
                self.set_pushbutton_background(pushbutton)
        else:
            self.pushCheckOneLine.setEnabled(True)
            self.thread.stop()
        pass
        

    def set_pushbutton_background(self, pushbutton:QPushButton):
        if pushbutton.text() in currency.get_ip_tails(self.onLineIps):
            pushbutton.setStyleSheet("background-color: rgb(0,255,0)") 
    

    def on_clicked_check(self):
        """ 开始检查IP是否ping的通 """
        logger.info("self.pushCheckOneLine is clicked")

        self.pushCheckOneLine.setEnabled(False)
        self.thread.start()
        checking_ips()

    
    
    def on_clicked_modify(self):

        logger.info("self.pushConfigIp is clicked")
        pass
    
    def on_clicked_ips(self):

        text = self.sender().text()
        logger.info("text = {}".format(text))
        pass


    
def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())


