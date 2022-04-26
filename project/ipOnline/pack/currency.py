# -*- coding: utf-8 -*-
'''
@File    :   currency.py
@Time    :   2022/03/20 20:51:36

'''
import os

from configobj import ConfigObj

from .log import logger


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


# -----------------------------------------------------------
# 
# -----------------------------------------------------------


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
    return ip.split('.')


def get_ip_sec_tail(ip: str):
    secs = split_ip(ip)
    return secs[-2], secs[-1]


def get_ip_before(ip: str):
    return '.'.join(split_ip(ip)[:3])


def get_ip_tails(ip_list: list):
    return [get_ip_sec_tail(ip)[1] for ip in ip_list] if ip_list else []


def main():
    conobj = MyConfigObj(path, logger)
    # conobj.add_section('ip', 'start', '192.168.0.2')
    # conobj.add_section('ip', 'end', '192.168.0.254')
    # logger.info("conobj.get_val() = {}".format(conobj.get_value('ip', 'start')))
    # logger.info("conobj.get_value('ip', 'end') = {}".format(conobj.get_value('ip', 'end')))
    logger.info("get_range_ips() = {}".format(get_range_ips()))


if __name__ == '__main__':
    a = [1, 2, 3]
    b = ['a', 'b', 'c', 'd']
    c = [('a', 1), ('b', 2), ('c', 3)]
    d = [(i, j) for i in range(5) for j in range(4)]
    z = zip(b, a)
    for m, n in zip(a, c):
        print(m, *n)
    print(list(z))
    print(d)
    print(len(d))
    print(list(range(1, 20)))
    print(list(range(0, 20)))
    print(list(range(20)))
    a = range(2, 20)
    a = [str(i) for i in a]
    d = d
    for id, ia in zip(d, a):
        print(*id, ia)
    print(len(list(zip(a, d))))

    print(get_ip_sec_tail('192.169.123.3'))
    print(get_ip_tails(['192.168.1.3', '192.156.2.9']))

    get_ip_before('192.168.2.3:7')
