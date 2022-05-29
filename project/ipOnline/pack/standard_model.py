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
        for index, ipo in self.co:
            ip_str = ipo.get_ip()
            item = QStandardItem(ip_str)
            # item.setBackground()
            color = ipo.get_color()
            print("color is : {}".format(color))
            if color:
                item.setBackground(color)

            items.append(item)
        return items



class ContainerAtModel(QStandardItemModel, ContainerAt):
    def __init__(self):
        super(ContainerAtModel, self).__init__()

    def add_ip_update_all_model(self, ip: str):
        self.removeRows(0, self.rowCount())
        # self.clear()
        # self.set_header()
        super().add_ip(ip)
        row = -1
        for co in self.list:
            row += 1
            obj = ContainerRow(co)
            items = obj.to_row_items()
            self.insertRow(row, items)
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
        HeaderLabels = ["字段", "IP1", "IP2", "IP3", "IP4", "IP5", "IP6", "IP7", "IP8", "IP9", "IP10"]
        self.setColumnCount(len(HeaderLabels))
        self.setHorizontalHeaderLabels(HeaderLabels)


def factory_container_model_obj(model = None):
    """ """
    # from project.ipOnline.pack.test_generate_ip import iplist
    from project.ipOnline.test.test_generate_ip import iplist
    if model:
        obj = model
    else:
        obj = ContainerAtModel()
    for ip in iplist:
        # obj.add_ipo(ip)
        obj.add_ip_update_all_model(ip)
    print(obj)
    return obj


if __name__ == '__main__':
    factory_container_model_obj()

