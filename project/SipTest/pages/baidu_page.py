#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
from selenium.webdriver.edge.webdriver import WebDriver

from project.SipTest.pages.base_page import BasePage
from project.SipTest.utils.locators import BaiduPageLocators


class BaiduPage(BasePage):
    def __init__(self, driver, base_url=''):
        """ """
        self.loc = BaiduPageLocators()
        super(BaiduPage, self).__init__(driver, base_url)

    def login(self):
        print(self.get_title())
        print(self.get_url())
        # self.hover(*self.loc.logo)
        self.wait_element(*self.loc.news_lab)
        self.find_element(*self.loc.news_lab).click()

        pass


# def get_driver():
#     global driver
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service
options = EdgeOptions()
options.use_chromium = True
options.add_argument('start-maximized')
path = r"D:\wsy\project\pyqt5_test\edgedriver\msedgedriver.exe"
path2 = r"d:\_python\xdkj_test\edgedriver\msedgedriver.exe"
s = Service(path2)
driver = Edge(service=s, options=options)
# driver = get_driver()


if __name__ == '__main__':
    url = "https://www.baidu.com"
    obj = BaiduPage(driver, base_url=url)
    obj.open()
    obj.login()




