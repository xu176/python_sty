#!/usr/bash/python
#-*- encoding='utf-8' -*-
# import time
# a='2400-11-7'
# # b=time.strptime(a,'%Y-%m-%d')
# # c=['一','二','三','四','五','六','日']
# # print(b)
# # if b[0]%100!=0:
# #   if b[0]%4!=0:
# #       print('不是闰年',b[-2],'星期{}'.format(c[b[-3]]))
# #   else:
# #       print('闰年',b[-2],'星期{}'.format(c[b[-3]]))
# # else:
# #   if b[0]%400==0:
# #       print('闰年',b[-2],'星期{}'.format(c[b[-3]]))
# #   else:
# #       print('不是闰年',b[-2],'星期{}'.format(c[b[-3]]))
# import pymysql
# con=pymysql.connect(host='192.168.0.222',
#                     port=3306,
#                     user='root',
#                     passwd='123456',
#                     charset='utf8')
# a=con.cursor()
# a.execute('use douban1;')
# a.execute('select * from douban2')
# b=a.fetchall()
# b=list(b)
# print(type(b))
# with open('s.txt','a',encoding='utf-8')  as f:
#  for n in range(len(b)):
#     print(b[n][0])
#     for m in range(len(b[n])):
#         c=b[n][m]
#         c=str(c)
#         print(type(c))
#         f.write(c)
#     f.write('\n')
# import paramiko
# ssh123=paramiko.SSHClient()
#第一次连接主机，known_hosts 存放的主机地址，跳过查找
#允许连接不在know_host文件中的主机
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#连接主机
# ssh123.connect(hostname='192.168.0.222',
#                port=22,
#                username='root',
#                password='123456')
# #执行所有linux命令
# a,b,c=ssh123.exec_command('vmstat')
# #第一个变量；表示输入的命令
# #第二个变量：命令执行的结果
# #第三个变量：命令的报错
# print(b.read().decode())
# ssh123.close()
# while True:
#     m=input('<<<')
#     if m=='exit':
#         break
#     else:
#         a,b,c=ssh123.exec_command(m)
#         print(b.read().decode())
#传输文件
#建立一个传输通道
# ssh123=paramiko.Transport('192.168.0.222',22)
#连接linux
# ssh123.connect(username='root',password='123456')
#创建一个传输文件的对象
# sftp = paramiko.SFTPClient.from_transport(ssh123)
#从linux到windows
#第一个参数表示要传输的文件
#第二个参数表示存放的本机位置
# sftp.get('install.log',r'.\abc.log')
#从windows到linux上
# sftp.put('day1.py',r'/home/day3.py')
# ssh123.close()
#socket 自带的
#socket：套接字，是实现最底层的一种通信方式
#采用cs架构
#通过tcp协议进行通信 socket
#
# import socket
# #server服务端
# #创建一个套接字,规定使用tcp协议,ip版本ipv4
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip,端口号
# s.bind(('127.0.0.1',8888))
# #监听服务是否开启，数字指的是最大等待数
# s.listen(3)
# while True:
#     #接受请求 ，第一个:连接信息，第二个变量；客户端的ip和端口号
#     coon,addr=s.accept()
#     #接收数据 1024表示一次性最大能接受1024字节的数据
#     reg=coon.recv(1024)
#     print(reg.decode('utf-8'))
#     #发送数据
#     msg=input('>>>')
#     coon.send(msg.encode('utf-8'))
# import xlrd
# f=xlrd.open_workbook('haha.xls')
# sh=f.sheets()[0]
# with open('b.text','w',encoding='utf-8')  as o:
#   for k in range(sh.nrows):
#     i=sh.row_values(k)
#     for g in range(len(i)):
#         o.write(str(i[g])+' ')
#     o.write('\n')
# import xlwt
# with open('g.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
#     print(a)
#     b=xlwt.Workbook(encoding='utf-8')
#     bb=b.add_sheet('xinxi')
#     s=-1
#     for n in a:
#         n=n.replace('\n','').split(' ')
#         s+=1
#         for m in range(len(n)):
#            bb.write(s,m,n[m])
#     b.save('how1.xls')
# for n in range(1,10):
#   for m in range(1,n+1):
#       print('{}*{}={}'.format(n,m,n*m),end='\t')
#   print()
# a='adsvnjaaakl'
# f=a.upper()
# print(f)
# print(a.capitalize())
# print(a.swapcase())
# print(a.count('a'))
# print(a.index('s'))
# import socket
# a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a.bind(('127.0.0.1',8888))
# a.listen(3)
# while True:
#     b,c=a.accept()
#     reg=b.recv(1024)
#     print(reg.decode('utf-8'))
#     while True:
#         m=input('<<<')
#         b.send(m.encode('utf-8'))
#         red=b.recv(1024)
#         print(red.decode('utf-8'))
# import re
# import requests
# class douluo(object):
#     def wz(self,x):
#         ur='https://www.81xzw.com/book/110171/{}.html'.format(x)
#         head = {
#                      'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
#                  }
#         a=requests.get(url=ur,headers=head)
#         b=a.content.decode('utf-8')
#         return b
#     def gv(self,ab):
#         c=re.compile('<div class="yd_text2" id="content">(.*?)<div class="pereview">',re.S)
#         cc=c.findall(ab)
#         return  cc
#     def save(self,dd):
#         with open('ff.txt','w',encoding='utf-8') as f:
#             for i in dd:
#                 i=str(i)
#                 n=i.strip().replace('br','').replace('<p class="anti-transform" style="margin:0">','').replace('http://www.81xzw.com/</p><>','').replace('<>','').split(' ')
#                 print(len(n))
#                 for m in range(len(n)):
#                     print(m)
#                     f.write(n[m]+'\n')
# ba=douluo()
# nn=ba.wz(31)
# mm=ba.gv(nn)
# ba.save(mm)
# import pymysql
# import xlwt
# a=pymysql.connect(port=3306,
#                   user='root',
#                   passwd='123',
#                   charset='utf8',
#                   host='192.168.0.222')
# b=a.cursor()
# b.execute('show databases')
# b.execute('use haha')
# b.execute('show tables')
# b.execute('select * from xs2')
# cc=b.fetchall()
# print(len(cc))
# f=xlwt.Workbook('utf-8')
# ff=f.add_sheet('xinxi')
# for n in range(len(cc)):
#     for m in range(len(cc[n])):
#         ff.write(n,m,cc[n][m])
# f.save('456.xls')
# import time
# print(time.localtime())
# bb=time.time()
# bb=int(bb)-86400
# print(time.localtime(bb))
# print(time.strftime('%Y-%m-%d',time.localtime(bb)))
# a='2019-5-21'
# print(time.strptime(a,'%Y-%m-%d'))
# for b in range(1,10):
#     for c in range(1,b+1):
#         print('{}*{}={}'.format(b,c,b*c),end='\t')
#     print('')
# x=int(input('='))
#  y=0
#  for m in range(2,x):
#      for n in range(2,m):
#          if m%n==0:
#              break
#      else:
#        y=y+m
#  print(y)
# x=0
# for n in range(1,2):
#     for m in range(1,5):
#         n=n*m
#         x=x+n
# print(x)
# a=input('随便输入三个数以逗号隔开')
# b=a.split(',')
# c=b.sort()
# x=int(b[0])
# y=int(b[1])
# z=int(b[2])
# if x+y>z and x+z>y  and z+y>x:
#      if x**2+y**2==z**2:
#          print('直角三角形')
#      elif x**2+y**2>z**2:
#          print('锐角三角形')
#      else:
#          print('钝角三角形')
# else:
#     print('不是三角形')
# a='jdfsahkf'
# # if  a.endswith('f'):
# #     print('123')
# # elif a.startswith('f'):
# #     print('456')
# a=input('随机输入数字以逗号隔开')
# a=a.split(',')
# b=[]
# for k in  a:
#   if k  not in b:
#     b.append(k)
# b.sort()
# print(b)
# a=input('=')
# for n in range(len(a)):
#     if  a[n]!=a[-(n+1)]:
#       print('不是回文字符串')
#       break
# else:
#   print('是回文字符串')
# a=input('请随机输入一组数以逗号隔开')
# a=a.split(',')
# for n in range(len(a)-1):
#     for m in range(len(a)-1):
#         if int(a[m])>int(a[m+1]):
#             a[m],a[m+1]=a[m+1],a[m]
# print(a)
# for n in range(100,1000):
#     x=n//100
#     y=n//10%10
#     z=n%10
#     if x**3+y**3+z**3==n:
#         print(n)
# import pymysql
# import xlrd
# a=pymysql.connect(host='192.168.0.222',
#                   user='root',
#                   port=3306,
#                   passwd='123',
#                   charset='utf8')
# b=a.cursor()
# b.execute('show databases;')
# b.execute('use word')
# b.execute('show tables')
# c=xlrd.open_workbook('how1.xls')
# cc=c.sheets()[0]
# print(c.sheet_names()[0])
# print(cc.ncols)
# for n in range(cc.nrows):
#     m=cc.row_values(n)
#     print(m)
#     if n==0:
#         b.execute('create table xy({} char(255),{} char(255),{} char(255),{} char(255),{} char(255))'.format(m[0],m[1],m[2],m[3],m[4]))
#     else:
#         b.execute('insert into xy values("{}","{}","{}","{}","{}")'.format(m[0],m[1],m[2],m[3],m[4]))
# a.commit()
# b.execute('select * from xy')
# a.close()
import paramiko
ssh1=paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh1.connect(hostname='192.168.0.222',
             port=22,
             username='root',
             password='123456')
a,b,c=ssh1.exec_command('netstat -anu')
print(b.read().decode())