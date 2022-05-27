# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

# import PyQt5.QtCore as PQC
from PyQt5.QtCore import pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QTableWidgetItem, QTableWidget
                            ,QVBoxLayout, QHBoxLayout, QMessageBox
                            ,QSpacerItem, QSizePolicy
                             )

from PyQt5 import QtCore

from project.ipOnline.pack import currency
from project.ipOnline.pack.ping_ip import ManageTheads
from project.ipOnline.ui.ip_online import Ui_Form
from project.ipOnline.ui import mtab
from project.ipOnline.pack.container_ip import ContainerAt, Container, set_init_containat, IpState
from project.ipOnline.pack.standard_model import ContainerRow, ContainerAtModel


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
        """ """
        self.model = ContainerAtModel()
        self.tableWidget.setModel(self.model)
        # self.model.current_section = 12

    def _get_current_section(self):
        iptt = self.lIpStart.text()
        if iptt:
            sec = IpState(iptt).section()
            self.model.current_section = sec
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
        h_box_1.addWidget(self.comboBox_switch_ip)
        h_box_1.addWidget(self.pushConfigIp)
        h_box_1.addWidget(self.push_test)
        spaceritem = QSpacerItem(20, 20, QSizePolicy.Expanding)
        h_box_1.addSpacerItem(spaceritem)

        # 第二横向Box 进度条
        h_box_2.addWidget(self.pushCheckOneLine)
        h_box_2.addWidget(self.progressBar)
        h_box_2.addSpacerItem(spaceritem)

        # 第三层 横向Box 表格
        h_box_3.addWidget(self.tableWidget)

        # 总Box开始添加各个层
        global_box.addLayout(h_box_1)
        global_box.addLayout(h_box_2)
        global_box.addLayout(h_box_3)
        # global_box.addLayout(v_box_1)

        # 设置总Box
        self.setLayout(global_box)

    def initUI(self):

        # 设置表格
        if isinstance(self.tableWidget, QTableWidget):
            mtab.set_header(self.tableWidget)
        mtab.set_header(self.model)

        self.clear_progressBar()
        self.init_lineEdit_text()  # 初始化两个输入LineEdit
        self.pushConfigIp.clicked.connect(self.on_clicked_save)  # LineEdit 数据保存到配置
        self.pushCheckOneLine.clicked.connect(self.on_clicked_checking_ip)
        # test button
        self.push_test.clicked.connect(self.on_test)

    def on_test(self):
        """

        """



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
        self.model.add_ipoa_update_all_model(ip)
        # self.table_display()






    def on_clicked_checking_ip(self):
        """ 开始检查IP是否ping的通 """
        print("-------------------> on_clicked_checking_ip !")
        self._get_current_section()

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
