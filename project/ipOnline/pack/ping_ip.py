# -*- coding: utf-8 -*-
'''
@File    :   ping_ip.py
@Time    :   2022/03/20 18:30:25

'''

import subprocess

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from project.ipOnline.pack.log import logger
from project.ipOnline.pack.ip import _get_range_ips
import encodings.idna
from ping3 import ping


class PingBase(QObject):
    signal_ping_send_ip = pyqtSignal(str)
    signal_ping_check_end = pyqtSignal()

    def __init__(self, ip):
        """ """
        self.ip = ip

    def run(self):
        pass


class PingIp3(QObject):
    signal_ping_send_ip = pyqtSignal(str)
    signal_ping_check_end = pyqtSignal()

    def __init__(self, ip):
        """ """
        super(PingIp3, self).__init__()
        self.ip = ip

    def run(self):
        code = ping(self.ip, timeout=2)
        if code:
            self.signal_ping_send_ip.emit(self.ip)
        else:
            self.signal_ping_check_end.emit()


class PingIp(QObject):
    signal_ping_send_ip = pyqtSignal(str)
    signal_ping_check_end = pyqtSignal()

    def __init__(self, ip):
        super(PingIp, self).__init__()
        self.ip = ip

    def run(self):
        p = subprocess.Popen(['ping.exe', self.ip], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             shell=False)
        res = p.stdout.readlines()
        for line in res:
            if 'TTL' in line.decode('gbk'):
                logger.info("IP {} is online".format(self.ip))
                self.signal_ping_send_ip.emit(self.ip)
                break
        else:
            self.signal_ping_check_end.emit()


class ManageTheads(QObject):
    manage_signal_finishedall = pyqtSignal()  # 所有线程结束时发送
    manage_signal_send_onlineip = pyqtSignal(str)  # ping 通IP时发送
    manage_signal_oneth_end = pyqtSignal(int, int)  # 当一个线程结束时产生, 发送当前已经结束的线程数和总的线程数

    num_finished_threads = 0

    def __init__(self):
        super(ManageTheads, self).__init__()

    def create_threads(self, start=None, end=None):
        ips = _get_range_ips(start, end)
        self.ths = []
        self.objs = []

        for ip in ips:
            ip_obj = PingIp3(ip)
            # ip_obj = PingIp(ip)
            th = QThread()

            ip_obj.moveToThread(th)
            th.started.connect(ip_obj.run)

            ip_obj.signal_ping_check_end.connect(self.slot_finised_thread)
            # ip_obj.signal_check_end.connect(self.emit_signal)
            ip_obj.signal_ping_send_ip[str].connect(self.slot_send_ip)

            self.ths.append(th)
            self.objs.append(ip_obj)

        logger.info("创建的线程数量为:  {}".format(self.len_threads()))

    def slot_send_ip(self, ip):
        """ """
        print("f-> slot_send_ip: {}".format(ip))
        self.manage_signal_send_onlineip.emit(ip)
        # self.num_finished_threads += 1
        self.slot_finised_thread()

    # def emit_signal(self):
    #     self.signal_one_thread_end.emit(self.num_finished_threads, self.len_threads())


    def slot_finised_thread(self):

        self.num_finished_threads += 1
        if self.num_finished_threads >= self.len_threads():
            self.manage_signal_finishedall.emit()
            print("全部线程已经运行完成,发射信号:singal_all_thread_finished")
        self.manage_signal_oneth_end.emit(self.num_finished_threads, self.len_threads())
        print("manage_signal_oneth_end emit-> args is {}, {}".format(self.num_finished_threads, self.len_threads()))

    def quit(self):
        for th in self.ths:
            th.quit()

    def start(self):
        for th in self.ths:
            th.start()

    def len_threads(self):
        return len(self.ths)

if __name__ == '__main__':
    pass

