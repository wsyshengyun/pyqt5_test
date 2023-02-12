# coding:utf8

from ...pack.ip import IP
# from project.ipOnline.pack.standard_model import ContainerAtModel
from ...pack.config import JsonIpOnline

def check_edit_text(ip_text:str, flag='start'):
    """
    如果ip_text是一个ip,则直接返回
    如果ip是一个正数,其范围在0到255,
        输出一个元组
    """
    try:
        
        ipobj = IP(ip_text)
        print("is obj")
        return ip_text
    except TypeError:
        print("not ipobj")
        try:
            val = int(ip_text)
            if val < 255:
                fax = "192.168." + ip_text.strip() + '.'
                s1 = (fax+'2', fax+'254')
                s2 = (fax+'254', fax+'2`')
                if flag == "start":
                    return s1
                else:
                    return s2
            else:
                raise ValueError("输入的值应该小于255")
        except ValueError:
            # 返回为空
            raise ValueError("输入的数值错误,不是一个IP,也不是一个数字")
            pass
        
        
        

class GlobalDataUi(object):
    def __init__(self):
        """ """
        self.start1 = ""
        self.end1 = ""
        self.start2 = ""
        self.end2 = ""
        self.config = JsonIpOnline()
        self.read_cfg()

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
        
        
    
    
    def set_start_end1(self, start, end):
        if self.check_ip1_ip2(start, end):
            self.start1, self.end1 = start, end
        else:
            raise ValueError("输入的ip第一个要小于第二个, 且字段要相同")
    
    
    def set_start_end2(self, start, end):
        if self.check_ip1_ip2(start, end):
            self.start2, self.end2 = start, end
        else:
            raise ValueError("输入的ip第一个要小于第二个, 且字段要相同")
    

    
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

