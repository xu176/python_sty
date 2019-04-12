#!/usr/bin/python
#-*- coding='utf-8' -*-
# from selenium import  webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.jd.com')
# sleep(2)
# w=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_element_by_tag_name('li')
# #控制鼠标来移动到元素的位置上
# ActionChains(dr).move_to_element('w').perform()#执行
# sleep(2)
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import  ActionChains
# from time import sleep
# from selenium.webdriver.support.ui as ui
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.jd.com')
# dr.find_element_by_xpath('//*[@id="J_user"]/div/div[2]/p[2]/a[1]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('jkl')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# sleep(2)
# start=dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
# #drag_and_drop(起始位置，结束位置)
# #drag_and_drop_by_offset()
# ActionChains(dr).drag_and_drop_by_offset(start,60,0).perform()
# sleep(10)
# dr.quit()
# dr.get('http://www.lwfree.cn/yurenjie/yuerenjie1.html')
# sleep(2)
# #切换到弹出框
# ww=dr.switch_to.alert
# #获取弹出框上面的内容
# print(ww.text)
# #点击确认
# ww.accept()
# #点击取消
# ww.dismiss()
# #输入
# ww.send.keys('内容')
# sleep(2)
# dr.get('https://www.jd.com')
# sleep(2)
# #处理进度条
# for i in range(1,10000,2000):
#   js="var q=document.documentElement.scrollTop={}".format(i)
# #执行JavaScript语句
#   dr.execute_script(js)
#   sleep(2)
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import  ActionChains
# import selenium.webdriver.support.ui as ui
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https://www.jd.com')
# #强制等待
# #sleep(2)
# #只能等待  设置一个最大等待时间
# #检测到某个元素出现，就不会继续等待
# #设置最大等待时间
# unit = ui.WebDriverWait(dr,10)
# #直到定位的元素出现，就不会等待了
# unit.until(lambda dr:dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a'))
# print('hello')
# w=dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[3]/a')
# #获取定位到某个元素某个属性的值
# a=w.get_attribute('href')
# from  selenium  import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('https://www.baidu.com')
# print(dr.get_cookies())
# dr.delete_all_cookies()
# dr.add_cookie({'name': 'H_PS_PSSID', 'value': '1450_21109_18560_28769_28721_28557_28584_28639_26350_28627_28606'})
# dr.add_cookie({'name': 'BAIDUID', 'value': '4EDAEF2124CA36486C21FB3762D5F87A:FG=1'})
#
# dr.get('https://www.baidu.com')
#
# sleep(3)
# dr.quit()
