# coding:utf8


from selenium import webdriver
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
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

    def get_url(self, ip):
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

    def run(self, ip=None, url=None):
        if url:
            url = url
        else:
            url = self.get_url(ip)
        print(url)
        self.driver.get(url)
        self.driver.implicitly_wait(1)
        self.login()

    def login(self):
        # self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element(By.ID, "username").send_keys('admin')
        self.driver.find_element(By.ID, "password").send_keys('admin')
        # langue
        langue_obj = self.driver.find_element(By.ID, "langSelect")
        Select(langue_obj).select_by_index(1)    # 索引从0开始
        time.sleep(2)
        self.driver.find_element(By.ID, "logonButton").click()
        self.driver.implicitly_wait(10)
        time.sleep(3)
        print('wait end')

        upbtn = "top_curTitle"
        self.driver.find_element(By.ID, upbtn).click()

        pass





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


