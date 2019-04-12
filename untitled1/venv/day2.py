#!/usr/bin/python
#-*- encoding='utf-8' -*-
# from time import sleep
# import threading
# def  bb():
#     for n in range(3):
#        print('打篮球')
#        sleep(3)
# def aa():
#     for m in range(3):
#      print('买饮料')
#      sleep(2)
# threading.Thread(target=bb).start()#.start 开启线程
# threading.Thread(target=aa).start()
# import time
# print(time.localtime())
#按现代化格式显示时间
# abc=time.localtime()
# print(abc)
# print(time.strftime('%Y-%m-%d %H:%M:%S',abc))
# bb=time.time()
# print(bb)
# # abc=time.localtime(1000000000)
# # print(abc)
# #根据现代化时间，格式化成元组类型
# pp=time.strptime('1970-01-02','%Y-%m-%d')
# #按现代化格式显示时间，
# print(time.strftime('%Y-%m-%d',time.localtime(10000000)))
# #将元组类型的时间变成时间戳
# print(time.mktime(pp))
# import smtplib #连接邮件服务器
# import email.mime.multipart #处理邮件组成
# import email.mime.text #处理邮件正文
#
# server='smtp.163.com' #邮件服务器
# from_user='m17629636773@163.com'
# res='2397553559@qq.com'
# passwd='m123456'  #授权码 允许登陆客户端的密码
# #创建一个空的邮件
# message=email.mime.multipart.MIMEMultipart()
# message['From']=from_user #邮件的发件人
# message['To']=res  #邮件的接收者
# message['Subject'] = 'python zhuti'#邮件主题
# text="""
# 你好
# 很高兴认识你
# 我是来在月球的兔子
# 我的名字叫咕噜
# """
# txt=email.mime.text.MIMEText(text,'plain','utf-8')
# #将正文添加到邮件中
# message.attach(txt)
# #带附件
# #对附件进行读取和编码
# att2=email.mime.text.MIMEText(open(r'C:\Users\XSW\PycharmProjects\untitled1\a.txt','rb').read(),'base64','utf-8')
# #给附件添加头部信息
# att2["Content-Type"]='application/octet-stream'
# att2["Content-Type"]='attachment;filename="p.txt"'
# #将附件添加到邮件里
# message.attach(att2)
# #连接服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登陆服务器
# smtp123.login(from_user,passwd)
# #发送邮件
# smtp123.sendmail(from_user,res,message.as_string())
# #断开连接
# smtp123.close()
#client 客户端
# import socket
# # sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # sock.connect(('127.0.0.1',8888))
# # #发送请求
# # a=input('<<<')
# # sock.send(a.encode('utf-8'))
# # # 接收数据
# # bb=sock.recv(1024)
# # print(bb.decode('utf-8'))
# # sock.close()
# from tkinter import *
# from tkinter import  messagebox
# from PIL import Image
# from PIL import ImageTk
# def closewindow():
#     #设置提示信息
#     messagebox.showinfo(title='关不掉',message='不要拒绝好吗，都听你的')
#     #关闭窗口
#     window.destroy()
#     return
# def love():
#     #创建一个顶级的窗口，依赖于原始窗口存在
#     love=Toplevel(window)
#     love.title('太好了')
#     love.geometry('300x300')
#     label=Label(love,text='往后余生都是你',font=("微软雅黑",20))
#     label.pack()
#     love.mainloop()
# def nolove():
#     nolove=Toplevel(window)
#     nolove.title('我真的很爱你')
#     nolove.geometry('300x300')
#     label=Label(nolove,text='上交所有钱,你是领导',font=("微软雅黑",20))
#     label.pack()
#     nolove.mainloop()
# #创建一个窗口
# window=Tk()
# #命名窗口的标题
# window.title('hey 小姐姐')
# #设置窗口的大小
# window.geometry('700x700')
# #设置窗口的位置
# window.geometry('+800+0')
# #当用户关闭窗口时出发
# window.protocol('WM_DELETE_WINDOW',closewindow)
# #添加一个文本标签(控件)
# label = Label(window,text='你是人间的四月天',font=("微软雅黑",20))
# #显示标签 N  W E S
# label.grid(row=0,column=0,sticky=W)
# #添加图片控件
# photo=Image.open('123.png')
# phot=ImageTk.PhotoImage(photo)
# pho=Label(window,image=phot)
# #显示数据
# pho.grid(row=2,columnspan=2)
# #按钮
# botten=Button(window,text='同意',width=10,height=2,command=love)
# botten.grid(row=3,column=0,sticky=W)
# botten2=Button(window,text='不同意',width=10,height=2,command=nolove)
# botten2.grid(row=3,column=0,sticky=E)
# #显示窗口
# window.mainloop()
# import paramiko
# sh=paramiko.SSHClient()
# sh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# sh.connect(hostname='192.168.0.222',
#            port=22,
#            username='root',
#            password='123456'
#            )
# a,b,c=sh.exec_command('pstree')
# print(b.read().decode())
# import time
# ab=time.localtime()
# # print(ab)
# print(time.strftime('%Y-%m-%d %H:%M:%S',ab))
# print(time.strptime('2019-02-26','%Y-%m-%d'))
# print(time.time())
# import  pymysql
# a=pymysql.connect(host='192.168.0.222',
#                   user='root',
#                   port=3306,
#                   passwd='123456',
#                   charset='utf8')
# b=a.cursor()
# b.execute('create database haha;')
# b.execute('show databases;')
# b.execute('use haha;')
# with open('p.txt','r',encoding='utf-8') as f:
#   c=f.readlines()
#   m=1
#   for d in  c:
#     k=d.replace('\n','').split(',')
#     print(len(k))
#     print(k[0],k[1],k[2],k[3])
#     if m==1:
#         b.execute('create table xs2({} char(255),{} char(255),{} char(255),{} date);'.format(k[0],k[1],k[2],k[3]))
#         m+=1
#     else:
#         b.execute('insert into xs2 values("{}","{}","{}","{}");'.format(k[0],k[1],k[2],k[3]))
#         m+=2
# b.execute('select * from xs2;')
# print(b.fetchall())
# b.close()

