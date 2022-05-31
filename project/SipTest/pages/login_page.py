#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from project.SipTest.pages.base_page import BasePage
from project.SipTest.utils.locators import LoginPageLocators
from project.SipTest.utils import users


class LoginPage(BasePage):
    def __init__(self, driver):
        """ """
        super(LoginPage, self).__init__(driver)
        self.locator = LoginPageLocators

    def _enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def _enter_password(self, password):
        self.find_element(*self.locator.password).send_keys(password)

    def _click_login_button(self):
        self.find_element(*self.locator.submit).click()

    def login(self, user):
        user = users.get_user(user)
        print(user)
        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).