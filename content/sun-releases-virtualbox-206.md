Title: Sun 推出 VirtualBox 2.0.6 Bug 修订版
Date: 2008-11-24 11:43
Author: toy
Category: News
Tags: VirtualBox, VM
Slug: sun-releases-virtualbox-206

几天前，Sun 推出了[虚拟机软件
VirtualBox](http://linuxtoy.org/archives/virtualbox.html) 的更新版
2.0.6。这是一个 bug 修订版，改善了 SATA 的性能、修正了 USB 对 iPhone 及
Nokia 设备的支持等等，详细列表可见如下 Changelog。

> * VMM: ﬁxed Guru meditation when running 64 bits Windows guests (bug
> #2220)  
>  * VMM: ﬁxed Solaris 10U6 boot hangs (VT-x and AMD-V) bug #2220)  
>  * VMM: ﬁxed Solaris 10U6 reboot hangs (AMD-V only; bug #2220)  
>  * GUI: the host key was sometimes not properly displayed (Windows
> hosts only, bug #1996)  
>  * GUI: the keyboard focus was lost after minimizing and restoring
> the VM window via the Windows taskbar (bugs #784)  
>  * VBoxManage: properly show SATA disks when showing the VM
> information (bug #2624)  
>  * SATA: ﬁxed access if the buffer size is not sector-aligned (bug
> #2024)  
>  * SATA: improved performance  
>  * SATA: ﬁxed snapshot function with ports>1 (bug #2510)  
>  * E1000: ﬁxed crash under rare circumstances  
>  * USB: ﬁxed support for iPhone and Nokia devices (Linux host: bugs
> #470 & #491)  
>  * Windows host installer: added proper handling of open VirtualBox
> applications when updating the installation  
>  * Windows host installer: ﬁxed default installation directory on
> 64-bit on new installations  
>  * Windows host installer: added proper handling of open VirtualBox
> applications when updating the installation  
>  * Linux/Solaris/Darwin hosts: verify permissions in
> /tmp/vbox-$USER-ipc  
>  * Linux hosts: ﬁxed assertion on high network load (AMD64 hosts, ﬁx
> for Linux distributions with glibc 2.6 and newer (bug #616)  
>  * Linux hosts: don’t crash during shutdown with serial ports
> connected to a host device  
>  * Solaris hosts: ﬁxed incompatibility between IPSEC and host
> interface networking  
>  * Solaris hosts: ﬁxed a rare race condition while powering off VMs
> with host interface networking  
>  * Solaris hosts: ﬁxed VBoxSDL on Solaris 10 by shipping the required
> SDL library (bug #2475)  
>  * Windows additions: ﬁxed logged in users reporting via guest
> properties when using native RDP connections  
>  * Windows additions: ﬁxed Vista crashes when accessing shared
> folders under certain circumstances (bug #2461)  
>  * Windows additions: ﬁxed shared folders access with MS-Ofﬁce (bug
> #2591)  
>  * Linux additions: ﬁxed compilation of vboxvfs.ko for 64-bit guests
> (bug #2550)  
>  * SDK: added JAX-WS port caching to speedup connections

VirtualBox 2.0.6 for Linux
可从[这里下载](http://www.virtualbox.org/wiki/Linux_Downloads)。
