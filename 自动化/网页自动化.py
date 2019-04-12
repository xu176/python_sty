#!/usr/bin/python
#-*- coding='utf-8' -*-
# from time import sleep
#
# dr = webdriver.Chrome()
# dr.get('http://www.baidu.com')
# dr.find_element_by_id('kw').send_keys('京东商城')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# sleep(2)
# ss = dr.window_handles
# dr.switch_to.window(ss[1])
# print(dr.title)
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('书籍')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/a[2]').click()
# from selenium  import webdriver
import unittest
from ddt import ddt,data,unpack

@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')
    @data([1,2,3])
    def test_1(self,value):
        print(value)
if __name__ == '__main__':
    unittest.main()