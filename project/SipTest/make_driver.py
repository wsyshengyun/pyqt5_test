#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8


# def get_driver():
#     global driver
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service
options = EdgeOptions()
options.use_chromium = True
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_argument('start-maximized')
options.binary_location = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
# path_levo = r"D:\wsy\project\pyqt5_test\edgedriver\msedgedriver.exe"
# path_home = r"d:\_python\xdkj_test\edgedriver\msedgedriver.exe"
path_philips = r"E:\wsy\py_pro\pyqt5_test\edgedriver\msedgedriver.exe"
s = Service(path_philips)
driver = Edge(service=s, options=options)