# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

from PyQt5 import QtCore
# import PyQt5.QtCore as PQC
from PyQt5.QtCore import pyqtSignal, QCoreApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication)

from project.ipOnline.pack.middle import GlobalDataUi
from project.ipOnline.pack.ping_ip import ManageTheads
from project.ipOnline.pack.standard_model import ContainerAtModel
from project.ipOnline.ui import mtab
from .pack.middle import check_edit_text
from .ui.ip_online import Form
from ..pack.ip import IpState


class MyClass(Form):
    _startThread = pyqtSignal()
    
    def __init__(self):
        super(MyClass, self).__init__()
        
        self.manage_threads = ManageTheads()
        self.gdata = GlobalDataUi()
        self.model = ContainerAtModel()
        print('init')
        self.progressBar.setValue(0)
        self.tableview.setColumnWidth(0, 50)
        self.tableview.setModel(self.model)
        
        # 设置表格
        mtab.set_header(self.model)
        
        # LineEdit
        self.init_lineedit()  # 初始化两个输入LineEdit
    
    # -------------------------------------------------------------
    # 继承下来的槽函数
    # -------------------------------------------------------------
    @pyqtSlot()
    def on_btn_search1_clicked(self):
        print("btn1 click")
        self.on_checkip_start()
    
    @pyqtSlot()
    def on_btn_search2_clicked(self):
        print("btn2 click")
        self.on_checkip_start()
        pass
    
    @pyqtSlot()
    def on_line_end1_editingFinished(self):
        text1 = self.line_end1.text()
        
        pass
    
    @pyqtSlot()
    def on_line_end2_editingFinished(self):
        pass
    
    @pyqtSlot()
    def on_line_start1_editingFinished(self):
        self.line_edit_auto_text(self.line_start1, self.line_end1)
    
    @staticmethod
    def line_edit_auto_text(edit_s, edit_e):
        if not edit_s.hasFocus():
            return
        text = edit_s.text()
        try:
            result = check_edit_text(text, flag='start')
            if isinstance(result, tuple):
                edit_s.setText(result[0])
                edit_e.setText(result[1])
            else:
                edit_s.setText(result[0])
        except ValueError:
            pass
    
    @pyqtSlot()
    def on_line_start2_editingFinished(self):
        self.line_edit_auto_text(self.line_start2, self.line_end2)
    
    @pyqtSlot()
    def on_push_test_clicked(self):
        """
        测试按扭
        """
        print('on_test')
        start, end = self._get_start_end_ip(self.btn_search1)
        self._set_current_section(start)
        self.model.flush()
        
        self.model.current_section = '8'
        from project.ipOnline.pack.standard_model import factory_container_model_obj
        factory_container_model_obj(self.model)
        pass

    @pyqtSlot()
    def on_btn_clear_clicked(self):
        """
        清空表格
        """
        pass

    # -------------------------------------------------------------
    # 结束
    # -------------------------------------------------------------
    
    def _set_current_section(self, ip):
        sec = IpState(ip).section()
        print("sec is {}".format(sec))
        self.model.switch_section(sec)
    
    def init_ping_ip(self, start, end):
        self.manage_threads.create_threads(start, end)
        self.manage_threads.manage_signal_finishedall.connect(self.slot_finished_all_thread)
        self.manage_threads.manage_signal_send_onlineip.connect(self.slot_receive_ip)
        self.manage_threads.manage_signal_oneth_end[int, int].connect(self.update_progressbar)
    
    def init_lineedit(self) -> object:
        self.line_start1.setText(self.gdata.start1)
        self.line_start2.setText(self.gdata.start2)
        self.line_end1.setText(self.gdata.end1)
        self.line_end2.setText(self.gdata.end2)
    
    def slot_receive_ip(self, ip):
        """
        singal信号的槽
        作用:设置一个在线IP 所对应的IP的 背景颜色
        """
        print(" 接收到ip = {}".format(ip))
        self.model.add_ip_update_all_model(ip)
    
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
    
    def on_checkip_start(self):
        """ 开始检查IP是否ping的通 """
        print("-------------------> on_clicked_checking_ip !")
        self._enable_btn(False)
        self.progressBar.setValue(0)
        sender = self.sender()
        start, end = self._get_start_end_ip(sender)
        self._set_start_end_ip(sender, start, end)
        self._set_current_section(start)
        self.model.flush()
        self.init_ping_ip(start, end)
        self.manage_threads.start()
    
    def slot_finished_all_thread(self):
        print("收到信号,执行槽 finished_all_ths")
        self._enable_btn(True)
        # 结束所有的th
        self.manage_threads.quit()
        self.progressBar.setVisible(100)
        
        # no on line
        self.model.update_not_online()
        self.model.flush()
    
    def update_progressbar(self, finished_ths, sum_ths):
        # print(finished_ths, sum_ths)
        value = int(100 * finished_ths / sum_ths)
        self.progressBar.setValue(value)
    
    def closeEvent(self, a0) -> None:
        print('closeEvent')
        self.gdata.save_cfg()
    
    def _enable_btn(self, b_enable):
        b_enable = bool(b_enable)
        self.btn_search1.setEnabled(b_enable)
        self.btn_search2.setEnabled(b_enable)


def main():
    # PyQt / Qt解决分辨率不同的设备显示问题
    QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    import sys
    app = QApplication(sys.argv)
    win = MyClass()
    win.push_test.hide()
    win.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()
