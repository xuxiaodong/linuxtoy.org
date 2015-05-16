Title: 快速重装软件的技巧
Date: 2006-08-25 16:39
Author: toy
Category: Tutorials
Slug: reinstallation_software_tip

我们每个人都有过重装系统的经历，在安装好系统之后，如何才能快速重装原来那些自己所钟爱的软件？[nixCraft](http://www.cyberciti.biz/tips/linux-get-list-installed-software-reinstallation-restore.html)
提供了一个有用的技巧。它的原理是在系统完好无损的时候，就做好已安装软件的备份工作。然后，在重装系统后，就可以利用先前备份的文档来执行还原操作了。下面是相关的实施步骤（以
Debian 为例）：

1.  执行备份操作：`dpkg --get-selections > installed-software.log`，这将当前系统中已安装的软件保存到
    installed-software.log 中。
2.  在还原时使用 `dpkg --set-selections < installed-software.log`
    导入软件列表，再利用 `dselect` 工具安装软件。

上述方法同样适用于 Ubuntu。另外，原文也介绍了基于 RPM
包管理器的发行版如何执行的步骤，有兴趣的可以直接去看。

（Via [nixCraft](http://www.cyberciti.biz), thanks!）
