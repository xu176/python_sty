#!/usr/bin/python
#-*- coding='utf-8' -*-

# sleep(2)
# #前进
# dr.forward()# from selenium import  webdriver
# # from time import sleep
# # #定义使用浏览器
# # dr=webdriver.Chrome()
# # #打开网址
# # # dr.get('https://www.baidu.com')
# # # #获取网址的标题
# # # print(dr.title)
# # # #获取打开网页的网址
# # # print(dr.current_url)
# # # #关闭浏览器断开连接
# # # dr.quit()
# # # #关闭浏览器不断开连接
# # # dr.close()
# # dr.get('https://www.baidu.com')
# # # sleep(2)
# # dr.get('https://www.jd.com')
# # sleep(2)
# # #回退
# # dr.back()
# sleep(2)
#设置浏览器窗口的大小
# dr.set_window_size(300,100)
# sleep(2)
# #设置浏览器的位置
# dr.set_window_position(600,100)
#设置浏览器全屏
# dr.maximize_window()
# sleep(2)
# #设置浏览器最小化
# dr.minimize_window()
# sleep(2)
# dr.quit()
# from selenium import webdriver
# import time
#
# dr = webdriver.Chrome()
#
# url = 'http://www.baidu.com'
# print("now access %s" %(url))
# dr.get(url)
# time.sleep(3)
#
# dr.quit()
from selenium import  webdriver
from time import sleep
dr=webdriver.Chrome()
# dr.get('https://www.baidu.com')
#定位 （核心）
#1 id来定位 通过id定位
# dr.find_element_by_id('kw').send_keys('凉山')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(2)
#2class_name定位  标签的class属性
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# sleep(3)
# dr.find_element_by_class_name('bg s_btn').click()
# sleep(3)
#3通过name定位 标签页的name属性定位
# dr.find_element_by_name('wd').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(3)
# dr.quit()
#4text定位  通过标签的文本定义
#5partial_link_text定位  标签的模糊文本定位
# dr.find_element_by_link_text('视频').click()
# dr.find_element_by_partial_link_text('地').click()
#6tag_name 定位 通过标签的名称来定位 最不唯一的一个定位，通常用来定位一组数据
# dr.find_elements_by_tag_name('input')
#8#css_selector定位，通过css来定位
# dr.find_element_by_css_selector('#kw')
#7xpath定位（路径定位） xpath路径标记语言  xml可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').click()
#id > css >xpath >name >classname ....
#自动登录qq空间
# dr.get('http://i.qq.com/')
# # sleep(1)
# # dr.switch_to_frame('login_frame')
# # dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# # sleep(1)
# # dr.find_element_by_id('u').send_keys(2397553559)
# # sleep(1)
# # dr.find_element_by_id('p').send_keys('ailaopo0629')
# # sleep(1)
# # dr.find_element_by_xpath('//*[@id="login_button"]').click()
# # sleep(5)
# # dr.quit()
# dr.get('https://mail.qq.com/')
# sleep(2)
#定位一组数据对象
# dr.get('https://www.ctrip.com/?sid=155947&allianceid=4897&ouid=cuoP&gclid=COuBteuLtuECFekAXAodkTQPbA&gclsrc=ds')
# sleep(2)
# for i in wd:
#     if i.text=='hao123':
#         continue
#     else:
#        dr.find_element_by_link_text(i.text)
#        sleep(2)
#        dr.back()
#层级定位，遇到复杂的元素定位
# wd=dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]')
# wd.click()
# qwe=wd.find_elements_by_tag_name('option')
# print(len(qwe))
# for i in  qwe:
#     i.click()
#     sleep(2)
# dr.quit()
#模拟动作
#1，send_keys()输入
#2，click()点击
# 3，text 获取定位到的元素的文本
# 4，clear()清空定位到的元素上面的数据
# dr.get('http://i.qq.com')
# sleep(2)
# dr.switch_to_frame('login_frame')
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys(1683425336)
# sleep(1)
# dr.find_element_by_id('p').send_keys('ailaopo0629.')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(1)
# dr.maximize_window()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="tab_menu_care"]/div[3]/span').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="tab_menu_me"]/div[3]/span').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="tab_menu_mv"]/div[3]/span').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="tab_menu_sdc"]/div[2]/span').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="tab_menu_sdc"]/div[2]/span').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="tab_menu_app"]/div[3]/span').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="tab_menu_fav"]/div[2]/span').click()
# sleep(2)
# dr.quit()
# dr.get('http://qzno. qq.com')
# #处理框架 iframe(窗口)
# #dr.switch_to.frame() 框架的id或者name,xpath,先定位
# #切换到某一个框架
# dr.switch_to.frame("login_frame")
# #回到最开始的页面中
# dr.switch_to.default_content()
# #回到父框架的页面中
# dr.switch_to.parent_frame()
#处理浏览器窗口的问题
#获取当前窗口的字符串（句柄）
# r.get('https://www.douban.com/')
# print(dr.current_window_handle)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# # 获取所窗口的句柄
# qq = dr.window_handles
# print(qq)
# # 切换句柄
# dr.switch_to.window(qq[-1])
# print(dr.title)
# dr.get('https://qzone.qq.com/')
# dr.switch_to.frame("login_frame")
# sleep(1)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys(1683425336)
# sleep(1)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('ailaopo0629.')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
# dr.find_element_by_xpath('//*[@id="tab_menu_me"]/div[3]/span').click()
# # dr.switch_to.frame("feed_me")
# sleep(2)
# dr.find_element_by_xpath('//*[@id="fct_1332926001_403_2_1553484679_1_1"]/div[1]/div[4]/div[1]/a').click()
# qq = dr.window_handles
# print(qq)
# dr.switch_to.window(qq[1])
# for  i in range(5):
#   dr.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys('我爱你')
#   dr.find_element_by_xpath('//*[@id="pageContent"]/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/a/span').click()
# dr.quit()

