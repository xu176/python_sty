#!/usr/bin/python
#-*- coding='utf-8' -*-
from 接口测试666.config import 配件明细
from  接口测试666.data import 配件明细_d
import unittest
class yl(unittest.TestCase):
    shuju=配件明细_d.sj_1()
    shuju123=shuju.duqu()
    def  test_6(self):
        qingq = 配件明细.peijian()
        asd=qingq.wzhi(self.shuju123[0][0])
        self.assertEqual(asd['data']['orderTypeDesc'],'常规订单')
    def  test_7(self):
        qingq = 配件明细.peijian()
        asd=qingq.wzhi(self.shuju123[1][0])
        self.assertEqual(asd['message'],"get error")
    def  test_8(self):
        qingq = 配件明细.peijian()
        asd=qingq.wzhi(self.shuju123[2][0])
        self.assertEqual(asd['message'],"get error")
    def  test_9(self):
        qingq = 配件明细.peijian()
        asd=qingq.wzhi(self.shuju123[3][0])
        self.assertEqual(asd['status'],1)
    def  test_10(self):
        qingq = 配件明细.peijian()
        asd=qingq.wzhi(self.shuju123[4][0])
        self.assertEqual(asd['status'],1)
if __name__=='__main__':
    unittest.main()