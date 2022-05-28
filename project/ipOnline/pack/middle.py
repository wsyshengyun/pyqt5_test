# coding:utf8

from project.ipOnline.pack.standard_model import ContainerAtModel

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






