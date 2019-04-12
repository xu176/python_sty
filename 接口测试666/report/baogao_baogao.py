#!/usr/bin/python
#-*- coding='utf-8' -*-
import unittest
from 接口测试666.report  import  HTMLTestRunner
def baogao_(aa):
  suit=unittest.TestSuite()
    #两个参数，1路径，2匹配条件
    #到这个路径下匹配所有的以test开头的文件
    #test开头文件中找到函数以test开头
  for o in aa:
    dis=unittest.defaultTestLoader.discover(r'C:\Users\XSW\PycharmProjects\接口测试666\suopei_test',pattern='test_{}.py'.format(o.strip()))
    print(dis)
    for  i in dis:
       suit.addTest(i)
  f=open(r'C:\Users\XSW\PycharmProjects\接口测试666\report\c.html','wb')
  runner=HTMLTestRunner.HTMLTestRunner(title='索赔',stream=f,description='结果如下',tester='xu')
  runner.run(suit)
  f.close()
if __name__=='__main__':
     baogao_()
