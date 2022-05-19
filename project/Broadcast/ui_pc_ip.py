#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem,
                             QApplication)
from project.Broadcast.ui.pcip import Ui_Form
from project.Broadcast.pack.set_pc import NetWorkCard
import project.Broadcast.pack.set_pc as pc
from project.Broadcast.ui._table import _Table


class UI_pc_ip(QWidget, Ui_Form):
    def __init__(self):
        super(UI_pc_ip, self).__init__()
        self.setupUi(self)
        self.init_data()
        self.init_ui()

    def init_data(self):
        self.network = pc.obj_network
        self.card = pc.card

    def init_ui(self):
        # 初始化列表框
        default = self.card.get_name()
        names: list = list(self.network.get_card_names())
        if default in names:
            names.remove(default)
        names.insert(0, default)

        for name in names:
            self.box_card.addItem(name)
        pass

        # 初始化默认IP
        self.line_gateway.setText(self.card.gateway())

        # 初始化button
        self.pushButton.setEnabled(True)

        # 初始化表格
        self.tb = _Table(self.table)
        HeaderLabels = ['IP', '子网掩码']
        self.tb.set_header(HeaderLabels)

        # datas = [('a', '1', ''), ('d', '2', ''), ('c', '3', ''), ('b', '4', 'nihao')]
        datas = self.card.ip_subnet_tuples()
        datas = list(datas)
        self.tb.insert_datas(datas)

        # 事件
        self.table.itemChanged[QTableWidgetItem].connect(self.itemChanged)

        # btn 事件
        self.pushButton.clicked.connect(self.btn_clecked)

    def btn_clecked(self):
        """ """

        # print(self.tb.get_datas())
        datas = self.tb.get_datas()
        if datas:
            # 修改IP
            print(*datas)
            # inner()
            # self.card.set_ip_and_mask(*datas)
            pc.set_ip_object = datas
            pc.write()
            # pc.set_ips_and_masks()
            pc.get_admin_and_do(pc.set_ips_and_masks)

            # 禁止修改表格了
            self.btn_false()

    def itemChanged(self, item: QTableWidgetItem):
        """ """
        # print(item.text())
        self.btn_true()

    def btn_true(self):
        self.pushButton.setEnabled(True)

    def btn_false(self):
        self.pushButton.setEnabled(False)


if __name__ == '__main__':
    import sys
    # import ctypes
    # print('++++++++++++++++++++++')
    # if not ctypes.windll.shell32.IsUserAnAdmin():
    #     print('..............')
    #     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 0)
    # print('-----------')
    app = QApplication(sys.argv)
    wid = UI_pc_ip()
    wid.show()
    sys.exit(app.exec_())
