#!/usr/bin/python
#-*- coding:'utf-8' -*-
import xlrd
class suopei_shuju(object):
    def duqu_jichu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\XSW\PycharmProjects\接口测试666\data\123.xlsx')
        sheet=f.sheets()[0]
        num=sheet.nrows
        for i in range(num):
          if i==0:
              continue
          else:
            shuju.append(sheet.row_values(i))
        return shuju
if __name__=='__main__':
    s=suopei_shuju()
    ss=s.duqu_jichu()
    print(ss)