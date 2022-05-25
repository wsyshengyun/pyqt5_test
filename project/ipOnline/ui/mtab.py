#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import  QTableWidget, QTableWidgetItem

# HeaderLabels = ["字段", "IP1", "IP2", "IP3", "IP4", "IP5", "IP6", "IP7", "IP8", "IP9", "IP10"]
HeaderLabels = ["IP1", "IP2", "IP3", "IP4", "IP5", "IP6", "IP7", "IP8", "IP9", "IP10"]
table_column_count = 11


def set_header(table: QTableWidget):
    # todo 表格只显示了一半,怎么设置显示合适的宽度,把表头的IP显示完
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(True)
    table.setColumnCount(len(HeaderLabels))
    table.setHorizontalHeaderLabels(HeaderLabels)
    table.setRowCount(2)
