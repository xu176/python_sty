#!/usr/bin/python
#-*- coding='utf-8' -*-
import unittest
from 接口测试666.report import  HTMLTestRunner
def baog():
    suit=unittest.TestSuite()
    dis = unittest.defaultTestLoader.discover(r'C:\Users\XSW\PycharmProjects\接口测试666\suopei_test',pattern='test_电子发票.py')
    print(dis)
    for i in dis:
        suit.addTest(i)
    f=open(r'C:\Users\XSW\PycharmProjects\接口测试666\report\电子发票.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(title='索赔',stream=f,description='结果如下',tester='xu')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    baog()
