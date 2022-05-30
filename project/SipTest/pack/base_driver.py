# coding:utf8


from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service
import time
import os


class BaseDriver(object):
    def __init__(self, path=None):
        """ """
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument('start-maximized')
        s = Service(path)
        self.driver = Edge(service=s, options=options)
        # self.driver = Edge(executable_path=path, options=options)

    @staticmethod
    def get_url(ip):
        return 'http://' + str(ip)

    def max_windows(self):
        self.driver.maximize_window()

    def path_other(self):
        # current_path = os.path.dirname(__file__)  # 获取当前的路径
        # driver_path = os.path.join(current_path, '../driver/chromedriver.exe')  # 当前路径 + chromedriver路径相连
        pass

    def set_other(self, options):
        # service_args = ['--verbose']
        # driver = webdriver.Edge(service_args = service_args)
        # 最大化窗口
        options.add_argument('start-maximized')
        # 最小化窗口
        options.add_argument('start-minimized')
        # F11 全屏
        options.add_argument('start-fullscreen')
        # 无窗口运行
        options.add_argument("headless")







def main():
    """ """
    obj = BaseDriver(path=r"D:\wsy\project\pyqt5_test\edgedriver\msedgedriver.exe")
    ip = '192.168.0.246'
    # ip = '192.168.9.69'
    obj.run(ip=ip)

    while(1):
        time.sleep(2)

if __name__ == '__main__':
    main()


