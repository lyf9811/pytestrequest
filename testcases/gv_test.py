import re
import requests


# class Testrequest:

# 拼图的newcoming接口
def test_gv_newcoming():
        url = "https://puzzle.dev.smartcoder.top/v1/jgspz/home_page/u1/get"
        data = {
            "data": '{"app_package_name":"art.color.planet.jigsaw.puzzle.online","timezone":8,"country":"CN","platform":"ios","device_model":"phone","new_item_version_code":"1686219710","offset":0,"segment_token":123,"muid":"cda2f41a-6ba0-4006-8d02-50da84151379"}',
            "skv": "1",
            "sig": "8cc848329113965c0613d58c6462725fd5896c8acc6ff3d01df9197a3124b085"
        }
        # res = requests.get(url,params=data,headers=headers)
        res = requests.request("get", url=url, params=data)
        print(res.json())


    # gv的统一接口
def test_gv():
        url = "https://commonapi.dev.smartcoder.top/api/v3/behavior/get_next"
        data = {
            "behaviors": '{"filename": "6464eb814abbd284b95104149b4d050d","prev_hash": "f71f9d1d448084e2da92f087a7448bba","hash": "6464eb814abbd284b95104149b4d050d","proto_cls": "Aiolos"}',
            "force": "true",
            "muid": "cda2f41a-6ba0-4006-8d02-50da84151379",
            # "behaviors": '[{"filename": "6464eb814abbd284b95104149b4d050d","prev_hash": "f71f9d1d448084e2da92f087a7448bba","hash": "6464eb814abbd284b95104149b4d050d","proto_cls": "Aiolos"}]',
            "data": '{"muid": "cda2f41a-6ba0-4006-8d02-50da84151379","force": "true","behaviors": "[{"filename" : "6464eb814abbd284b95104149b4d050d","prev_hash" : "f71f9d1d448084e2da92f087a7448bba","hash" : "6464eb814abbd284b95104149b4d050d","proto_cls" : "Aiolos"}]"}',
            "sig": "26ff9136f398f4c488b7f4339904df0e5ef1e36135eaac080e4cc8ec5c097b3e",
            "skv": "1"
        }
        headers = {
            "Host":"commonapi.dev.smartcoder.top",
            "Content-Type": "multipart/form-data; boundary=Boundary+03C898E65173FDB0",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Accept-Encoding": "br, gzip, deflate"
        }
        res = requests.request("post",url=url,json=data,headers=headers)
        print(res.json())


if __name__ == '__main__':
    test_gv_newcoming()
    test_gv()