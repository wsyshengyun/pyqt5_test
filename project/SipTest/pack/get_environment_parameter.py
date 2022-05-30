#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
import os
import yaml
class GetEnvironmentParameter(object):

    def __init__(self):
        cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.parameter_path = os.path.join(os.path.join(cur_path, 'config'), 'environment_parameter.yaml')
        if not os.path.exists(self.parameter_path):os.mkdir(self.parameter_path)


    # def environment_parameter(self, environment_name):
    #     """
    #     获取环境参数
    #     :param environment_name: 环境名称
    #     :return:
    #     """
    #     with open(self.parameter_path, 'r', encoding='utf-8') as f:
    #         parameter = yaml.load(f)
    #     return parameter[environment_name]