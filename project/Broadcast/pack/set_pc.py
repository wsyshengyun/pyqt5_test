#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

import re
import socket
from time import sleep

import psutil
import wmi
from wmi import WMI

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


def set_ips_and_masks():
    print("in set_ips_and_masks()....")
    if set_ip_object:
        ips, masks, card_text = set_ip_object
        print('in set_ips_and_masks(): {}'.format(ips, masks))
        # input('.......~~~~')
        card = obj_network.get_card_from_name(card_text)
        result = card.card.EnableStatic(IPAddress=ips, SubnetMask=masks)
        print(result)
        if result[0] == 0 or result[0] == 1:
            print("设置ip成功!")
        else:
            print("设置IP不成功~~")


def inner():
    # 获取管理员权限
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
        """
        如果self.cards为空 则返回
        如果根据名字没有找到相应的card,则返回第一个card
        """
        if not self.cards:
            return
        
        for card in self.cards:
            if name in card.get_name():
                return card
        else:
            return self.cards[0]
    
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
    
    @staticmethod
    def check_ip(ip: str):
        import re
        match = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip)
        if not match:
            return None
        ip_int_list = [int(d) for d in ip.split('.')]
        for d in ip_int_list:
            if not 0 <= d <= 255:
                return None
        return True
    
    def ips(self):
        """
        获得所有的IP

        """
        ips: set = self.card.IPAddress
        return self._filter_ip(ips)
    
    def _filter_ip(self, ips):
        filter_ips = []
        if ips:
            ips = list(ips)
            for ip in ips:
                if self.check_ip(ip):
                    filter_ips.append(ip)
                pass
        return filter_ips
    
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
        return self._filter_ip(subnets)
    
    def ip_subnet_tuples(self):
        ips = self.ips()
        subnets = self.ip_subnet()
        if len(ips) == len(subnets) and ips:
            return zip(ips, subnets)
        else:
            return []
    
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


import ctypes, sys


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
        # input('')
    else:
        # Re-run the program with admin rights
        print("re-run the program with admin rights ")
        # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


obj_network = NetWorkCard()
card = obj_network.get_card_from_name()
# def update_card():
#     global card
#     card = obj_network.get_card_from_name()

if __name__ == '__main__':
    read()
    get_admin_and_do(set_ips_and_masks)
    
    # todo 删除一些IP
    # todo 网卡根据名字来差早;
    # todo 长传忽略文件
    pass
