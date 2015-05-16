Title: Ubuntu Dapper 用户暂时不要升级 xserver-xorg-core
Date: 2006-08-22 18:07
Author: toy
Category: Tutorials
Slug: do_not_upgrade_ubuntu

Ubuntu Demon 在他的 Blog 中提醒用户，暂时不要升级 Ubuntu
Dapper，因为其中所包含的 xserver-xorg-core version 1:1.0.2-0ubuntu10.3
已经损坏。如果你已经升过级了，那么可以通过以下步骤解决：

1.  sudo apt-get install xserver-xorg-core=1:1.0.2-0ubuntu10
2.  sudo reboot

更新，目前 Ubuntu 源中的 xserver-xorg-core 已经更新到
1:1.0.2-0ubuntu10.4，解决了其中的 bug，大家可放心升级。

（Via [Ubuntu Demon’s
blog](http://ubuntudemon.wordpress.com/2006/08/22/latest-dapper-xserver-xorg-upgrade-might-break-the-xserver/)）
