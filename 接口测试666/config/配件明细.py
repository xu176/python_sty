#!/usr/bin/python
#-*- coding='utf-8' -*-
import requests
class peijian(object):
    def  wzhi(self,x):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head={
            'Content-Type':'application/json',
            'x-dealer-code':'2100005',
            'x-position-code':'D_PO_1028',
            'x-resource-code':'pol4s_partOrder_orderPartDetail',
            'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code':'dhxc1u',
            'x-access-token':'0da5606a534fa727dfd7f502df38be65'
        }
        body='{"partOrderItemId":%s}'%(x)
        b=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=b)
        return res.json()
if __name__=='__main__':
    ss=peijian()
    s=ss.wzhi('jkl')
    print(s)