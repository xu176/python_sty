#!/usr/bin/python
#-*- coding='utf-8' -*-
import  xlrd
def duqu():
    sj=[]
    f=xlrd.open_workbook(r'C:\Users\XSW\PycharmProjects\手机app\手机测试框架\data\账号.xlsx')
    sheet=f.sheets()[0]
    num=sheet.nrows
    for i in range(num):
        if i==0:
            continue
        else:
         sj.append(sheet.row_values(i))
    return sj

