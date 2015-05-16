Title: Ailurus 10.03.2 发布
Date: 2010-03-23 20:33
Author: toy
Category: Apps
Tags: Ailurus, Fedora, Ubuntu
Slug: ailurus-10032

{ 撰文/[Homer](http://ailurus.cn) }

Ailurus 是个让 Linux 更好用的程序。现在 10.03.2 版已经发布。

[![Ailurus](http://i.linuxtoy.org/images/2010/03/ailurus-new-gui-thumb.png)](http://i.linuxtoy.org/images/2010/03/ailurus-new-gui.png)

主要的改进有:

对于安装软件功能，

* 增加打字练习软件 Typespeed  
* 增加 NScript。NScript 是一套好用的 Nautilus
脚本，可以创建文件校验和，diff 文件，快捷方式等。  
* 增加计算软件 Extcalc  
* 增加 Fcitx  
* 提高 VirtualBox 的安装速度  
* 简化 CUPS 的安装  
* 删去 FoxitReader

对于系统设置功能，

* 改变窗口标题栏的按钮的布局

[![Ailurus](http://i.linuxtoy.org/images/2010/03/ailurus-change-titlebar-buttons-thumb.png)](http://i.linuxtoy.org/images/2010/03/ailurus-change-titlebar-buttons.png)

* 在 Nautilus 的列表视图中，隐藏“大小”列，以加速 Nautilus

对于搜索最快的源的功能，

* 改进搜索方法。减少了 60% 的搜索时间  
* 自动保存源的速度  
* 可以将零散的源配置文件合并

对于“速配”功能，

* 可以跳过网络状态的检测  
* 可以跳过对源的搜索

其它改进，

* 减少了从源码安装 Ailurus 的耗时

最新版本的 Ailurus 可以在 Ubuntu 8.04~10.04, Fedora 11~12 上使用。

Ubuntu 用户这样安装

sudo add-apt-repository ppa:ailurus  
sudo apt-get update  
sudo apt-get install ailurus

Fedora 用户这样安装

su -c 'wget http://homerxing.fedorapeople.org/ailurus.repo -O
/etc/yum.repos.d/ailurus.repo'  
su -c 'yum makecache'  
su -c 'yum install ailurus'

开发团队定期发布 pre-release 版。 Ubuntu 用户使用  
`sudo add-apt-repository ppa:ailurus/ailurus-experiment`  
可以添加实验版的源。

要跟踪最新开发信息，不妨 Follow 开发团队的推特帐号

如果您想一起开发，可阅读

源代码发布在这

{ Thanks Homer. }
