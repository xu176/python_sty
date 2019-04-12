#!/usr/bin/python
#-*- coding='utf-8' -*-
from 接口测试666.config import  订单明细1
from 接口测试666.data import  订单明细
import unittest
class  dingdmx(unittest.TestCase):
    shuju=订单明细.dingdanmx_duqu()
    def test_1(self):
        dd=订单明细1.dzmx()
        asd=dd.dzmx_c(int(self.shuju[1][0]),int(self.shuju[1][1]),self.shuju[1][2])
        self.assertEqual(asd['data']['pageInfo']['list'][0]['partCode'],'10280777')
    def test_2(self):
        dd=订单明细1.dzmx()
        asd=dd.dzmx_c(self.shuju[2][0],int(self.shuju[2][1]),self.shuju[2][2])
        self.assertEqual(asd['message'],'get error')
    def test_3(self):
        dd=订单明细1.dzmx()
        asd=dd.dzmx_c(int(self.shuju[3][0]),self.shuju[3][1],self.shuju[3][2])
        self.assertEqual(asd['message'],'get error')
    def test_4(self):
        dd=订单明细1.dzmx()
        asd=dd.dzmx_c(int(self.shuju[4][0]),int(self.shuju[4][1]),self.shuju[4][2])
        self.assertEqual(asd['errMsg'],'该订单号对应的订单不存在！')
    def test_5(self):
        dd=订单明细1.dzmx()
        asd=dd.dzmx_c(int(self.shuju[5][0]),int(self.shuju[5][1]),self.shuju[5][2])
        self.assertEqual(asd['errMsg'],'该订单号对应的订单不存在！')
if __name__=='__main__':
    unittest.main()


