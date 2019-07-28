# coding:utf-8
import unittest, time
import requests
import urllib3, warnings


class Base_Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ss = requests.session()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        urllib3.disable_warnings()  # 去除警告
        warnings.simplefilter("ignore", ResourceWarning)
        self.start = time.perf_counter()
        print("============【{}测试用例开始】====================".format(self.__class__.__name__))

    def tearDown(self) -> None:
        self.end = time.perf_counter()
        print('【用例运行时长】: {}秒'.format(self.end - self.start))
        print("====================【{}测试用例结束】====================".format(self.__class__.__name__))

