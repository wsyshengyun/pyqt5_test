#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from project.SipTest.pack.process_sip import BaseOption, SipFlow
from project.SipTest.pack.base_driver import BaseDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class DriverOption(BaseOption, BaseDriver):
    def login(self, ip=None, url=None):
        if url:
            url = url
        else:
            url = self.get_url(ip)

        self.driver.get(url)
        self.driver.implicitly_wait(1)


        # self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element(By.ID, "username").send_keys('admin')
        self.driver.find_element(By.ID, "password").send_keys('admin')
        # langue
        langue_obj = self.driver.find_element(By.ID, "langSelect")
        Select(langue_obj).select_by_index(1)  # 索引从0开始
        time.sleep(2)
        self.driver.find_element(By.ID, "logonButton").click()
        self.driver.implicitly_wait(10)
        time.sleep(3)
        print('wait end')

        upbtn = "top_curTitle"
        self.driver.find_element(By.ID, upbtn).click()

    def update(self):
        pass

    def config(self):
        super().config()

    def option_other(self):
        super().option_other()

    def option_remove_broadcast(self):
        super().option_remove_broadcast()


class SubFlow(SipFlow):
    pass


def main():
    """ """
    subflow = SubFlow()
    subflow.run()


if __name__ == '__main__':
    main()
