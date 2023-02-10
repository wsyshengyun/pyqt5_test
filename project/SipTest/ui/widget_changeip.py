#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox
from project.SipTest.ui.ui_changeip import Ui_Form
from project.ipOnline.pack._currency import IpState
from project.SipTest.pack.modify_sip_config import ManageConfigFile
from project.SipTest.ui.widget_set import WidgetSet


class WidgetChangeIp(QWidget, Ui_Form):
    def __init__(self):
        """ """
        super(WidgetChangeIp, self).__init__()
        self.setupUi(self)
        self.currip = None
        self.init_data()

    def init_data(self):
        self.currip = None
        ip = ManageConfigFile().ip
        self.set_currip(ip)
        self.btn_last.clicked.connect(self.on_btn_last_ip)
        self.btn_next.clicked.connect(self.on_btn_next_ip)
        self.btn_save_config.clicked.connect(self.on_btn_save_config)
        self.btn_set.clicked.connect(self.on_btn_set)
        pass

    def set_currip(self, ip):
        self.currip = ip
        self.line_currip.setText(self.currip)

    def on_btn_set(self):
        """
        功能：弹出设置窗口
        """
        self.dia = WidgetSet()
        self.dia.show()
        # dia.exec()


    def on_btn_save_config(self):
        obj = ManageConfigFile()
        obj.update_ip(self.currip)
        try:
            obj.write()
            self.label_info.setText("保存成功！")
            font = self.label_info.font()
            print("font style is : {}".format(font.style()))
            # QMessageBox.about(self, "提示", "保存成功！")
        except:
            self.label_info.setText("保存失败！")
            pass

    def on_btn_next_ip(self):
        if self.currip:
            next_ip = IpState(self.currip).next_ip()
            self.set_currip(next_ip)
        pass

    def on_btn_last_ip(self):
        if self.currip:
            last_ip = IpState(self.currip).last_ip()
            self.set_currip(last_ip)
        pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = WidgetChangeIp()
    window.show()
    sys.exit(app.exec())