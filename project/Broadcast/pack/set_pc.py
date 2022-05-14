#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

import psutil
import os
import re
from time import sleep
from wmi import WMI
from socket import AddressFamily


local_addrs = []
for name, info in psutil.net_if_addrs().items():
    print('name is ', name)
    for addr in info:
        # 只放入IPV4的地址
        if AddressFamily.AF_INET == addr.family:
            print(addr.address)
            local_addrs.append(addr.address)
print(local_addrs)


class UpdateIp(object):
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
            ip = re.findall("\d+.\d+.\d+.\d+", con.IPAddress[0])
            if len(ip) > 0:
                return 0
            else:
                flag = flag + 1

    def runset(self, ip, subnetmask, interway, dns):
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
        wayres = adapter.SetGateways(DefaultIPGateway=interway, GatewayCostMetric=[1])
        if wayres[0] == 0:
            print('设置网关成功')
        else:
            print('修改网关失败')
            return False
        # 修改dns
        dnsres = adapter.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
        if dnsres[0] == 0:
            print('设置DNS成功,等待3秒刷新缓存')
            sleep(3)
            # 刷新DNS缓存使DNS生效
            os.system('ipconfig /flushdns')
        else:
            print('修改DNS失败')
            return False
