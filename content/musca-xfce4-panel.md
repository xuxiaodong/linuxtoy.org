Title: Musca + Xfce4-panel：接近完美
Date: 2009-12-05 15:24
Author: jiqingwu
Category: Tips
Tags: Musca
Slug: musca-xfce4-panel

{ 撰文/[吴吉庆](http://hi.baidu.com/jiqing0925) }

我上篇讲 [Musca  
配置的文章](http://linuxtoy.org/archives/musca-config.html)中所说的用
Conky  

显示窗口列表，效果并不是很好，文本经常显示不全。而且也不能像真的任务栏那样操作。

PyPanel 也不行，根本不能显示窗口列表。

我一开始还以为是 Musca 不符合 MWM 规范呢，但看到一个网友用 Tint2
可以显示窗口列表。  
他告诉我说，就 PyPanel 不行，别的 panel 都可以。  
原来这样，看来 Musca 都可以嵌入到 GNOME 中用了，真的很不错啊。

我试用了 Tint2，基本满意，但是有两个问题：

1. 它对系统托盘程序的支持并不好。它对方形的托盘图标显示没问题，但是对于
Workrave 这样的长矩形托盘也只能显示个方形，显示不全。  
2.
用鼠标激活窗口时，任务栏上的窗口才显示被激活的状态，用快捷键激活窗口时，任务栏上所有的窗口都没有被激活的状态。

我于是试了下 Xfce4-panel，效果几乎完美。Tint2 的那两个问题都解决了。  
而且对工作区的显示非常棒，你看截图右下角的工作区显示。  
可能美中不足的就是它是 Xfce4
的组件，不能独立安装，也不能独立调节它的显示外观。希望朋友们提出更好的方案。

[![Musca](http://i.linuxtoy.org/images/2009/12/musca\_xfce\_panel-thumb.jpg)](http://i.linuxtoy.org/images/2009/12/musca\_xfce\_panel.jpg)

{
[Source](http://hi.baidu.com/jiqing0925/blog/item/5d2c646da99654f14216945f.html).
Thanks jiqing. }
