
# Bert_vits2
- [Bert_vits2](https://github.com/fishaudio/Bert-VITS2)
- [获取更多模型](https://www.bilibili.com/read/cv26912729/?jump_opus=1)
# 部署
## 1、colab部署(推荐)
[点击并依次运行即可](https://colab.research.google.com/drive/1n8lI6pOiDtli2zC5fL9PZ9TZqbOafqma?usp=sharing)
## 2、源码部署
**请确保已经安装[python3.9.0](https://github.com/avilliai/wReply/releases/tag/yirimirai-Bot) ，由于使用了非此版本的py解释器部署此项目产生的报错请自行搜索解决。**<br>
#### 1.1克隆仓库到本地
找一个你喜欢的目录，打开cmd执行
```
git clone https://github.com/avilliai/Bert_Vits2_Sever.git
```
下面获取必要文件，也可以从2.1提供的压缩包中获取，以确保git能够提供稳定更新支持
#### 1.2下载必要文件
从[Huggingface](https://huggingface.co/avillia/bbb/tree/main/bert/chinese-roberta-wwm-ext-large)  **下载如下三个文件并放入bert/chinese-roberta-wwm-ext-large文件夹**
- flax_model.msgpack
- pytorch_model.bin
- tf_model.h5<br>
#### 1.3获取模型
[获取模型](https://www.bilibili.com/read/cv26912729/?jump_opus=1) <br>
创建logs文件夹，模型和配置文件的放置应当如下所示。注意它们在同一个文件夹即{角色名}文件夹内
- Bert_Vits2_Sever/logs/{角色名}/{模型名(无所谓)}.pth
- Bert_Vits2_Sever/logs/{角色名}/config.json
#### 1.4安装必要环境并启动
- 双击安装脚本.bat<br>
- 双击启动脚本.bat<br>
#### 更新
双击update.bat
## 3、压缩包部署
文件比较大github放不下，自带一个azusa模型。压缩包部署将不支持获取github更新<br>
1、下载bert_vits2_sever.rar
- 进群628763673群文件下载
- [百度网盘](https://pan.baidu.com/s/1d5WKFYZ4yGAz09rbroqP2g?pwd=9uyg) 提取码：9uyg<br>

2、双击安装脚本.bat<br>
3、双击启动脚本.bat<br>
#### 更新
从git仓库下载源码压缩包，解压，替换同名文件
#### 如果你需要测试服务是否可用
测试用的代码放在test.py，**激活虚拟环境并安装了对应的模型后**，运行test.py如果生成了可用音频，代表测试成功。
# 安装更多模型
在logs文件夹下新建一个文件夹，如otto
把你的模型和配置文件放进去<br>
如新增一个otto语音模型则
  - logs/otto/G_114514.pth
  - logs/otto/config.json
**以及，务必填写characters.yaml**
# 使用
  要使用你的模型，需要在使用时传入对应的参数
## 对接到QQ机器人
现有方案 [Manyana](https://github.com/avilliai/Manyana) 已经完成对接<br>
你也可以使用[berglm](https://github.com/avilliai/Bergml) 对接，它是一个打包好的exe文件
#### Manyana用户操作指北
请根据你的characters.yaml填写Manyana/config/settings.yaml，在bert_speakers填写所有你bert_vits中可用的角色<br>
先启动Manyana，随后执行 启动脚本.bat 即可<br>
指令格式： xx说XXXXXXXXX 
  
## 自行调用api
**务必确认已填写characters.yaml，你没有的模型对应的配置可以删除**<br>
你可以用你喜欢的语言来调用这个api<br>
在执行 启动脚本.bat 后<br>
向http://localhost:9080/synthesize 发送post请求<br>
如果使用colab部署，笔记里面有写，自己看<br>
api将需要下面的参数
- text          文本
- speaker       说话人(参考characters.yaml)

以下是一个示例(json)
```
{
    "text": "早上好，请关注我", 
    "speaker":"塔菲",
}
```
api将返回语音的二进制文件，你需要保存它
>如果你熟悉python，test.py里面是一个调用实例，但我更建议使用异步的httpx而不是requests来调用它
# 使用GPU加速
如果你已经开始使用了，一定能感觉到，合成的速度并不能让人满意。<br>
这时候，如果你有一张N卡，我们可以通过安装cuda,使用GPU加速来实现更快的语音合成。
- [安装cuda](https://blog.csdn.net/weixin_45763636/article/details/123169495) 
  - 上面的教程关于pytorch的部分不用看
- [根据你的实际情况选择一个torch版本](https://pytorch.org/get-started/locally/)
<img src="bert/chinese-roberta-wwm-ext-large/img.png">

  - 复制蓝色部分
- 在Bert_Vits_Sever文件夹打开cmd
  - 依次输入如下指令
  - cd venv/Scripts
  - call activate.bat
  - pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html <br>(这是根据我的系统、包管理器、Python版本和CUDA版本所生成的，不一定适合你)

重启即可
# 声明
**严禁将此项目用于一切违反《中华人民共和国宪法》，《中华人民共和国刑法》，《中华人民共和国治安管理处罚法》和《中华人民共和国民法典》之用途。**<br>
**严禁用于任何政治相关用途。**
