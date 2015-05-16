Title: 小熊猫 Ailurus 10.06 发布
Date: 2010-07-01 17:32
Author: Homer Xing
Category: News
Slug: ailurus-10-06-released

小熊猫 Ailurus 是一个 Linux
增强软件，提供安装好用的软件、调整系统设置、提示 Linux
命令技巧等等贴心的功能，支持 Ubuntu, Fedora,
ArchLinux。开发团队是来自北京、上海、广州的10位工程师、学生。

目前小熊猫正式发布了 10.06 版本，带来了以下的主要改进:

-   在线同步软件条目、软件图标
-   可以通过代理服务器下载软件包
-   改进了软件安装面板的布局
-   调整 Firefox 首选项的功能
-   重置 GConf
-   ArchLinux 版本中增加了多个优秀的软件
-   不再试图修复 Flash 字体错误，可以恢复 Flash 字体设置

共有42项改进。[详细的更新记录在这里](http://github.com/homerxing/Ailurus/raw/master/ChangeLog)。

Ubuntu 用户这样安装

    sudo add-apt-repository ppa:ailurus
    sudo apt-get update
    sudo apt-get install ailurus

Fedora 用户这样安装

    su -c 'wget http://homerxing.fedorapeople.org/ailurus.repo -O /etc/yum.repos.d/ailurus.repo'
    su -c 'yum makecache'
    su -c 'yum install ailurus'

ArchLinux 用户可通过 AUR 安装

也可到这里直接下载安装程序
<http://code.google.com/p/ailurus/downloads/list>

小熊猫不会安装那些不开源的程序。不过，您可手动装个扩展，命令是：

    wget 'http://github.com/homerxing/Ailurus/raw/master/unfree/for_ubuntu.py' -O ~/.config/ailurus/for_ubuntu.py
    wget 'http://github.com/homerxing/Ailurus/raw/master/unfree/for_fedora.py' -O ~/.config/ailurus/for_fedora.py

执行完这个命令后，界面上会增加不开源的程序。Fedora上还会出现第三方源。
