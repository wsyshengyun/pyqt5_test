#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QBoxLayout
from project.ipOnline.pack.currency import CompareIpListAt
from project.ipOnline.pack.currency import IpState
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt




class HBoxlayout(object):
    def __init__(self, widget, key="" ):
        """ """
        self.widget = widget
        self.key = key
        # self.lay = QHBoxLayout(self.widget)
        self.lay = QHBoxLayout()
        self.lay.setAlignment(Qt.AlignLeft)
        # self.lay.setAlignment()
        self.num = 0
        if self.key:
            self.add_label(key)
            self.num += 1

    def is_full(self):
        return True if self.num>=10 else False

    def get_key(self):
        return self.key

    def add_label(self, key):
        if key != "" and isinstance(key, str):
            self.label = QLabel(key, self.widget)
            self.lay.addWidget(self.label)

    def add_button(self, tail):
        if self.is_full(): return False

        if isinstance(tail, str) and tail != "":
            btn = QPushButton(tail, self.widget)
            btn.setMaximumWidth(70)
            self.lay.addWidget(btn)
            self.num += 1
            return True






class Vlayout(object):
    def __init__(self, widget, comiplistat: CompareIpListAt):
        self.widget = widget
        self.comiplistat = comiplistat
        # self.v_box = QtWidgets.QVBoxLayout(self.widget)
        self.v_box = QtWidgets.QVBoxLayout()
        self.h_box_list = []
        pass

    def get_box(self):
        return self.v_box

    def get_main_v_box(self):
        return self.v_box

    def insert_h_box(self, h_box: HBoxlayout):
        if isinstance(h_box, HBoxlayout):
            key = h_box.get_key()
            ind = 0
            for hbox in self.h_box_list:
                if key == hbox.get_key():
                    ind = self.h_box_list.index(hbox)
                    break
            else:
                ind = -1
            self.h_box_list.insert(ind, h_box)
            self.v_box.insertLayout( ind, h_box.lay)
            # h_box.lay.insertLayout(ind, self.v_box)
            # self.v_box.insertItem(ind, h_box)


    def insert_ipobj(self, ipobj:IpState):
        find_box = None
        key = ipobj.section()
        for box in self.h_box_list:
            if box.get_key() == key and not box.is_full():
                find_box = box
                break
        else:
            # 新建一个
            find_box = HBoxlayout(self.widget, key)
            self.insert_h_box(find_box)
        find_box.add_button(ipobj.tail())


    def insert_comiplist_at(self):
        for obj_ip in self.comiplistat.ips:
            self.insert_ipobj(obj_ip)
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






