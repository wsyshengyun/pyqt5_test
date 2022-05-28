# coding:utf8

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QColor
from project.ipOnline.pack.container_ip import ContainerAt, Container, IpState


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


    # def add_ip(self, ip: IpState):
    #     row, col, obj = super().add_ip(ip)
    #
    #     if col == 0:
    #         # 新的横向容器
    #         items = ContainerRow(obj).to_row_items()
    #         self.insertRow(row, items)
    #     else:
    #         # 先删除一行, 在插入一行
    #         self.removeRow(row)
    #         items = ContainerRow(obj).to_row_items()
    #         self.insertRow(row, items)

    def add_ip_update_all_model(self, ip: str):
        self.clear()
        super().add_ip(ip)
        row = -1
        for co in self.list:
            # for col, ipoat_ in co:
            #     item = QStandardItem(ipoat_.get_ip())
            #     self.setItem(row, col, item)
            row += 1
            obj = ContainerRow(co)
            items = obj.to_row_items()
            self.insertRow(row, items)
        pass





def factory_container_model_obj(model = None):
    """ """
    from project.ipOnline.pack.test_generate_ip import iplist
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

