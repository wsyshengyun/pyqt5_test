#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import unittest
from project.ipOnline.pack.middle import GlobalDataUi
print('------------------middle-------------\r\n')


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.gobj = GlobalDataUi()
        self.start = '192.168.3.17'
        self.end = '192.168.3.91'
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        val = self.gobj.get_start_end_ip()
        print(val)
        pass

    def test_2(self):
        self.gobj.set_sart_end_ip(self.start, self.end)
        print(self.gobj.get_start_end_ip())
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