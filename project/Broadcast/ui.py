# coding:utf8

#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
                             QApplication)
from PyQt5.QtCore import pyqtSignal
from project.Broadcast.ui.widget import Ui_Form
from project.Broadcast.middle import OneIp
from project.Broadcast.configat import MySocket


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        """ """
        # super.__init__(self)   # error
        # super.__init__()   # error
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.init_data()
        self.init()

    def init_data(self):
        self.one_ip = OneIp()
        self.sock = MySocket()
        self.sock.set_purpose_ip(self.one_ip)

    def init(self):
        self.Next.clicked.connect(self.next_ip)
        self.Send.clicked.connect(self.send_ip)
        pass

    def next_ip(self):
        print('next_ip')
        next_ip = self.one_ip.next_ip()
        self.Ip.setText(next_ip)

        pass

    def send_ip(self):
        """ """
        # set one_ip
        ip = self.Ip.text().strip()
        port = self.Port.text().strip()
        try:
            self.one_ip.set_ip(ip)
        except ValueError:
            return
        self.one_ip.set_port(port)

        #
        # self.Sends_listView
        #

        #
        data, addr = self.sock.send_ip_message()

        print('send_ip')

    def Ip_edit_finish(self):
        ip = self.Ip.text().strip()
        ip = str(ip)
        self.one_ip.set_ip(ip)
        print('IP edit finish')
        pass


# if __name__ == '__main__':
import sys
app = QApplication(sys.argv)
wid = MyWidget()
wid.show()
sys.exit(app.exec_())
