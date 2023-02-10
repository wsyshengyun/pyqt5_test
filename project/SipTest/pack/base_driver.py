# coding:utf8


from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
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


class BasePage(BaseDriver):
    # def __init__(self, driver):
    #     """ """
    #     self.drver = driver

    def find_element(self, loc):
        try:
            WebDriverWait(self.drver, 15).until(lambda driver: driver.find_element(*loc).is_display())
            return self.drver.find_element(*loc)
        except:
            print("没有找到元素")
            return None

    def clear_key(self, loc):
        """
        重写清空文本框
        """
        time.sleep(3)
        self.find_element(loc).clear()

    def send_keys(self, loc, value):
        """
        loc: (id, "name")
        """

        self.clear_key(loc)
        self.find_element(loc).send_keys(value)

    def click_button(self, loc):
        """
        点击按钮
        """
        self.find_element(loc).click()

    def switch_to_frame(self, value):
        """
        进入iframe页面
        """
        self.driver.switch_to.frame(value)


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


