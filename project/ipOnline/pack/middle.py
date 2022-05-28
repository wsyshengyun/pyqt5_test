# coding:utf8

from project.ipOnline.pack.standard_model import ContainerAtModel

class Switech_ip(object):
    def __init__(self, model: ContainerAtModel):
        """ """
        self.section = ""
        self.model = model
        pass

    def update(self, section: str):
        self.section = section
        self.change_last_section_state()

    def change_last_section_state(self):
        pass

    def flush_model(self):
        pass






