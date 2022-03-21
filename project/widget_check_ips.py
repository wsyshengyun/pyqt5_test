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
            time.sleep(0.01) 
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

        self.set_start_end_lineEdit()
        self.pushConfigIp.clicked.connect(self.on_clicked_save)

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
    
    def set_start_end_lineEdit(self):
        if currency.is_exists_ini_path():
            start, end = currency.get_start_ip(), currency.get_end_ip()
            self.lIpStart.setText(start)
            self.lIpEnd.setText(end)

    def on_receive_ip(self, ip):
        """ singal信号的槽 """
        logger.info(" 接收到ip = {}".format(ip))
        if ip!= '0':
            self.onLineIps.append(ip)
            rection, tail = currency.get_ip_sec_tail(ip)
            self.set_pushbutton_background(tail)
        else:
            self.pushCheckOneLine.setEnabled(True)
            self.thread.stop()
        pass
        

    def set_pushbutton_background(self, will_set_text, color = '#00ff00'):
        """ 设置在线IP的按钮背景颜色 绿色 """
        for pushbutton in self.btns:
            if pushbutton.text()  ==  will_set_text:
                logger.info("将要设置的btn:{}, 颜色值为{}".format(will_set_text ,color))
                pushbutton.setStyleSheet("background-color: %s" % color) 
    

    def reset_some(self):
        logger.info("-------------->reset_some")
        q_ips.queue.clear()

        for ip in self.onLineIps:
            sec, tail = currency.get_ip_sec_tail(ip)
            self.set_pushbutton_background(tail, color='#ff0000')
        self.onLineIps.clear()


    def on_clicked_check(self):
        """ 开始检查IP是否ping的通 """
        logger.info("-------------------> on_clicked_check !")

        self.reset_some()

        self.pushCheckOneLine.setEnabled(False)
        self.thread.set_flg()   # flg = True
        self.thread.start()
        logger.info("开始检测")
        checking_ips()

    
    def on_clicked_modify(self):
        """ modify enable ip range 0 - 255 or other """
        logger.info("self.pushConfigIp is clicked")
        pass
    

    def on_clicked_ips(self):
        """ 254个button通用的槽函数 """
        text = self.sender().text()
        logger.info("text = {}".format(text))
        pass

    
    def on_clicked_save(self):
        start = self.lIpStart.text().strip()
        end = self.lIpEnd.text().strip()
        currency.set_start_ip(start)
        currency.set_end_ip(end)
        pass
    
     


    
def main():
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())


