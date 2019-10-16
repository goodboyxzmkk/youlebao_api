'''封装钉钉群发消息'''
import base64

import requests, json


def send_ding(message):
    url = "https://oapi.dingtalk.com/robot/send?access_token=91a1f571187a08969a787ba29443c709c42ab62e10e4d30e5793d9c4387aeec8"
    String_textMsg = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "at": {
            "atMobiles": [
                "18620101998"  # 如果需要@某人，这里写他的手机号 与at 所有人不可同时用
            ],
            # "isAtAll": 1  # 如果需要@所有人，值为1
        }
    }
    headers = {
        'Content-Type': 'application/json ;charset=utf-8'
    }
    f = requests.post(url, data=json.dumps(String_textMsg), headers=headers)
    if f.status_code == 200:
        return True
    else:
        return False


def send_ding_url(message, file_url):
    '''
    钉钉机器人群发送图片
    :param message: 显示标题
    :param file_url: 显示图片地址
    :return:
    '''
    url = "https://oapi.dingtalk.com/robot/send?access_token=91a1f571187a08969a787ba29443c709c42ab62e10e4d30e5793d9c4387aeec8"

    with open(file_url, 'rb') as f:  # 二进制方式打开图文件
        base64_data = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        bs64 = base64_data.decode()
    my_data = {
        "msgtype": "markdown",
        "markdown": {
            "title": message,
            "text": "# 测试-{} ![](data:image/png;base64,{})".format(message, bs64)
        },
        "at": {
            "atMobiles": [
                "18620101998"  # 如果需要@某人，这里写他的手机号
            ],
            "isAtAll": 1  # 如果需要@所有人，这些写1
        }
    }
    headers = {
        'Content-Type': 'application/json ;charset=utf-8'
    }

    f = requests.post(url, data=json.dumps(my_data).encode("utf-8"), headers=headers)
    if f.status_code == 200:
        return True
    else:
        return False

if __name__ == '__main__':
    send_ding("s")
