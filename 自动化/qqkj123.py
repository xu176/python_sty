#!/usr/bin/python
#-*- coding='utf-8' -*-
# from selenium import webdriver
# from time import sleep
# import unittest
# from ddt import ddt, data, unpack
# import xlrd
# def  denglu(dr,x,y):
#     dr.find_element_by_id('switcher_plogin').click()
#     sleep(5.0)
#     dr.tswitch_to.default_content()
#     dr.switch_to.frame('login_frame')
#     dr.find_element_by_id("u").send_keys(x)
#     sleep(1.0)
#     dr.find_element_by_id('p').send_keys(y)
#     sleep(1.0)
#     dr.find_element_by_class_name('login_button').click()
#     sleep(1.0)
#     return dr.title
# def shuj():
#     shuju=[]
#     f=xlrd.open_workbook('测试数据.xlsx')
#     sheet=f.sheets()[0]
#     num=sheet.nrows
#     print(num)
#     for i in range(num):
#         shuju.append(sheet.row_values(i))
#     return shuju
# @ddt
# class yl(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.de = webdriver.Chrome()
#         cls.de.get(url='https://qzone.qq.com/')
#         cls.de.implicitly_wait(10.0)
#         cls.de.switch_to.frame('login_frame')
#     @data(shuj()[0],shuj()[1])
#     def test_1(self,value):
#         print(value)
#         a = value[0]
#         print(a)
#         b = a[0]
#         c = a[1].strip()
#         print(c)
#         d=denglu(self.dr,int(b),c)
#         self.assertEqual(d,'勿忘初心的空间 [http://1683425336.qzone.qq.com]')
#     @classmethod
#     def tearDownClass(cls):
#         cls.de.quit()
# if __name__=='__main__':
#     unittest.main()
from selenium import webdriver
from time import  sleep
dr=webdriver.Chrome()
dr.get('https://qzone.qq.com/')
dr.switch_to.frame("login_frame")
sleep(1)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(1)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('1683425336')
sleep(1)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('ailaopo0629.')
sleep(1)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="tab_menu_me"]/div[3]/span').click()
sleep(5)
dr.find_element_by_xpath('//*[@id="fct_1332926001_403_2_1553484679_1_1"]/div[1]/div[4]/div[1]/a').click()
sleep(5)
qq=dr.window_handles
dr.switch_to.window(qq[-1])
print(dr.title)
dr.find_element_by_xpath('//*[@id="friendship_promote_layer"]/table/tbody/tr[1]/td[2]/a').click()
sleep(3)
# dr.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[3]/div/div[1]/h3/a').click()
# sleep(3)
# # dr.switch_to.frame('veditor1_Iframe')
# sleep(3)
dr.find_element_by_xpath('//*[@id="$1_content_content"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys('你好')
dr.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/a/span').click()
# sleep(5)





