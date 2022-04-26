# -*- coding: utf-8 -*-
'''
@File    :   ping_ip.py
@Time    :   2022/03/20 18:30:25

'''

import subprocess

from PyQt5.QtCore import QObject, QThread, pyqtSignal

from .currency import get_range_ips
from .log import logger


# -----------------------------------------------------------
# 重构  用QThread实现
# -----------------------------------------------------------
class Ping_Ip(QObject):
    send_ip_signal = pyqtSignal(str)
    signal_check_end = pyqtSignal()

    def __init__(self, ip):
        super(Ping_Ip, self).__init__()
        self.ip = ip

    def run(self):
        p = subprocess.Popen(['ping.exe', self.ip], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             shell=True)
        res = p.stdout.readlines()
        for line in res:
            if 'TTL' in line.decode('gbk'):
                logger.info("IP {} is online".format(self.ip))
                self.send_ip_signal.emit(self.ip)
                break

        self.signal_check_end.emit()


# def create_ip_ths():
#     ips = get_range_ips()
#     thread_objects = []
#     ping_objs = []
#     for ip in ips:
#         ip_obj = Ping_Ip(ip)
#         th = QThread()
#         ip_obj.moveToThread(th)
#         th.started.connect(ip_obj.run)
#         thread_objects.append(th)
#         ping_objs.append(ip_obj)
#     return thread_objects, ping_objs


class ManageTheads(QObject):
    signal_all_thread_finished = pyqtSignal()  # 所有线程结束时发送
    signal_send_ip = pyqtSignal(str)  # ping 通IP时发送
    signal_thread_end = pyqtSignal(int, int)  # 当一个线程结束时产生, 发送当前已经结束的线程数和总的线程数

    num_finished_threads = 0

    def __init__(self):

        super(ManageTheads, self).__init__()

        self.objs = []
        self.ths = []

    def create_threads(self):

        ips = get_range_ips()
        self.ths = []
        self.objs = []

        for ip in ips:
            ip_obj = Ping_Ip(ip)
            th = QThread()

            ip_obj.moveToThread(th)
            th.started.connect(ip_obj.run)

            ip_obj.signal_check_end.connect(self.slot_finised_thread)
            ip_obj.signal_check_end.connect(self.emit_signal)
            ip_obj.send_ip_signal.connect(self.signal_send_ip)

            self.ths.append(th)
            self.objs.append(ip_obj)

        logger.info("创建的线程数量为:  {}".format(self.len_threads()))

    def emit_signal(self):
        self.signal_thread_end.emit(self.num_finished_threads, self.len_threads())

        pass

    def quit(self):
        for th in self.ths:
            th.quit()

    def start(self):

        for th in self.ths:
            th.start()

    def len_threads(self):

        return len(self.ths)

    def slot_finised_thread(self):

        self.num_finished_threads += 1

        if self.num_finished_threads == self.len_threads():
            self.signal_all_thread_finished.emit()
            logger.info("全部线程已经运行完成,发射信号:singal_all_thread_finished")


def main():
    pass