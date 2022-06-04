#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFileDialog
from project.SipTest.ui.ui_set import Ui_Form
from project.SipTest.pack.data import get_config, set_config, config_dict
from project.SipTest.pack.modify_sip_config import ManageConfigFile


class WidgetSet(QWidget, Ui_Form):
    def __init__(self):
        """ """
        super(WidgetSet, self).__init__()
        self.setupUi(self)
        self.config_dict = None
        self.init_data()

    def init_data(self):
        self.btn_ok.clicked.connect(self.on_btn_ok)
        self.btn_open.clicked.connect(self.on_btn_open)
        self.config_dict = config_dict
        get_config()
        self.line_cfg_path.setText(self.config_dict.get('path_config'))
        self.line_ip_section.setText(self.config_dict.get('ip_section'))
        self.line_ip_start.setText(self.config_dict.get('ip_start'))
        self.line_ip_step.setText(self.config_dict.get('ip_step'))
        self.line_sip_ip.setText(self.config_dict.get('sip_service'))

    def on_btn_open(self):
        """

        """
        # 打开选择文件对话框
        # 把路径定位到桌面
        fd = QFileDialog(
            # self, "选择SIP配置文件", "./", "ALL(*, *);;Images(*.png *.jpg);;Python文件(*.py)"
            self, "选择SIP配置文件", "./", "txt文件(*.txt);;Images(*.png *.jpg);;Python文件(*.py)"
        )
        # -------接收模式-----------
        fd.setAcceptMode(QFileDialog.AcceptOpen)  # 打开
        # fd.setAcceptMode(QFileDialog.AcceptSave)  # 保存
        # ------默认后缀名----------
        fd.setDefaultSuffix("txt")
        # ------设置文件模式--------
        fd.setFileMode(QFileDialog.AnyFile)  # 任何文件
        # fd.setFileMode(QFileDialog.ExistingFile)  # 存在的文件（单个）
        # fd.setFileMode(QFileDialog.ExistingFiles)  # 存在的文件（多个）
        # fd.setFileMode(QFileDialog.Directory)  # 目录
        fd.open()
        fd.fileSelected[str].connect(self.open_file)

    def open_file(self, path_file):
        self.line_cfg_path.setText(path_file)
        # 保存路径到配置文件里面
        self.config_dict['path_config'] = path_file
        set_config()

        # 读取文件内容， 分析文件内容，把结果显示在text框里面
        manage = ManageConfigFile(path_file)
        self.textEdit_2.setText(manage.get_config_info())

    def on_btn_ok(self):
        """

        """
        # 保存数据
        # 关闭窗口


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = WidgetSet()
    window.show()
    sys.exit(app.exec())


