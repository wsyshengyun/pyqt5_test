# -*- coding: utf-8 -*-
'''
@File    :   ping_ip.py
@Time    :   2022/03/20 18:30:25

'''

import subprocess

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from project.ipOnline.pack.log import logger
from project.ipOnline.pack.ip import _get_range_ips


class PingIp(QObject):
    signal_send_ip = pyqtSignal(str)
    signal_check_end = pyqtSignal()

    def __init__(self, ip):
        super(PingIp, self).__init__()
        self.ip = ip

    def run(self):
        p = subprocess.Popen(['ping.exe', self.ip], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             shell=True)
        res = p.stdout.readlines()
        for line in res:
            if 'TTL' in line.decode('gbk'):
                logger.info("IP {} is online".format(self.ip))
                self.signal_send_ip.emit(self.ip)
                break
        self.signal_check_end.emit()


class ManageTheads(QObject):

    signal_all_thread_finished = pyqtSignal()  # 所有线程结束时发送
    signal_ip_on_line = pyqtSignal(str)  # ping 通IP时发送
    signal_one_thread_end = pyqtSignal(int, int)  # 当一个线程结束时产生, 发送当前已经结束的线程数和总的线程数

    num_finished_threads = 0

    def __init__(self):

        super(ManageTheads, self).__init__()
        self.objs = []
        self.ths = []

    def create_threads(self, start=None, end=None):
        ips = _get_range_ips(start, end)
        self.ths = []
        self.objs = []

        for ip in ips:
            ip_obj = PingIp(ip)
            th = QThread()

            ip_obj.moveToThread(th)
            th.started.connect(ip_obj.run)

            ip_obj.signal_check_end.connect(self.slot_finised_thread)
            ip_obj.signal_check_end.connect(self.emit_signal)
            ip_obj.signal_send_ip.connect(self.signal_ip_on_line)

            self.ths.append(th)
            self.objs.append(ip_obj)

        logger.info("创建的线程数量为:  {}".format(self.len_threads()))

    def emit_signal(self):
        self.signal_one_thread_end.emit(self.num_finished_threads, self.len_threads())


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

if __name__ == '__main__':
    pass

