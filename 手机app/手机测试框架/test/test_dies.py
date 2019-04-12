#!/usr/bin/python
#-*- coding='utf-8' -*-
import unittest
from 手机app.手机测试框架.config  import ds
from 手机app.手机测试框架.data import shuju
class yl(unittest.TestCase):
    shuju123=shuju.duqu()
    def test_1(self):
        dr=ds.denglu(int(self.shuju123[0][0]),self.shuju123[0][1])
    def test_2(self):
        dr = ds.denglu(int(self.shuju123[0][0]), self.shuju123[0][1])
    def test_3(self):
        dr = ds.denglu(int(self.shuju123[0][0]), self.shuju123[0][1])
    def test_4(self):
        dr = ds.denglu(int(self.shuju123[0][0]), self.shuju123[0][1])

if  __name__=='__main__':
    unittest.main()




