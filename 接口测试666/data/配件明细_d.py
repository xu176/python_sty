#!/usr/bin/python
#-*- coding='utf-8' -*-
import xlrd
class sj_1(object):
    def duqu(self):
        f=xlrd.open_workbook(r'C:\Users\XSW\PycharmProjects\接口测试666\data\配件明细.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        shuju=[]
        for i in range(num):
            shuju.append(sheet.row_values(i))
        return shuju
if __name__=='__main__':
    ss=sj_1()
    s=ss.duqu()