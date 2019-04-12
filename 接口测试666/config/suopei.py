#!/usr/bin/python
#-*- coding:utf-8 -*-
import requests
class suopei(object):
    def jcsj(self,x,y):
        url = 'https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
        head = {
            'Content-Type': 'application/json',
            'x-dealer-code': '2100150',
            'x-position-code': 'D_PO_1028',
            'x-resource-code': 'BASIC_DATA',
            'x-track-code': '4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code': 'djy0mx',
            'x-access-token': '0da5606a534fa727dfd7f502df38be65'
        }
        body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": %s,"curPage": %s}'%(x,y)
        b=body.encode('utf-8')
        res = requests.post(url=url, headers=head, data=b)
        return  res.json()
if __name__=='__main__':
    ss=suopei()
    c=ss.jcsj(10,1)
    print(c)

