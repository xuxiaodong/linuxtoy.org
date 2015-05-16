Title: VirtualBox 2.2.0 发布
Date: 2009-04-09 09:48
Author: toy
Category: Apps
Tags: VirtualBox, VM
Slug: virtualbox-220-released

在经过两个 [Beta
测试版](http://linuxtoy.org/archives/virtualbox-22-beta-1.html)后，Sun
最终在今天发布了[开源虚拟机软件
VirtualBox](http://linuxtoy.org/archives/virtualbox.html) 的 2.2.0
正式版本。作为一个重要更新版本，VirtualBox 2.2.0
包含许多改进，比如：支持 OVF 应用、针对 Linux/Solaris 客户机的 3D
加速、每个虚拟机支持内存达 16 GB，等等。

以下为 VirtualBox 2.2.0 添加的主要特性：

* OVF (Open Virtualization Format) appliance import and export  
* Host-only networking mode  
* Hypervisor optimizations with significant performance gains for high
context switching rates  
* Raised the memory limit for VMs on 64-bit hosts to 16GB  
* VT-x/AMD-V are enabled by default for newly created virtual
machines  
* USB (OHCI & EHCI) is enabled by default for newly created virtual
machines (Qt GUI only)  
* Experimental USB support for OpenSolaris hosts  
* Shared folders for Solaris and OpenSolaris guests  
* OpenGL 3D acceleration for Linux and Solaris guests  
* Added C API in addition to C++, Java, Python and Web Services

完整的更改情况，你可以查看 [VirtualBox 2.2.0
Changelog](http://www.virtualbox.org/wiki/Changelog)。

VirtualBox 2.2.0 的源代码及二进制包可从以下地址下载。

[VirtualBox](http://www.virtualbox.org/wiki/Downloads)

{ 感谢 matri 同学提示 }
