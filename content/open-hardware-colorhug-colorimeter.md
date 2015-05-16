Title: 开源硬件：ColorHug 色度计
Date: 2011-11-16 10:14
Author: lovenemesis
Category: Gadget
Tags: colord, colorhug
Slug: open-hardware-colorhug-colorimeter

在几周艰苦开发工作之后，著名的开源开发者 Richard Hughes
宣布了开源色度计ColorHug的预发布版本，通过它，你可以测量屏幕的颜色生成色彩特性文件，从而校准显示器颜色。*感谢
jcome 来稿*

如果您一直感到疑惑为何同样的照片在相机上和显示器上看起来那么不一样呢？原因就是您的显示器没有经过色彩校准：

[![](http://linuxtoy.org/img/2011/11/color-camera.png "color-camera")](http://linuxtoy.org/img/2011/11/color-camera.png)

在相机上的照片

[![](http://linuxtoy.org/img/2011/11/color-display.png "color-display")](http://linuxtoy.org/img/2011/11/color-display.png)

在未经校准的显示器上的照片

相对市面上已有的色度计，ColorHug 主要的优势在于**价廉物美**：仅售
£60，测量速度快，80秒即可完成测量。而且整个仪器十分小巧。

[![](http://linuxtoy.org/img/2011/11/colorhug3.jpg "colorhug3")](http://linuxtoy.org/img/2011/11/colorhug3.jpg)

目前该色度计只支持 colord，也就是说只支持 Linux 平台，但是生成的标准 ICC
文件可以在 Win 和 OS X 上使用。

上市时间大概会在十二月份，会包括 5 年质保，2
米的USB线，和包含所有必须软件的最新版 Fedora16
LiveCD。所有源代码，包括固件，设计图，PCBs，放在 Gitorious 中，以GPL
授权。

目前是**预订阶段**：无需实际支付，只需表达购买意愿，即可享受 £48
的优惠价格。

更多细节请前往[项目主页](http://www.hughski.com/)

更多关于[开源色彩管理 Colord 及 Richard Hughes
的内容](http://linuxtoy.org/archives/richard-hughes-with-color-management-on-linux-gnome.html)。
