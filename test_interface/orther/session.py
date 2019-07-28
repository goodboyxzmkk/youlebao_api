import requests
import urllib3
from urllib.parse import urlencode  # body数据转码

urllib3.disable_warnings()  # 去除警告
s = requests.session()  # 保持会话s

login_url = "http://localhost:9999/DTOWebLogin"
header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
body = {
    "UserName": "11",
    "Password": "MQ=="
}
r1 = s.post(url=login_url, headers=header, data=body, verify=False)  # verify=False 不校验SSL
# 登录后，session自动保存cookies
print(r1.cookies)
print(r1.text)

# 退出登录

url2 = "http://localhost:9999/Organization/DTOAddBizEmployee"

header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}
body2 = {
    "ID": "1205c781-fb4d-445c-bcb0-aa510115560e",
    "LoginName": "sy04",
    "Password": "1",
    "RealName": "收银4",
    "Phone": "",
    "CashAble": "true",
    "DeparmentID": '[{"roleid": "b8b8219a-3e14-4e2a-8451-807805940d2e"}]',
    "DefaultRoleId": "",
    "DataSelectGet": "0",
    "DateSelectTotle": "0",
    "Terminal": ""
}

data_gb2312 = urlencode(body2, encoding='gb2312')

r2 = s.post(url=url2, headers=header, data=data_gb2312, verify=False)
print(r2.text)
# r2.up
print(r2.cookies)
