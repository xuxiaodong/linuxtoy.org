Title: Skype Call Recoder
Date: 2010-10-02 16:19
Author: lovenemesis
Category: Instant Messenger
Tags: Recorder, Skype
Slug: skype-call-recoder

如果你常常使用 Skype 语音聊天或者进行电话会议，那么 Skype Call Recoder
绝对是保留语音记录的好帮手。

Skype Call Recoder (SCR) 由 jlh 基于 Skype API 开发，可以将 Skype
语音聊天录制为 MP3/OGG/WAV 格式保存在本地，不限长度。

以 Fedora 14 i686 为例的**安装说明**：

1. 需要 [skype 2.X+
以上版本](http://linuxtoy.org/archives/skype-2-1-beta-2-for-linux.html)，1.X
系列不支持……

2. 安装必要的依赖：`pkcon install id3lib`

3. 创建必要的库链接解决以来问题：
`su -c 'ln -vs /usr/lib/libssl.so.1.0.0a /usr/lib/libssl.so.0.9.8'`

4. 下载 SCR 并安装：[32bit 及 64bit
二进制DEB/RPM包、源代码包下载](http://atdot.ch/scr/download/)

5. 首先启动 Skype 然后再启动 SCR，然后允许 SCR 访问 Skype 。

6. 默认会在每次通话前询问是否录音，格式为 MP3，保存在 `~/Skype Calls`
目录下。若要更改配置右键点击系统托盘区的图标即可。

*消息来源*：
[Linux.com](http://www.linux.com/learn/tutorials/367395-weekend-project-record-from-skype-calls-and-other-apps-on-linux)
（原文中包含很多 **PulseAudio 配置技巧和其他解决方案**，值得阅读）

[Skype Call Recorder Win32
测试版](http://atdot.ch/scr/2010/07/experimental-windows-version/)
