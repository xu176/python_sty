import unittest
import requests
from 接口测试666.config import  suopei
from 接口测试666.data import  suopeishuju
class suopie_case(unittest.TestCase):
    shuju=suopeishuju.suopei_shuju()
    shuju123=shuju.duqu_jichu()
    def test_1(self):
        suo=suopei.suopei()
        asd=suo.jcsj(int(self.shuju123[0][0]),int(self.shuju123[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'],'多装')
    def test_2(self):
        suo = suopei.suopei()
        asd = suo.jcsj((self.shuju123[1][0]), int(self.shuju123[1][1]))
        self.assertEqual('get error',asd['message'])
    def test_3(self):
        suo = suopei.suopei()
        asd = suo.jcsj(int(self.shuju123[2][0]), (self.shuju123[2][1]))
        self.assertEqual('get error',asd['message'])
if __name__=='__main__':
  unittest.main()

