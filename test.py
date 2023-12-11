import base64
import json

import requests

# 设置请求参数


# 发送请求到后端服务
url = "http://localhost:9080/synthesize" # 后端服务的地址
params = {"text": "早上好，请关注我喵喵喵喵喵", "out": "test.wav","speaker":"Azusa","model":["logs/azusa/G_2800.pth","logs/azusa/config.json"],"lang":"[ZH]"} # 请求参数
response = requests.post(url,json=json.dumps(params)) # 发送post请求
print(response.text)

