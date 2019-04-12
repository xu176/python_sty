#!/usr/bin/python
#-*- coding='utf-8' -*-
import xlrd
def dingdanmx_duqu():
    shuju=[]
    f=xlrd.open_workbook(r'C:\Users\XSW\PycharmProjects\接口测试666\data\订单明细.xlsx')
    sheet=f.sheets()[0]
    num=sheet.nrows
    for n in range(num):
        shuju.append(sheet.row_values(n))
    return shuju
if __name__=='__main__':
    print(dingdanmx_duqu())