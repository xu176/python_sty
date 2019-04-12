from 接口测试666.report.baogao_baogao  import  baogao_
import sys
sys.path.append(r'‪C:\Users\join\Desktop\Python_dome')
def run(aa):
    baogao_(aa)
with open(r'C:\Users\XSW\PycharmProjects\接口测试666\driver\huigui.txt','r')  as f:
    a=f.readlines()
    print(a)
    if len(a)==1:
        run('*')
    else:
        run(a)
        print(a)