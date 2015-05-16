Title: QReadBook 发布
Date: 2007-11-17 12:10
Author: toy
Category: Apps
Slug: qreadbook

在 [ZhuaShuShell](http://linuxtoy.org/archives/zhuashu-shell.html)
发布以后，很多朋友问我在 Linux 下阅读用什么软件比较好，而我一般都是在
Windows 下用 Readbook 这款软件来读 :(
于是想着自己编一个，用了几天的课余时间，编写了一个非常简单的文本阅读工具
QReadBook。

[![QReadBook](http://i.linuxtoy.org/i/2007/11/qreadbook-thumb.png)](http://i.linuxtoy.org/i/2007/11/qreadbook.png)  
*QReadBook 屏幕截图*

**QReadBook 简介**

利用几天的课余时间完成的 QT 小程序，支持用 ZhuShuShell 抓下来的 GB2312
编码的文本阅读。

-   开发平台: Ubuntu Linux
-   编程语言: C++, QT4.3 Library

**QReadBook 特点**

1.  灵活的文本打开方式：
    菜单或快捷键 (Ctrl + O) 呼出“打开文件”对话框，Tab
    键呼出目录树，双击树型结构中的 txt 文件调入。
2.  避免视觉疲劳的设置：
    提供快捷键设置：F2 设置文本字体，F3 设置文本颜色，F4
    设置背景颜色，F11 全屏阅读。
3.  自动翻书的功能：
    F5
    设置控制方式：可以选择程序自动滚屏翻书或键鼠控制（键盘的上下键滚屏换行，PageUp/PageDown
    翻页，鼠标左键控制右侧滚动条等），F6/F7 设置翻书速度的增大/减小。
4.  老板键：
    F12 缩小到系统托盘，提供系统托盘选择菜单，双击托盘图标复原。
5.  设置的保存：
    界面设置的保存：文本字体，颜色，背景颜色；上次阅读点的保存：只要上次阅读过该文件，将会自动翻到上次的最后阅读点。
6.  定时提醒，防止误事，保护视力：
    F8
    键设置两种定时提醒功能：间歇提醒（用于保护视力），定时提醒（防止误事）。

**QReadBook 演示视频**

<http://www.tudou.com/programs/view/kxSc-t-kZoE/>

**QReadBook 代码下载**

地址：<http://code.google.com/p/qreadbook/>

基本功能应该是够了，需要改进的地方很多，不过时间较紧，希望有愿意一起开发的可以加入到开发队伍里来
:)

[作者/[fangvv](http://hi.baidu.com/vvfang)]
