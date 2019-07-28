# coding:utf-8
import json
import unittest

import requests


class Base_Requests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ss = requests.Session()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def get(self, url, payload):
        headers = self.requestHeader()
        response = self.ss.get(url=url, headers=headers, params=payload)
        # print response.url
        return response

    # post请求
    def post_json(self, url, payload, query_string):
        headers = self.requestHeader()
        response = self.ss.request("POST", url, data=payload, headers=headers, params=query_string)
        return response

        # post请求

    def post_data(self, url, payload, query_string):
        headers = self.requestHeader()
        response = self.ss.request("POST", url, data=payload, headers=headers, params=query_string)
        return response

    # 设置请求的header
    def requestHeader(self, type):
        if type == 'data':
            headers = {
                'Content-Type': "multipart/form-data",
                'Cache-Control': "no-cache"
            }
        elif type == 'json':
            headers = {
                'Content-Type': "application/json",
                'Cache-Control': "no-cache"
            }
        else:
            headers = {
                'Content-Type': "x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
        return headers
