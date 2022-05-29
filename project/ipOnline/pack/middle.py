# coding:utf8

from project.ipOnline.pack.standard_model import ContainerAtModel
from project.ipOnline.pack.ip import IP, IpState
from project.ipOnline.pack.config import MyConfigObj


class GlobalDataUi(object):
    def __init__(self):
        """ """
        self.start1 = ""
        self.end1 = ""
        self.start2 = ""
        self.end2 = ""
        self.last_section = ""
        self.curr_section = ""
        self.config = MyConfigObj()
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


    def cfg_read(self):
        ips = self.config.get_value('ip', 'ips')


    @staticmethod
    def ip_lt_ip(first, second):
        first =IP(first)
        second = IP(second)
        return first < second

    @staticmethod
    def ip_section_equal(first, second):
        first =IP(first)
        # second = IP(second)
        return first.is_equal_section(second)

    def check_ip1_ip2(self, first, second):
        return self.ip_lt_ip(first, second) and \
                self.ip_section_equal(first, second)





class ListSelectIp(object):
    def __init__(self):
        """ """
        pass



class SwitchIP(object):
    def __init__(self, model: ContainerAtModel):
        """ """
        self.model = model
        pass

    def change_section(self, section: str):
        """
        当IP字段改变的时候,应有的变化
        """
        self.model.switch_section(section)

    def _change_last_section_state(self):
        """
        刷新一下上一个IP字段的对应的ipoat对象的状态
        """

        pass

    def flush_model(self):
        """
        刷新model,改变第一行的数据和之前行的IP状态,以不同的颜色显示
        """

        pass






