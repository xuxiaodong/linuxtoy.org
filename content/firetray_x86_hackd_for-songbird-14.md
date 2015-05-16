Title: 把你的 SongBird 嵌入 SysTray 托盘 FireTray_x86_hacked For-SongBird-1.4.*
Date: 2010-01-01 14:21
Author: ihipop
Category: Music Player
Tags: firefray, Songbird, tray
Slug: firetray_x86_hackd_for-songbird-14

{ 撰文/[ihipop](http://ihipop.gicp.net/)}  
  
前几天 Toy 介绍了新版本的
[SongBird](http://linuxtoy.org/archives/songbird-141-released.html)，呵呵，其实我一直再用的，不爽的就是那个默认不能缩放到托盘，官方插件库里面的那个
firefray，版本号一直停留在 Version: 0.1.13，

也是只支持到 SongBird 1.1.1就没有更新过，装不上，

这里我下载了原始的 xpi 文件（[Linux
32-bit](http://addons.songbirdnest.com/xpis/3327?source=download)）修改了下他的兼容版本信息，骗过了
SongBird 的检查，大家下载即可，不敢太嚣张，所以修改成了 1.4.+
版本通用的信息，文件和修改方法如下

这个是修改好的文件
[firetray\_x86\_hack\_to-SongBird-1.4.*](http://i.linuxtoy.org/images/2010/01/firetray_x86_hack_to-14.zip)，下载后解压缩拖放到
SongBird 的窗口里面即可

[![](http://i.linuxtoy.org/images/2010/01/screenshot_010-399x214.png)](http://i.linuxtoy.org/images/2010/01/screenshot_010.png)

下面开始授人以渔

1.  下载原始的 xpi 文件（[Linux
    32-bit](http://addons.songbirdnest.com/xpis/3327?source=download)，firetray\\\_x86.xpi），然后我在
    /tmp 目录建立一个文件夹，命名为 test，这个随意阿
2.  mv firetray\\\_x86.xpi /tmp/test
3.  unzip firetray\\\_x86.xpi
4.  gedit install.rdf
5.  查找 <em:maxversion>1.1.1</em:maxversion>，改为
    <em:maxversion>1.4.*</em:maxversion>，存盘退出
6.  rm -f firetray\\\_x86.xpi
7.  zip -r firetray\\\_x86\\\_hacked.xpi *
8.  收工

