# coding:utf8

from project.ipOnline.pack.ip import IP
from project.ipOnline.pack.standard_model import ContainerAtModel
from ...pack.config import JsonIpOnline


class GlobalDataUi(object):
    def __init__(self):
        """ """
        self.start1 = ""
        self.end1 = ""
        self.start2 = ""
        self.end2 = ""
        self.last_section = ""
        self.curr_section = ""
        self.config = JsonIpOnline()
        # self.config = MyConfigObj()
        self.read_cfg()
    
    def set_curr_section(self, section):
        self.last_section, self.curr_section = self.curr_section, section
    
    def get_sart_end1(self):
        return self.start1, self.end1
    
    def set_start_end1(self, start, end):
        if self.check_ip1_ip2(start, end):
            self.start1, self.end1 = start, end
        else:
            raise ValueError("输入的ip第一个要小于第二个, 且字段要相同")
    
    def get_sart_end2(self):
        return self.start2, self.end2
    
    def set_start_end2(self, start, end):
        if self.check_ip1_ip2(start, end):
            self.start2, self.end2 = start, end
        else:
            raise ValueError("输入的ip第一个要小于第二个, 且字段要相同")
    
    def read_cfg(self):
        try:
            self.start1, self.end1 = self.config.get_value('ip', 'start_end1')
        except KeyError:
            self.start1, self.end1 = '', ''
        try:
            self.start2, self.end2 = self.config.get_value('ip', 'start_end2')
        except KeyError:
            self.start2, self.end2 = '', ''
    
    def save_cfg(self):
        print("save cfg: {},{}".format(self.start2, self.end2))
        self.config.add_section('ip', 'start_end1', [self.start1, self.end1])
        self.config.add_section('ip', 'start_end2', [self.start2, self.end2])
    
    @staticmethod
    def ip_lt_ip(first, second):
        first = IP(first)
        second = IP(second)
        return first < second
    
    @staticmethod
    def ip_section_equal(first, second):
        first = IP(first)
        # second = IP(second)
        return first.is_equal_section(second)
    
    def check_ip1_ip2(self, first, second):
        return self.ip_lt_ip(first, second) and \
               self.ip_section_equal(first, second)

