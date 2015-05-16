Title: Optipng - 优化 PNG 图像
Date: 2008-07-21 09:45
Author: toy
Category: Apps
Tags: Optipng, PNG Optimizer
Slug: optipng

PNG 即 Portable Network Graphic 的简称，PNG
图像是一种无损压缩图像文件格式。因为网络传输的需要，我们总是希望 PNG
图像的容量能够小些、小些、再小些。要优化 PNG 图像，可以使用 Optipng
这个专门的 PNG 图像优化工具。

**安装 Optipng**

可使用下列命令来安装 Optipng：

-   Debian/Ubuntu：`$ sudo apt-get install optipng`
-   Fedora：`# yum install optipng`
-   Archlinux：`# pacman -S optipng`

**Optipng 用法**

Optipng 是命令行工具，直接在其后追加所需优化的 PNG 图像即可
(当然，给原文件备份是一种好习惯)：

`optipng desktop.png`

如下图所示，原图 desktop.png 为 857 KB，经 Optipng 优化后为 677
KB，优化的效果还是比较明显的。

[![Optipng](http://i.linuxtoy.org/i/2008/07/optipng-thumb.png)](http://i.linuxtoy.org/i/2008/07/optipng.png)

可以 `man optipng` 详细了解 Optipng 的优化参数。

值得一提的是，Optipng 也可以将其他图像格式 (如 bmp、gif、tiff)
转换成已优化的 PNG 图像。

[Optipng](http://optipng.sourceforge.net/)

**更新**

读者推荐的其他 PNG 优化工具，包括
[pngrewrite](http://entropymine.com/jason/pngrewrite/)、[pngcrush](http://pmt.sourceforge.net/pngcrush/)、[pngout](http://advsys.net/ken/utils.htm#pngout)
(win32)、[pngnq](http://pngnq.sourceforge.net/) 等。
