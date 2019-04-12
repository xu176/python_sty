#!/usr/bin/python
#-*- coding='utf-8' -*-
import unittest
from 接口测试666.config import 电子信息查询
from 接口测试666.data  import 电子发票数据
class dianzifapiao(unittest.TestCase):
    shuju=电子发票数据.dianzishuju()
    shuju123=shuju.duqu()
    def test_1(self):
        dz=电子信息查询.dianzi()
        asd=dz.xinxi(self.shuju123[0][0])
        self.assertEqual(asd['data']['orderDate'],"2019-03-26")
    def test_2(self):
        dz=电子信息查询.dianzi()
        asd=dz.xinxi(self.shuju123[1][0])
        self.assertEqual(asd['errMsg'],'处理成功')
    def test_3(self):
        dz=电子信息查询.dianzi()
        asd=dz.xinxi(self.shuju123[2][0])
        self.assertEqual(asd['errMsg'],'处理成功')
    def test_4(self):
        dz=电子信息查询.dianzi()
        asd=dz.xinxi(self.shuju123[3][0])
        self.assertEqual(asd['errMsg'],'处理成功')
    def test_5(self):
        dz=电子信息查询.dianzi()
        asd=dz.xinxi(self.shuju123[4][0])
        self.assertEqual(asd['errMsg'],'处理成功')
if __name__=='__main__':
    unittest.main()
