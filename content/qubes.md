Title: 最具有安全特色的系统－Qubes
Date: 2010-04-25 09:18
Author: toy
Category: Distros
Tags: Qubes
Slug: qubes

{ 撰文/linooxlee }

[Qubes](http://qubes-os.org/)  
是一个开源操作系统，旨在为桌面计算提供强有力的安全保障。Qubes 以 Xen、X
Window  
系统和 Linux 为基础，大多数 Linux 应用软件和 Linux  
驱动可以直接在其上运行。

[![qubes](http://i.linuxtoy.org/images/2010/04/thumb-qubes.png)](http://i.linuxtoy.org/images/2010/04/qubes.png)

Qubes 采取隔离的办法实现系统安全。Qubes
让每个（组）应用软件在各自的轻量级虚拟机（VM）中运行，许多系统级的组件如网络或存储子系统也是在沙盘中运行，这样的隔离手段有效地保证了系统的安全。同时
Qubes
对各个隔离的应用支持安全的复制和粘贴、文件共享等功能，使得它们各自独立又能协同工作。

Qubes
在系统运行效率、界面和操作的一致性和系统的完整性下了功夫，使得安全与性都能得到保证，特别是系统浑然一体（并非只是视觉上）这是
vbox 之类的虚拟机所不可比的。

日前 Qubes 发布了它的第一个版本，虽然是 alpha 版但已经运行良好。Qubes  
的截图见[这里](http://qubes-os.org/Screenshots.html)。需要安装 Qubes  
的朋友可以[参考这里](http://qubes-os.org/trac/)。

{ Thanks linooxlee. }
