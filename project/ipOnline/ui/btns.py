#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from project.ipOnline.pack.currency import CompareIpListAt
from project.ipOnline.pack.currency import IpState



class Buttons(object):
    def __init__(self, widget, comiplistat: CompareIpListAt):
        self.widget = widget
        self.comiplistat = comiplistat
        pass

    def create_control(self):
        dit = self.comiplistat.type_ips()
        widget_dit = {}
        if dit:
            seckeys = dit.keys()
            for seckey in seckeys:
                lab = QLabel(seckey, self.widget)
                widget_dit[seckey] = [lab]
            for seckey in dit:
                ips = dit[seckey]
                for ipobj in ips:
                    if isinstance(ipobj, IpState):
                        tail = ipobj.tail()
                        btn = QPushButton(tail, self.widget)
                        widget_dit[seckey].append(btn)
        return widget_dit


    def create_layout(self):
        # {key: HBox}
        dit_layout = {}
        widget_dit = self.create_control()
        len_ = len(widget_dit)
        h_box_list = [QHBoxLayout(self.widget)] * len_

        for key in widget_dit:
            if key not in dit_layout:
                dit_layout[key] = QHBoxLayout(self.widget)

            lay = dit_layout.get(key)
            for wid in widget_dit[key]:
                lay.addWidget(wid)

        return dit_layout






