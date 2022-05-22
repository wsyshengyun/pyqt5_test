#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

import re, wmi
from time import sleep


def get_wangka_info():
    w = wmi.WMI()
    num1 = 0
    try:
        # 遍历所有网卡
        for network in w.Win32_NetworkAdapterConfiguration(IPEnabled=True):
            # print(network.Description)
            # 获取有效网卡
            if network.IPAddress:
                print('{}. {}'.format(num1, network.IPAddress))
                num1 += 1
        # 网络索引数
        n = int(input('请选择网卡：'))
        # 选择网卡
        net = w.Win32_NetworkAdapterConfiguration(IPEnabled=True)[n]

        i = input('10.10.21.')
        # IP地址
        add = ['10.10.21.{}'.format(i)]
        # 掩码
        mask = ['255.255.255.0']
        # 24位掩码 获取网络位
        zhuji = re.findall(r'(\d+.\d+.\d+.)\d+', i)
        # 配置网关地址
        g = input('网关:{}'.format(zhuji[0]))
        # 网关
        gateway = [zhuji[0] + g]
        # 网关优先级 数字越低优先级越高
        gateway_metric = [1]
        # dns
        dns = ['114.114.114.114', '223.5.5.5']
        # 配置IP、掩码
        # 我的电脑上返回值为 (-2147024891,)
        sta = net.EnableStatic(IPAddress=add, SubnetMask=mask)
        # print(sta[0])
        # 修改成功返回0
        if sta[0] != 0:
            print('{} ip/掩码修改失败！！！'.format(add))
        else:
            print('{} ip修改成功！'.format(add))
        # 配置网关、网关优先级
        gat = net.SetGateways(DefaultIPGateway=gateway, GatewayCostMetric=gateway_metric)
        # print(gat[0])
        if gat[0] != 0:
            print('{} 网关修改失败！！！'.format(gateway))
        else:
            print('{} 网关修改成功！'.format(gateway))
        # 配置DNS
        dnss = net.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
        # print(dns[0])
        if dnss[0] != 0:
            print('{} dns修改失败！！！'.format(dns))
        else:
            print('{} dns修改成功！'.format(dns))
        print('\n修改结束！')
        sleep(6)


    except Exception as e:
        print('程序出错{}'.format(e))
        sleep(6)


get_wangka_info()
