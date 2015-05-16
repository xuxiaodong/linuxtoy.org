Title: Pickyfont: 实时更改 X 终端字体
Date: 2010-05-25 14:44
Author: toy
Category: Apps
Tags: Font, Perl, Pickyfont
Slug: pickyfont

Pickyfont 是一个使用 Perl 语言写成的小程序，通过它你可以实时更改 X  
终端的字体。你无需重新启动 X
终端程序，更改是立即生效的。目前，Pickyfont 支持 Xterm 和 (U)Rxvt 终端。

![pickyfont](http://i.linuxtoy.org/images/2010/05/pickyfont.png)

首先，利用 `pickyfont list`
列出可用的字体列表，之后即可执行形如以下的命令来更改字体：

pickyfont set ter1

该命令将终端的字体设置为 Terminus 12px。

Pickyfont 的源代码可通过 [github](http://github.com/trapd00r/pickyfont)
获取。
