# coding:utf8

import socket

import wmi
import ctypes
import subprocess
from project.Broadcast.middle import OneIp

order_str = "HEADER|Name|IPX|PORT|MASS|GATE|MDNS|PDNS|UART|Ver|MIP1|MPO1|MIP2|MPO2|MIP3|MPO3|UserSet"

MESSAGE_DICT = {
    'HEADER': '535a5844000001011e5368656e5a68656e2058696e4469616e2c',  # # SZXD ... SHENZHEN XINGDIAN
    'Name': '535045414b53504f54312c',  # # SPEAKSPOT1
    'IPX': '3139322e3136382e3130302e3230302c',  # # 192.168.100.200
    'PORT': '36303030302c',  # # 6000
    'MASS': '3235352e3235352e3235352e3030302c',  # # 255.255.255.0
    'GATE': '3139322e3136382e3130302e3030312c',  # # 192.168.100.1
    'MDNS': '3139322e3136382e3130302e3030312c',  # # 192.168.100.1
    'PDNS': '3139322e3136382e3130302e3030312c',  # # 192.168.100.1
    'UART': '393630302e4e2e382e312c',  # # 9600.N.8.1
    'Ver': '332e312e332c',  # # 3.1.3
    'MIP1': '3139322e3136382e3130302e3030312c',  # # 192.168.100.1
    'MPO1': '35303030302c',  # # 5000
    'MIP2': '3139322e3136382e3130302e3030322c',  # # 192.168.100.2
    'MPO2': '35303030302c',  # # 5000
    'MIP3': '3139322e3136382e3130302e3030332c',  # # 192.168.100.3
    'MPO3': '35303030302c',  # # 5000
    'UserSet': '55736572536574',  # # UserSet
}


class Message(object):
    def __init__(self, ip: str = None):
        """ """
        self.MESSAGE_DICT = MESSAGE_DICT.copy()
        self.handler = Handler()
        if ip:
            self.set_message_from_ip(ip)

    def set_message_from_ip(self, ip: str):
        ip_message = self.handler.handler_ip(ip)
        self.MESSAGE_DICT['IPX'] = ip_message

    def generate_message_string(self):
        key_list = self._key_list()

        line_list = []
        header = self.MESSAGE_DICT.get("HEADER")
        tail = self.MESSAGE_DICT.get("UserSet")

        for key in key_list[1:-1]:
            tsr = self.handler.join_key_value(key, self.MESSAGE_DICT)
            line_list.append(tsr)

        line_list.insert(0, header)
        line_list.append(tail)
        message = ''.join(line_list)
        return message

    def _key_list(self):
        return order_str.split('|')


class Handler(object):

    def handler_ip(self, ip: str):
        """ """
        if '.' not in ip or ip.count('.') != 3:
            raise ValueError("ip 格式有错误")

        iplist: [str] = ip.split('.')
        return '2e'.join([self._section_insert_3(section) for section in iplist]) + '2c'

    @staticmethod
    def _section_insert_3(ip_section: str) -> str:
        """ """
        len_str = len(ip_section)

        # 001 192 098 的形式
        if len_str == 0 or len_str > 3:
            raise ValueError("ip的段不能为空, 长度不能大于3")

        elif len_str == 1:
            ip_section = '00' + ip_section

        elif len_str == 2:
            ip_section = '0' + ip_section

        lista = list(ip_section)
        for i in range(2, -1, -1):
            lista.insert(i, '3')
        return ''.join(lista)

    @staticmethod
    def _to_hex(tsr):
        by = bytes(tsr, 'utf8')
        hexstring = by.hex()  # 16进制的字符串, 不带0x
        return hexstring

    def join_key_value(self, key, dicta: dict):
        """
        join之前, 先把key转化为16进制的字符串, 再与value合并

        """
        value = dicta[key]
        key_ = self._to_hex(key)
        return '3d'.join([key_, value])


class MySocket(object):
    def __init__(self):
        """ """
        # socket.AF_INET    指定IPv4协议
        # socket.SOCK_DGRAM  指定UDP数据报式的协议
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(2)
        self.purpose_one_ip: OneIp = None

    def set_purpose_ip(self, one_ip: OneIp):
        self.purpose_one_ip = one_ip

    def send(self, msg):
        """ """
        self.socket.sendto(msg, (self.purpose_one_ip.get_ip(), self.purpose_one_ip.get_port()))
        data, addr = self.socket.recvfrom(4096)
        return data, addr

    def send_ip_message(self):
        send_ip = self.purpose_one_ip.get_ip()
        msg = Message(send_ip).generate_message_string()
        return self.send(msg)

    def close(self):
        self.socket.close()


def check_ip_on_line(self, ip):
    pass


def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


def is_admin():
    try:
        mid = ctypes.windll
        return mid.shell32.IsUserAnAdmin()
    except:
        return False


def getWinNetList(net_list):
    netcardnum = 0
    net_card = {}
    wmiservice = wmi.WMI()
    configs = wmiservice.Win32_NetworkAdapterConfiguration(IPEnabled=True)  # 获取到本地所有有网卡信息,list
    for nic in configs:
        if nic.MACAddress is not None:
            net_card['num'] = netcardnum
            net_card['mac'] = nic.MACAddress
            # net_card['ip'] = []
            # if nic.IPAddress is not None:
            #     for i in range(len(nic.IPAddress)):
            #         net_card['ip'].append(nic.IPAddress[i])
            # print('ip:'+ str(nic.IPAddress[i]))
            net_list.append(net_card)
            netcardnum += 1
        net_card = {}
    return configs


if __name__ == '__main__':
    # net_list = []
    # res = getWinNetList(net_list)
    # print(res)
    # print(net_list)
    obj = Message()
    obj.set_message_from_ip('192.168.100.200')
    print(obj.generate_message_string())
    pass
