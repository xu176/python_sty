#!/usr/bin/python
#-*- coding='utf-8' -*-
import unittest
from  手机app.手机测试框架.rebort import HTMLTestRunnertest
def  baogao():
    suit=unittest.TestSuite()
    dis=unittest.defaultTestLoader.discover(r'C:\Users\XSW\PycharmProjects\手机app\手机测试框架\test',pattern='test_dies.py')
    for i in dis:
        suit.addTest(i)
    f=open(r'C:\Users\XSW\PycharmProjects\手机app\手机测试框架\rebort\蝶声.html','wb')
    runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title='蝶声测试',description='结果如下',tester='xu')
    runner.run(suit)
    f.close()
if __name__=='__main__':
    baogao()

