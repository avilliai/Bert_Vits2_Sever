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
url = "http://127.0.0.1:9080/synthesize" # 后端服务的地址
params = {"text": "似乎没有对应的角色呢","speaker": "阿梓"} # 请求参数
response = requests.post(url,json=json.dumps(params)) # 发送post请求
#print(response.text)
with open("audi2o1.wav", "wb") as f:
    f.write(response.content)

