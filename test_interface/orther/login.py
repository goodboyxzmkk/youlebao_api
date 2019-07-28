import requests

'''在登陆模块创建一个全局session，在其他接口操作时带入登陆时的session，保持session的一致性'''
s = requests.Session()  # 定义一个全局session


class testlogin():
    login_url = "http://api-xxxxxx/api/Account/Login"
    username = "xxxxx"
    password = "123456"

    def test_login(self):
        data = {
            "UserName": self.username,
            "Password": self.password
        }
        r = s.post(self.login_url, data)
        print(r.cookies)
        return s
