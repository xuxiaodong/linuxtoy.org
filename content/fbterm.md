Title: FbTerm: 支持中文显示的控制台
Date: 2008-08-08 10:09
Author: toy
Category: Terminal Emulator
Tags: FbTerm, Terminal
Slug: fbterm

FbTerm 提供了一个快速的终端仿真器，它直接运行在你的系统中的帧缓冲
(framebuffer) 之上。使用帧缓冲可以在终端渲染 UTF-8
文本时可以提高性能。FbTerm 旨在提供国际化和现代字体支持时至少与 Linux
内核终端一样快。它允许你在同一个帧缓冲上创建多达 10
个不同的终端窗口，每个窗口都有它的回滚历史。

![FbTerm](http://i.linuxtoy.org/i/2008/08/fbterm.png)

要运行 FbTerm，首先检查当前用户是否在 video 组，如不在，则加入。当运行
FbTerm 后，会在用户主目录下生成 .fbtermrc
配置文件，其中可以更换字体样式及大小、默认前/背景色。

若你不能看到中文，按 Ctrl\_Alt\_E 退出后，再运行下面的命令：

`LANG=zh_CN.utf-8 fbterm`

[FbTerm](http://code.google.com/p/fbterm/)

(感谢 zhong)

[via [LinuxSir](http://www.linuxsir.org/bbs/thread334807.html) &
[Linux.com](http://www.linux.com/feature/143118)]
