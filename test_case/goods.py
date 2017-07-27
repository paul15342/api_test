"""common返回的参数是code,和status_code"""
import requests
import json
import unittest
from data.data import *
from common.common import *


class Api(unittest.TestCase):
    def setUp(self):
        self.code = 0
        self.statusCode = 200
        self.base_url = "http://192.168.10.11:82/api/shop/goodslist"


    def test_get_goods(self):
        """获取兑换奖品数据"""
        param = eval(get_data(1,3))              #第一条数据, 预期结果通过
        res = method(self.base_url,param)
        self.assertEqual(res[0], self.code)
        self.assertEqual(res[1],self.statusCode)

    def test_get_goods_empty01(self):
        """获取兑换奖品数据,page值为空"""
        param = eval(get_data(2, 3))
        res = method(self.base_url, param)
        self.assertEqual(res[0], self.code)
        self.assertEqual(res[1], self.statusCode)

    def test_get_goods_empty02(self):
        """获取兑换奖品数据,size值为空"""
        param = eval(get_data(3, 3))
        res = method(self.base_url, param)
        self.assertEqual(res[0], self.code)
        self.assertEqual(res[1], self.statusCode)

    def test_get_goods_empty03(self):
        """获取兑换奖品数据,page,size值都不传"""
        param = eval(get_data(4, 3))
        res = method(self.base_url, param)
        self.assertEqual(res[0], self.code)
        self.assertEqual(res[1], self.statusCode)

    def test_get_goods_empty04(self):
        """获取兑换奖品数据,不传page"""
        param = eval(get_data(5, 3))
        res = method(self.base_url, param)
        self.assertEqual(res[0], self.code)
        self.assertEqual(res[1], self.statusCode)

    def test_get_goods_empty05(self):
        """获取兑换奖品数据,不传page"""
        param = eval(get_data(6, 3))
        res = method(self.base_url, param)
        self.assertEqual(res[0], self.code)
        self.assertEqual(res[1], self.statusCode)

if __name__=="__main__":
    unittest.main()
