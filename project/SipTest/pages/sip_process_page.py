#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from project.SipTest.pages.base_page import BasePage
from project.SipTest.utils.locators import SipMainLocators


class SipProcess(BasePage):
    def __init__(self,driver, base_url=""):
        """ """
        super(SipProcess, self).__init__(driver, base_url)
        self.loc = SipMainLocators()
        # todo 目标版本?升级文件路径?配置文件路径?
        self.target_version = "	T2.4.15"
        self.path_update_file = ""
        self.path_config_file = ""
        self.js_path = r"E:\wsy\py_pro\pyqt5_test\project\SipTest\other\xmlUtil.js"

    def init_js(self):
        # with open(self.js_path, 'r') as f:
        #     cont = f.read()
        # self.driver.execute_script(cont)
        js = 'window.scrollTo(0,document.body.scrollHeight)' # js语句     页面直接滚到最下方
        self.driver.execute_script(js) # 执行js的方
        print('init js')

    def is_in_main(self):
        print(self.loc.connect)
        return self.is_exists_element(self.loc.connect)

    def test_ui_elements(self):
        # print(self.driver)
        self.find_element(self.loc.connect)
        self.find_element(self.loc.config_page)
        self.find_element(self.loc.update_page)
        self.find_element(self.loc.dj_page)
        content = self.driver.page_source
        write(content)

    def pro_config(self):
        # 判断是否在这个页面
        if not self.is_in_main():
            print("没有在主界面")
            return
        self.until_find_element(self.loc.config_page)
        self.click_button(self.loc.config_page)
        self.click_button(self.loc.config_select_file)
        # todo 弹出输入配置文件窗口了怎么办?
        #
        self.click_button(self.loc.config_submit)

        pass

    def get_version(self):
        return

    def pro_update(self):
        # 判断是否在这个页面
        # 检查版本
        if self.get_version() != self.target_version:
            # 升级
            self.click_button(self.loc.update_page)
            self.click_button(self.loc.update_select_file)
            # todo 弹出输入升级窗口了怎么办?
            #
            self.click_button(self.loc.update_submit)  # 提交升级
            # 等待半分钟到一分钟,将会到login页面
            pass

        pass

    def pro_setother(self):
        # 判断是否在这个页面
        # 设置相机
        self.click_button(self.loc.dj_page)  # 对讲页
        self.click_button(self.loc.camera_page)  # 相机设置页面
        self.select_combox_index(self.loc.camera_outer_box, 1) # 选择外接 为第二项
        self.click_button(self.loc.camera_btn_submit)  # 提交设置
        # todo 此处要等待
        # 设置广播模式
        self.click_button(self.loc.dj_page)  # 对讲页
        self.click_button(self.loc.mt_page)
        self.click_button(self.loc.mt_bro)
        # todo 媒体设置下面的两个方框选项处理
        pass

    def pro_quit_broadcast(self):
        # 判断是否在这个页面
        # 退出广播模式
        pass


def write(text):
    path = './source.txt'
    with open(path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    from project.SipTest.make_driver import driver
    from project.SipTest.pages.sip_login_page import LoginPage
    ip = "192.168.0.246"
    # obj = LoginPage(driver)
    # obj.open_and_login(ip)
    import time
    mainobj = SipProcess(driver)
    mainobj.open_ip(ip)
    # mainobj.pro_config()
    mainobj.init_js()
    time.sleep(2)
    mainobj.test_ui_elements()
