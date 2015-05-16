Title: KDocker 4.0 发布
Date: 2009-09-17 13:36
Author: toy
Category: Apps
Tags: KDocker
Slug: kdocker-40-released

[KDocker](http://linuxtoy.org/archives/kdocker.html)  
的用途是把窗口缩小到系统托盘里。新近发布的 [KDocker  
4.0](http://john.nachtimwald.com/2009/09/16/kdocker-4-0/) 版已经移植到  
Qt4，不依赖 KDE。

![KDocker](http://i.linuxtoy.org/images/2009/09/kdocker.png)

**安装 KDocker**

在[下载源码](https://launchpad.net/kdocker/+download)并解包后执行下列命令：

qmake kdocker.pro  
make  
sudo cp kdocker /usr/bin/kdocker

**KDE 4 绑定快捷键**

进入“系统设置－常规－输入动作，编辑－新建－全局快捷键－命令/URL”：修改触发器成  
Meta+Z (Meta 就是 Win 键），可能与 Amarok  
的快捷键冲突，自己挑选其他快捷键，修改动作成 kdocker。

**Bug**

有些程序缩小到系统托盘的图标是黑乎乎的，比如 Konsole。

{ Thanks [qii](http://www.twitter.com/qiheizhiya). }
