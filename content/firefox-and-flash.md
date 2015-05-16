Title: 解决 Flash 全屏时 Firefox 崩溃的问题
Date: 2009-07-17 11:50
Author: toy
Category: Tips
Tags: Firefox, Flash
Slug: firefox-and-flash

在 Firefox 中看 Flash 时一旦点击全屏，Firefox
即刻崩溃。这个问题自打俺使用 Firefox 3.5 Beta
测试版时便已存在。先前是通过 Gcell 兄所说的禁用 Flash
硬件加速的办法来解决。最近，我了解到这其实是由 NVIDIA 驱动程序的 bug
造成的，据说 ATI 用户也有类似的问题。以下是另一种解决办法。

找到 Firefox 安装目录中的 firefox.sh，在其第二行加入：

export LD\_PRELOAD=/usr/lib/libGL.so.1

或者创建一个包含如下内容的脚本：

#!/bin/sh  
LD\_PRELOAD=/usr/lib/libGL.so.1 firefox

注意：有的系统没有 libGL.so.1，而是 libGL.so，只需作相应的替换即可。

{via [UbuntuForums](http://ubuntuforums.org/showthread.php?p=7487421)}
