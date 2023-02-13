# coding:utf8

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QColor
from project.ipOnline.pack.container_ip import ContainerAt, Container


class ContainerRow(object):
    def __init__(self, co: Container):
        self.co = co

    def to_row_items(self):
        items = []
        first = QStandardItem("字段{}".format(self.co.section))
        items.append(first)
        for _, ipo in self.co:
            # ip_str = ipo.get_ip()
            ip_str = ipo.ip
            item = QStandardItem(ip_str)
            color = ipo.get_color()
            if color:
                item.setBackground(color)

            items.append(item)
        return items


class ContainerAtModel(QStandardItemModel, ContainerAt):
    def __init__(self) -> object:
        super(ContainerAtModel, self).__init__()

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
            
    def clear(self):
        self.list = []
        self.reset_data()
        self.flush()

    def set_header(self):
        header_labels = ["字段", "IP1", "IP2", "IP3", "IP4", "IP5", "IP6", "IP7", "IP8", "IP9", "IP10"]
        self.setColumnCount(len(header_labels))
        self.setHorizontalHeaderLabels(header_labels)


def factory_container_model_obj(model = None):
    """ """
    # from project.ipOnline.test.test_generate_ip import iplist
    # if model:
    #     obj = model
    # else:
    #     obj = ContainerAtModel()
    # for ip in iplist:
    #     obj.add_ip_update_all_model(ip)
    # print(obj)
    # return obj
    pass


if __name__ == '__main__':
    factory_container_model_obj()

