#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
"""
1, 解决页面等待问题
2, 解决弹出窗口,输入路径问题

"""


class BaseOption(object):
    def __init__(self):
        """ """
        super(BaseOption, self).__init__()

    def input_url(self, ip):
        pass

    def login(self):
        # 判断页面是否为登陆界面
            # 登陆
        # No 直接进入
        pass

    def update(self):
        # 首先要判断页面的状态,是否在登陆页面,如果是,要先登陆
        # 关键是会弹出窗口,选择文件
        pass

    def config(self):
        # 首先要判断页面的状态,是否在登陆页面,如果是,要先登陆
        # 如果不是,直接配置
        # 弹出窗口, 选择
        pass

    def option_other(self):
        # 注意延时,等待界面刷新完成
        pass

    def option_remove_broadcast(self):
        pass


class SipFlow(object):
    def run(self, option: BaseOption):
        # option.input_url(ip=None)
        option.login()
        option.update()
        option.config()
        option.option_other()
        option.option_remove_broadcast()

    

