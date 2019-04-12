#!/usr/bin/python
#-*- coding='utf-8' -*-
from selenium import webdriver
from time import sleep
class kj(object):
  def denglu(self,x,y):
     dr=webdriver.Chrome()
     dr.get('https://qzone.qq.com/')
     dr.switch_to.frame("login_frame")
     sleep(1)
     dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
     sleep(1)
     dr.find_element_by_xpath('//*[@id="u"]').send_keys('{}'.format(x))
     sleep(1)
     dr.find_element_by_xpath('//*[@id="p"]').send_keys('{}'.format(y))
     sleep(1)
     dr.find_element_by_xpath('//*[@id="login_button"]').click()
     sleep(3)
     d=dr.title
     return d
ss=kj()
s=ss.denglu(1683425336,'ailaopo0629.')
print(s)