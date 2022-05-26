# coding:utf8

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from project.ipOnline.ui.test_view_standard import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication

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
