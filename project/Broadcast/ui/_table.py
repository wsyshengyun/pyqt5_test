#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget , QApplication ,QPushButton \
     , QHBoxLayout

class _Table(object):

    def __init__(self, table: QTableWidget):
        """ """
        self.tw = table

    def set_header(self, HorizontalLabel: list):
        self.tw.horizontalHeader().setVisible(True)
        self.tw.verticalHeader().setVisible(False)
        column_count = len(HorizontalLabel)
        self.tw.setColumnCount(column_count)
        # HorizontalLabel.append("操作")
        self.tw.setHorizontalHeaderLabels(HorizontalLabel)

    def set_row_column(self, num):
        self.tw.setRowCount(num)

    def count_column(self):
        return self.tw.columnCount()

    def insert_datas(self, datas: list):
        int_rows = len(datas)
        if int_rows < 1 : return
        self.set_row_column(int_rows)

        len_datas = len(datas[0])

        for row in range(int_rows):
            for col in range(self.count_column()):
                # if col == len_datas:
                #     control = self.create_control()
                #     self.tw.setCellWidget(row, col, control)
                # else:
                str_data = datas[row][col]
                item = QTableWidgetItem(str_data)
                self.tw.setItem(row, col, item)

    def ___create_control(self):
        box = QHBoxLayout(self.tw)
        btn_up = QPushButton("向上")
        btn_down = QPushButton("向下")
        btn_del = QPushButton("删除")
        box.addWidget(btn_up)
        box.addWidget(btn_down)
        box.addWidget(btn_del)
        return box


    def get_datas(self):
        """ """
        int_rows = self.tw.rowCount()
        int_cols = self.count_column()

        ips = []
        masks = []

        for row in range(int_rows):
            data = self.tw.item(row, 0).text()
            ips.append(data)

        for row in range(int_rows):
            data = self.tw.item(row, 1).text()
            masks.append(data)

        return ips, masks


    def clear(self):
        # self.tw.clear()
        self.tw.clearContents()








if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dia = _Table()
    dia.show()
    sys.exit(app.exec_())
