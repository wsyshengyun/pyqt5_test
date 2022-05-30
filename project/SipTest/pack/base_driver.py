# coding:utf8


from selenium import webdriver
import time
import os


current_path = os.path.dirname(__file__)  # 获取当前的路径
driver_path = os.path.join(current_path, '../driver/chromedriver.exe')  # 当前路径 + chromedriver路径相连

driver = webdriver.Chrome(executable_path=driver_path)
url = 'https://www.jd.com'
driver.get(url)
driver.maximize_window()
driver.find_element_by_class_name('link-login').click()

