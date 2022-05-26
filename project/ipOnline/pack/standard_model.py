# coding:utf8

from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MyStandardModel(QStandardItemModel):
    def __init__(self):
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
