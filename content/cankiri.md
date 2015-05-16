Title: Cankiri：小巧实用的屏幕录像机
Date: 2006-07-31 10:58
Author: toy
Category: Apps, Featured
Slug: cankiri

我在阅读 Michael Urman 的 [Blog](http://www.tortall.net/mu/blog/)
时看到其开发的
[Cankiri](http://www.tortall.net/mu/blog/2006/07/29/cankiri_1)，觉得非常实用，特介绍给大家。

**Cankiri 是什么**

简单地说，Cankiri
就像是一个屏幕录像机，它可以将你在桌面上的所有动态操作录制下来，并最终生成电影文件。当前，Cankiri
具有程序小巧（本身只含一个文件）、录制稳定之特点。而从录制功能上来看，现在
Cankiri 可以录制声音、
鼠标指针、全屏或区域。在生成的电影文件格式上，Cankiri 选择的是
ogg。虽然从目前来说，Cankiri
的功能算不上强大，但对于需求不大的用户仍然值得一用。

**怎样使用 Cankiri**

Cankiri（可[在此](http://www.tortall.net/svn/mu/trunk/cankiri/cankiri.py)下载）的使用亦很简单，首先，通过在终端执行指令
`python cankiri.py` 来启动 Cankiri。启动后的 Cankiri
将在系统托盘显示一个图标。

![Cankiri Icon](http://i.linuxtoy.org/i/cankiri_icon.png)

之后，点击该图标即可打开屏幕录像设置窗口。在这里，既可以设置电影文件的保存位置及名称，也可以选择屏幕录像的选项参数。单击“OK”按钮将会立即开始屏幕录像工作。如果需要停止录制过程，再次点击系统托盘中的图标即可。

[![Cankiri
Set](http://i.linuxtoy.org/i/cankiri_set_s.png)](http://i.linuxtoy.org/i/cankiri_set.png)

**如何播放 Cankiri 录制的电影**

你可以使用任何支持播放 ogg 格式的软件，比如我喜欢在终端中使用
`mplayer -fs *.ogg` 来播放。

PS.
我使用这个小工具录制了一段[更改桌面壁纸的视频](http://linuxtoy.org/dls/screencast-xxd-2006-07-31-10:01.ogg)，感兴趣的朋友可以看看。
