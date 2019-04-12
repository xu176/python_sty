#!/usr/bin/python
#-*- coding='utf-8' -*-
# import requests
# import re
# class tp(object):
#     def htp(self,a):
#         ur='http://www.budejie.com/{}'.format(a)
#         head = {
#                                               'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#                                            }
#         aa=requests.get(url=ur,headers=head)
#         ab=aa.content.decode(encoding='utf-8')
#         # print(ab)
#         return ab
#     def guolv(self,b):
#         bb=re.compile('<div class="j-r-c">(.*?)<div class="j-r-wrst gud-put  index-wrst  ">',re.S)
#         bc=bb.findall(b)
#         print(len(bc))
#         shuju=[]
#         for k in bc:
#             c=re.compile(' <div class="j-r-list-c-desc">(.*?)<div class="j-r-list-tool"',re.S)
#             cc=c.findall(k)
#             print(len(cc))
#             print(cc)
#             for n in cc:
#                 d=re.compile('data-original="(.*?)" title')
#                 dc=d.findall(n)
#                 shuju.append(dc[0])
#
#             print(shuju)
#             return shuju
#     def save(self,v):
#         x=1
#         for i in v:
#             vi=requests.get(i)
#             vv=vi.content
#             with open('E:\图片\{}.jpg'.format(x),'wb') as f:
#                 f.write(vv)
#                 x+=1
# op=tp()
# qq=op.htp(1)
# qw=op.guolv(qq)
# qwe=op.save(qw)
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',8888))
# while True:
#     conn,addr=s.recvfrom(1024)
#     print(conn.decode('utf-8'))
#     while True:
#         a=input('<<<')
#         if a!='exit':
#            s.sendto(a.encode('utf-8'),addr)
#         else:
#             break
# import time
# import threading
#
#
# def foo():
#   for m in range(3):
#     print(123)
#     time.sleep(2)
#
#
# def bar():
#   for n in range(3):
#     print(456)
#     time.sleep(2)
#
#
# t1 =threading.Thread(target=foo())
# t1.start()
# for n in range(1,10):
#     for m in range(1,n):
#         print('{}*{}={}'.format(n,m,n*m),end='\t')
# #     print()
# import requests
# import re
# class  pc(object):
#     def jx(self,a):
#         ur='https://www.qisuu.la/du/23/23858/{}.html'.format(a)
#         head = {
#                                                        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#                                                     }
#         ab=requests.get(url=ur,headers=head)
#         ba=ab.content.decode(encoding='utf-8')
#         print(ba)
#         return ba
#     # def gl(self,b):
#     #     bc=re.compile()
#
# pc().jx(1753538)
#接口，请求传参和结果对比
#http协议，requests
# import json
# import requests
# import unittest
# url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
# head={
#   'Content-Type':'application/json',
#   'x-dealer-code':'2100150',
#   'x-position-code':'D_PO_1028',
#   'x-resource-code':'BASIC_DATA',
#   'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
#   'x-user-code':'djy0mx',
#   'x-access-token':'0da5606a534fa727dfd7f502df38be65'
# }
# body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
# res=requests.post(url=url,headers=head,data=body)
# print(res.json)
# mes=json.loads(res.text)
# mes=res.json()
# assert  mes['data']['applicationType'][0]['name']=='多装'
# assert  mes['data']['applicationType'][0]['value']=='1'
import requests
import unittest
#面向对象
class suopei(unittest.TestCase):
    def test_1(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head={
           'Content-Type':'application/json',
           'x-dealer-code':'2100150',
           'x-position-code':'D_PO_1028',
           'x-resource-code':'BASIC_DATA',
           'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
           'x-user-code':'djy0mx',
           'x-access-token':'0da5606a534fa727dfd7f502df38be65'
         }
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        mes=res.json()
        self.assertEqual(mes['data']['applicationType'][0]['name'],'多装')
    def test_2(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head={
           'Content-Type':'application/json',
           'x-dealer-code':'2100150',
           'x-position-code':'D_PO_1028',
           'x-resource-code':'BASIC_DATA',
           'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
           'x-user-code':'djy0mx',
           'x-access-token':'0da5606a534fa727dfd7f502df38be65'
         }
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 你好,"curPage": 1}'.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        mes=res.json()
        self.assertNotEqual(mes['data']['applicationType'][0]['name'],'多装')
    def test_3(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head={
           'Content-Type':'application/json',
           'x-dealer-code':'2100150',
           'x-position-code':'D_PO_1028',
           'x-resource-code':'BASIC_DATA',
           'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
           'x-user-code':'djy0mx',
           'x-access-token':'0da5606a534fa727dfd7f502df38be65'
         }
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        mes=res.json()
        self.assertEqual(mes['data']['applicationType'][0]['value'],'1')
    def test_4(self):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head={
           'Content-Type':'application/json',
           'x-dealer-code':'2100150',
           'x-position-code':'D_PO_1028',
           'x-resource-code':'BASIC_DATA',
           'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
           'x-user-code':'djy0mx',
           'x-access-token':'0da5606a534fa727dfd7f502df38be65'
         }
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
        res=requests.get(url=url,headers=head,data=body)
        mes=res.json()
        self.assertEqual(mes['data']['applicationType'][0]['value'],'2')
if __name__=='__main__':
    unittest.main()