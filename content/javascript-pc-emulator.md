Title: JavaScript PC 模拟器
Date: 2011-05-17 23:54
Author: lovenemesis
Category: Emulator
Tags: javascript
Slug: javascript-pc-emulator

很难想象竟然用了这么久，Linux 才可以运行在浏览器的 JavaScript
引擎里面，要知道[2008
年就可以在土豆上运行了](http://www.bbspot.com/news/2008/12/linux-on-a-potato.html)~

[![](http://linuxtoy.org/img/2011/05/linux2.png "linux2")](http://linuxtoy.org/img/2011/05/linux2.png)

如何实现的：

1.  作者 Fabrice Bellard 使用 JavaScript 编写了一个简单的 PC
    模拟器，包含32位 x86 兼容 CPU、8259 可编程中断控制器、8254
    可编程中断计时器
2.  实现 16450 UART 串口设备
3.  用 JavaScript 实现一个终端
4.  编译包含 FPU 模拟的 Linux 内核镜像。
5.  使用 Buildroot 创建文件系统并在启动时载入 RAM。
6.  添加基本工具集 [BusyBox](http://www.busybox.net/)，微型 C 编译器
    [TinyCC](http://bellard.org/tcc)，以及迷你编辑器
    [QEmacs](http://bellard.org/qemacs)

根据作者的描述，该模拟器的初衷是了解现在 JavaScript 引擎的工作，尤其是
Firefox 4 的 Jaeger Monkey 和 Chrome 的 V8，这个探索的结果，可以被用来：

-   通过 Linux 的启动时间反应浏览器的 JavaScript 性能。(作者说目前在
    Firefox 4 下比 Chrome 11 要快 2倍，Chrome 12 有 Bug 无法运行)。
-   实验在用 JavaScript 进行客户端运算时载入 x86 运行库的可能性。
-   进一步发展从而支持 DOS 游戏的运行。

[JS-Linux 主页](http://bellard.org/jslinux/)

[技术内涵](http://bellard.org/jslinux/tech.html)
