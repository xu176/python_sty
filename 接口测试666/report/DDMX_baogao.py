#!/usr/bin/python
#-*- coding='utf-8' -*-
from 接口测试666.report  import HTMLTestRunner
import unittest
def baogao():
    suit=unittest.TestSuite()
    dis=unittest.defaultTestLoader.discover(r'C:\Users\XSW\PycharmProjects\接口测试666\suopei_test',pattern='test_订单明细.py')
    print(dis)
    for n in dis:
        suit.addTest(n)
    f=open(r'C:\Users\XSW\PycharmProjects\接口测试666\report\订单明细.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(title='订单明细',stream=f,tester='xu',description='结果如下')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    baogao()

