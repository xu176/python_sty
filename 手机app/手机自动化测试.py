#!/usr/bin/python
#-*- coding='utf-8' -*-
# from appium import webdriver
# from  time  import sleep
# desired_caps={'platformName':'Android',
#               'deviceName':'127.0.0.1:5554',
#               'appPackage':'com.netease.cloudmusic',
#               'appActivity':'.activity.LoadingActivity '
#
# }
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# sleep(15)
# driver.find_element_by_id('com.netease.cloudmusic:id/alp').click()
# sleep(8)
# driver.find_element_by_id('com.tencent.mobileqq:id/name').click()
# sleep(6)
# driver.find_element_by_id('com.tencent.mobileqq:id/account').send_keys(2397553559)
# sleep(1)
# driver.find_element_by_id('com.tencent.mobileqq:id/password').send_keys('ailaopo0629')
# driver.find_element_by_id('com.tencent.mobileqq:id/name').click()
# sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
# sleep(2)
# aa=driver.find_element_by_id("com.netease.cloudmusic:id/af4").text
# if aa=='小时候170626':
#     print('pass')
# else:
#   print('fail')
import unittest
from appium import webdriver
import time
class ceshi(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
        #                'platformVersion':'6.0',
                        'deviceName': '127.0.0.1:5554',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': '.activity.LoadingActivity'}
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(10)
    def test_1(self):
        self.driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()  # 点击手机号登录
        time.sleep(5)
        self.driver.find_element_by_id("com.netease.cloudmusic:id/ik").send_keys("15537831769")  # 输入手机号
        time.sleep(3)
        self.driver.find_element_by_id("com.netease.cloudmusic:id/ii").send_keys("gao19930903")  # 输入密码
        time.sleep(3)
        self.driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()  # 点击登录
        time.sleep(10)
        # 断言
        self.driver.find_element_by_id("com.netease.cloudmusic:id/qn").click()  # 点击抽屉菜单
        time.sleep(3)
        aa = self.driver.find_element_by_id("com.netease.cloudmusic:id/af4").text
        if aa == "亚的网易云没有名":
            print("pass")
        else:
            print("fail")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
      unittest.main()
