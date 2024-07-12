import json
import re
import requests
import websocket
import asyncio
import ssl



# 拼图的newcoming接口
def test_gv_newcoming():
        # url = "https://puzzle.dev.smartcoder.top/v1/jgspz/home_page/u1/get"
        url = "https://api.colorplanet.art/v1/jgspz/home_page/u1/get"
        data = {
            # "data": '{"app_package_name":"art.color.planet.jigsaw.puzzle.online","timezone":8,"country":"CN","platform":"ios","device_model":"phone","new_item_version_code":"1686219710","offset":0,"segment_token":123,"muid":"cda2f41a-6ba0-4006-8d02-50da84151379"}',
            "data": "%7B%22app_package_name%22:%22art.color.planet.jigsaw.puzzle.online%22,%22timezone%22:8,%22country%22:%22SG%22,%22platform%22:%22ios%22,%22device_model%22:%22phone%22,%22new_item_version_code%22:%221719991553%22,%22offset%22:0,%22segment_token%22:123,%22muid%22:%22b8a04d2d-1b00-45ec-a2e7-26dce04cb74b%22%7D",
            "skv": "K6657942",
            "sig": "43c2bae996dbf8296cb65b662918ad27f43c26f0f3e142982139975c444c5e43"
        }
        # res = requests.get(url,params=data,headers=headers)
        res = requests.get(url=url, params=data)
        assert res.status_code == 200,"返回值错误，不是200"
        assert "code" in res.json()["meta"]
        # for i in range(len(res.json()['data']['recommend']['items'])):
        #     print(res.json()['data']['recommend']['items'][i]['img_info']['id'])
        # assert res.json()['data']['recommend']['items'][0]['img_info']['id'] == "img_VO4VKsH8MU"
        assert "drop" in res.json()["data"]["recommend"]
        assert isinstance(res.json()["data"]["recommend"]["drop"],bool),"返回值不是布尔值"


        # assert "type" in res.json()["data"]["recommend"]["items"][0]
        # assert "drop" in res.json()["data"]
        # assert "drop" in res.json()["data[0].recommend"]
        # assert res.json().data.recommend.drop == "true"
        # 运行程序时 pyhon -O main.py 跳过所有的assert断言
        print(res.json())



    # gv的统一接口
def test_gv():
        url = "https://commonapi.dev.smartcoder.top/api/v3/behavior/get_next"
        data = {
            "behaviors": {'filename': '6464eb814abbd284b95104149b4d050d','prev_hash': 'f71f9d1d448084e2da92f087a7448bba','hash': '6464eb814abbd284b95104149b4d050d','proto_cls': 'Aiolos'},
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


def test_team():
    ssl_context = ssl.create_default_context()
    # 禁用证书验证
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    ws = websocket.create_connection("wss://ws.dev.smartcoder.top/game/login/checkin", sslopt=ssl_context.options)
    ws.send("Your message")
    print(ws.recv())

    ws.close()




    # uri = "wss://ws.dev.smartcoder.top/game/login/checkin"
    # async with websockets.connect(uri) as websocket:
    #     await websocket.send("hello")
    #     response = await websocket.recv()
    #     print(f'Received:{response}')

# asyncio.get_event_loop().run_until_complete(test_team())

    # data = {
    #     "muid": "cda2f41a-6ba0-4006-8d02-50da84151379"
    # }
    # res = requests.get(url=url,params=data)
    # print(res.json())


if __name__ == '__main__':
    test_gv_newcoming()
    test_gv()
    test_team()