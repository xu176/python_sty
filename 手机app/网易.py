#!/usr/bin/python
#-*- coding='utf-8' -*-
from appium import webdriver
import time
import unittest
class ceshi(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
#                'platformVersion':'6.0',
                        'deviceName':'127.0.0.1:62001',
                        'appPackage':'com.netease.cloudmusic',
                        'appActivity':'.activity.LoadingActivity'
                       }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(15)
    def test_1(self):
       self.driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()#点击手机号登录
       time.sleep(5)
       self.driver.find_element_by_id("com.netease.cloudmusic:id/ik").send_keys("15537831769")#输入手机号
       time.sleep(3)
       self.driver.find_element_by_id("com.netease.cloudmusic:id/ii").send_keys("gao19930903")#输入密码
       time.sleep(3)
       self.driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()#点击登录
       time.sleep(10)
#断言
       self.driver.find_element_by_id("com.netease.cloudmusic:id/qn").click()  #点击抽屉菜单
       time.sleep(3)
       aa=self.driver.find_element_by_id("com.netease.cloudmusic:id/af4").text
       if aa=="亚的网易云没有名":
          print("pass")
       else:
          print("fail")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()
