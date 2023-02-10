# coding:utf8

from project.ipOnline.pack.container_ip import ContainerAt, Container
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from project.ipOnline.ui.test_view_standard import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class ContainerRow(object):
    def __init__(self, co: Container):
        self.co = co

    def to_row_items(self):
        items = []
        first = QStandardItem("字段{}".format(self.co.section))
        items.append(first)
        for _, ipo in self.co:
            ip_str = ipo.get_ip()
            item = QStandardItem(ip_str)
            color = ipo.get_color()
            if color:
                item.setBackground(color)

            items.append(item)
        return items


class ContainerAtModel(QStandardItemModel, ContainerAt):
    def __init__(self):

    def add_ip_update_all_model(self, ip: str):
        self.removeRows(0, self.rowCount())
        super().add_ip(ip)
        row = 0
        for co in self.list:
            obj = ContainerRow(co)
            items = obj.to_row_items()
            self.insertRow(row, items)
            row += 1
        pass

    def flush(self):
        # self.clear()
        self.removeRows(0, self.rowCount())
        # self.set_header()
        for co in self.list:
            obj = ContainerRow(co)
            items = obj.to_row_items()
            self.appendRow(items)

    def set_header(self):
        header_labels = ["字段", "IP1", "IP2", "IP3", "IP4", "IP5", "IP6", "IP7", "IP8", "IP9", "IP10"]
        self.setColumnCount(len(header_labels))
        self.setHorizontalHeaderLabels(header_labels)


def factory_container_model_obj(model = None):
    """ """
    from project.ipOnline.test.test_generate_ip import iplist
    if model:
        obj = model
    else:
        obj = ContainerAtModel()
    for ip in iplist:
        obj.add_ip_update_all_model(ip)
    print(obj)
    return obj


if __name__ == '__main__':
    factory_container_model_obj()
        super(MyStandardModel, self).__init__()
        self.init()


    def init(self):
        self.setHorizontalHeaderLabels(["L1", "L2", "L3"])
        self.setRowCount(10)
        self._data()

        pass

    def _data(self):
        """

        """
        for i in range(10):
            for j in range(3):
                self.setItem(i, j, QStandardItem(str((i,j))))




def factory_standard_item_model():
    obj = MyStandardModel()
    return obj




class MyUi(QWidget, Ui_Form):
    def __init__(self):
        """ """
        super(MyUi, self).__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.model = factory_standard_item_model()
        self.tableView.setModel(self.model)

    def on_clicked_btn(self):
        print('nihao')
        item = QStandardItem()
        lit_str = ['name1', 'name2' ]
        list_item = [QStandardItem(item_str) for item_str in lit_str]
        # self.model.appendRow(list_item)
        self.model.insertRow(2, list_item)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dia = MyUi()
    dia.show()
    sys.exit(app.exec())


    pass
