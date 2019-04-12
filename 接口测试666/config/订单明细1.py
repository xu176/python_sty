#!/usr/bin/python
#-*- coding='utf-8' -*-
import requests
class dzmx(object):
    def dzmx_c(self,x,y,z):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        head={
            'Content-Type':'application/json',
            'x-dealer-code':'2100005',
            'x-position-code':'D_PO_1028',
            'x-resource-code':'pol4s_partOrderSearch_partOrderDetailSearch',
            'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code':'dhxc1u',
            'x-access-token':'0da5606a534fa727dfd7f502df38be65'
        }
        b='{"pageNum":%s,"pgeSize":%s,"queryTerms":{"orderNo":"%s"}}'%(x,y,z)
        body=b.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()
if __name__=='__main__':
    ss=dzmx()
    s=ss.dzmx_c(1,10,'V2100880181219390')
    print(s)

