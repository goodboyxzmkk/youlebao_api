import requests
import json
import base64
import operator
from common import config_manage

http_config = config_manage.get_yaml_config()
global_cooikes = None


class Base_Request(object):
    '''配置要测试接口服务器的 ip、端口、域名等信息，封装 http 请求方法，http 头设置'''

    def __init__(self, session, data):
        self.__session = session  # 保持会话s
        self.data = json.loads(json.dumps(data))  # 先转json编码格式，再转json对象
        self.cookies = None
        self.url = data["url"]
        self.headers = eval(data["headers"])
        self.method = data["method"]
        try:
            self.params = eval(data["params"])
        except:
            self.params = None
        try:
            self.body = eval(data["body"])  # 字符串转为字典
        except:
            self.body = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, headers):
        self._header = headers

    def set_cookies(self, ck):
        global global_cooikes
        global_cooikes = ck

    def get_cookies(self):
        global global_cooikes
        return global_cooikes

    def send_get(self):
        '''封装 HTTP GET 请求方法，返回json报文'''
        # params = urllib.parse.urlencode(eval(params))  # 将参数转为 url 编码字符串
        url = 'http://' + http_config['HTTP']['host'] + ':' + str(http_config['HTTP']['port']) + self.url
        try:
            if self.headers != None:
                response = self.__session.get(url, params=self.params, cookies=global_cooikes, headers=self.headers,
                                              verify=False)
                return json.loads(response.text)
            else:
                response = self.__session.get(url, params=self.params, cookies=global_cooikes, verify=False)
                return json.loads(response.text)
        except Exception as e:
            print('GET请求异常：%s' % e)
            return {}

    def send_post(self):
        '''封装 HTTP POST 请求方法，返回json报文'''
        url = 'http://' + http_config['HTTP']['host'] + ':' + str(http_config['HTTP']['port']) + self.url
        print("请求url：{}".format(url))
        data = self.base64(self.body)
        if self.data["type"] == "data":
            testdata = data  # 请求参数在body,表单中（form data），Content-Type: application/x-www-form-urlencoded需要传字典格式
        else:
            testdata = json.dumps(data)  # Content-Type: application/json,参数需要转json编码
        try:
            print("请求头：{}".format(self.headers))
            print("请求参数：{}".format(testdata))
            response = self.__session.post(url, data=testdata, cookies=global_cooikes, headers=self.headers, verify=False)
            print("响应信息:{}".format(response.text))
            return response
        except Exception as e:
            print('POST请求异常：%s' % e)
            return {}

    def send_request(self):
        '''判断请求方法'''
        if self.method == 'post':
            print("请求方法：post")
            return self.send_post()
        else:
            print("请求方法：get")
            return self.send_get()

    def base64(self, body):
        '''登录接口，密码需要转码'''
        if 'DTOWebLogin' in self.url:
            tt = base64.b64encode(body["Password"].encode('utf-8'))
            body["Password"] = str(tt, 'utf-8')
            return body
        return body

    def assert_is_equal_dict(self, dict_one, dict_two):
        '''判断两个字典是否相等'''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one, dict_two)





if __name__ == '__main__':
    payload = {'UserName': 'admin', 'Password': 'admin'}
    payload2 = {'ClassName': '1级分类1', 'Code': '', 'SuperiorId': ''}
    ss = requests.session()
    request = Base_Request(ss, payload)
    # header = {
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    # }
    # request.set_header(header)
    response = request.send_request()
    print(response)
    response2 = request.send_request()
    print(response2)
