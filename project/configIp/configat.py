# coding:utf8

import socket
import wmi
import ctypes
import subprocess



class MySocket(object):
    def __init__(self):
        """ """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # socket.AF_INET    指定IPv4协议
        # socket.SOCK_DGRAM  指定UDP数据报式的协议

    def send(self, bstr, ip_, port):
        """ """
        self.socket.send(bstr, (ip_, port))

    def revect(self):
        """ """
        data, addr = self.socket.recv(1024)
        data = data.decode('utf8')

    def close(self):
        self.socket.close()

    def bind(self, ip, port):
        self.bind((ip, port))


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
# res = is_admin()
# pass


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

net_list = []
res = getWinNetList(net_list)
print(res)

