#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import unittest
from project.ipOnline.pack import config as cfg 

print('---------------------config------------------\r\n')

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cfg = cfg.MyConfigObj()
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        name = 'aa.ini'
        print(cfg.get_path(name))
        print("path is : {}".format(cfg.path))
        pass

    def test_2(self):
        items = [['192.168.1.12', '192.168.1.99'], ['192.168.2.12', '192.168.2.99']]
        self.cfg.add_section('ip', 'ips', items)
        print()
        pass

    def test_3(self):
        pass

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