# -*- coding: utf-8 -*-
'''
@File    :   widget_check_ips.py
@Time    :   2022/03/20 14:44:28

'''

#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.



from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QTableWidgetItem, QTableWidget
                            ,QVBoxLayout, QHBoxLayout, QMessageBox
                            ,QSpacerItem, QSizePolicy
                             )
from project.ipOnline.ui.ip_online import Ui_Form


class MainWidget(Ui_Form, QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        self.init_layout()
        self.init_ui()


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
        # 设置总Box
        self.setLayout(global_box)

    def init_ui(self):
        # 设置表格
        self.tableview.setColumnWidth(0, 50)
        # 进度条
        self.clear_progressBar()
        # 隐藏test button
        # self.push_test.hide()

    def _enable_btn(self, able: bool=True):
        print("able is : {}".format(able))
        self.btn_search1.setEnabled(able)
        self.btn_search2.setEnabled(able)

    def clear_progressBar(self):
        self.progressBar.setValue(0)


def main():
    import sys
    app = QApplication(sys.argv)
    win = MainWidget()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
