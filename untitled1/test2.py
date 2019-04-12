# import socket
# import os
# server = socket.socket()#声明socket类型，并且生成socket连接对象
# server.bind(('localhost',969))#把服务器绑定到localhost的6969端口上
# server.listen(5)#开始监听
# print("等待连接中……")
# while True:
#         conn,addr = server.accept()#接收连接
#         print("***连接成功***")
#         while True:
#                 data = conn.recv(512)#接收客户发来的数据
#                 print("接收到的命令为：",data)
#                 if not data:
#                         print("客户断开连接")
#                         break
#                 com = os.popen(data.decode()).read()#read()读取内存地址的内容
#                 print(data.decode())#输出结果为字符串dir
#                 print(os.popen(data.decode()))#输出结果为一个内存地址
#                 #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
#                 conn.sendall(com.encode('utf-8'))
# server.close()
# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',8888))
# s.listen(3)
# while True:
#   c,a=s.accept()
#   re=c.recv(1024)
#   print(re.decode('utf-8'))
# import time
# p=time.strptime('2019-03-02','%Y-%m-%d')
# print(time.mktime(p))
# import  socket
# a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a.bind(('127.0.0.1',8888))
# a.listen(3)
# while True:
#     con,son=a.accept()
#     print(con)
#     reg=con.recv(1024)
#     print(reg.decode('utf-8'))
#     while True:
#       m=input('<<<')
#       con.send(m.encode('utf-8'))
#       red=con.recv(1024)
#       print(red.decode('utf-8'))
# for i in range(1,10):
#     for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
# class kk(object):
#     x=3
#
# class qq(kk):
#     pass
# class  oo(kk):
#     pass
# print(kk.x,qq.x,oo.x)
# import socket
# a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# a.bind(('127.0.0.1',8888))
# a.listen(3)
# while True:
#     con,son=a.accept()
#     reg=con.recv(1024)
#     print(reg.decode('utf-8'))
#     while True:
#         m=input('<<<')
#         if m=='exit':
#             break
#         else:
#           con.send(m.encode('utf-8'))
#           ref=con.recv(1024)
#           print(ref.decode('utf-8'))
#
#     a.close()
# import requests
# import unittest
# import time
# import HTMLTestRunnertest
# #面向对象
# #所有的用例函数，必须test开头
# class  suopei(unittest.TestCase):
#     #初始化测试环境
#     # def setUp(self):
#     #     print(123)
#     # def tearDown(self):
#     #     print(456)
#     def test_1(self):
#         self.assertEqual(123,456)
#     def test_2(self):
#         self.assertEqual(456,456)
#     def test_3(self):
#         self.assertEqual(789,789)
#     def test_4(self):
#         self.assertNotEqual(123,456)
#
# if __name__=='__main__':
#     #创建一个测试套件
#     suit=unittest.TestSuite()
#     #添加测试用例
#     for i in range(1,5):
#       suit.addTest(suopei('test_{}'.format(i)))
#     now=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
#     #打开一个文件
#     f=open('abc.html','wb')
#     #定义测试报告的内容
#     runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title='索赔测试报告',tester='许颂伟',
#     description='结果如下')
#     runner.run(suit)
#     f.close()
# import unittest
# class demoTest(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(4+5,9)
#     def test2(self):
#         self.assertNotEqual(5*2,10)
#     def test3(self):
#         self.assertTrue(4+5==9,"The result is False")
#     def test4(self):
#         self.assertTrue(4+5==10,"The result is  fails")
#     def test5(self):
#         self.assertIn(3,[1,2,3])
#     def test6(self):
#         self.assertNotIn(3,range(5))
#
# if __name__=='__main__':
#     unittest.main()


