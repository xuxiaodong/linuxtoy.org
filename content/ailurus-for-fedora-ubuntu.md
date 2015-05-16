Title: Ailurus 发布 Fedora 版本和 Ubuntu 版本，增加一些新功能
Date: 2010-01-19 11:33
Author: toy
Category: Apps
Tags: Ailurus, Fedora, Ubuntu
Slug: ailurus-for-fedora-ubuntu

{ 撰文/Homer }

[Ailurus](http://ailurus.cn/) 是系统快速安装配置程序，它让 Linux  
更好用，帮助新手老手节约时间。

最近，Ailurus 开发团队发布了 Fedora 版本。Fedora 9/10/11/12  
都能用。

这样安装:

cd /tmp  
wget http://ailurus.googlecode.com/files/ailurus-10.01.3-1.noarch.rpm  
su -c 'rpm -U ailurus-10.01.3-1.noarch.rpm'

装好以后，点击“应用程序->系统工具->Ailurus”启动。

截图

![Ailurus](http://i.linuxtoy.org/images/2010/01/ailurus-10.01.png)

Fedora 版本的主要特性有:

+ 安装一些好用的软件，如 Skype，Vuze，Google Chrome，Flash 插件  
+ 开启 RPMFusion、Adobe、Google Chrome、Skype、Livna、ATrpms 源  
+ 更改 GNOME 的隐藏设置  
+ “日积月累” 窗口包含一些 Linux 技巧，帮助您学习 Linux。  
+ 开启 sudo  
+ 开启彩色的 Bash 提示符  
+ 安装好用的 Firefox 扩展

同时，开发团队也增强了 Ailurus 的 Ubuntu 版本。  
新版本支持 Ubuntu 8.04, 8.10, 9.04 和 9.10。Kubuntu、Xubuntu、Mint  
5/6/7/8 都能用。  
Ailurus 10.04.4 版已经上传到 Launchpad PPA 源。

这样安装:

向 /etc/apt/sources.list 中添加这一行

deb http://ppa.launchpad.net/ailurus/ppa/ubuntu karmic main

(8.04, 8.10, 9.04 用户请将 karmic 换成 hardy, intrepid 或者 jaunty)

然后执行

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 9A6FE242  
sudo apt-get update  
sudo apt-get install ailurus

相比 10.01.1 版，新的 Ailurus 10.01.4 版本有了如下增强:

+ “日积月累”窗口中增加了 10% 的 Linux 知识。  
+ 增加了 “速配” 功能。ubuntuabc.com 有详细报导
http://ubuntuabc.com/123/?p=130  
+ 增加了 Aptana, Mylyn, PDT, RadRails 和 Subversive 等几个 Eclipse
插件  
+ 增加了 61 个 Eclipse 下载镜像，加快了下载速度。  
+ 64 位系统上可以安装 Adobe 原生的 64 位 Flash 了。 Flash 是从 Adobe
网站直接下载的，没有安全隐患。  
+ Bug 检测功能得到增强。  
+ 通过调用 tasksel，增加了 LAMP, Ubuntu Enterprise Cloud Cluster
等配置服务器的功能。  
+ 改进了 MPlayer-vod 的安装代码  
+ 改进了 Adobe Reader 等软件的检测  
+ 增加了 20% 的第三方源

Ailurus 的发展，离不开大家的帮助。Ailurus  
开发团队向全体用户敬礼！向所有 Linux 设置软件敬礼！

{ Thanks Homer. }
