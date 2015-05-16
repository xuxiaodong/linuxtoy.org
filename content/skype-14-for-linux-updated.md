Title: Skype 1.4 for Linux 获得更新
Date: 2007-05-24 14:08
Author: toy
Category: Apps
Slug: skype-14-for-linux-updated

[Skype for Linux 的 1.4
版](https://developer.skype.com/LinuxSkype)获得了小幅更新，其版本号已从
1.4.0.58 变成了 1.4.0.64。不过，它依然没有摆脱 Alpha
状态。之前在上一个版本中暂时去掉的创建新用户、图释表情支持等功能又回来了。当然，这个版本也免不了进行一些除错工作。

[![Skype](http://i.linuxtoy.org/i/2007/05/skype-about_s.png)](http://i.linuxtoy.org/i/2007/05/skype-about.png)  
*Skype 1.4.0.64 Alpha*

我在启动这个版本时，出现了一点小纰漏，它提示说 libdbus-1.so.2
文件无法被找到并加载。此问题可以通过将 /usr/lib/ 中的类似文件（我这里是
libdbus-1.so.3.2.0）做一个链接来解决。

- [Download Skype for Linux 1.4.0.64
Alpha](https://developer.skype.com/LinuxSkype#head-4a6331c0a4169dd1d5a2d316916d25512dd26a61)
