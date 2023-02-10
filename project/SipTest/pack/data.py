#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
"""
[set]
path_config = ""
sip_service = 192.168.9.240
ip_section = 9
ip_start = 2
ip_step = 1
"""

from project.ipOnline.pack.config import MyConfigObj

config_dict ={
    'path_config': "",
    "sip_service": "",
    "ip_section": "",
    "ip_start": "",
    "ip_step": ""
}


def get_config():
    global config_dict
    obj = MyConfigObj(pth=r"D:\_python\my\xdkj_test\project\SipTest\other\sip_app.ini")
    for key in config_dict:
        config_dict[key] = obj.get_value('set', key)


def set_config():
    global config_dict
    obj = MyConfigObj(pth=r"D:\_python\xdkj_test\project\SipTest\other\sip_app.ini")
    for key in config_dict:
        value = config_dict.get(key)
        obj.add_section('set', key, value)


# todo 启动时的数据
class AllData(object):
    def __init__(self):
        """ """
        self.config_dict ={
            'path_config': "",
            "sip_service": "",
            "ip_section": "",
            "ip_start": "",
            "ip_step": ""
        }

        self.start = None   # 配置的IP开始的末段数；
        self.sep = None     # 配置IP时，自动跳过的步长，默认为1
        self.section = None  # 配置的IP字段
        self.sip_server = None  # SIP服务器地址
        self.path_config_file = ""   # SIP导入的配置文件路径




if __name__ == '__main__':
    config_dict['path_config'] = '123'
    set_config()
    get_config()
    print(config_dict)
