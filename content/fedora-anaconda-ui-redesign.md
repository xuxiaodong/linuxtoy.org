Title: Fedora Anaconda 安装器新 UI
Date: 2011-06-18 10:56
Author: lovenemesis
Category: News
Tags: anaconda, Fedora
Slug: fedora-anaconda-ui-redesign

Fedora UX MM [Máirín Duffy
最近在她的博客](http://mairin.wordpress.com/2011/06/16/making-fedora-easier-to-use-the-installer-ux-redesign/)上分享了对于
Fedora Anaconda 安装器的 UI 新设计，**计划在 Fedora 17 时实现**。

[![](http://linuxtoy.org/img/2011/06/anaconda-2hub-overview.png "anaconda-2hub-overview")](http://linuxtoy.org/img/2011/06/anaconda-2hub-overview.png)

新流程预览。从中可以看出新的安装流程由三大部分组成，第一部分毫无例外的是**语言选择**。

[![](http://linuxtoy.org/img/2011/06/hub1.png "hub1")](http://linuxtoy.org/img/2011/06/hub1.png)

第二部分为**安装概要**。这里罗列了所有需要在真正安装过程开始前需要配置的信息，如果需要更改的话可以点击弹出选择菜单。设计要点是尽量多的检测出符合当前安装硬件系统的默认设置，减少用户需要手动调整的机会。这样子用户就可以直接点击下一步开始安装了。

这一步里，用户也可以选择安装后自动重启计算机。

[![](http://linuxtoy.org/img/2011/06/hub2.png "hub2")](http://linuxtoy.org/img/2011/06/hub2.png)

第三部分为**安装和个性化**。此时往硬盘写入数据的过程已经开始了，**与此同时**，允许执行创建用户账户、设定同步选项和注册系统等其他工作。

当然，这只是目前的设计构想，还有一些问题尚未解决，比如默认何种安装目标设备和方式。如果用户反馈指出了此种设计的不足，会做出对应的修改的。

**PS：**这里有 [FUDCon 时针对 Fedora
安装过程的重构漫画说明](http://duffy.fedorapeople.org/app%20design/anaconda/comic/anaconda-comic_1.png)，和本文介绍的又是另一种风格。

**PSS：**[Mairin
在她的博客](http://mairin.wordpress.com/2011/06/16/making-fedora-easier-to-use-the-installer-ux-redesign/)中用大量篇幅阐述了
**Fedora
的理念**：传播自由软件文化；鼓励协作沟通；还予对内容和设备的控制权。
