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


class ConfigFile(object):
    restr = r".*WAN IP             :(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    re_ip_tail = r".*WAN IP\s+:\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})"

    re_number = r".*SIP1 Phone Number\s.*:8(\d{1,3})"
    re_name = r".*SIP1 Display Name\s.*:8(\d{1,3})"
    re_user = r".*SIP1 Register User\s.*:8(\d{1,3})"

    re_ip_tail_ = r"(.*WAN IP\s+:\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}"
    re_user_ = r"(.*SIP1 Register User\s.*:8)\d{1,3}"
    re_name_ = r"(.*SIP1 Display Name\s.*:8)\d{1,3}"
    re_number_ = r"(.*SIP1 Phone Number\s.*:8)\d{1,3}"

    re_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    re_gateway = r"(.*WAN Gateway\s+:)" + re_ip
    re_sip_service = r"(.*SIP1 Register Addr\s+:)" + re_ip

    def __init__(self, path=r"D:\_python\xdkj_test\project\SipTest\sip_config.txt"):
        """ """
        self.path = path
        self.ip = None
        self.content = None
        self.get_currip()

    def replace_ip(self, value):
        tsr = re.sub(self.re_number_, lambda m: m.group(1) + value, self.content)
        tsr = re.sub(self.re_name_, lambda m: m.group(1) + value, tsr)
        tsr = re.sub(self.re_user_, lambda m: m.group(1) + value, tsr)
        tsr = re.sub(self.re_ip_tail_, lambda m: m.group(1) + value, tsr)
        self.content = tsr
        self.write()
        return tsr

    def write(self):
        with open(self.path, 'w', encoding='utf8') as f:
            f.write(self.content)

    def get_currip(self):
        self.ip = None
        content = self.readfile()
        matter = re.search(self.restr, content)
        if matter:
            return matter.group(1)

    def readfile(self):
        with open(self.path, 'r', encoding='utf8') as f:
            line_list = f.readlines()
            content = ''.join(line_list)
            # print(content)
            self.content = content
            return content

    def set_ip_add1(self):
        """
        IP的末端值+1
        """

        pass

    def set_ip_value(self, tail_num):
        """
        设置iP的末端到某个值
        """
        pass

    def set_base(self):
        """
        设置本次配置文件的基本参数
        """
        pass

    def replace_gateway(self, ip_gateway):
        tsr = re.sub(self.re_gateway, lambda m: m.group(1) + ip_gateway, self.content)
        self.content = tsr
        return tsr
        pass

    def replace_sip_service(self, ip_sip_service):
        tsr = re.sub(self.re_sip_service, lambda m: m.group(1) + ip_sip_service, self.content)
        self.content = tsr
        return tsr


def main():
    """ """
    obj = ConfigFile()
    # obj.readfile()
    print(obj.get_currip())
    pass


if __name__ == '__main__':
    main()

