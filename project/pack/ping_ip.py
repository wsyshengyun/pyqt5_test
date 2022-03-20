# -*- coding: utf-8 -*-
'''
@File    :   ping_ip.py
@Time    :   2022/03/20 18:30:25

'''



import imp
import os, time
from sys import stdin 
from .log import logger
import subprocess 
import threading 
from queue import Queue

# -----------------------------------------------------------
# ping 多个IP  都在同一网段， 比如 192.168.2.1~ 2.254
# 从1开始
# -----------------------------------------------------------
def pingComputer():
    range_max_num = 2
    for i in range(1,range_max_num):
        host = '192.168.2.' + str(i)
        status1 = 'ping success'
        status2 = 'ping faild' 
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())
        )
        p = os.popen('ping ' + host + " -n 3") 
        line = p.read()

        find_str = "无法访问目标主机"
        str_time_out = "请求超时"
        print(line)
        if find_str in line or str_time_out in line:
            print(now_time, host, status2)
        else:
            print(now_time, host, status1)

# pingComputer()


def ping_one_ip(ip):
    p = os.popen('ping ' + ip + " -n 3") 
    line = p.read()
    print(line)

# ip = '192.168.43.214'
# ping_one_ip(ip)

# -----------------------------------------------------------
# 多线程ping  IP 速度快 
# -----------------------------------------------------------


on_line_ips = []
q_ips = Queue(255)

def ping_of_subprocess(ip_dns):
    p = subprocess.Popen(['ping.exe',ip_dns], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    res = p.stdout.readlines()
    # logger.info('res length: %s' % len(res))
    for line in res:
        if 'TTL' in line.decode('gbk'):
            # on_line_ips.append(ip_dns)
            q_ips.put(ip_dns)
            logger.info('{} is online!'.format(ip_dns))
            return True
    # else:
        # if threading.active_count()   #TODO
        # pass


def checking_ips():
    ip0= '192.168.43.'
    ths = []
    for ip_num in range(2,255):
        ip = ip0 + str(ip_num) 
        # logger.info(ip)

        th = threading.Thread(target=ping_of_subprocess,args=(ip,))
        ths.append(th)
        th.setDaemon(True)
        th.start()

    for th in ths:
        th.join()
    q_ips.put('0')
    logger.info("检查IP结束")

def main():
    checking_ips()
    on_line_ips.append(0)
    logger.info('End!')

