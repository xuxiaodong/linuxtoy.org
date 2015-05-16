Title: WordJoy 发布 0.19 版本
Date: 2009-07-17 10:00
Author: toy
Category: Apps
Tags: WordJoy
Slug: wordjoy-019-released

{撰文/[renewjoy](http://linux.cuit.edu.cn)}

WordJoy 是一个用 PyGTK 编写的背单词软件。目前只在 Linux
下成功测试，至于在 Windows 下运行需要安装哪些库，请参考其它 PyGTK
写的程序。

[![WordJoy](http://i.linuxtoy.org/images/2009/07/wordjoy-thumb.png)](http://i.linuxtoy.org/images/2009/07/wordjoy.png)

WordJoy 基于 TualatriX 大侠的 MyWord 改写而成，而 MyWord 又是继承于
StarDict 作者 HuZheng 的 Reciteword
背单词软件而来。具体请参看这两款软件的信息。

**本程序的特色：**

1. 采用全新的书本格式，争取做到更加简洁、明了、实用。  
2. 每个单词配以三个例句，让你在句子中学习单词的意思与用法。  
3. 支持使用 WyabdcRealPeopleTTS 真人语音包发音。  
4. 支持单词测试，随时掌握自己的学习情况。  
5. 支持背诵的遗忘曲线，采用记录的方式提醒你，今天该背诵的单词。  
6.
支持自定义词库，自己制作背诵的书本（只需要给出单词列表，即可自动生成）。  
7. 更多特色由你来扩展……

**发布说明：**

时间仓促，先发布一个功能不完整版本，暂时只实现了两个基本功能：

1. 选择等级或书本（由我整理了 10 来本书）。  
2. 单词浏览记忆，配以例句，支持发音（需要 WyabdcRealPeopleTTS
真人语音包和 alsa-utils 支持）。

只因期待你的建议、参与一起丰富功能，遂发布此功能不完整版本。

下载与 Wiki:

**安装运行说明：**

安装：本程序暂时无需安装（因功能不完整，想必你也不会安装），下载包解压即可。

**运行环境：**

1. Linux 环境（或者你会想办法让它运行在 Windows 上，It’s up 2 you!）  
2. Python 环境（或者你可以用其它语言改写）  
3. gtk+2.0  
4. libglade (因界面采用 glade3 来设计)

运行：`$ python wordjoy.py`
