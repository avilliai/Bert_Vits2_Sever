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
url = "https://regularly-speakers-external-transform.trycloudflare.com/synthesize" # 后端服务的地址
params = {"text": "我的心情还不错，你呢", "out": "test.wav","speaker":"阿梓"} # 请求参数
response = requests.post(url,json=json.dumps(params),proxies=proxies) # 发送post请求
#print(response.text)
with open("audio1.wav", "wb") as f:
    f.write(response.content)

