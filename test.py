import base64
import json

import requests

# 设置请求参数
proxy="http://127.0.0.1:1080"
proxies = {
            "http://": proxy,
            "https://": proxy
        }
# 发送请求到后端服务
url = "https://initially-messaging-coverage-paste.trycloudflare.com//synthesize" # 后端服务的地址
params = {"text": "早上好，请关注我喵喵喵喵喵，你今天过得怎么样，开心吗", "out": "test.wav","speaker":"Azusa","model":["logs/test.pth","logs/config.json"],"lang":"[ZH]"} # 请求参数
response = requests.post(url,json=json.dumps(params),proxies=proxies) # 发送post请求
print(response.text)
with open("audio.wav", "wb") as f:
    f.write(response.content)

