#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
"""
装集合的容器

"""
from project.ipOnline.pack.currency import IpState
from project.ipOnline.pack.currency import CompareIpListAt
from typing import List

class Container(object):
    """
    横向容器 容纳10个对象
    """

    def __init__(self):
        """ """
        self.size_max = 10
        self.section = ""
        self.list: List[IpState] = []  # 里面是相同的字段的IP

    def add(self, ipoat: IpState):
        """
        默认按顺序排序 从小到大

        """
        sec_ = ipoat.section()

        # 如果列表为空
        if not self.list:
            if not self.section:
                self.list.append(ipoat)
                self.section = sec_
                return 0  # 索引位置
            else:
                if sec_ == self.section:
                    self.list.append(ipoat)
                    return 0
                else:
                    # 要添加的第一个元素字段不一致,添加失败
                    return None

        if self.section != sec_:  # 添加的元素的字段不一致
            return None

        if self.isfull():
            raise ValueError("列表已经满,不能再插入")

        tail = int(ipoat.tail())
        for ipo_ in self.list:
            tail_ = int(ipo_.tail())
            if tail <= tail_:  # 如果要插入的尾部 <= 现在的对象尾部, 立即插入到现在对象的前面,否则
                index_ = self.list.index(ipo_)
                self.list.insert(index_, ipoat)
                return self.list.index(ipoat)  # todo 可以修改更简单的方法
            else:
                continue
        self.list.append(ipoat)

    def isfull(self):
        return True if len(self.list) == self.size_max else False

    def set_section(self, section):
        self.section = section

    def get_section(self):
        return self.section

    def __str__(self):
        eles = ','.join([ipo.get_ip() for ipo in self.list])
        tsr = "<Container> [{}]".format(eles)
        return tsr

    def __lt__(self, other):
        this = int(self.section)
        return True if this < int(other.section) else False

    def __gt__(self, other):
        this = int(self.section)
        return False if this < int(other.section) else True

    def __le__(self, other):
        this = int(self.section)
        return True if this <= int(other.section) else False
        pass

    def __ge__(self, other):
        this = int(self.section)
        return False if this <= int(other.section) else True
        pass



class ContainerAt(object):
    """
    纵向容器, 容纳横向容器
    """

    def __init__(self, current_section):
        """ """
        self.list: List[Container] = []
        self.current_section = current_section  # 当前的字段

    def add_ipo(self, ipoat: IpState):
        """
         添加一个ipoat对象
        """
        # 根据ipoat对象的字段找到一个co对象
        for co_ in self.list:
            if co_.section == ipoat.section() and not co_.isfull():
                co_.add(ipoat)
                break
        else:
            new_co = Container()
            new_co.set_section(ipoat.section())
            new_co.add(ipoat)
            self.add_co(new_co)

    def add_co(self, co: Container):
        # 如果list为空,直接插入
        if self.is_empty():
            self.list.append(co)
            return

            # 判断是否为当前的字段容器
        # 如果是则放在第一位
        if co.section == self.current_section:
            self.list.insert(0, co)
            return
        else:
            # 不是当前的字段容器
            # 找到相同字段的容器,放在它的前面
            b, pos = self.is_container_section(co.section)
            if b:
                self.list.insert(pos, co)
                return
            else:
                # 列表里面没有相同字段的容器
                # 放比它小的容器前面
                for obj_ in self.list:
                    if obj_.section == self.current_section:
                        continue
                    else:
                        if co <= obj_:
                            index_ = self.list.index(obj_)
                            self.list.index(index_, co)
                            return index_
                else:
                    # 没有知道比它小的,放在最后
                    self.list.append(co)
                    return self.list.index(co)

    def is_empty(self):
        return True if len(self.list) == 0 else False

    def is_firt_equal_section(self):
        """
         如果列表第一个元素的字段为当前字段,则返回True
         否则返回False
         如果列表为空,返回None
        """

        if self.is_empty(): return None
        if self.list[0].section == self.current_section:
            return True
        else:
            return False

    def is_current_section(self, co: Container):
        return True if self.current_section == co.section else False

    def is_container_section(self, section: str):
        for co in self.list:
            if co.section == section:
                return True, self.list.index(co)
        return False, False


    def __str__(self):
        str_list = []
        for obj in self.list:
            str_list.append(str(obj))
        tsr_all = '\r\n'.join(str_list)
        return tsr_all


if __name__ == '__main__':
    from project.ipOnline.pack.test_generate_ip import iplist

    # obj = Container()
    # for ip in iplist:
    #     obj.add(IpState(ip))

    # print(obj)
    obj2 = Container()
    obj2.section = "5"
    for ip in iplist:
        obj2.add(IpState(ip))

    # print(obj2)
    # print("obj>obj2: {}".format(obj > obj2))
    # print("obj<obj2: {}".format(obj < obj2))

    objAt = ContainerAt('12')
    for ip in iplist:
        ipoat = IpState(ip)
        objAt.add_ipo(ipoat)

    print(objAt)


