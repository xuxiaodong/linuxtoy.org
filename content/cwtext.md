Title: cwtext —— 莫尔斯电码生成器
Date: 2009-11-02 16:45
Author: MDZ
Category: Apps
Tags: cwtext, morse
Slug: cwtext

好久没上 LinuxToy 发表文章了，今天我看到 LinuxToy
欣欣向荣的景象，倍感骄傲。至于为什么那么久都没上 LinuxToy
发文，源于今年上半年换了个单位，“被迫”用了许久的 Windows
XP（连同维护单位的计算机）。在这段“黑暗”的时间里，事实再次证明 Windows
有多糟糕 —— 我不得不请出 GHOST、360、杀毒软件、Windows 清理助手甚至 DOS
共同维护这些脆弱的洋娃娃。Oh, Damned！好在经过长时间努力，我终于又回到
Linux 怀抱，倒是这样，工作开展得更加顺利。想不到啊，在众多的 Windows
包围下，Linux 却显得更成熟稳重，这可能正是 Linux 的生命力之所在吧！

言归正传，今天要给朋友们介绍的是 cwtext ——
莫尔斯电码生成器。最近忙里偷闲，看了麦家的小说《风声》、《暗算》，一下子对莫尔斯电码产生了浓厚的兴趣。在兴趣的驱使下，我突然想到，我们是否也可以模拟一个莫尔斯编码系统，将有些东西用莫尔斯电码存储，防君子不防小人？呵呵。这一切对使用
Linux
的同仁们简直太简单了，简单到我的想法只是又做了一个已经由别人重复制作了上万次的轮子，因为已经有了一大堆类似功能的软件，而
cwtext 只是其中简简单单的一个（甚至源代码都是那么简简单单）。

cwtext 做的事情很简单，就是将 plain ASCII
转化成为国际通用的莫尔斯电码。至于中文嘛，将其先转化为区位码或拼音或自定义的码表，将中文和英文数字建立起映射关系，然后再用
cwtext 转化为莫尔斯电码。具体使用何种码表，这就要看你的聪明才智啦！

[![](http://i.linuxtoy.org/images/2009/11/morse_code.jpg)](http://i.linuxtoy.org/images/2009/11/morse_code.jpg)

或许仅仅用 cwtext 转化成为莫尔斯电码还不过瘾，那我们也可以使用 cwtext
自带的 cwpcm 转化成为音频脉冲信号，再通过 sox 生成音频文件 ——
听那一大堆的滴滴达达，呵呵，要想破解，先学点无线电知识再说！（不过
cwtext 包中的 README
说的生成方法跟我测试时有出入，本人正在寻求解决办法…）

这里我用 cwtext 生成了一组莫尔斯电码，有兴趣的可以翻译一下：

`.... . .-.. .-.. ---  .-.. .. -. ..- -..- - --- -.-- . .-. ...`

官方网站：<http://cwtext.sourceforge.net/> （网站更新不及时）

下载地址：<http://sourceforge.net/projects/cwtext/>

安装方法：to read README
