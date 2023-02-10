# coding:utf8
"""
关于配置文件的修改
一次IP增加1

SIP1 Phone Number       :8058
SIP1 Display Name       :8058
SIP1 Register User      :8058
.*SIP1 Phone Number\s.*:8(\d{1,3})
.*SIP1 Display Name\s.*:8(\d{1,3})
.*SIP1 Register User\s.*:8(\d{1,3})
.*SIP1 Phone Number\s.*:8\(d{1,3}).* .*SIP1 Display Name\s.*:8\(d{1,3}).* .*SIP1 Register User\s.*:8\(d{1,3}).*

SIP1 Register Addr      :192.168.9.240
WAN Gateway        :192.168.9.1
WAN IP             :192.168.9.058
"""
import re
from project.ipOnline.pack._currency import IP


class ManageConfigFile(object):
    __common_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    re_ip = r".*WAN IP\s+:({})".format(__common_ip)
    re_ip_tail = r".*WAN IP\s+:\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})"
    re_number = r".*SIP1 Phone Number\s.*:8(\d{1,3})"
    re_name = r".*SIP1 Display Name\s.*:8(\d{1,3})"
    re_user = r".*SIP1 Register User\s.*:8(\d{1,3})"

    re_ip_tail_ = r"(.*WAN IP\s+:\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}"
    re_user_ = r"(.*SIP1 Register User\s.*:8)\d{1,3}"
    re_name_ = r"(.*SIP1 Display Name\s.*:8)\d{1,3}"
    re_number_ = r"(.*SIP1 Phone Number\s.*:8)\d{1,3}"

    re_gateway = r".*WAN Gateway\s+:({})".format(__common_ip)
    re_sip_service = r".*SIP1 Register Addr\s+:({})".format(__common_ip)
    re_gateway_ = r"(.*WAN Gateway\s+:)" + __common_ip
    re_sip_service_ = r"(.*SIP1 Register Addr\s+:)" + __common_ip

    def __init__(self, path=r"D:\_python\my\xdkj_test\project\SipTest\sip_config.txt"):
        """ """
        self.path = path
        self.ip = None
        self.__content = self.readfile()
        self.get_currip()

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value

    def update_ip_tail(self, ip_tail: str):
        tsr = re.sub(self.re_number_, lambda m: m.group(1) + ip_tail, self.content)
        tsr = re.sub(self.re_name_, lambda m: m.group(1) + ip_tail, tsr)
        tsr = re.sub(self.re_user_, lambda m: m.group(1) + ip_tail, tsr)
        tsr = re.sub(self.re_ip_tail_, lambda m: m.group(1) + ip_tail, tsr)
        self.content = tsr
        return tsr

    def write(self):
        if self.content == self.readfile():
            return

        with open(self.path, 'w', encoding='utf8') as f:
            f.write(self.content)

    def get_currip(self):
        matter = re.search(self.re_ip, self.content)
        if matter:
            self.ip = matter.group(1)
            return self.ip

    def readfile(self):
        with open(self.path, 'r', encoding='utf8') as f:
            line_list = f.readlines()
            return ''.join(line_list)

    def check_ip(self, ip: str):
        if not IP(self.ip).is_equal_section(ip):
            raise ValueError("IP不在一个网段")

    def replace_gateway(self, ip_gateway):
        self.check_ip(ip_gateway)
        self.content = re.sub(self.re_gateway_, lambda m: m.group(1) + ip_gateway, self.content)

    def replace_sip_service(self, ip_sip_service):
        self.check_ip(ip_sip_service)
        self.content = re.sub(self.re_sip_service_, lambda m: m.group(1) + ip_sip_service, self.content)

    def get_config_info(self):
        """

        """
        info_dict = {'配置文件IP为：': self.ip}

        match = re.search(self.re_gateway, self.content)
        if match:
            info_dict['默认网关为：'] = match.group(1)

        match = re.search(self.re_sip_service, self.content)
        if match:
            info_dict['SIP服务器地址为:'] = match.group(1)

        return '\n'.join([' '.join([key, value]) for key, value in info_dict.items()])

    def update_ip(self, ip):
        """

        """
        # 更新ip配置文件的当前ip值
        # 更新电话号码3个
        self.check_ip(ip)
        tail = IP(ip).tail()
        self.update_ip_tail(tail)
        self.ip = ip


def main():
    """ """
    obj = ManageConfigFile()
    print(obj.get_config_info())
    pass


if __name__ == '__main__':
    main()

