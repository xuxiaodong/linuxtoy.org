Title: VirtualBox 1.4.0 发布
Date: 2007-06-06 20:26
Author: toy
Category: Apps
Slug: virtualbox-140-released

开放源码的 [VirtualBox](http://linuxtoy.org/tag/virtualbox)
虚拟机程序于日前发布了一个新的版本 1.4.0。这个版本相对于 VirtualBox
的发布历程而言，是一个十分重要的版本。之所以如此说，是因为新版本为用户带来了许多明显的改进。

[![VirtualBox](http://i.linuxtoy.org/i/2007/06/virtualbox_s.png)](http://i.linuxtoy.org/i/2007/06/virtualbox.png)

VirtualBox 1.4.0 的主要改进内容包括：

1.  完全支持 64 位 Linux 主机，RDP 会话重影，剪贴板同步，serial
    串口，以及更容易的网络接口等
2.  支持 VMware 磁盘映像 (VMDK)，并且虚拟机也能够访问物理磁盘和分区
3.  新的界面语言支持，包含简体/繁体中文等 12 种
4.  支持更多的 Linux 发行版本

VirtualBox 1.4.0 提供有 Debian、Ubuntu、Fedora、openSUSE、Mandriva、Red
Hat Enterprise Linux、Xandros Desktop 等 Linux 发行版本可用的包。

另外，基于 Debian 的 Linux 发行版也可以通过使用以下的源来安装
VirtualBox：  

` deb http://www.virtualbox.org/debian feisty non-free deb http://www.virtualbox.org/debian edgy non-free deb http://www.virtualbox.org/debian dapper non-free deb http://www.virtualbox.org/debian etch non-free deb http://www.virtualbox.org/debian sarge non-free deb http://www.virtualbox.org/debian xandros4.0-xn non-free`

请根据所用的 Linux 发行版选择对应的地址，并将其添加到
/etc/apt/sources.list
中。不要忘了添加密钥（可从[这里](http://www.virtualbox.org/debian/innotek.asc)获取）：  
`apt-key add innotek.asc`

- [Download VirtualBox 1.4.0](http://www.virtualbox.org/wiki/Downloads)
