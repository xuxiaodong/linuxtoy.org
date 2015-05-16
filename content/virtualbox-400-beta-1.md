Title: VirtualBox 4.0.0 Beta 1 发布
Date: 2010-12-07 22:31
Author: liangsuilong
Category: Apps
Tags: VirtualBox
Slug: virtualbox-400-beta-1

开源虚拟化解决方案 VirtualBox 发布了下一代 4.0.0 的第一个测试版本。  

该版本为重大更新版本，引入了众多新特性：

-   USB 2.0 EHCI 控制器和 RDP 服务器移入到 Extension
    Pack，不再包含在发布版本当中，保证了 VirtualBox
    是完全的开源软件。USB 1.1 OHCI
    控制器一直是核心部件，两者的区别在于传输速度。（使用打印机和网银 USB
    key 需要注意。）
-   全新设计的用户界面，增加了 NAT 端口转发的 GUI 设置界面。
-   增加 Open Virtualization Format Archive （OVA 格式）的支持。
-   支持在 32bit host 上的虚拟机使用 1.5GB/2GB 内存。
-   增加 ICH9 的 3 个 PCI 设备的支持。
-   支持虚拟机使用 Intel HD Audio 音频设备。（Windows 7 Guest
    不再需要额外找 Realtek AC97 驱动。）
-   增加 iSCSI、VMDK、VHD 和 Parallels 镜像的异步 I/O 特性；允许 VHD 和
    VDI 的大小缩放。
-   增加自动更新 Guest Addition 功能
-   引入 copy-and-paste 的特性。
-   编程语言：API 增加标准 Java 语言的本地和远程的支持。
-   增加 Scale Mode 适应分辨率不高的全屏程序。

<div>

PS：早前言之确凿的 WDDM 支持，也就是 Vista/Win7 的 Aero
特效，将不会包含在 VirtualBox 4.0
的计划内，最快要等到下一个重大更新版本中。

</div>

<div>

[完整的
Changelog](http://forums.virtualbox.org/viewtopic.php?f=15&t=36748)
[下载地址](http://download.virtualbox.org/virtualbox/4.0.0_BETA1/)

</div>

<div>

[![](http://linuxtoy.org/img/2010/12/virtualbox.png)](http://linuxtoy.org/img/2010/12/virtualbox.png)

</div>
