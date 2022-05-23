#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem,
                             QLayout, QHBoxLayout, QVBoxLayout,QApplication,
                            QMessageBox
                             )
from project.Broadcast.ui.pcip import Ui_Form
from project.Broadcast.pack.set_pc import NetWorkCard
import project.Broadcast.pack.set_pc as pc
from project.Broadcast.ui._table import _Table


# todo 增加修改网关的功能, 和修改DNS的功能
# todo 界面适当的修改
# todo 添加IP的尾部默认值
# todo 启动界面慢的解决
# todo 增加配置文件
# todo 快捷设置IP


class UI_pc_ip(QWidget, Ui_Form):
    def __init__(self):
        super(UI_pc_ip, self).__init__()
        self.setupUi(self)
        self.init_data()
        self.init_layout()
        self.init_ui()

    def get_screen_h_w(self):
        desktop = QApplication.desktop()
        return desktop.height(), desktop.width()

    def get_self_size(self):
        s_height, s_width = self.get_screen_h_w()
        if 0 < s_height <=1024:
            return 400, 600
        elif 1024 <= s_height < 1440:
            return 500, 700
        elif 1440 <= s_height < 1920:
            return 800, 1000
        elif 1920<= s_height <=2560:
            return 1000, 1200


    def init_layout(self):
        """
        初始化布局
        """
        h_box_1 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        h_box_3 = QHBoxLayout()
        v_box_1 = QVBoxLayout()
        v_box = QVBoxLayout()
        h_box_1.addWidget(self.label_card)
        h_box_1.addWidget(self.box_card)
        h_box_2.addWidget(self.label_grate_way)
        h_box_2.addWidget(self.line_gateway)
        h_box_3.addWidget(self.btn_del)
        h_box_3.addWidget(self.btn_add)
        h_box_3.addWidget(self.pushButton)
        v_box_1.addWidget(self.table)
        v_box_1.addWidget(self.label_info)
        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addLayout(h_box_3)
        v_box.addLayout(v_box_1)
        self.setLayout(v_box)

    def init_data(self):
        self.network = pc.obj_network
        self.card = self.network.get_card_from_name()

    def init_ui(self):
        size = self.get_self_size()
        self.setGeometry(0, 0, *size)
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
        # self.pushButton.setEnabled(True)
        self.pushbutton_false()

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
        self.box_card.currentTextChanged[str].connect(self.box_current_text_changed)

        # btn 事件
        self.pushButton.clicked.connect(self.btn_clecked)
        self.btn_del.clicked.connect(self.del_one_line)
        self.btn_add.clicked.connect(self.add_one_line)

    def add_one_line(self):
        """ """
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem('192.168.0.151'))
        self.table.setItem(row_count, 1, QTableWidgetItem('255.255.255.0'))

    def del_one_line(self):
        """ """
        row_count = self.table.rowCount()
        if row_count == 1:
            # 剩余一行,不能删除
            return
        else:
            item = self.table.currentItem()
            row_num = item.row()
            self.table.removeRow(row_num)
            self.pushbutton_true()
            pass

    def box_current_text_changed(self, text):
        """ """
        self.tb.clear()
        card = self.network.get_card_from_name(text)
        if card:
            self.card = card
            pc.card = card
            datas = list(self.card.ip_subnet_tuples())
            if datas:
                self.tb.insert_datas(datas)
        else:
            return

    def btn_clecked(self):
        """ """

        # print(self.tb.get_datas())
        try:
            datas = self.tb.get_datas()
        except ValueError:
            QMessageBox.information(self, "提示", "IP格式错误", QMessageBox.Yes)
            self.pushbutton_false()
            return

        print('...sdfsdfsdf...')
        if datas:
            # 修改IP
            pc.set_ip_object = list(datas)
            text = self._box_card_text()
            pc.set_ip_object.append(text)
            print(pc.set_ip_object)
            pc.write()
            pc.get_admin_and_do(pc.set_ips_and_masks)

            # 禁止修改表格了
            self.pushbutton_false()

    def _box_card_text(self):
        text = self.box_card.currentText()
        return text

    def itemChanged(self, item: QTableWidgetItem):
        """ """
        # print(item.text())
        self.pushbutton_true()

    def pushbutton_true(self):
        self.pushButton.setEnabled(True)

    def pushbutton_false(self):
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
