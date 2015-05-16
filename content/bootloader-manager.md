Title: Bootloader Manager — 图形化的引导管理器
Date: 2007-08-20 14:30
Author: toy
Category: Apps
Slug: bootloader-manager

[Bootloader Manager](https://launchpad.net/ubuntu-bootloader-manager/)
是使用 Python 语言编写的 GRUB
前端，它为普通用户提供图形化的方式来设置操作系统的引导次序、定制外观、以及完成其他的配置。虽然目前宣称是为
Ubuntu 系统而开发，但应该也能用于其他的 Linux 发行版。

[![Bootloader
Manager](http://i.linuxtoy.org/i/2007/08/bootloader-manager_s.png)](http://i.linuxtoy.org/i/2007/08/bootloader-manager.png)

*Screenshot via [Pensées de
LaserJock](http://laserjock.wordpress.com/2007/08/18/gsoc-ubuntu-bootloader-manager-02/)*

需要提请注意的是，此工具现在还处于早期的开发阶段，可能存在潜在的风险，在使用时要作好重要文件的备份。[Bootloader
Manager
的源代码](https://code.launchpad.net/ubuntu-bootloader-manager/)可从这里获取。在获取源代码时，你需要使用
Bazaar 版本控制系统工具，之后可以通过执行 `python setup.py install`
来完成安装。
