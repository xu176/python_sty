#!/usr/bin/python
#-*- coding='utf-8' -*-
import xlrd
class xuexiao_shuju(object):
    def  duqu_shuju(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\XSW\PycharmProjects\地址测试\data\456.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for n in range(num):
            shuju.append(sheet.row_values(n))
        return shuju
if __name__=='__main__':
    s=xuexiao_shuju()
    a=s.duqu_shuju()
    print(a)