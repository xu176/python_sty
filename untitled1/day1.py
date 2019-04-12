#!/usr/bin/python
#-*- coding:utf-8 -*-
#对数据库的操作
#import pymysql
#来连接数据库
#需要给数据库设置允许外部主机连接的权限
# conn=pymysql.connect(host='192.168.0.222',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
#创建游标（控制器）
# abc=conn.cursor()
#执行sql语句
# abc.execute('create database python_test;')
# abc.execute('use python_test;')
# abc.execute('create table biao1(name char(20),age int,sex char(10));')
# abc.execute('insert into biao1 values("xiaogang",20,"nan"),("xiaohong","21","nv");')
#对数据库的数据进行更改的时候
#是有链接数据库的变量名来提交
# conn.commit()
# abc.execute('select * from biao1;')
#abc.execute('show databases;')
#abc.execute('use sys;')
# abc.execute('show tables;')
#任何结果都需要容器接受
# print(abc.fetchall())  #接受上一个sql语句的结果
# print(abc.fetchmany(20)) #接受上一个sql语句的结果，默认只接受第一行，在括号里面写入数字几就接受多少行
# print(abc.fetchone())#接受上一个sql语句的结果每次只接受一行
#断开数据库
# conn.close()
# import pymysql
# conn=pymysql.connect(host='192.168.0.222',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# ab=conn.cursor()
# while True:
#     aa=input('???')
#     if aa!='exit':
#         ab.execute(aa)
#         print(ab.fetchall())
#     elif  'insert' in aa:
#         for k in range(10):
#             ab.execute(aa)
#             conn.commit()
#     else:
#         break
#     conn.close()
# import json
# a={'name':123}
# json_data=json.dumps(a)
# print(json_data)
# abc=json.loads(json_data)
# print(abc['name'])
#动态爬虫
# abc={
# #     'name':'小刚',
# #     'age':20,
# #     'sex':'男'
# #
# # }
# # print(abc['sex'])

# import json
# import requests
# import re
# class zhilian(object):
#     def  qq(self,aa):
#         ur='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=1&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试&kt=3&_v=0.57091182&x-zp-page-request-id=04a6ce3303d34a688a744624b9f685e4-1550652347694-399181'.format(aa)
#         head = {
#                                                       'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#                                                     }
#         bb=requests.get(url=ur,headers=head)
#         cc=bb.content.decode(encoding='utf-8')
#         return cc
#     def  zy(self,uu):
#         u=re.compile('"display":(.*?)"items":',re.S)
#         uuu=u.findall(uu)
#         print(uuu)
#         w=re.compile(' "welfare": (.*?),"salary":',re.S)
#         ww=w.findall(uu)
#         print(ww)
#         s=re.compile('"name":(.*?)"type"',re.S)
#         ss=s.findall(uu)
#         print(ss)
#         a=[]
#         for b in range(3):
#             if b==0:
#                 a.append(uuu)
#             elif b==1:
#                 a.append(ww)
#             else:
#                 a.append(ss)
#         print(a)
#         return a
    # def save(self,cc):
    #     with open('a.txt','w',encoding='utf-8') as f:
    #         for n in range(3):
    #           f.write(cc[n])

# s=zhilian()
# for  m in  range(1,2):
#     h=s.qq(m)
#     hh=s.zy(h)
    # s.save(hh)


# import xlwt
# with open('p.txt','r',encoding='utf-8')  as f:
#     b=f.readlines()
#     print(b)
#     m=xlwt.Workbook(encoding='utf-8')
#     bb=m.add_sheet('信息1')
#     for i,j in enumerate(b):
#         print(j)
#         j=j.replace('\n','').split(',')
#         for n in range(len(j)):
#            bb.write(i,n,j[n])
# m.save('x.xls')
# import xlrd
# import pymysql
# con=pymysql.connect(host='192.168.0.222',
#                     port=3306,
#                     user='root',
#                     passwd='123456',
#                     charset='utf8')
# a=con.cursor()
# # a.execute('create database douban1;')
# a.execute('use douban1;')
# f=xlrd.open_workbook('douban.xls')
# ff=f.sheets()[0]
# for n in range(ff.nrows):
#     if n==0:
#         c=ff.row_values(n)
#         a.execute('create table douban2({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         c=ff.row_values(n)
#         a.execute('insert into douban2 values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
#         con.commit()
# a.execute('select * from douban2;')
# print(a.fetchall())
# con.close()
# import requests
# import re
# class douban(object):
#     def wangzhan(self,aa):
#         u='https://movie.douban.com/top250?start={}&filter='.format(aa)
#         head={
#             'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#         }
#         uu=requests.get(url=u,headers=head)
#         a=uu.content.decode(encoding='utf-8')
#         return(a)
#     def guolv(self,bb):
#         c=re.compile('<div class="item">(.*?)<li>',re.S)
#         cc=c.findall(bb)
#         shuju=[]
#         for x in  cc:
#             x=x.replace('\n','').strip()
#             shuju.append(x)
#         print(shuju)
#         dy=[]
#         for y in shuju:
#           d=re.compile('<span class="title">(.*?)</span>',re.S)
#           dd=d.findall(y)
#           dy.append(dd[0])
#         print(dy)
#         tp=[]
#         for vv in shuju:
#           e=re.compile('src="(.*?)"',re.S)
#           ee=e.findall(vv)
#           tp.append(ee[0])
#         print(tp)
#         return dy,tp
#     def save(self,nn,mm):
#         for i in  range(len(mm)):
#             res=requests.get(mm[i])
#             ht=res.content
#             with open('E:\setup1\\{}.jpg'.format(nn[i]),'wb') as f:
#                 f.write(ht)
#
# z=douban()
# oo=0
# for o in range(2):
#   zz=z.wangzhan(oo)
#   t,tt=z.guolv(zz)
#   z.save(t,tt)
#   oo=+25

# import os
# class shanchu():
#
#     def shan(self):
#         for i in os.listdir():
#                 if i.endswith('.lnk'):
#                     os.remove(i)
#                 else:
#                     continue
#
# siri=shanchu()
# siri.shan()
# a=[1,2,3,4,5,6]
# a=str(a)
# b=a.replace(',','')
# b=str(b)
# print(b[0])
# import requests
# import re
# class  doutu(object):
#     def wangzhan(self):
#         ur='https://www.doutula.com/article/detail/1279735'
#         head={
#             'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#         }
#         aa=requests.get(url=ur,headers=head)
#         b=aa.content.decode(encoding='utf-8')
#         c=re.compile('<div class="random_tips" style="margin-top: 10px;">(.*?)<div class="artile_des doutula_money">',re.S)
#         cc=c.findall(b)
#         print(cc)
#         return cc
#     def guolv(self,t):
#         shuju=[]
#         m=1
#         for n in t:
#           o=re.compile('<td>\n<a href="(.*?)">\n<img src=""',re.S)
#           oo=o.findall(n)
#           print(len(oo))
#         for m in range(len(oo)):
#           shuju.append(oo[m])
#         print(shuju)
#         return shuju
#     def gl(self,x):
#         sj=[]
#         mz=[]
#         for i in x:
#             print(i)
#             y=0
#             res=requests.get(i)
#             ht=res.content.decode(encoding='utf-8')
#             xx=re.compile('<td>\n<img src="(.*?)onerror="this.src=',re.S)
#             xxx=xx.findall(ht)
#             yy=re.compile('http:(.*?).jpg',re.S)
#             yyy=yy.findall(xxx[0])
#             sj.append(yyy[0])
#             h=re.compile('alt="(.*?)"',re.S)
#             hh=h.findall(xxx[0])
#             mz.append(hh[0])
#         return sj,mz
#     def save(self,z,l):
#         jj=0
#         for  j in z:
#             qq=('http:'+j+'.jpg')
#             print(qq)
#             res=requests.get(qq)
#             ht=res.content
#             with open('F:\start\新建文件夹\{}.jpg'.format(l[jj]),'wb')  as f:
#                 f.write(ht)
#                 jj+=1
#
# d=doutu()
# s=d.wangzhan()
# ss=d.guolv(s)
# k,kk=d.gl(ss)
# d.save(k,kk)
#udp 客户端
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送请求
# host=('127.0.0.1',8888)
# while True:
#   b=input('>>>')
#   if b!='exit':
#    sock.sendto(b.encode('utf-8'),host)
# #接收数据
#    msg=sock.recv(1024)
#    print(msg.decode('utf-8'))
#   else:
#       break
# sock.close()
# import socket
# b=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# b.connect(('127.0.0.1',8888))
# while True:
#     n=input('>>>')
#     b.send(n.encode('utf-8'))
#     bb=b.recv(1024)
#     print(bb.decode('utf-8'))
