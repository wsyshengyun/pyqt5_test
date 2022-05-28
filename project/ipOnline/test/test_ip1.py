#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import unittest
from project.ipOnline.pack.ip import _get_range_ips
from project.ipOnline.pack import ip


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.start = '192.168.2.2'
        self.end = '192.168.2.20'
        self.ip_other = '192.168.3.111'
        pass

    def tearDown(self) -> None:
        pass

    def test_get_range_ips(self):
        print(_get_range_ips(self.start, self.end))
        pass

    def test_is_equal_section(self):
        obj1 = ip.IP(self.start)
        self.assertTrue(obj1.is_equal_section(self.end))
        self.assertFalse(obj1.is_equal_section(self.ip_other))

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