#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

iplist = [
    '192.168.1.2',
    '192.168.1.13',
    '192.168.1.4',
    '192.168.1.14',

    '192.168.1.15',
    '192.168.1.16',
    '192.168.1.17',
    '192.168.1.18',
    '192.168.1.19',
    '192.168.8.2',
    '192.168.8.12',
    '192.168.5.12',
    '192.168.5.9',
    '192.168.5.3',

    '192.168.5.13',
    '192.168.1.8',
    '192.168.1.7',
    '192.168.8.32',
    '192.168.8.82',
    '192.168.1.69',
    '192.168.12.2',
    '192.168.12.12',
    '192.168.12.32',
    '192.168.12.82',
]


def generator_ip():
    for ip in iplist:
        yield ip

class B:
    def __init__(self):
        pass

    def fun(self):
        pass


class A:
    def __init__(self):
        """ """
        self.list = [1,2,3,4,11]
        self.pos = 0

    def __iter__(self):
        return self
        pass

    def __next__(self):
        if self.pos < len(self.list):
            item = self.list[self.pos]
            self.pos += 1
            return item
            pass
        else:
            self.pos = 0
            raise StopIteration

    def __contains__(self, item):
        return item in self.list

    def foo(self):
        for  val in self:
            print(val)
class C(A, B):
    def __init__(self):
        """ """
        super(C, self).__init__()
        pass


if __name__ == '__main__':
    # g = generator_ip()
    # for i in range(len(iplist)):
    #     print(next(g))

    # obj = A()
    # obj.foo()
    # obj.list.append('a')
    # print(obj.list)
    # print("a in self.list : {}".format('a' in obj.list))
    # obj.foo()
    # obj.foo()

    objc = C()
    objc.foo()
    objc.foo()

