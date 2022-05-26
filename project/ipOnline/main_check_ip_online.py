# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

# import PyQt5.QtCore as PQC
from PyQt5.QtCore import pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QTableWidgetItem
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
from project.ipOnline.ui import mtab
from project.ipOnline.pack.container_ip import ContainerAt, Container, set_init_containat, IpState


# todo 检查前先清除已经变颜色的Button和让进度条归0
# todo 界面button在不同的分辨率下正常的显示
# TODO 可同时检查两个字段的IP
# TODO  IP显示改用表格显示

# todo Git 如何将一个文件之前的版本应用到本地,仅仅是之前版本的一个文件

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
        # self.compare_ip_list = CompareIpListAt()
        # self.compare_ip_list.set_flg_start_true()
        # for ip in list_ip:
        #     self.compare_ip_list.add_new(ip)

        self.containat_obj = ContainerAt()
        # self.containat_obj = set_init_containat()
        self.containat_obj.current_section = '43'

    def _get_current_section(self):
        iptt = self.lIpStart.text()
        if iptt:
            sec = IpState(iptt).section()
            self.containat_obj.current_section = sec
        return ""

    def init_layout(self):
        """ """
        h_box_1 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        h_box_3 = QHBoxLayout()
        # v_box_1 = QVBoxLayout()
        global_box = QVBoxLayout()


        # 第一横向Box IP范围控件
        h_box_1.addWidget(self.lIpStart)
        h_box_1.addWidget(self.label_zhi)
        h_box_1.addWidget(self.lIpEnd)
        h_box_1.addWidget(self.pushConfigIp)
        spaceritem = QSpacerItem(20, 20, QSizePolicy.Expanding)
        h_box_1.addSpacerItem(spaceritem)

        # 第二横向Box 进度条
        h_box_2.addWidget(self.pushCheckOneLine)
        h_box_2.addWidget(self.progressBar)
        h_box_2.addSpacerItem(spaceritem)

        # 第三层 横向Box 表格
        h_box_3.addWidget(self.tableWidget)
        # v_box_3 = Vlayout(self, self.compare_ip_list)
        # v_box_3.insert_comiplist_at()


        # 第四层 竖向Box 弹性空间
        # v_box_1.addSpacerItem(spaceritem)
        # v_box_1.addStretch(1)

        # 总Box开始添加各个层
        global_box.addLayout(h_box_1)
        global_box.addLayout(h_box_2)
        global_box.addLayout(h_box_3)
        # global_box.addLayout(v_box_1)

        # 设置总Box
        self.setLayout(global_box)

    def initUI(self):

        # 设置表格
        mtab.set_header(self.tableWidget)
        # self.create_btns()
        self.clear_progressBar()
        self.init_lineEdit_text()  # 初始化两个输入LineEdit
        self.pushConfigIp.clicked.connect(self.on_clicked_save)  # LineEdit 数据保存到配置
        self.pushCheckOneLine.clicked.connect(self.on_clicked_checking_ip)
        self.pushCheckOneLine.clicked.connect(self.table_display)


    def create_threads(self):

        self.manage_threads = ManageTheads()
        self.manage_threads.create_threads()
        self.manage_threads.signal_all_thread_finished.connect(self.finished_all_ths)
        self.manage_threads.signal_ip_on_line.connect(self.on_receive_ip)
        self.manage_threads.signal_one_thread_end[int, int].connect(self.update_progressbar)
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
        print(" 接收到ip = {}".format(ip))

        # self.on_line_ips.append(ip)
        # self.compare_ip_list.add_new(ip)
        # _, tail = currency.get_ip_sec_tail(ip)
        # self.set_btn_background_from_ip_tail(tail)
        self.containat_obj.add_ipo(ip)
        self.table_display()


    def table_display(self):
        # self.tableWidget.clearContents()
        self.tableWidget.clearContents()
        row = len(self.containat_obj.list)
        self.tableWidget.setRowCount(row)
        for row, co in self.containat_obj:
            lit_co = list(co)
            for col in range(10):
                if col < len(lit_co):
                    ipoat = lit_co[col][1]
                    val = ipoat.get_ip()
                else:
                    val = ""
                item = QTableWidgetItem(val)
                self.tableWidget.setItem(row, col, item)
            pass



    def on_clicked_checking_ip(self):
        """ 开始检查IP是否ping的通 """
        print("-------------------> on_clicked_checking_ip !")
        self.pushCheckOneLine.setEnabled(False)

        self.clear_progressBar()

        self.create_threads()

        self.manage_threads.start()

    def finished_all_ths(self):

        print("收到信号,执行槽 finished_all_ths")

        self.pushCheckOneLine.setEnabled(True)
        self.finished_threads_num = 0

        # 结束所有的th
        self.manage_threads.quit()

    def on_thread_end(self):

        print("on_thread_end")

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

    # def on_clicked_ips(self):
    #     """ 254个button通用的槽函数 """
    #     text = self.sender().text()
    #     logger.info("text = {}".format(text))
    #     pass


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
