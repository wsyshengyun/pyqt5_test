#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage(object):
    def __init__(self, driver, base_url=''):
        """ """
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open(self, url=None):
        if url is None:
            url = ''
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, locator):
        element = self.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*locator))
        except TimeoutException:
            print('\n * element not found within given time! --> %s' % (locator[1]))
            self.driver.quit()

    def clear_key(self, locator):
        """
        重写清空文本框
        """
        time.sleep(3)
        self.find_element(locator).clear()

    def send_keys(self, locator, value):
        """
        locator: (id, "name")
        """

        self.clear_key(locator)
        self.find_element(locator).send_keys(value)

    def click_button(self, locator):
        """
        点击按钮
        """
        self.find_element(locator).click()

    def switch_to_frame(self, value):
        """
        进入iframe页面
        """
        self.driver.switch_to.frame(value)

    @staticmethod
    def conversion_ip_to_url(ip):
        return 'http://' + str(ip)

    def open_ip(self, ip):
        url = self.conversion_ip_to_url(ip)
        self.driver.get(url)

    def max_windows(self):
        self.driver.maximize_window()

    def path_other(self):
        """
        not  use
        """

        # current_path = os.path.dirname(__file__)  # 获取当前的路径
        # driver_path = os.path.join(current_path, '../driver/chromedriver.exe')  # 当前路径 + chromedriver路径相连
        pass

