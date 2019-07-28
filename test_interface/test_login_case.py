import json
import unittest
from ddt import ddt, data
from requests.cookies import RequestsCookieJar
import requests
from common.read_file import get_data_excel
from common.base_request import Base_Request
from test_interface.base_case import Base_Case
from common import config_manage

test_data = get_data_excel("test_api_data.xlsx", "login")


@ddt
class Test_Login_Case(Base_Case):

    @data(*test_data)
    def test_login_001(self, data):
        self.request = Base_Request(self.ss, data)
        self.result = self.request.send_request()
        ck = self.result.cookies  # 类型为RequestsCookieJar
        self.cookies = requests.utils.dict_from_cookiejar(ck)  # 转为字典

        assert str(self.result.status_code) == data['code']
        print("实际结果：{}".format(self.result.json()))
        print("预期结果：{}".format(eval(data['response'])))
        assert self.result.json() == eval(data['response'])
        self.set_cookies(data)

    def set_cookies(self, data):
        body = eval(data['body'])
        if body['UserName'] == 'admin' and body['Password'] == 'admin':
            self.request.set_cookies(self.result.cookies)
            config_manage.write_cookies(self.cookies)
            print("更新cookies:" + str(self.result.cookies))
            # cookies = RequestsCookieJar()
            # cookies.update(self.result.cookies)


if __name__ == '__main__':
    unittest.main()
