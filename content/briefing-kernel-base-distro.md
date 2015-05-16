Title: 短消息: Kernel Base Distro
Date: 2010-08-30 02:49
Author: lovenemesis
Category: News
Slug: briefing-kernel-base-distro

短消息数则，关于内核、基本系统和发行版及桌面环境。*感谢 Petty 来稿！*

*Linux内核*

最近一个月来有一些**改善桌面反应的补丁**提交到Linux内核，它们将在2.6.36以及之后的版本中被并入主线。消息来源：  
[Fixed: The Linux Desktop Responsiveness
Problem?](http://www.phoronix.com/scan.php?page=news_item&px=ODQ3Mw)  
[The Linux Desktop Responsiveness Patches Are Feeling
Good](http://www.phoronix.com/scan.php?page=news_item&px=ODQ3OQ)  
[More Patches To Improve Linux Desktop
Responsiveness](http://www.phoronix.com/scan.php?page=news_item&px=ODU0OQ)

2.6.36内核的**Direct Rendering Manager
(DRM)部分将加入一些有用的高级特性**，涉及到Intel、ATI、NVIDIA三家，同时Nouveau将加入Fermi（GTX
400s）的KMS支持。而发布已久的HD
5000s要到明年开源驱动支持才能初具规模，看来不仅NVIDIA的闭源驱动优于ATI，开源驱动也有后来居上的趋势。消息来源：  
[The Linux 2.6.36 Kernel Will Have Some Fun
DRM](http://www.phoronix.com/scan.php?page=news_item&px=ODQ3NQ)  
[Nouveau In Linux 2.6.36 Has NVIDIA Fermi
Mode-Setting](http://www.phoronix.com/scan.php?page=news_item&px=ODQ5MQ)

**AppArmor将进入2.6.36内核**，此项目与NSA的SELinux、NTT的TOMOYO以及Smack一样，是基于Linux
Security Modules
(LSM)内核接口的Linux内核模块，Ubuntu、OpenSUSE和Mandriva都在使用它。该项目原由SUSE发起，但现在是Canonical在资助，或许这可以缓解对于Ubuntu对于上游开发贡献不力的指责。消息来源：  
[AppArmor Is Going Into The Linux 2.6.36
Kernel](http://www.phoronix.com/scan.php?page=news_item&px=ODQ2Ng)

本月**2.6.36的RC1、RC2、RC3先后发布**，除上面已经提到的更新以外，可以肯定VIA's
graphics DRM和Reiser4 file-system将不会进入2.6.36。消息来源：  
[Linux 2.6.36-rc1 Kernel
Released](http://www.phoronix.com/scan.php?page=news_item&px=ODUxMA)  
[The Linux 2.6.36-rc2 Kernel Is Out With An
Announcement](http://www.phoronix.com/scan.php?page=news_item&px=ODUzNw)  
[Linux 2.6.36-rc3 Kernel
Released](http://www.phoronix.com/scan.php?page=news_item&px=ODU1NA)

**DisplayLink**——通过USB的显示设备接口的支持将进入2.6.37。消息来源：  
[DisplayLink Is Already Looking Towards Linux
2.6.37](http://www.phoronix.com/scan.php?page=news_item&px=ODUyMg)

*基础系统*

最近发现有一些**Windows商业程序的试用版会向MBR内写入数据**来防止盗版。这导致了Grub
2在内的一些引导程序被破坏。[消息来源](http://www.linuxtoday.com/developer/2010082900635NWUB)

**X的多点触摸支持**
[Canonical开发的多点触摸框架UTouch](http://www.phoronix.com/scan.php?page=news_item&px=ODUxMQ)最近[以X.Org
Gesture Extension
的名义提交到Xorg社区](http://www.phoronix.com/scan.php?page=news_item&px=ODUxMg)，但社区内为了手势识别是在服务端完成还是在客户端完成发生了争吵。Canonical的设计是在服务端完成，但包括Kristian
Høgsberg和MPX（[X的多点触摸协议](http://www.phoronix.com/scan.php?page=news_item&px=ODQ4MQ)）
的作者Peter
Hutterer在内的社区大佬则希望在客户端完成。Canonical的代表Chase
Douglas则对他们提出的理由[予以了反驳](http://lists.x.org/archives/xorg-devel/2010-August/012378.html)。  

[目前双方对此仍僵持不下](http://www.phoronix.com/scan.php?page=news_item&px=ODU1MQ)。

*发行版及桌面环境*

**Kontact 和 Akonadi** 预计将在KDE
4.5.X中合并。[消息来源](http://dot.kde.org/2010/08/26/akonadi-demystified)

**Btrfs不会成为Ubuntu 10.10的默认文件系统**，也不会出现在Live
CD的安装工具里，但将会出现在Alternate
CD中。[消息来源](http://www.phoronix.com/scan.php?page=article&item=ubuntu_1010_btrfs&num=1)
