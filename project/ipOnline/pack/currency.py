# -*- coding: utf-8 -*-
'''
@File    :   currency.py
@Time    :   2022/03/20 20:51:36

'''
import os

from configobj import ConfigObj

from project.ipOnline.pack.log import logger


# -----------------------------------------------------------
# 配置文件
# -----------------------------------------------------------
def get_path(filename):
    dirname = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dirname, filename)
    return path


path = get_path('app.ini')
logger.info("path = {}".format(path))


class MyConfigObj(object):
    def __init__(self, path, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = print

        self.path = path
        self.conf = ConfigObj(self.path, encoding='utf8')
        # self.conf.filename = self.path

    def add_section(self, sec, option=None, value=None):
        if sec not in self.conf:
            self.conf[sec] = {}
        if option and value:
            self.conf[sec][option] = value
        self.conf.write()

    def get_value(self, sec, option):
        return self.conf[sec][option]

    def remove_option(self, sec, option):
        del self.conf[sec][option]
        self.conf.write()

    def remove_section(self, sec):
        del self.conf[sec]
        self.conf.write()

    def save_other_file(self, path):
        self.conf.filename = path
        self.conf.write()


def is_exists_ini_path():
    return os.path.exists(path)


def set_start_ip(ip_start):
    MyConfigObj(path).add_section('ip', 'start', ip_start)
    pass


def set_end_ip(ip_end):
    MyConfigObj(path).add_section('ip', 'end', ip_end)
    pass


def get_start_ip():
    return MyConfigObj(path).get_value('ip', 'start')
    pass


def get_end_ip():
    return MyConfigObj(path).get_value('ip', 'end')
    pass


def get_range_ips():
    ip_start = get_start_ip()
    ip_end = get_end_ip()

    # logger.info("ip_start = {}".format(ip_start))
    # logger.info("ip_end = {}".format(ip_end))

    sec0, tail0 = get_ip_sec_tail(ip_start)
    sec1, tail1 = get_ip_sec_tail(ip_end)

    if sec0 != sec1:
        logger.info("错误, 设置的IP不在统一字段!")
        return
    if int(tail0) > int(tail1):
        tail0, tail1 = tail1, tail0

    before = get_ip_before(ip_start)

    # logger.info("before = {}".format(before))
    # logger.info("tail0 = {}".format(tail0))
    # logger.info("tail1 = {}".format(tail1))

    return ['.'.join([before, str(num)]) for num in range(int(tail0), int(tail1) + 1)]


# -----------------------------------------------------------
# 通用 
# -----------------------------------------------------------

def split_ip(ip: str):
    """
    用.分割一个IP, 得到一个4个长度的列表,元素为ip的各个字段;

    """
    return ip.split('.')


def get_ip_sec_tail(ip: str):
    """
    获取IP的最后两段的一个元组,比如192.168.2.100,
    返回的结果为 '2', '100'
    """
    secs = split_ip(ip)
    return secs[-2], secs[-1]


def get_ip_before(ip: str):
    """
    获取IP的前三段,用.连接的,例如192.168.100

    """
    return '.'.join(split_ip(ip)[:3])


def get_ip_tails(ip_list: list):
    """
    return : [str, str ...]
    结果为[ip的最后一段的列表]
    """
    return [get_ip_sec_tail(ip)[1] for ip in ip_list] if ip_list else []


class IP(object):
    def __init__(self, ip):
        """ """
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

    def set_new(self):
        self.state = STATE_NEW_ADD

class CompareIPList(object):
    def __init__(self):
        """ """
        # finded_ips 里面的IP可能有不同的字段
        self.finded_ips = []
        # new_find_ips 里面的IP都是一个字段的
        self.new_find_ips = []
        # 只有当flg_strt为True的时候才可以添加新的IP
        self.flg_start = False

    def clear_new_ips(self):
        """
        标志置为True
        已查找过的IP列表添加new_fnd_ips里面的IP
        清空新IP的列表
        """
        self.flg_start = True
        self.finded_ips.extend(self.new_find_ips)
        # 去重
        set_ips = set(self.finded_ips)
        self.finded_ips = list(set_ips)

        self.new_find_ips = []

    def add_new(self, ip):
        if self.flg_start:
            self.new_find_ips.append(ip)

    def set_flg_start_flase(self):
        self.flg_start = False

    @staticmethod
    def type_ips(ips: list):
        """ 把IP分类"""
        dit = {}
        for ip in ips:
            ipobj = IP(ip)
            sec = ipobj.section()
            if sec in dit:
                dit[sec].append(ip)
            else:
                dit[sec] = [ip]
        return dit

    def types_section_finded_ips(self):
        """
        返回列表中不同字段IP的种类

        """
        dit = self.type_ips(self.finded_ips)
        if dit:
            return len(dit.keys())
        else:
            return 0

    def compare_list(self, currect_section=None):
        """


        """
        dit = {
            'new': [],  # 这次新查找出来的IP
            'still_exist': [],  # 这次查找在线的IP在之前也出现过
            'lose': []  # 之前存在现在已经不在线的IP
            # still_exist + lose = finded_ips
            }
        for ip in self.new_find_ips:
            if ip in self.finded_ips:
                dit['still_exist'].append(ip)
            else:
                dit['new'].append(ip)

        # 获得已经不在线的IP
        still_ips = set(dit['still_exist'])
        type_sec_ips: dict = self.type_ips(self.finded_ips)
        # 这次查找的字段 在之前出现过
        if currect_section in type_sec_ips:
            set_ips = set(type_sec_ips.get(currect_section))
            lose_ips = set_ips - still_ips
            dit['lose'] = list(lose_ips)
        else:
            # 新的字段
            dit['lose'] = []
        return dit


class CompareIpListAt(CompareIPList):
    def __init__(self):
        super(CompareIpListAt, self).__init__()
        self.ips = []

    def add_new(self, ip_str):
        if self.flg_start:
            obj = None
            for ipobj in self.ips:
                if ip_str == ipobj.get_ip():
                    obj = ipobj
                    break
            else:
                obj = IpState(ip_str)
                self.ips.append(obj)
            obj.update_state()
            return obj

    def update_state_all(self):
        for ipobj in self.ips:
            ipobj.update_state()


    def type_ips(self):
        """ 把IP分类"""
        dit = {}
        for ipobj in self.ips:
            sec = ipobj.section()
            if sec in dit:
                dit[sec].append(ipobj)
            else:
                dit[sec] = [ipobj]
        return dit






def main():
    conobj = MyConfigObj(path, logger)
    # conobj.add_section('ip', 'start', '192.168.0.2')
    # conobj.add_section('ip', 'end', '192.168.0.254')
    # logger.info("conobj.get_val() = {}".format(conobj.get_value('ip', 'start')))
    # logger.info("conobj.get_value('ip', 'end') = {}".format(conobj.get_value('ip', 'end')))
    logger.info("get_range_ips() = {}".format(get_range_ips()))


if __name__ == '__main__':
    # a = [1, 2, 3]
    # b = ['a', 'b', 'c', 'd']
    # c = [('a', 1), ('b', 2), ('c', 3)]
    # d = [(i, j) for i in range(5) for j in range(4)]
    # z = zip(b, a)
    # for m, n in zip(a, c):
    #     print(m, *n)
    # print(list(z))
    # print(d)
    # print(len(d))
    # print(list(range(1, 20)))
    # print(list(range(0, 20)))
    # print(list(range(20)))
    # a = range(2, 20)
    # a = [str(i) for i in a]
    # d = d
    # for id, ia in zip(d, a):
    #     print(*id, ia)
    # print(len(list(zip(a, d))))
    #
    # print(get_ip_sec_tail('192.169.123.3'))
    # print(get_ip_tails(['192.168.1.3', '192.156.2.9']))
    #
    # get_ip_before('192.168.2.3:7')

    obj_ip = IP('192.168.11.151')
    print(obj_ip.tail())
    print(obj_ip.header_3())
    print(obj_ip.section())
    print(obj_ip.replace_section('23'))
    print(obj_ip.hope_grateway())
    print(obj_ip.replace_tail(222))
    obj_some = CompareIPList()
    obj_some.finded_ips = [
        '192.168.1.11',
        '192.168.1.12',
        '192.168.1.13',
        '192.168.1.14',
        '192.168.2.11',
        '192.168.3.11',
        '192.168.4.11',
        '192.168.4.18',
        '192.168.4.10',
    ]
    obj_some.new_find_ips = [
        '192.168.5.38',
        '192.168.5.19',
        '192.168.5.18',
        '192.168.5.10',
    ]

    print(obj_some.types_section_finded_ips())
    print(obj_some.compare_list('5'))
