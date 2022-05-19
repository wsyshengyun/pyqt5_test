#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

import psutil
import socket
import os
import re
from time import sleep
from wmi import WMI
import wmi

import ctypes, sys


# import sys
# import win32com.shell.shell as shell
# ASADMIN = 'asadmin'
#
# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     # sys.exit(0)

set_ip_object = []

import os, json

path = 'ips.json'

def write():
    with open(path, 'w', encoding='utf8') as f:
        json.dump(set_ip_object, f)

def read():
    global set_ip_object
    with open(path, 'r', encoding='utf8') as f:
        set_ip_object = json.load(f)



def set_ips_and_masks(card, set_ip_object):
    print("in set_ips_and_masks()....")



    if set_ip_object:
        ips, masks = set_ip_object
        print('in set_ips_and_masks(): {}'.format(ips, masks))
        # input('.......~~~~')
        result = card.EnableStatic(IPAddress=ips, SubnetMask=masks)
        print(result)
        if result[0] == 0 or result[0] == 1:
            print("设置ip成功!")
        else:
            print("设置IP不成功~~")

def inner():
   #获取管理员权限
   if ctypes.windll.shell32.IsUserAnAdmin():
       return
   else:
       ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 0)
       # sys.exit()


class NetWorkCard(object):
    def __init__(self):
        """ """
        self.w = WMI()
        self.configs = self.w.Win32_NetworkAdapterConfiguration(IPEnabled=True)
        self.cards = [Card(net) for net in self.configs]
        self.defaultCard = None

    def get_card_names(self):
        """
        获得所有网卡的名字

        """
        for net in self.configs:
            yield net.Description

    def get_card_from_name(self, name="环回"):
        for card in self.cards:
            if name in card.get_name():
                return card

    def get_card_from_index(self, index):
        for card in self.cards:
            if index == card.index():
                return card


class Card(object):

    def __init__(self, card: wmi._wmi_object):
        """ """
        self.card = card

    def get_name(self):
        return self.card.Description

    def index(self):
        pass
        return self.card.Index

    def ips(self):
        """
        获得所有的IP

        """
        ips = self.card.IPAddress
        if ips:
            ips = list(ips)
            return ips[:-1]
        pass

    def gateway(self):
        """
        返回默认网关

        """
        if self.card.DefaultIPGateway:
            return list(self.card.DefaultIPGateway)[0]
        pass

    def mac(self):
        """
        获得此网卡的mac地址

        """
        ips = self.card.IPAddress
        if ips:
            ips = list(ips)
            return ips[-1]

    def ip_subnet(self):
        """
        获得所有的dns

        """
        subnets = self.card.IPSubnet
        if len(subnets)>0:
            subnets = list(subnets)
            return subnets[:-1]
        pass

    def ip_subnet_tuples(self):
        ips = self.ips()
        subnets = self.ip_subnet()
        if len(ips) == len(subnets) and ips:
            return zip(ips, subnets)

    def set_ip_and_mask(self, ips: list, masks: list):
        print('ips: {}'.format(ips))
        print('masks: {}'.format(masks))
        result = self.card.EnableStatic(IPAddress=ips, SubnetMask=masks)
        print("设置IP的结果是: {}".format(result))
        if result[0] == 0 or result[0] == 1:
            print("设置ip成功!")
            return True
        else:
            print("设置IP不成功~~")
            return False

    def set_gateway(self, interway):
        # 修改网关
        if interway:
            wayres = self.card.SetGateways(DefaultIPGateway=interway, GatewayCostMetric=[1])
            if wayres[0] == 0:
                print('设置网关成功')
            else:
                print('修改网关失败')
                return False

    def set_dns(self, dns):
        # 修改dns
        if dns:
            dnsres = self.card.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
            if dnsres[0] == 0:
                print('设置DNS成功,等待3秒刷新缓存')
                sleep(3)
                # 刷新DNS缓存使DNS生效
                os.system('ipconfig /flushdns')
            else:
                print('修改DNS失败')
                return False


def method_name():
    local_addrs = []
    # name is 本地连接之类的名字 ,是不是网络适配器??
    # info 一个list , 和name相配
    # addr 一个 snicaddr对象; 又 family 和 address 属性
    for name, info in psutil.net_if_addrs().items():
        print('name is ', name)
        for addr in info:
            # 只放入IPV4的地址
            if socket.AddressFamily.AF_INET == addr.family:
                print(addr.address)
                local_addrs.append(addr.address)
    print(local_addrs)


def get_ips(name_wang_ka):
    ips = []
    for name, info in psutil.net_if_addrs().items():
        if name_wang_ka in name:
            for addr in info:
                if socket.AddressFamily.AF_INET == addr.family:
                    ips.append(addr.address)
        else:
            continue
    return ips if ips else None


def get_wangka_info():
    w = WMI()
    data = {}
    count = 0
    for nic in w.Win32_NetworkAdapterConfiguration():
        if nic.MACAddress is not None:
            count += 1
            iter_data = {}
            iter_data['macaddress'] = nic.MACAddress
            iter_data['model'] = nic.Caption
            iter_data['name'] = nic.Index

            if nic.IPAddress is not None:
                iter_data['ipaddress'] = nic.IPAddress[0]
                iter_data['netmask'] = nic.IPSubnet
            else:
                iter_data['ipaddress'] = ''
                iter_data['netmask'] = ''
            data["nic%s" % count] = iter_data
    return data



def set_wangka_ip(ip, mask, index):
    w = WMI()
    # confs = w.Win32_NetworkAdapterCinfiguration(IPEnabled=True)
    confs = w.Win32_NetworkAdapterConfiguration(IPEnabled=True)  # 获取到本地所有有网卡信息,list
    print("confs 的长度位  {}".format(len(confs)))
    if index <= len(confs):
        conf = confs[index]
        result = conf.EnableStatic(IPAddress=ip, SubnetMask=mask)
        print(result)
        if result[0] == 0 or result[0] == 1:
            print("设置ip成功!")
        else:
            print("设置IP不成功~~")


class UpdateIp(object):
    re_ip_str = r"\d+.\d+.\d+.\d+"

    def __init__(self):
        self.wmiservice = WMI()
        self.configs = self.wmiservice.Win32_NetworkAdapterConfiguration(
            IPEnabled=True  # # 获取到本机所有的网卡的信息,list
        )

    def get_inter(self):
        """ """
        flag = 0
        # 遍历所有网卡，找到要修改的那个
        for con in self.configs:
            ip = re.findall(self.re_ip_str, con.IPAddress[0])
            if len(ip) > 0:
                return 0
            else:
                flag = flag + 1
        return flag

    def runset(self, ip, subnetmask, interway=None, dns=None):
        adapter = self.configs[self.get_inter()]

        # 开始执行修改ip、子网掩码、网关
        ipres = adapter.EnableStatic(IPAddress=ip, SubnetMask=subnetmask)
        if ipres[0] == 0:
            print('设置IP成功')
        else:
            if ipres[0] == 1:
                print('设置IP成功，需要重启计算机！')
            else:
                print('修改IP失败')
                return False

        # 修改网关
        if interway:
            wayres = adapter.SetGateways(DefaultIPGateway=interway, GatewayCostMetric=[1])
            if wayres[0] == 0:
                print('设置网关成功')
            else:
                print('修改网关失败')
                return False

        # 修改dns
        if dns:
            dnsres = adapter.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
            if dnsres[0] == 0:
                print('设置DNS成功,等待3秒刷新缓存')
                sleep(3)
                # 刷新DNS缓存使DNS生效
                os.system('ipconfig /flushdns')
            else:
                print('修改DNS失败')
                return False


def get_admin_and_do(do_function, *args, **kwargs):
    """ """

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            print("False")
            return False

    if is_admin():
        # Code of your program here
        do_function(*args, **kwargs)
        input('')
    else:
        # Re-run the program with admin rights
        print("re-run the program with admin rights ")
        # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


obj_network = NetWorkCard()
card = obj_network.get_card_from_name()
read()
def update_card():
    global card
    card = obj_network.get_card_from_name()

if __name__ == '__main__':

    obj_network = NetWorkCard()
    card = obj_network.get_card_from_name()
    read()
    print('read....')
    print(set_ip_object)
    print("card is {}".format(card))
    get_admin_and_do(set_ips_and_masks, card.card, set_ip_object)
    input('!........')

    # print(set_ip_object)
    # set_ip_object = [['192'], ['244']]
    # write()
    # set_ip_object = []
    # print(set_ip_object)
    # read()
    # print(set_ip_object)

    # import random
    # tsr_tail = random.randint(2, 254)
    # tsr_tail2 = random.randint(2, 254)
    # ip1 = '192.168.11.' + str(tsr_tail)
    # ip2 = '192.168.13.' + str(tsr_tail2)
    # ip = [ip1, ip2]
    # mask = ['255.255.255.0'] * 2
    # obj = NetWorkCard()
    # card = obj.get_card_from_name()
    # print('原来的是 tuple is : ', list(card.ip_subnet_tuples()))
    # print('要设置的是: ', ip, mask)
    # get_admin_and_do(card.set_ip_and_mask, ip, mask)
    # print('..............')
    # input('.......')
      # todo 删除一些IP
      # todo 网卡根据名字来差早;
      # todo 长传忽略文件
    pass

