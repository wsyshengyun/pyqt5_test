#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
import os

from configobj import ConfigObj


def get_path(filename):
    dirname = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dirname, filename)
    return path


path = get_path('app.ini')


class MyConfigObj(object):
    def __init__(self, pth=None):
        self.path = pth
        self.conf = ConfigObj(self.path, encoding='utf8')

    def add_section(self, sec, option=None, value=None):
        if sec not in self.conf:
            self.conf[sec] = {}
        if option and value:
            self.conf[sec][option] = value
        self.conf.write()

    def get_value(self, sec, option):
        return self.conf[sec][option]

    def remove_option(self, sec, option):
        del self.conf[sec][option]
        self.conf.write()

    def remove_section(self, sec):
        del self.conf[sec]
        self.conf.write()

    def save_other_file(self, path):
        self.conf.filename = path
        self.conf.write()


config_obj = MyConfigObj(r"D:\wsy\py_pro\pyqt5_test\project\ipOnline\pack\app.ini")


def config_to_value(func):
    """ """
    key_name = func.__name__

    def inner(*args, **kwargs):
        section = kwargs.get('section')
        return config_obj.get_value(section, key_name)
    return inner


class GetObject(object):
    def __init__(self):
        """ """

    @config_to_value
    def end(self, section=None):
        pass


if __name__ == '__main__':
    obj = GetObject()
    print(obj.end(section='ip'))

