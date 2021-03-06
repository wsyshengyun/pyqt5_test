# coding:utf8

import re

reg_check_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# todo 学习打包
# todo class 的 set 和 get
# todo 异常的传递 以及 UI的异常
# todo git的复习 分支的练习 | 打标签 | 向一个库推送文件
#     一个项目两个子项目打标签

class OneIp(object):
    def __init__(self, ip=None, port=None):
        """ """

        self.ip = ip
        self.port = port

    def get_ip(self):
        return self.ip

    def get_port(self):
        """ """
        return self.port

    def set_ip(self, ip):
        self.check_ip(ip)
        self.ip = ip

    def set_port(self, port):
        self.port = port

    @staticmethod
    def check_ip(ip):
        """ """
        if not isinstance(ip, str):
            raise TypeError("ip must is string")

        mat = re.match(reg_check_ip, ip)
        if mat is None:
            raise ValueError('ip 的格式有错误')

    def next_ip(self) -> str:
        *ip_, tail = self.ip.split('.')
        tail_int = int(tail)
        tail_int += 1
        if tail_int >= 255:
            tail_int = 0
        ip_.append(str(tail_int))
        next_ip = '.'.join(ip_)
        self.set_ip(next_ip)
        return next_ip



