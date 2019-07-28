import urllib.request
import requests
import http.cookiejar
import urllib.parse
import json

import yaml

file = open("../configs/configs.yaml", 'r', encoding='UTF-8', errors='ignore')
http_config = yaml.load(file, Loader=yaml.FullLoader)  # 用load方法转字典


class Http_Config():
    '''配置要测试接口服务器的 ip、端口、域名等信息，封装 http 请求方法，http 头设置
    '''

    def __init__(self):
        self.host = http_config['HTTP']['host']
        self.port = http_config['HTTP']['port']
        self.headers = {}  # http 头
        self.session = requests.session()  # 保持会话s
        # install cookie
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    # 设置 http 头
    def set_header(self, headers):
        self.headers = headers

    def get_header(self, headers):
        return self.headers

    def send_get(self, url, params):
        '''封装 HTTP GET 请求方法'''
        # params = urllib.parse.urlencode(eval(params))  # 将参数转为 url 编码字符串
        url = 'http://' + self.host + ':' + str(self.port) + url
        try:
            response = self.session.get(url, params=params, headers=self.headers, verify=False)
            return json.loads(response.text)
        except Exception as e:
            print('GET请求异常：%s' % e)
            return {}

    # 封装 HTTP POST 请求方法
    def send_post(self, url, data):
        '''封装 HTTP POST 请求方法'''
        url = 'http://' + self.host + ':' + str(self.port) + url
        try:
            response = self.session.post(url, data=data, headers=self.headers, verify=False)
            return json.loads(response.text)
        except Exception as e:
            print('POST请求异常：%s' % e)
            return {}

    def main(self, url, method, data):
        if method == "POST":
            result = self.send_post(url, data)
        else:
            result = self.send_get(url, data)
        return result


if __name__ == '__main__':
    payload = {'UserName': 'admin', 'Password': 'YWRtaW4='}

    payload2 = {'ClassName': '1级分类1', 'Code': '', 'SuperiorId': ''}
    request = Http_Config()
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    request.set_header(header)
    response = request.send_post("/DTOWebLogin", data=payload)
    print(response)
    print(response["ResponseStatus"])
    response2 = request.send_post("/Goods/DTOAddGoodsClass", data=payload2)
    print(response2)
