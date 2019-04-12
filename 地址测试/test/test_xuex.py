#!/usr/bin/python
#-*- coding='utf-8' -*-
import unittest
from  地址测试.config import  xuexiao
from  地址测试.data  import   shuju
class xuexiao_case(unittest.TestCase):
    sj=shuju.xuexiao_shuju()
    sj123=sj.duqu_shuju()
    def test_1(self):
        xxiao=xuexiao.xuexiao()
        asd=xxiao.dz(self.sj123[0][0])
        self.assertEqual(asd['data'][0]['schoolName'],'北京中学')
    def test_2(self):
        xxiao=xuexiao.xuexiao()
        asd=xxiao.dz(self.sj123[1][0])
        self.assertEqual(asd['data'][0]['schoolName'],'郑州二中')
    def test_3(self):
        xxiao=xuexiao.xuexiao()
        asd=xxiao.dz(int(self.sj123[2][0]))
        self.assertEqual(asd['data'][0]['schoolName'],'丰城第四中学')
    def test_4(self):
        xxiao=xuexiao.xuexiao()
        asd=xxiao.dz(int(self.sj123[3][0]))
        self.assertEqual(asd['data'][0]['schoolName'],'洛阳第五十中学')
if __name__=='__main__':
  unittest.main()
