#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from project.SipTest.pages.base_page import BasePage
from project.SipTest.utils.locators import SipLoginLocators
from project.SipTest.make_driver import driver


class LoginPage(BasePage):
    def __init__(self, driver):
        """ """
        super(LoginPage, self).__init__(driver)
        self.locator = SipLoginLocators

    def is_login_page(self):
        pass

    def login(self):
        if not self.is_exists_element(self.locator.username):
            print("不是处在登陆界面")
            return
        self.send_keys(self.locator.username, "admin")
        self.send_keys(self.locator.password, "admin")
        self.select_combox_index(self.locator.selectbox, 1)
        self.click_button(self.locator.submit)

    def open_and_login(self, ip):
        self.open_ip(ip)
        self.sleep(5)
        self.login()


if __name__ == '__main__':
    ip = "192.168.0.246"
    obj = LoginPage(driver)
    obj.login(ip)