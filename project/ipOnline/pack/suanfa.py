#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

class CoObj(object):
    def __init__(self, key):
        """ """
        self.key = key

    def __str__(self):
        return "<coobj: {}".format(self.key)


class CoObjAt(object):
    def __init__(self):
        """ """
        self.list = [CoObj]
        self.cur_key = None

    def sort(self):
        pass


    def add_coobj(self):
        pass

    def add_ele(self):
        pass

    def flush(self):
        self.list.sort(key=lambda x: x.key)
        pass

    def __str__(self):
        return "\r\n".join([str(co) for co in self.list])

if __name__ == '__main__':
    coat = CoObjAt()
    coat.list = [
        CoObj(6),
        CoObj(4),
        CoObj(3),
        CoObj(7),
        CoObj(6),
        CoObj(7),
        CoObj(17),
        CoObj(97),
        CoObj(67),
    ]
    coat.flush()
    print(coat)

