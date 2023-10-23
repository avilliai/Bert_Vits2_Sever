
# Bert_vits2
- [Bert_vits2](https://github.com/fishaudio/Bert-VITS2)
- [获取更多模型](https://www.bilibili.com/read/cv26912729/?jump_opus=1)
# 部署
请确保已经安装pyton3.9.0，由于使用了非此版本的py解释器部署此项目产生的报错请自行搜索解决。<br>
文件比较大github放不下<br>
1、下载bert_vits2_sever.rar
- 进群628763673群文件下载
- 百度网盘(待更新)<br>

2、双击安装脚本.bat<br>
3、双击启动脚本.bat<br>
#### 如果你需要测试服务是否可用
测试用的代码放在test.py，**激活虚拟环境后**，运行test.py如果生成了test.wav，代表测试成功。
# 安装更多模型
把你的模型放在logs文件夹下的某一文件夹即可,如<br>
logs<br>
- otto
  - G_114514.pth
  - config.json
## 如果你是Manyana用户
请填写Manyana/config/bert_vits2.yaml，里面有填写示例<br>
先启动Manyana，随后执行 启动脚本.bat 即可<br>
指令格式： xx说XXXXXXXXX 
  
## 自行调用api
你可以用你喜欢的语言来调用这个api<br>
在执行 启动脚本.bat 后<br>
向http://localhost:9080/synthesize 发送post请求<br>
api将接收五个参数，如果你不需要指定自己的模型，传前两个参数即可。
- text 文本
- out 语音保存路径(绝对路径，否则将以bert_vits2_sever为根目录保存在相对路径)
(以下三项缺省选塔菲)
- speaker 说话人
- model 模型与配置文件路径(相对路径，以bert_vits2_sever为根目录)
- lang 语言类型

以下是一个示例(json)
```
{
    "text": "早上好，请关注我", 
    "out": "test.wav",
    "speaker":"taffy",
    "model":["logs/Taffy/G_15800.pth","logs/Taffy/config.json"],
    "lang":"[ZH]"
}
```
api将返回语音的路径，代表成功保存了。
