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

from project.ipOnline.pack import _currency
from project.ipOnline.pack.ping_ip import ManageTheads
from project.ipOnline.ui.ip_online import Ui_Form
from project.ipOnline.ui import mtab
from project.ipOnline.pack.ip import IpState
from project.ipOnline.pack.standard_model import ContainerRow, ContainerAtModel
from project.ipOnline.pack.middle import GlobalDataUi


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
        self.init_ui()

    def init_data(self):
        """ """
        self.model = ContainerAtModel()
        self.tableview.setModel(self.model)
        self.gdata = GlobalDataUi()
        self.num = 0

    def init_layout(self):
        """ """
        h_box_1 = QHBoxLayout()
        h_box_11 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        h_box_3 = QHBoxLayout()
        # v_box_1 = QVBoxLayout()
        global_box = QVBoxLayout()


        # 第一横向Box IP范围控件
        h_box_1.addWidget(self.line_start1)
        h_box_1.addWidget(self.label_zhi)
        h_box_1.addWidget(self.line_end1)
        h_box_1.addWidget(self.btn_search1)
        spaceritem = QSpacerItem(20, 20, QSizePolicy.Expanding)
        h_box_1.addSpacerItem(spaceritem)

        # 第二横向Box IP范围控件
        h_box_11.addWidget(self.line_start2)
        h_box_11.addWidget(self.label_zhi_2)
        h_box_11.addWidget(self.line_end2)
        h_box_11.addWidget(self.btn_search2)
        h_box_11.addSpacerItem(spaceritem)

        # 第二横向Box 进度条
        h_box_2.addWidget(self.progressBar)
        h_box_2.addWidget(self.push_test)
        h_box_2.addSpacerItem(spaceritem)

        # 第三层 横向Box 表格
        h_box_3.addWidget(self.tableview)

        # 总Box开始添加各个层
        global_box.addLayout(h_box_1)
        global_box.addLayout(h_box_11)
        global_box.addLayout(h_box_2)
        global_box.addLayout(h_box_3)
        # global_box.addLayout(v_box_1)

        # 设置总Box
        self.setLayout(global_box)

    def init_ui(self):

        # 设置表格
        mtab.set_header(self.model)
        self.tableview.setColumnWidth(0, 50)

        # 进度条
        self.clear_progressBar()
        # LineEdit
        self.init_lineEdit_text()  # 初始化两个输入LineEdit
        # 搜索按键1, 2
        self.btn_search1.clicked.connect(self.on_check_on_line)
        self.btn_search2.clicked.connect(self.on_check_on_line)
        self.push_test.clicked.connect(self.on_test)
        # 隐藏test button
        # self.push_test.hide()

    def _enable_btn(self, able: bool=True):
        print("able is : {}".format(able))
        self.btn_search1.setEnabled(able)
        self.btn_search2.setEnabled(able)

    def _set_current_section(self, ip):
        sec = IpState(ip).section()
        print("sec is {}".format(sec))
        self.model.switch_section(sec)
    def on_test(self):
        """

        """
        print('on_test')
        if self.num == 1:
            start, end = self._get_start_end_ip(self.btn_search1)
            self._set_current_section(start)
            self.model.flush()

        if self.num == 0:
            self.model.current_section = '8'
            from project.ipOnline.pack.standard_model import factory_container_model_obj
            factory_container_model_obj(self.model)
            self.num += 1

    def init_ping_ip(self, start, end):

        self.manage_threads = ManageTheads()
        self.manage_threads.create_threads(start, end)
        self.manage_threads.signal_all_thread_finished.connect(self.finished_all_ths)
        self.manage_threads.signal_ip_on_line.connect(self.on_receive_ip)
        self.manage_threads.signal_one_thread_end[int, int].connect(self.update_progressbar)
        pass

    def clear_progressBar(self):
        self.progressBar.setValue(0)

    def init_lineEdit_text(self):
        self.line_start1.setText(self.gdata.start1)
        self.line_start2.setText(self.gdata.start2)
        self.line_end1.setText(self.gdata.end1)
        self.line_end2.setText(self.gdata.end2)

    def on_receive_ip(self, ip):
        """
        singal信号的槽
        作用:设置一个在线IP 所对应的IP的 背景颜色
        """
        print(" 接收到ip = {}".format(ip))
        self.model.add_ip_update_all_model(ip)
        # self.table_display()

    def _get_start_end_ip(self, btn):
        if btn == self.btn_search1:
            return self.line_start1.text(), self.line_end1.text()
        else:
            return self.line_start2.text(), self.line_end2.text()

    def _set_start_end_ip(self, btn, start, end):
        if btn == self.btn_search1:
            self.gdata.set_start_end1(start, end)
        else:
            self.gdata.set_start_end2(start, end)

    def on_check_on_line(self):
        """ 开始检查IP是否ping的通 """
        print("-------------------> on_clicked_checking_ip !")
        self._enable_btn(False)
        self.clear_progressBar()
        sender = self.sender()
        start, end = self._get_start_end_ip(sender)
        self._set_start_end_ip(sender, start, end)
        self._set_current_section(start)
        self.model.flush()
        self.init_ping_ip(start, end)

        self.manage_threads.start()

    def finished_all_ths(self):

        print("收到信号,执行槽 finished_all_ths")

        self._enable_btn(True)
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


    def closeEvent(self, a0) -> None:
        self.gdata.save_cfg()




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
