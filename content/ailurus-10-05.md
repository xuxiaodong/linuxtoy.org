Title: 小熊猫 Ailurus 10.05 发布
Date: 2010-05-28 15:40
Author: toy
Category: Apps
Tags: Ailurus
Slug: ailurus-10-05

{ 撰文/Homer Xing }

小熊猫 [Ailurus](http://ailurus.cn) 开发小组正式发布了 10.05 版本。

[![ailurus10.05](http://i.linuxtoy.org/images/2010/05/thumb-ailurus10.05.png)](http://i.linuxtoy.org/images/2010/05/ailurus10.05.png)

这个版本带来了以下的新功能:

+ 调整了软件安装界面的布局，腾出更多空间。  
+ 增加了一些受欢迎的软件。  
+ 增强了清理系统的功能。可以清理不用的软件、残存的配置、Nautilus
缓存。  
+ 搜索最快源的面板得到增强，可以同时使用多个源。  
+ 增加了一些 GNOME 设置项目。  
+ 显示 CPU L1 Cache, L2 Cache 的详情。  
+ 增加电脑医生的功能，检测系统中存在的问题，帮助您进行修复。

共有 65
项改进。[这里是详细的更新记录](http://github.com/homerxing/Ailurus/raw/master/ChangeLog)。

Ubuntu 用户这样安装

sudo add-apt-repository ppa:ailurus  
sudo apt-get update  
sudo apt-get install ailurus

Fedora 用户这样安装

su -c 'wget http://homerxing.fedorapeople.org/ailurus.repo -O
/etc/yum.repos.d/ailurus.repo'  
su -c 'yum makecache'  
su -c 'yum install ailurus'

也可到这里直接下载安装程序

小熊猫不会安装那些不开源的程序。不过，您可以手动装个扩展，命令是：

wget
'http://github.com/homerxing/Ailurus/raw/master/unfree/for\_ubuntu.py' -O
~/.config/ailurus/for\_ubuntu.py  
wget
'http://github.com/homerxing/Ailurus/raw/master/unfree/for\_fedora.py' -O
~/.config/ailurus/for\_fedora.py

执行完这个命令后，会增加一些不开源的程序。Fedora 上还会出现第三方源。

如果出现这个错误，UnknownMethodException:
org.freedesktop.DBus.Error.UnknownMethod: Unknown method:
drop\_priviledge is not a valid method of interface cn.ailurus.Interface
不要慌，重启动电脑就好了。

最后，小熊猫的成长离不开各位开源人士、其它开源项目的帮助。在此，小熊猫的作者们，向所有
Linux 增强、设置类软件敬礼！

{ Thanks Homer Xing. }
