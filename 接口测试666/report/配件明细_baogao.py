#!/usr/bin/python
#-*- coding='utf-8' -*-
from 接口测试666.report import HTMLTestRunner
import unittest
def baogao():
    suit=unittest.TestSuite()
    dis=unittest.defaultTestLoader.discover(r'C:\Users\XSW\PycharmProjects\接口测试666\suopei_test',pattern='test_配件明细.py')
    for i in dis:
        suit.addTest(i)
    f=open(r'C:\Users\XSW\PycharmProjects\接口测试666\report\配件明细.html', 'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,tester='xu',description='结果如下',title='配件明细')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    baogao()