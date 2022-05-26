# coding:utf8

from PyQt5.QtGui import QStandardItemModel, QStandardItem
# from .container_ip import ContainerAt, Container, IpState
from project.ipOnline.pack.container_ip import ContainerAt, Container, IpState
from project.ipOnline.pack.test_generate_ip import iplist


class ContainerRow(object):
    def __init__(self, co: Container):
        self.co = co

    def to_row_items(self):
        items = []
        first = QStandardItem("字段{}".format(self.co.section))
        items.append(first)
        for index, ipo in self.co:
            ip_str = ipo.get_ip()
            items.append(QStandardItem(ip_str))
        return items






class ContainerAtModel(QStandardItemModel, ContainerAt):
    def __init__(self):
        super(ContainerAtModel, self).__init__()


    def add_ipo(self, ipoat: IpState):
        row, col, obj = super().add_ipo(ipoat)

        if col == 0:
            # 新的横向容器
            items = ContainerRow(obj).to_row_items()
            self.insertRow(row, items)
        else:
            # 先删除一行, 在插入一行
            self.removeRow(row)
            items = ContainerRow(obj).to_row_items()
            self.insertRow(row, items)





def factory_container_model_obj():
    """ """
    obj = ContainerAtModel()
    for ip in iplist:
        obj.add_ipo(ip)
    print(obj)
    return obj


if __name__ == '__main__':
    factory_container_model_obj()

