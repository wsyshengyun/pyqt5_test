#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGO = (By.ID, 'nav-logo')
    LOGO = (By.ID, 'nav-logo')
    SEARCH_LIST = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')


class LoginPageLocators(object):
    password = (By.ID, '')


class BaiduPageLocators(object):
    input = (By.ID, 'kw')
    logo = (By.ID, 's_mp')
    news_lab = (By.CLASS_NAME, 'mnav c-font-normal c-color-t')