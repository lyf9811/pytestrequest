import json
import re

import requests


class TestRequest:
    # 全局变量(类变量)，通过类名调用
    access_token = ""
    # csrf_token = ""

    # get请求：获取接口统一鉴权码token接口
    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }
        res = requests.request("get", url=url, params=data)
        print(res.json())
        TestRequest.access_token = res.json()['access_token']

    # post请求：编辑标签接口
    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestRequest.access_token
        data = {"tag": {"id": 134, "name": "广东人"}}
        # str_data = json.dumps(data)  #不用json传参，用data传参使用json.dumps()转换
        res = requests.request("post", url=url, json=data)
        print(res.json())

    # 文件上传
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + TestRequest.access_token
        data = {
            "media": open("/Users/yinfeng.liu/Desktop/111.png", "rb")
        }
        res = requests.request("post", url=url, files=data)
        print(res.json())

    # 访问首页接口
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = requests.request("get", url=url)
        print(res.text)
        # 正则提取
        obj = re.search('name ="csrf_token" value="(.*?)"', res.text)
        TestRequest.csrf_token = obj.group(1)
        print(TestRequest.csrf_token)

    # 登录接口
    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            " username ": "msxy",
            " password ": "msxy",
            "csrf_token": "TestRequest.csrf_token",
            " backurl ": "http://47.107.116.139/phpwind/",
            " invite ": ""
        }
        res = requests.request("post",url=url,data=data)
        print(res.json())


if __name__ == '__main__':
    TestRequest.test_get_token()
    TestRequest.test_edit_flag()
    TestRequest.test_file_upload()
    # TestRequest.test_start()
    # TestRequest.test_login()
