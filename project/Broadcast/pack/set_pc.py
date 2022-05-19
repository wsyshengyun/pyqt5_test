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


if __name__ == '__main__':
    #
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


    if is_admin():
        # Code of your program here
        pass
        ip = ['192.168.0.155', '192.168.6.151']
        mask = ['255.255.255.0', '255.255.255.0']
        set_wangka_ip(ip, mask, 3)
        input('...')
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


    # print(get_wangka_info())
    # datas = get_wangka_info()
    # for data in datas:
    #     print(data)
    #     print(datas[data])
    #     print(' - ' * 30)

    # obj = UpdateIp()
    # print(obj.get_inter())
    # print(method_name())
    # print(get_ips("本地连接* 1"))
    # obj.runset("192.168.100.100", subnetmask="本地连接* 1")
    # print(get_ips("本地连接* 1"))
    # print(method_name())
    # print(get_ips('bdlj'))
