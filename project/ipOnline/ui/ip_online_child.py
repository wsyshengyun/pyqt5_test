#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from .ip_online import Form

class MyForm(Form):
    def __init__(self):
        
        super(MyForm, self).__init__()

    def on_btn_search1_clicked(self):
        pass

    def on_btn_search2_clicked(self):
        pass

    def on_line_end1_editingFinished(self):
        pass

    def on_line_end2_editingFinished(self):
        pass

    def on_line_start1_editingFinished(self):
        pass

    def on_line_start2_editingFinished(self):
        pass

    def on_push_test_clicked(self):
        pass


def main():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()