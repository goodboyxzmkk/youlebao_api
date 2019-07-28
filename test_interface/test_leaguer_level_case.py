import json
import unittest
from ddt import ddt, data
# from requests.cookies import RequestsCookieJar
from common.read_file import get_data_excel
from common.base_request import Base_Request
from test_interface.base_case import Base_Case
from common import config_manage

test_data = get_data_excel("test_api_data.xlsx", "leaguerLevel")


@ddt
class Test_Leaguer_Level_Case(Base_Case):

    @data(*test_data)
    def test_leaguer_level_001(self, data):
        self.request = Base_Request(self.ss, data)
        self.request.set_cookies(config_manage.read_cookies())
        self.result = self.request.send_request()
        assert str(self.result.status_code) == data['code']
        assert json.loads(self.result.text) == eval(data['response'])


if __name__ == '__main__':
    unittest.main()
