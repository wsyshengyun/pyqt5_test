#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
from .middle import GlobalDataUi

class GlobalDataUi2(GlobalDataUi):
    def __init__(self):
        self.ip1 = []
        self.ip2 = []
        
        
        super(GlobalDataUi2, self).__init__()

    def read_cfg(self):
        super().read_cfg()

    def save_cfg(self):
        super().save_cfg()
        
    
    