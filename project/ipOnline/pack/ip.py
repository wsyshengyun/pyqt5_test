#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
from PyQt5.QtGui import QColor


def _get_range_ips(start: str, end: str):
    start_ = IP(start)
    end_ = IP(end)
    range_ = range(int(start_.tail()), int(end_.tail()) + 1)
    front = start_.header_3()
    return [front + '.' + str(tail) for tail in range_]


class IP(object):
    def __init__(self, ip):
        """ """
        if isinstance(ip, IP):
            self.__dict__ = ip.__dict__
        else:
            try:
                self.check_ip_formatter(ip)
            except TypeError as e:
                return e
            self.ip = ip

    def get_ip(self):
        return self.ip

    @staticmethod
    def check_ip_formatter(ip: str):
        import re

        if not isinstance(ip, str):
            raise TypeError("IP 必须是字符串类型")

        match = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip)
        if not match:
            return None
        ip_int_list = [int(d) for d in ip.split('.')]
        for d in ip_int_list:
            if not 0 <= d <= 255:
                return None
        return True

    def header_3(self):
        list_secs = self.list_4_section()
        list_secs.pop()
        return '.'.join(list_secs)

    def next_ip(self, n=1):
        int_tail = int(self.tail()) + n
        if int_tail > 255:
            raise ValueError("IP值超过范围")
        return self.replace_tail(int_tail)

    def last_ip(self, n=1):
        int_tail = int(self.tail()) - n
        if int_tail <= 0:
            raise ValueError("IP值超过范围")
        return self.replace_tail(int_tail)

    def tail(self):
        """ """
        list_section = self.list_4_section()
        return list_section[-1]

    def section(self):
        list_section = self.list_4_section()
        return list_section[-2]

    def hope_grateway(self):
        list_secs = self.list_4_section()
        list_secs.pop()
        list_secs.append('1')
        return '.'.join(list_secs)

    def list_4_section(self):
        return self.ip.split('.')

    @staticmethod
    def join_4_section(ip_sections):
        return '.'.join(ip_sections)

    def replace_section(self, section: [int, str]):
        """
        生成一个替换掉字段的IP
        返回一个ip字符串
        """
        int_sec = int(section)
        if int_sec >= 0 and int_sec <= 255:
            str_sec = str(int_sec)
            lit = self.list_4_section()
            lit[2] = str_sec
            return self.join_4_section(lit)
        else:
            raise ValueError("ip_sections 字段不在正确的范围")

    def replace_tail(self, tail: [int, str]):
        """
        生成一个替换掉尾部的IP
        返回一个ip字符串
        """
        int_tail = int(tail)
        if int_tail >= 0 and int_tail <= 255:
            str_tail = str(int_tail)
            lit = self.list_4_section()
            lit[-1] = str_tail
            return self.join_4_section(lit)
        else:
            raise ValueError("ip_sections 字段不在正确的范围")

    def generate_2_254_ips(self):
        """
        生成同字段的Ip列表, 范围为2到254
        返回一个IP生成器

        """
        for num in range(2, 255):
            yield self.replace_tail(num)

    def is_equal_section(self, ip):
        return IP(ip).section() == self.section()

    def __lt__(self, other):
        """
        <
        """
        if self.is_equal_section(other):
            # 字段相同
            return int(self.tail()) < int(other.tail())
        else:
            # 比较字段
            return int(self.section()) < int(other.section())

    def __str__(self):
        return f"<IP: {self.ip}>"


STATE_UN_KNOW = 0
STATE_FINDED = 1
STATE_ON_LINE = 2
STATE_NEW_ADD = 3


class IpState(IP):
    def __init__(self, ip):
        """ """
        super(IpState, self).__init__(ip)
        # value in [0, 1, 2, 3]
        # 0 : 未知状态
        # 1 : 查找过的
        # 2 : 查找过的 并且 在线的
        # 3 : 查找过的 新加入的

        self.state = STATE_UN_KNOW
        self.name = ""  # IP 对应的拥有者

    def get_name(self):
        # todo 关于一个类的变量描述符的应用, 可以去掉get_, 直接使用name代替
        return self.name

    def get_color(self):
        if self.state == STATE_UN_KNOW:
            return QColor(255, 255, 255)
        elif self.state == STATE_FINDED:
            return QColor(170, 170, 170)
        elif self.state == STATE_ON_LINE:
            return QColor(22, 150, 209)
        elif self.state == STATE_NEW_ADD:
            return QColor(29, 140, 29)

    def update_state(self):
        if self.state == STATE_UN_KNOW:
            self.state = STATE_NEW_ADD
        elif self.state == STATE_FINDED:
            self.state = STATE_ON_LINE
        elif self.state == STATE_ON_LINE:
            self.state = STATE_FINDED
        elif self.state == STATE_NEW_ADD:
            self.state = STATE_FINDED

    def set_unknow(self):
        self.state = STATE_UN_KNOW

    def set_online(self):
        self.state = STATE_ON_LINE

    def set_new(self):
        self.state = STATE_NEW_ADD

    def set_finded(self):
        self.state = STATE_FINDED

    def __str__(self):
        return f"<IpState: {self.ip}"
