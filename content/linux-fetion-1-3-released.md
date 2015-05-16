Title: Linux-Fetion 1.3 发布
Date: 2010-01-02 18:20
Author: toy
Category: Apps
Tags: fetion
Slug: linux-fetion-1-3-released

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

在 Windows 版本发布不久以后，Linux  
版本的小飞信也如期而至。本次更新主要是修复 1.2 版本的  
bug，提高性能和节省流量。功能上和 1.2 没有大的出入。

[Linux-Fetion](http://code.google.com/p/libfetion-gui/) 1.3.0 的
Changelog：

+ 优化好友列表管理操作，极大的提高程序性能和登录速度。  
+ 缓存好友信息，节约网络流量，加快好友信息的显示。  
+ 解决过多好友显示为 NULL 的 bug。  
+ 修复一个特殊条件下，新消息托盘没有提示的 bug
(但已记录到聊天记录里面)。  
+ 修复更新好友昵称和心情短语的问题。  
+ 修复作者窗口没有关闭按钮的 bug (Linux)。  
+ 修复程序任务栏没有图标的 bug (Linux)。  
+ 修复不能显示部分手机型号的飞信发来的表情符号的 bug。  
+ 修复关闭最后一个聊天对象标签程序崩溃的 bug (Windows)。  
+ 完善聊天窗口输入焦点的问题，增加程序易用性。

使用 Fedora 12 的朋友，可以在这里获取 rpm 包  
(理论上此包还可以用在旧版本 Fedora )：
href="http://dl.dropbox.com/u/1352061/yum/12/x86\_64/linux-fetion-1.3-1.fc12.x86\_64.rpm">64
位，
href="http://dl.dropbox.com/u/1352061/yum/12/i386/linux-fetion-1.3-1.fc12.i686.rpm">32
位

或者使用下列命令获取 Linux-Fetion 的 Fedora rpm 包：

su -c 'wget http://dl.dropbox.com/u/1352061/liangsuilong.repo -P
/etc/yum.repos.d/'

然后刷写缓存后即可透过用 yum 安装 Linux-Fetion

yum makecache && yum install linux-fetion

[Linux-Fetion  

源代码下载地址](http://libfetion-gui.googlecode.com/files/linux_fetion_v1.3.tar.gz)

{ Thanks liangsuilong. }
