#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import unittest
from project.Broadcast.pack import setip

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isAdmin(self):
        print('+'*50)
        print(setip.isAdmin())
        pass

    def test_2(self):
        lit = []
        result = setip.getWinNetList(lit)
        print('lit is {}'.format(lit))
        print('result is {}'.format(result))
        pass

    # @unittest.skip
    # def test_3(self):
    #     print("设置IP测试")
    #     adapter = 'bdlj'
    #     iplist = ['192.168.1.151', '192.168.2.151', '192.168.3.151']
    #     masklist = ['255.255.255.0'] * 3
    #     result = setip.setIpMask(adapter, iplist, masklist)
    #     print("结果是: ", result)
    #     pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass


if __name__ == '__main__':
    unittest.main()