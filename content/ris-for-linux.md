Title: RIS for Linux：通过 PXE 安装 Windows 
Date: 2008-08-29 11:18
Author: hmy
Category: Apps
Slug: ris-for-linux

[撰文/hmy]

光驱是易损坏的，所以很多没有光驱的人要重装 Windows
是很痛苦的。我们知道，Linux 可以方便的通过网络安装系统。其实 Windows
也是可以通过 PXE
安装系统。适用于没有光驱，但是支持网卡启动的机器。另外需要一台 Linux
机器配置好环境。

原理是在 Linux 上配置一个 PXE 环境，供需要装 Windows
的机器从网卡启动。Windows 启动后通过 DHCP 配置好网络，然后通过网络从
Linux 机器上下载 Windows 安装程序，开始安装过程。

我用这个方法成功安装过 Win2000 和 Win2003。

这里是说明文档：<http://oss.netfarm.it/guides/pxe.php>
