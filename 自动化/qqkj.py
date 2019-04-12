#!/usr/bin/python
#-*- coding='utf-8' -*-
# from selenium import webdriver
# from time import sleep
# class kj(object):
#  def denglu(x,y):
#    dr=webdriver.Chrome()
#    dr.get('https://qzone.qq.com/')
#    dr.switch_to.frame("login_frame")
#    sleep(1)
#    dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#    sleep(1)
#    dr.find_element_by_xpath('//*[@id="u"]').send_keys('{}'.format(x))
#    sleep(1)
#    dr.find_element_by_xpath('//*[@id="p"]').send_keys('{}'.format(y))
#    sleep(1)
#    dr.find_element_by_xpath('//*[@id="login_button"]').click()
#    sleep(3)
#    d=dr.title
#    return d
# ss=kj()
# s=kj.denglu(1683425336,'ailaopo0629.')
# print(s)
# from selenium import webdriver
# from time import sleep
# import unittest
# from ddt import ddt, data, unpack
#
#
# def login(argument, u, p):
#     argument.find_element_by_id('switcher_plogin').click()
#     sleep(5.0)
#     argument.switch_to.default_content()
#     argument.switch_to.frame('login_frame')
#     argument.find_element_by_id("u").send_keys(u)
#     sleep(1.0)
#     argument.find_element_by_id('p').send_keys(p)
#     sleep(1.0)
#     argument.find_element_by_class_name('login_button').click()
#     sleep(1.0)
#     return argument.title
#
#
# @ddt  # 固定写法
# class T1(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Chrome()
#         cls.dr.get(url='https://qzone.qq.com/')
#         cls.dr.implicitly_wait(10.0)
#         cls.dr.switch_to.frame('login_frame')
#
#     # def test_1(self):
#     #     dr.implicitly_wait(10.0)
#     #     dr.switch_to_frame('login_frame')
#     #     dr.find_element_by_id('switcher_plogin').click()
#     #     sleep(5.0)
#     #     dr.switch_to.default_content()
#     #     dr.switch_to_frame('login_frame')
#     #     dr.find_element_by_id("u").send_keys('825069672')
#     #     sleep(1.0)
#     #     dr.find_element_by_id('p').send_keys('houec1019')
#     #     sleep(1.0)
#     #     dr.find_element_by_class_name('login_button').click()
#     #     sleep(1.0)
#
#     @data([1683425336,'ailaopo0629.'])
#     def test_2(self,value):
#         # print(value)
#         a = value[0].split(',')
#         print(a)
#         b = a[0]
#         c = a[1].strip()
#         print(c)
#         d = login(self.dr, b, c)
#         self.assertEqual(d,'勿忘初心的空间 [http://1683425336.qzone.qq.com]')
#
#     @classmethod
#     def tearDownClass(cls):
# #         cls.dr.quit()
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
# import xlrd
# import   unittest
# from selenium import webdriver
# from time import sleep
# def shuj():
#     shuju=[]
#     f=xlrd.open_workbook(r'C:\Users\XSW\PycharmProjects\自动化\测试数据.xlsx')
#     sheet=f.sheets()[0]
#     num=sheet.nrows
#     print(num)
#     for i in range(num):
#         print(sheet.row_values(i))
#         shuju.append(sheet.row_values(i))
#     return shuju
# def denglu(x,y):
#     dr=webdriver.Chrome()
#     dr.get('https://qzone.qq.com/')
#     dr.switch_to.frame("login_frame")
#     sleep(1)
#     dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#     sleep(1)
#     dr.find_element_by_xpath('//*[@id="u"]').send_keys('{}'.format(x))
#     sleep(1)
#     dr.find_element_by_xpath('//*[@id="p"]').send_keys('{}'.format(y))
#     sleep(1)
#     dr.find_element_by_xpath('//*[@id="login_button"]').click()
#     sleep(3)
#     d=dr.title
#     return d
# class JianShu(unittest.TestCase):
#     dr=webdriver.Chrome()
#     def setUp(self):
#         dr = webdriver.Chrome()
#         dr.get('https://qzone.qq.com/')
#         dr.switch_to.frame("login_frame")
#         dr.implicitly_wait(5.0)
#     def test_1(self):
#         hh=denglu(int(shuj()[0][0]),shuj()[0][1])
#         self.assertEqual(hh,'勿忘初心的空间 [http://1683425336.qzone.qq.com]')
#     def tearDown(self):
#         self.dr.quit()
#
# if __name__ == '__main__':
#     unittest.main()
from selenium import  webdriver


