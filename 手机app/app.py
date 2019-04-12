#!/usr/bin/python
#-*- coding='utf-8' -*-
from appium import webdriver
from time import sleep

desired_caps = {'platformName': 'Android',
                'platformVersion':'8.1.0',
                'deviceName': 'f2968ac',
                'appPackage': 'com.qk.butterfly',
                'appActivity': '.main.LauncherActivity',
                "noReset": 'True'}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(10)
driver.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
sleep(5)
driver.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(17629636773)
sleep(2)
driver.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('ailaopo0629')
sleep(2)
driver.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(10)
driver.quit()