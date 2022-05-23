# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

# import PyQt5.QtCore as PQC
from PyQt5.QtCore import pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget
                            ,QVBoxLayout, QHBoxLayout, QMessageBox
                            ,QSpacerItem, QSizePolicy
                             )

from PyQt5 import QtCore

from project.ipOnline.pack import currency
from project.ipOnline.pack.currency import IP, CompareIpListAt
from project.ipOnline.pack.log import logger
from project.ipOnline.pack.ping_ip import ManageTheads
from project.ipOnline.ui.ip_online import Ui_Form
from project.ipOnline.ui.vlayout import Vlayout, HBoxlayout


# todo 检查前先清除已经变颜色的Button和让进度条归0
# todo 界面button在不同的分辨率下正常的显示
# TODO 可同时检查两个字段的IP
# TODO  IP显示改用表格显示

class MyClass(Ui_Form, QWidget):
    # signal = pyqtSignal(str)
    _startThread = pyqtSignal()

    def __init__(self):

        super(MyClass, self).__init__()
        self.setupUi(self)
        self.init_data()
        self.init_layout()
        self.initUI()

    def init_data(self):
        list_ip = [
            '192.168.1.5',
            '192.168.1.6',
            '192.168.11.6',
            '192.168.3.5',
            '192.168.3.7',
            '192.168.2.5',
            '192.168.2.6',
            '192.168.2.7',
            '192.168.2.8',
            '192.168.2.20',
            '192.168.2.9',
            '192.168.2.10',
            '192.168.2.15',
            '192.168.2.17',
            '192.168.2.16',
            '192.168.2.18',
            '192.168.2.19',
        ]
        """ """
        self.compare_ip_list = CompareIpListAt()
        self.compare_ip_list.set_flg_start_true()
        for ip in list_ip:
            self.compare_ip_list.add_new(ip)



    def init_layout(self):
        """ """
        h_box_1 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        v_box_1 = QVBoxLayout()
        v_box = QVBoxLayout()

        h_box_1.addWidget(self.lIpStart)
        h_box_1.addWidget(self.label_zhi)
        h_box_1.addWidget(self.lIpEnd)
        h_box_1.addWidget(self.pushConfigIp)
        spaceritem = QSpacerItem(20, 20, QSizePolicy.Expanding)
        h_box_1.addSpacerItem(spaceritem)

        h_box_2.addWidget(self.pushCheckOneLine)
        h_box_2.addWidget(self.progressBar)
        h_box_2.addSpacerItem(spaceritem)

        v_box_3 = Vlayout(self, self.compare_ip_list)
        v_box_3.insert_comiplist_at()

        v_box_1.addSpacerItem(spaceritem)
        v_box_1.addStretch(1)


        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addLayout(v_box_3.get_box())
        v_box.addLayout(v_box_1)

        self.setLayout(v_box)

    def initUI(self):

        # self.create_btns()


        self.clear_progressBar()

        self.on_line_ips = []
        self.init_lineEdit_text()  # 初始化两个输入LineEdit
        self.pushConfigIp.clicked.connect(self.on_clicked_save)  # LineEdit 数据保存到配置

        self.pushCheckOneLine.clicked.connect(self.on_clicked_checking_ip)

        # 生成线程
        # self.ths, self.ping_objs = create_ip_ths()
        # for ping_obj in self.ping_objs:
        #     ping_obj.send_ip_signal[str].connect(self.on_receive_ip)
        #     ping_obj.signal_check_end.connect(self.on_thread_end)

        # self.finished_threads_num = 0
        # self.create_threads()

    def create_threads(self):

        self.manage_threads = ManageTheads()
        self.manage_threads.create_threads()
        self.manage_threads.signal_all_thread_finished.connect(self.finished_all_ths)
        self.manage_threads.signal_send_ip.connect(self.on_receive_ip)
        self.manage_threads.signal_thread_end[int, int].connect(self.update_progressbar)
        pass

    def create_btns(self):

        # grid 
        btn_int = [i for i in range(255)]
        positions = [(i, j) for i in range(16) for j in range(16)]

        len_ = len(btn_int)
        self.btns = [None] * len_

        for position, i in zip(positions, btn_int):
            btn = QPushButton(str(i), self)
            # btn.setMaximumHeight(20)
            # btn.setMaximumWidth(40)
            self.gridLayout.addWidget(btn, *position)
            self.btns[i] = btn

    def _create_btns(self):

        pass

    def clear_progressBar(self):
        self.progressBar.setValue(0)

    def init_lineEdit_text(self):
        if currency.is_exists_ini_path():
            start, end = currency.get_start_ip(), currency.get_end_ip()
            self.lIpStart.setText(start)
            self.lIpEnd.setText(end)

    def on_receive_ip(self, ip):
        """
        singal信号的槽
        作用:设置一个在线IP 所对应的IP的 背景颜色
        """
        logger.info(" 接收到ip = {}".format(ip))

        self.on_line_ips.append(ip)
        self.compare_ip_list.add_new(ip)
        _, tail = currency.get_ip_sec_tail(ip)
        self.set_btn_background_from_ip_tail(tail)

    def set_btn_background_from_ip_tail(self, will_set_text, color='#00ff00'):
        """ 设置在线IP的按钮背景颜色 绿色 """
        logger.info("将要设置的btn:{}, 颜色值为{}".format(will_set_text, color))
        btn_i = int(will_set_text)
        self.btns[btn_i].setStyleSheet("background-color: %s" % color)

    def on_clicked_checking_ip(self):
        """ 开始检查IP是否ping的通 """
        logger.info("-------------------> on_clicked_checking_ip !")
        self.pushCheckOneLine.setEnabled(False)

        self.clear_progressBar()

        self.create_threads()

        self.manage_threads.start()

    def finished_all_ths(self):

        logger.info("收到信号,执行槽 finished_all_ths")

        self.pushCheckOneLine.setEnabled(True)
        self.finished_threads_num = 0

        # 结束所有的th
        self.manage_threads.quit()

    def on_thread_end(self):

        logger.info("on_thread_end")

        self.finished_threads_num += 1
        if self.finished_threads_num == len(self.ths):
            self.finished_all_ths()

    def update_progressbar(self, finished_ths, sum_ths):

        value = int(100 * finished_ths / sum_ths)
        self.progressBar.setValue(value)
        pass

    def on_clicked_save(self):
        """ 保存起始IP和终止IP的数据 """
        start = self.lIpStart.text().strip()
        end = self.lIpEnd.text().strip()
        currency.set_start_ip(start)
        currency.set_end_ip(end)
        pass

    def on_clicked_ips(self):
        """ 254个button通用的槽函数 """
        text = self.sender().text()
        logger.info("text = {}".format(text))
        pass


def main():
    # PyQt / Qt解决分辨率不同的设备显示问题
    QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
