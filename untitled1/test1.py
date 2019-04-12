# import socket
# client = socket.socket()#声明socket类型，同时生成socke连接t对象
# client.connect(('localhost',969))  #连接到localhost主机的6969端口上去
# while True:
#         msg = input(">>:").strip()
#         if len(msg) == 0:continue
#         client.send(msg.encode('utf-8'))#把编译成utf-8的数据发送出去
#         data = client.recv(512)#接收数据
#         print("从服务器接收到的数据为：",data.decode('utf-8'))
# client.close()
# for n in range(1,10):
#    for m in range(1,n+1):
#     print('{}*{}={}'.format(n,m,n*m),end='\t')
#    print('')
# a=input('请输入一组数以逗号隔开')
# b=a.split(',')
# print(len(b))
# # for n in range(len(b)-1):
# #   for m in range(len(b)-1):
# #    if b[m] > b[m+1]:
# #       b[m],b[m+1]=b[m+1],b[m]
# # print(b)
# for n in range(len(b)):
#    for m in range(len(b)):
#      if b[n] < b[m]:
#          b[n],b[m]=b[m],b[n]
# print(b)
# a=[14,34,98,45,19,25]
# a.append(23)
# a.sort()
# print(a)
# for n in range(100):
#         for m in range(100):
#                 for k in range(100):
#                        if n+m+k==100  and  2*n+m+0.5*k==100 :
#                                print(n,m,k)
# while True:
#    a=input('随机输入一组数,以逗号隔开')
#    if a=='exit':
#            break
#    b=a.split(',')
#    s=0
#    for k in b:
#         s=s+int(k)
#         print(s)
#         for n in b:
#            if int(n) < s//len(b):
#                 print(n)
# a=[]
# for n in range(1,1000):
#    for m in range(1,n):
#         if n%m==0:
#           a.append(m)
#    if sum(a)==n:
#         print(a)
#         print(n)
#    a=[]
# a=int(input('请随机输入一个数'))
# b=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
# f=[]
# while True:
#   c=a%16
#   a=a//16
#   f.append(str(b[c]))
#   if a==0:
#     break
# f.reverse()
# x=''.join(f)
# print(x)
# a=input('请随机输入一组数,以逗号隔开')
# a=a.split(',')
# for n in range(len(a)-1):
#     a[n],a[n+1]=a[n+1],a[n]
# print(a)
# a=input('请随机四个数,以逗号隔开')
# a=a.split(',')
# for x in a:
#     for y in a:
#         for k in a:
#             if x!=y and x!=k and y!=k :
#                 print(x,y,k)
# a=input('请随机输入一个数')
# f=0
# x=len(a)-1
# for b in range(len(a)):
#     for c in range(10):
#         if a[b]==str(c):
#             f=f+c*10**x
#             print(f)
#     print(x)
#     x=x-1
# print(f)
# a=input('请随机输入一组数,以逗号隔开')
# a=a.split(',')
# b=[]
# for c in a:
#   if c not in b:
#       b.append(c)
# b.sort()
# print(b)
# for n in a:
#     if int(n)==int(b[-1])  or int(n)==int(b[-2]):
#         print(n)
#  for a in range(100,1000):
 #     b=str(a)
 #     if int(b[0])**3+int(b[1])**3+int(b[2])**3==a:
 #         print(a)
 #阶乘之和
# a=int(input('请随机输入一个数'))
# m=1
# n=0
# for c in range(1,a+1):
#     m=m*c
#     n=n+m
# print(n)
# s=0
# # a=int(input('请随机输入一个数'))
# # for n in range(2,a):
# #     for m in  range(2,n):
# #         if n%m==0:
# #             break
# #     else:
# #         s=s+n
#  print(s)
# a=lambda m,n:m*n
# print(a(3,6))
# a=[ '{}*{}={}'.format(x,y,x*y) for x in range(1,10) for y in range(1,10)]
# print(a)
# a=[ n for n in range(2,100) for m in range(2,n) if n%m==0   ]
# print(a)
# import xs
# b=xs.cheng(5,6)
# print(b)
# from xs import *
# b=jia(10,60)
# print(b)
# c=cheng(10,6)
# print(c)
# import xlwt
# # a=xlwt.Workbook(encoding='utf-8')
# # b=a.add_sheet('xinxi')
# # b.write(0,0,'你好')
# # a.save('haha.xls')
# import xlrd
# f=xlrd.open_workbook('douban.xls')
# b=f.sheets()[0]
# print(b.nrows)
# print(b.ncols)
# c=b.row_values(2)
# print(c)
# d=b.col_values(1)
# print(d)
# import xlrd
# a=xlrd.open_workbook('haha.xls')
# b=a.sheets()[0]
# with open('g.txt','w',encoding='utf-8') as f:
#     for c in range(b.nrows):
#         d=b.row_values(c)
#         print(d)
#         for n in d:
#             n=str(n)
#             f.write(n+' ')
#         f.write('\n')
# import xlwt
# with open('p.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
#     b=xlwt.Workbook(encoding='utf-8')
#     c=b.add_sheet('123')
#     x=0
#     for n in a:
#         nn=n.replace('/n','').split(',')
#         for m in range(len(nn)):
#             c.write(x,m,nn[m])
#         x+=1
# b.save('banji.xls')
#追加
# from xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('banji.xls')
# k=copy(f)
# t=k.get_sheet(0)
# t.write(7,0,'我在那里?')
# k.save('banji.xls')
# import os
# # a=os.getcwd()
# # b=os.listdir(path='C:')
# # c=os.popen('ping 192.168.0.6')
# # print(c.read())
# with open('a.txt','r',encoding='utf-8') as  f:
#     for a  in f.readlines()[1:6]:
#         print(a)
# def a():
#     for n in range(1,10):
#         for m in range(1,n+1):
#             print('{}*{}={}'.format(n,m,n*m),end='\t')
#         print()
# a
# def a(b,c=0):
#     for n in range(2,b):
#         for m in range(2,n):
#             if n%m==0:
#                 break
#         else:
#             c=c+n
#     return  c
# print(a(100,0))
# import re
# a='try123to456expe@#.ct'
# b=re.compile('t(.*?)t',re.S)
# c=b.findall(a)
# print(c)
# class abc():
#     def cf(self,x,y):
#         m=x*y
#         return m
#     def chuf(self,x,y):
#         m=x//y
#         return m
#     def  jf(self,x,y):
#         m=x-y
#         return m
#     def jiaf(self,x,y):
#         m=x+y
#         return m
# q=abc()
# print(q.cf(6,5))
# print(q.chuf(10,2))
# print(q.jf(9,6))
# print(q.jiaf(9,9))
#
#
# class  kk(abc):
#     pass
# b=kk()
# print(b.cf(3,6))
# import re
# import requests
# class aa(object):
#     def fenxi(self,c):
#         ur='https://www.qiushibaike.com/text/page/{}/'.format(c)
#         bb=requests.get(url=ur)
#         cc=bb.content.decode(encoding='utf-8')
#         return cc
#     def guolv(self,d):
#         shuju=[]
#         dd=re.compile('<div id="content-left" class="col1">(.*?)<ul class="pagination">',re.S)
#         x=dd.findall(d)
#         print(x)
#         for n in x:
#             t=re.compile('<span>(.*?)</span>',re.S)
#             tt=t.findall(n)
#             print(tt)
#         return tt
#     def save(self,ko):
#         with open('h.txt','a',encoding='utf-8') as f:
#             for m in ko:
#                 print(m)
#                 m=m.replace('\n','').replace('<br/>','')
#                 f.write(m+'\n')
#
# op=aa()
# q=op.fenxi(2)
# qq=op.guolv(q)
# qs=op.save(qq)
# import requests
# import re
# class  tp(object):
#     def wz(self):
#         ur='https://www.doutula.com/article/detail/7626546'
#         head = {
#                          'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#                      }
#         a=requests.get(url=ur,headers=head)
#         aa=a.content.decode(encoding='utf-8')
#         return aa
#     def guolv(self,b):
#         bb=re.compile('<a href="https://www.doutula.com/photo/6865018">(.*?)<div class="artile_des doutula_money">',re.S)
#         ab=bb.findall(b)
#         print(ab)
#         for c in ab:
#             cc=re.compile('<img src="(.*?)" alt=',re.S)
#             cb=cc.findall(c)
#         cb.remove('')
#         print(cb)
#         return  cb
#     def save(self,qq):
#         x=1
#         for i in qq:
#             print(i)
#             k=requests.get(i)
#             kk=k.content
#             with open('E:\图片\{}.jpg'.format(x),'wb') as f:
#                 f.write(kk)
#                 x+=1
#
# tcp=tp()
# op=tcp.wz()
# vi=tcp.guolv(op)
# xm=tcp.save(vi)
# import pymysql
# con=pymysql.connect(host='192.168.0.222',
#                     user='root',
#                     port=3306,
#                     passwd='123456',
#                     charset='utf8')
# a=con.cursor()
# a.execute('show databases;')
# a.execute('use haha;')
# a.execute('show tables;')
# a.execute('select * from xs2')
# # a.execute('select * from douban2;')
# # a.execute('use sys;')
# # a.execute('show tables;')
# b=a.fetchall()
# print(b)
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in b:
#         print(i)
#         for j in i:
#             j=str(j)
#             print(j)
#             f.write(j+' ')
#         f.write('\n')
# a=[1,2,3,'ww','qwe',6,8,7]
# b=['qwer','df',1,2,3]
# a.extend(b)
# print(a)
# import socket
# a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a.connect(('127.0.0.1',8888))
# while True:
#   b=input('<<<')
#   a.send(b.encode('utf-8'))
#   bb=a.recv(1024)
#   print(bb.decode('utf-8'))
# import time
# a='1997-02-12'
# c=time.strptime(a,'%Y-%m-%d')
# print(c)
# b=time.mktime(c)
# print(b)
# f=int(b)-86400
# print(time.strftime('%Y-%m-%d',time.localtime(f)))
# print(time.localtime(f))
# import socket
# b=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b.connect(('127.0.0.1',8888))
# while True:
#     n=input('<<<')
#     b.send(n.encode('utf-8'))
#     rt=b.recv(1024)
#     print(rt.decode('utf-8'))
#     b.close()
# import pymysql
# import xlwt
# a=pymysql.connect(host='192.168.0.222',
#                   port=3306,
#                   user='root',
#                   passwd='123456',
#                   charset='utf8')
# b=a.cursor()
# b.execute('show databases;')
# b.execute('use haha;')
# b.execute('select * from xs2;')
# c=b.fetchall()
# print(c)
# print(len(c))
# x=xlwt.Workbook(encoding='utf-8')
# xs=x.add_sheet('学生信息表')
# for n in range(len(c)):
#     print(n)
#     for m in range(len(c[0])):
#         print(c[n][m])
#         xs.write(n,m,c[n][m])
# x.save('789.xls')
#b.close()
# import pymysql
# import xlrd
# a=pymysql.connect(host='192.168.0.222',
#                   port=3306,
#                   user='root',
#                   passwd='123456',
#                   charset='utf8')
# b=a.cursor()
# b.execute('show databases;')
# b.execute('use haha;')
# print(b.fetchall())
# b.commit()
# c=xlrd.open_workbook('haha.xls')
# d=c.sheets()[0]
# for n in range(d.nrows):
#     m=d.row_values(n)
#     # print(len(m))
#     # print(m[0],m[1],m[2],m[3],m[4])
#     if n==0:
#         b.execute('create table xus3({} char(255),{} char(255),{} char(255),{} char(255),{} char(255));'.format(m[0],m[1],m[2],m[3],m[4]))
#     else:
#         b.execute('insert into xus3 values("{}","{}","{}","{}","{}");'.format(m[0],m[1],m[2],m[3],m[4]))
# b.execute('select * from xus3')
# print(b.fetchall())
# b.close()
# for n in range(2,1000):
#     a=0
#     for m in range(1,n):
#         if n%m==0:
#             a=a+m
#             # print(a)
#     if a==n:
#       print(n)
# import  unittest
# import HTMLTestRunnertest
# class   qq(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(123,123)
#     def test_2(self):
#         self.assertEqual(456,456)
#     def test_3(self):
#         self.assertNotEqual(789,789)
#     def test_4(self):
#         self.assertEqual(147,258)
# if __name__=='__main__':
#     suit=unittest.TestSuite()
#     for i in range(1,5):
#       suit.addTest(qq('test_{}'.format(i)))
#     f=open('b.html','wb')
#     runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title='你好',tester='许颂伟',description='结果如下')
#     runner.run(suit)
#     f.close()
import requests
import unittest
class dizhi(unittest.TestCase):
    def test_1(self):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput=北京'
        head={
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml;q= 0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.77Safari/537.36',
            'Cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA',
        }
        res=requests.get(url,headers=head)
        mes=res.json()
        print(mes)
        self.assertEqual(mes['data'][0]['schoolName'],'北京中学')
        self.assertEqual(mes['data'][0]['schoolId2.0'],'4146')
if __name__ == '__main__':
    unittest.main()