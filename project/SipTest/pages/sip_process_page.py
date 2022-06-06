#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from project.SipTest.pages.base_page import BasePage
from project.SipTest.utils.locators import SipMainLocators


class SipProcess(BasePage):
    def __init__(self):
        """ """
        self.loc = SipMainLocators()
        # todo 目标版本?升级文件路径?配置文件路径?
        self.target_version = ""
        self.path_update_file = ""
        self.path_config_file = ""

    def is_in(self):
        # return self.is_exists_element(self.loc.)
        # todo 体现本页存在的标签名称
        return True

    def pro_config(self):
        # 判断是否在这个页面
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


