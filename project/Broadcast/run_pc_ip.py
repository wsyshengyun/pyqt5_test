#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8


import ctypes, sys
from project.Broadcast.ui_pc_ip import UI_pc_ip
from PyQt5.QtWidgets import QApplication
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # 此处添加需要获得管理员权限的os 语句
    app = QApplication(sys.argv)
    wid = UI_pc_ip()
    wid.show()
    sys.exit(app.exec_())
    # input(...)
    pass
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        # 此处添加需要获得管理员权限的os 语句
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

# if is_admin():
#     # Code of your program here
#     import sys
#     app = QApplication(sys.argv)
#     wid = UI_pc_ip()
#     wid.show()
#     sys.exit(app.exec_())
#     input(...)
#     pass
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
