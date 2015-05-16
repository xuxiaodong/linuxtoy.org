Title: 短消息: Virtualbox Kernel ethX
Date: 2010-12-07 22:17
Author: lovenemesis
Category: Tools
Tags: eth, Kernel, VirtualBox
Slug: briefin-virtualbox-kernel-ethx

**Virtualbox 4.X** 发布首个 Beta；**Kernel 2.6.37-rc5** 发布;
**网卡的命名规则**将在 Fedora 15 中改变。

来自 Oracle 的虚拟化产品 VirtualBox 发布 4.0.0 Beta 1 版本，带来 OVA
(Open Virtualization Format Archive) 支持，Java 语言绑定，**虚拟机 CPU
和 I/O 占有率限制**，**VDI/VHD
镜像大小缩放**等功能。更多内容请参考[本站深入报道](http://linuxtoy.org/archives/virtualbox-400-beta-1-%E5%8F%91%E5%B8%83.html)。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=ODg3Ng)

Linux 内核 2.6.37-rc5 发布，主要集中在 config 的配置文件的清理，同时对于
NFS readdir
的错误修复也在计划中。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=ODg3OA)

计划在 Fedora 15中实现的新功能将使网卡的命名方式从难以区分的 ethX
风格转而通过 **biosdevname** 的方式：

-   主板集成网卡： *em<port\_number>*
-   PCI网卡：*pci<slot\_number>#<port\_number>*
-   虚拟网卡：添加后缀 *\_<virtual\_instance>*

提倡者 Matt Domsch
希望借此解决系统管理员“猜网卡”的苦恼。[消息来源](http://fedoranext.wordpress.com/2010/12/07/a-lesson-in-persistency/)
