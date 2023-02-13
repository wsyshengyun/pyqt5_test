# -*- coding: utf-8 -*-
'''
@File    :   currency.py
@Time    :   2022/03/20 20:51:36

'''
import os

from project.ipOnline.pack.config import path, MyConfigObj
from ...pack.ip import IP, IpState
from project.ipOnline.pack.log import logger

# -----------------------------------------------------------
# 配置文件
# -----------------------------------------------------------


logger.info("path = {}".format(path))


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

    def set_flg_start_true(self):
        self.flg_start = True

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

#
# class CompareIpListAt(CompareIPList):
#     def __init__(self):
#         super(CompareIpListAt, self).__init__()
#         self.ips = []
#         self.current_section = None  # 当前IP段
#
#     def set_current_section(self, current_section):
#         self.current_section = current_section
#
#     def add_new(self, ip_str):
#         if self.flg_start:
#             obj = None
#             # 遍历所有的ipobj
#             for ipobj in self.ips:
#                 # 要插入的ip已经存在; 什么也不做
#                 if ip_str == ipobj.get_ip():
#                     obj = ipobj
#                     break
#             else:
#                 # 新建一个ipobj
#                 # obj = IpState(ip_str)
#                 # self.ips.append(obj)
#
#                 # 如果是新的IP要找到它的插入位置
#                 # 首先与相同字段的IP放在一起, 没有则按字段从小到大排列
#                 # 如果有想同的字段,则根据尾部排序,从小到大
#                 obj = self._inert_ip_from_sort(ip_str)
#
#             obj.update_state()
#             return obj
#
#     def _inert_ip_from_sort(self, ip_str):
#         obj = IpState(ip_str)
#         sec = obj.section()
#         tail = obj.tail()
#         will_insert_pos = 0
#         for obj_ in self.ips:
#             # IP的字段相同
#             if obj_.section() == sec:
#                 obj_pos = self.ips.index(obj_)
#                 if will_insert_pos == -2:
#                     will_insert_pos = obj_pos
#                     continue
#                 if obj_.tail() > tail:
#                     will_insert_pos = obj_pos
#         self.ips.insert(will_insert_pos, obj)
#         return obj
#
#
#
#
#     def update_state_all(self):
#         for ipobj in self.ips:
#             ipobj.update_state()
#
#
#     def type_ips(self):
#         """ 把IP分类"""
#         dit = {}
#         for ipobj in self.ips:
#             sec = ipobj.section()
#             if sec in dit:
#                 dit[sec].append(ipobj)
#             else:
#                 dit[sec] = [ipobj]
#         return dit
#





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

    # obj_ip = IP('192.168.11.151')
    # print(obj_ip.tail())
    # print(obj_ip.header_3())
    # print(obj_ip.section())
    # print(obj_ip.replace_section('23'))
    # print(obj_ip.hope_grateway())
    # print(obj_ip.replace_tail(222))
    # obj_some = CompareIPList()
    # obj_some.finded_ips = [
    #     '192.168.1.11',
    #     '192.168.1.12',
    #     '192.168.1.13',
    #     '192.168.1.14',
    #     '192.168.2.11',
    #     '192.168.3.11',
    #     '192.168.4.11',
    #     '192.168.4.18',
    #     '192.168.4.10',
    # ]
    # obj_some.new_find_ips = [
    #     '192.168.5.38',
    #     '192.168.5.19',
    #     '192.168.5.18',
    #     '192.168.5.10',
    # ]

    # print(obj_some.types_section_finded_ips())
    # print(obj_some.compare_list('5'))


    ips = [
        '192.168.1.13',
        '192.168.1.12',
        '192.168.1.14',

        '192.168.12.14',
        '192.168.12.24',
        '192.168.1.11',
        '192.168.12.64',

        '192.168.2.13',
        '192.168.2.12',
        '192.168.12.13',
        '192.168.2.11',
        '192.168.2.14',
    ]
    # CompareIpListAt
    # obj = CompareIpListAt()
    # obj.set_flg_start_true()
    # for ip in ips:
    #     obj.add_new(ip)
    # print(obj.ips)
    # for obj in obj.ips:
    #     print(obj.ip)
    #
    pass

