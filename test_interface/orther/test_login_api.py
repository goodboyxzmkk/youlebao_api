from study.login import testlogin
import unittest

'''这里导入之前的登陆模块，调用登陆模块的session，然后去执行其他接口'''
s = testlogin().test_login()


class testtransfer(unittest.TestCase):
    def setUp(self):
        self.transfer_url = "http://xxxxxxx/Transfer/DoTransferToGame"

    def test_transfer(self):
        url = self.transfer_url
        data = {"Amount": "123456",
                "GamePlatform": "xxxx"
                }
        r = s.send_post(url, data)

        print(r.text)


if __name__ == "__main__":
    unittest.main()
