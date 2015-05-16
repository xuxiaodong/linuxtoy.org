Title: VirtualBox 更新至 3.0.12
Date: 2009-11-18 10:39
Author: toy
Category: Apps
Tags: VirtualBox, VM
Slug: virtualbox-updated-to-3012

今天，Sun 将旗下的[开源虚拟机软件  
VirtualBox](http://linuxtoy.org/archives/virtualbox.html) 升级到了
3.0.12  
版本。该版本主要对之前版本中的缺陷进行了修正。

在 VirtualBox 3.0.12 中修正的缺陷包括：

* VMM: reduced IO-APIC overhead for 32 bits Windows NT/2000/XP/2003
guests; requires 64 bits support (VT-x only; bug #4392)  
* VMM: fixed double timer interrupt delivery on old Linux kernels
using IO-APIC (caused guest time to run at double speed; bug #3135)  
* VMM: reinitialize VT-x and AMD-V after host suspend or hibernate;
some BIOSes forget this (Windows hosts only; bug #5421)  
* VMM: fix loading of saved state when RAM preallocation is enabled  
* BIOS: ignore unknown shutdown codes instead of causing a guru
meditation (bug #5389)  
* GUI: never start a VM on a single click into the selector window
(bug #2676)  
* Serial: reduce the probability of lost bytes if the host end is
connected to a raw file  
* VMDK: fix handling of split image variants and fix a 3.0.10
regression (bug #5355)  
* VRDP: fixed occasional VRDP server crash  
* Network: even if the virtual network cable was disconnected, some
guests were able to send / receive packets (E1000; bug #5366)  
* Network: even if the virtual network cable was disconnected, the
PCNet card received some spurious packets which might confuse the guest
(bug #4496)  
* Shared folders: fixed changing case of file names (bug #2520)  
* Windows Additions: fix crash in seamless mode (contributed by
Huihong Luo)  
* Linux Additions: fix writing to files opened in O\_APPEND mode (bug
#3805)  
* Solaris Additions: fix regression in guest additions driver which
among other things caused lost guest property updates and periodic error
messages being written to the system log

详情可参阅
[ChangeLog](http://www.virtualbox.org/wiki/Changelog)。你可以从[这里下载
VirtualBox 3.0.12
的二进制包](http://download.virtualbox.org/virtualbox/3.0.12/)。
