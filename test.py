import asyncio
import base64
import json

import httpx
import requests


# 发送请求到后端服务
url = "https://opening-chuck-burst-nominated.trycloudflare.com/synthesize" # 后端服务的地址
params = {"text": "看来没有对应的角色给你用呢，杂鱼","speaker": "阿梓"} # 请求参数
response = requests.post(url,json=json.dumps(params)) # 发送post请求
#print(response.text)

        # 请求参数
async def eh():
    async with httpx.AsyncClient(timeout=200) as client:
        r=await client.post(url, json=json.dumps(params))
        p="aT.wav"
        print("bert_vits语音合成路径："+p)
        with open(p, "wb") as f:
            f.write(r.content)
asyncio.run(eh())


