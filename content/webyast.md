Title: WebYaST 简介
Date: 2009-08-28 19:39
Author: gmsh
Category: Apps, Network, News
Tags: openSUSE, WebYaST
Slug: webyast

WebYaST 是 openSUSE 的下一版 openSUSE 11.2
中新添的应用，本文简单介绍一些关于 WebYaST的情况。

### WebYaST 是什么？

YaST 是 SUSE 系 Linux 发行版的默认系统安装配置工具。YaST 是 Yet another
Setup Tool 的缩写。WebYaST 是 网页端管理工具。

*转自 <http://blog.gmsh.pp.ru/2009/08/webyast/> (Gmsh's blog)*

### 不得不提的 YaST Research

YaST的功能是十分强大的，但它只是本地一对一的系统管理工具。在 Web 2.0
的时代，openSUSE 社区要把 YaST
发展为一个可靠的网页用户界面。也就是，在计算机上运行 http
服务，然后在远程通过浏览器控制计算机。现在，几乎所有的联网硬件都可以通过网络来控制，运行
openSUSE 的电脑为什么不可以呢？这就是YaST Research 项目的初衷。

### WebYaST 的定位

WebYaST 源于 YaST Research 项目。openSUSE
社区给了它一个响亮的名字——WebYaST。  
正如摘要中提到的，WebYaST 是 openSUSE 11.2 中新添加的特性。WebYaST
的功能目标是成为一种以浏览器为依托，以网页为操作界面的远程主机管理工具。

### WebYaST 的功能

配置:

-   基本网络配置
-   基本用户管理
-   设置密码
-   SMTP 邮件提醒
-   服务管理
-   多语言
-   时区日期

管理:

-   状态查看
-   日志查看
-   可控升级
-   重启

其他特性:

-   易用的第三方配置
-   首次启动配置向导
-   品牌（branding）

### WebYast 的架构

架构图  

[![](http://i.linuxtoy.org/images/2009/08/webyastarchitecture.jpeg)](http://i.linuxtoy.org/images/2009/08/webyastarchitecture.jpeg)

### WebYast 简评

[John Smith](http://linuxtoy.org/archives/author/gmsh/)
觉得它颇有＂云计算＂的意味，也可以在没有本地图形用户界面的计算机上运行。它的前景是很广阔的，笔者觉得它很有可能成为超过
cPanel 的远程虚拟主机控制工具。（ cPanel 是商业性的）。openSUSE 11.2
将于11月12日发布，届时 WebYast 将作为技术预览和大家见面。

参考资料：http://en.opensuse.org/YaST/Web/
