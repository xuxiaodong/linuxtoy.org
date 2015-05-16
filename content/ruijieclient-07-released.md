Title: Ruijieclient 0.7 发布
Date: 2009-06-17 16:44
Author: lovenemesis
Category: Network
Tags: ruijie
Slug: ruijieclient-07-released

锐捷网络设备被广泛应用于中国大学，RuijieClient
是一个用于锐捷802.1x网络的认证客户端，适用于包括Linux在内的UNIX体系下的操作系统。发布于LGPL。

我们很荣幸地宣布RuijieClient新版本发布，这个版本的性能、易用性、可移植性和先前的版本相比都有了很大的提升。值得一提的是，在项目开发团队中的新进2位成员的努力下，RuijieClient已经被移植到家用的路由器上（安装的是openwrt），这意味着什么？想用的话就请低调！

特别要感谢的是经验丰富的MicroCai同学，他为新版本的发布做出了巨大贡献，几乎重写代码。sthots同学主要负责了路由器上的编译移植。

rpm, deb, 源码包可以到官方站点下载。spec 和debian
打包配置在SVN仓库中已经写好。

**主要功能**

1. 支持静态认证和3种DHCP认证  
2. 支持2种服务器发现包  
3. 支持客户端版本欺骗  
4. 支持伪造IP  
5. 支持智能重连  
6. 支持后台daemon驻留，可以加入Linux启动脚本  
7. 支持服务器消息读取和转码  
8. 良好的嵌入式移植特性  
9. 支持2种文件配置和命令行传参配置

**自从 version 0.1后的主要变化:**

version 0.7.0  
NEW: 支持ini文件（用于移植到嵌入式设备）  
NEW: 内置ICMP测试网络连通性（可以自定义测试地址，或者自动测试网关）  
NEW: 断网后自动重连  
NEW: 支持3种 DHCP认证模式（BETA）  
NEW:
可以在后台以daemon形式驻留，并且被作为默认启动方式（这意味着可以被加到开机启动脚本）  
NEW: 添加强大的命令行参数解析（详情见'ruijieclient --help'）  
CHG: 新的收/发包结构，更方便开发人员使用  
DEL: 去除了libnet依赖  
DEL: 去除了openssl依赖

站点地址：<http://ruijieclient.googlecode.com/>

安装配置指南：[http://code.google.com/p/ruijieclien...llAndConfigure](http://ruijieclient.googlecode.com/)

下载地址：[http://code.google.com/p/ruijieclient/downloads/list](http://ruijieclient.googlecode.com/)
