#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8


# 一键修改IP工具,但是有些电脑可能不太好用,不知道是为什么
import os
import sys
import wmi
import ctypes
import subprocess


# from __future__ import print_function

def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
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


def setIpMask(adapter, iplist, masklist):
    for i in range(len(iplist)):
        print('ip:' + str(iplist[i]) + ' mask:' + str(masklist[i]))
        # 开始执行修改ip、子网掩码、网关
    ipres = adapter.EnableStatic(IPAddress=iplist, SubnetMask=masklist)
    if ipres[0] == 0:
        print('设置IP成功')
    else:
        if ipres[0] == 1:
            print('设置IP成功')
        else:
            print('修改IP失败')
            print(ipres[0])
            return False
    # #修改网关
    # wayres = adapter.SetGateways(DefaultIPGateway=interway, GatewayCostMetric=[1])
    # if wayres[0] == 0:
    #     print('设置网关成功')
    # else:
    #     print('修改网关失败')
    #     return False
    # #修改dns
    # dnsres = adapter.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
    # if dnsres[0] == 0:
    #     print('设置DNS成功,等待3秒刷新缓存')
    #     sleep(3)
    #     # 刷新DNS缓存使DNS生效
    #     os.system('ipconfig /flushdns')
    # else:
    #     print('修改DNS失败')
    #     return False


# 执行windows命令
def execCommand(commands) -> list:
    """执行windows命令"""
    if not commands:
        return list()
    # 子进程的标准输出设置为管道对象
    if isinstance(commands, str):
        commands = [commands]
    return_list = []
    for i in commands:
        p = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        # p.wait()
        res = "".join(p.stdout.readlines())
        return_list.append(res)
    return return_list


def getConfigurableNetCard():
    net_card_data = []
    res = execCommand("ipconfig /all")
    temp_dict = {}
    for x in res[0].splitlines():
        # 如果发现新的适配器，则重置上一个网卡是否可用的状态
        if "网适配器" in x:
            if "以太网适配器" in x:
                if '蓝牙' in x:
                    continue
                else:
                    temp_dict['card_name'] = x.split(" ", 1)[1][:-1]
                    temp_dict['mac'] = []
                    # print("当前网卡 %s" % (temp_dict['card_name']))
                    continue

        if temp_dict:
            # # 匹配IP正则
            # if "IPv4 地址" in x:
            #     pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
            #     ip = pattern.search(x).group()
            #     temp_dict['ip'].append(ip)
            #     continue
            if "物理地址" in x:
                mac = x.split(': ')[1].replace('-', ':')
                temp_dict['mac'].append(mac)
                net_card_data.append(temp_dict)
                temp_dict = {}
            else:
                continue

    return net_card_data


def getModifyNetCardMac(netCardName, configuraList):
    for i in range(len(configuraList)):
        if netCardName in configuraList[i]['card_name']:
            mac = configuraList[i]['mac'][0]
            break
    return mac


def getModifyNetCardNum(netCardMac, winNetLists):
    for i in range(len(winNetLists)):
        if netCardMac in winNetLists[i]['mac']:
            num = winNetLists[i]['num']
            break
    return num


def getNetCardName(str):
    name = ''
    if 'netcardname' in str:
        name = str.split(':')[1]
    return name


def getConfigIpMask(str):
    info = {}
    if 'ip' in str:
        ip = str.split('ip:')[1].split(' ')[0]
        if 'mask' in str:
            mask = str.split('mask:')[1].split(']')[0]
            info['ip'] = ip
            info['mask'] = mask
    return info


def ReadConfig(netcardname):
    data = {}
    data['ip'] = []
    data['mask'] = []
    linenum = 0
    config = 'config.txt'
    if True == os.path.exists(config):
        with open(config, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                if 0 == linenum:
                    tmpName = getNetCardName(line)
                    netcardname.append(tmpName)
                    print('要配置的网卡:' + str(netcardname))
                else:
                    tmpinfo = getConfigIpMask(line)
                    data['ip'].append(tmpinfo['ip'])
                    data['mask'].append(tmpinfo['mask'])
                linenum += 1
    # print(data)
    return data


def main():
    netcardname = []
    winNetLists = []

    datainfo = ReadConfig(netcardname)

    configuraList = getConfigurableNetCard()

    configs = getWinNetList(winNetLists)

    modifyMac = getModifyNetCardMac(netcardname[0], configuraList)

    modifyNetCardNum = getModifyNetCardNum(modifyMac, winNetLists)

    setIpMask(configs[modifyNetCardNum], datainfo['ip'], datainfo['mask'])

    input('按回车退出')


if __name__ == '__main__':

    if isAdmin():
        print('管理员权限操作')
        main()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

# 关于config.txt文件的配置要求如下：
# 第一行必须配置网卡名, 且只可以改“netcardname:”后面的字符 其它几行配置IP和掩码以及注释，须按照
# XXXX[ip:xxx.xxx.xxx.xxx
# mask: xxx.xxx.xxx.xxx]的格式 其中x需要填数字, X可选填汉字也可不填,
# 注意ip的最后一位与mask字符中间有一个空格.
#
# 例如：config.txt
# netcardname: ElecOC 设备1[ip:10.16 .94 .2 mask: 255.0 .0 .0]
# 设备2[ip:10.16 .94 .6 mask: 255.0 .0 .0]
# 设备3[ip:10.24 .10 .2 mask: 255.0 .0 .0]
# 设备4[ip:10.24 .94 .6 mask: 255.0 .0 .0]
# 设备5[ip:10.24 .94 .2 mask: 255.0 .0 .0]
# 设备6[ip:10.24 .10 .6 mask: 255.0 .0 .0]
# 设备7[ip:10.28 .94 .6 mask: 255.0 .0 .0]
# 设备8[ip:10.28 .94 .2 mask: 255.0 .0 .0]
