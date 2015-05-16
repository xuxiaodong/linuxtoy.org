Title: Sun 发布 VirtualBox 2.1.0，新增 3D 加速特性
Date: 2008-12-18 09:20
Author: toy
Category: News
Tags: VirtualBox, VM
Slug: sun-releases-virtualbox-210

Sun 已经发布了旗下[开源虚拟机软件
VirtualBox](http://linuxtoy.org/archives/virtualbox.html) 的新版本
2.1.0，其中包含多项重要更新，如更好的 64 位支持、Mac
平台上的硬件虚拟化、3D 加速功能、更易设置的连网功能、VMDK/VHD
支持，等等。

以下为 VirtualBox 2.1.0 的 Changlog，供大家参考：

新特性

* Support for hardware virtualization (VT-x and AMD-V) on Mac OS X
hosts  
* Support for 64-bit guests on 32-bit host operating systems
(experimental; see user manual, chapter 1.6, 64-bit guests, page 16)  
* Added support for Intel Nehalem virtualization enhancements (EPT and
VPID; see user manual, chapter 1.2, Software vs. hardware virtualization
(VT-x and AMD-V), page 10))  
* Experimental 3D acceleration via OpenGL (see user manual, chapter
4.8, Hardware 3D acceleration (OpenGL), page 66)  
* Experimental LsiLogic and BusLogic SCSI controllers (see user
manual, chapter 5.1, Hard disk controllers: IDE, SATA (AHCI), SCSI, page
70)  
* Full VMDK/VHD support including snapshots (see user manual, chapter
5.2, Disk image ﬁles (VDI, VMDK, VHD), page 72)  
* New NAT engine with signiﬁcantly better performance, reliability and
ICMP echo (ping) support (bugs #1046, #2438, #2223, #1247)  
* New Host Interface Networking implementations for Windows and Linux
hosts with easier setup (replaces TUN/TAP on Linux and manual bridging
on Windows)

改进与 Bug 修正

* VMM: signiﬁcant performance improvements for VT-x (real mode
execution)  
* VMM: support for hardware breakpoints (VT-x and AMD-V only; bug
#477)  
* VMM: VGA performance improvements for VT-x and AMD-V  
* VMM: Solaris and OpenSolaris guest performance improvements for
AMD-V (Barcelona family CPUs only)  
* VMM: ﬁxed guru meditation while running the Dr. Web virus scanner
(software virtualization only; bug #1439)  
* VMM: deactivate VT-x and AMD-V when the host machine goes into
suspend mode; reactivate when the host machine resumes (Windows, Mac OS
X & Linux hosts; bug #1660)  
* VMM: ﬁxed guest hangs when restoring VT-x or AMD-V saved
states/snapshots  
* VMM: ﬁxed guru meditation when executing a one byte debug
instruction (VT-x only; bug #2617)  
* VMM: ﬁxed guru meditation for PAE guests on non-PAE hosts (VT-x)  
* VMM: disallow mixing of software and hardware virtualization
execution in general (bug #2404)  
* VMM: ﬁxed black screen when booting OS/2 1.x (AMD-V only)  
* GUI: pause running VMs when the host machine goes into suspend mode
(Windows & Mac OS X hosts)  
* GUI: resume previously paused VMs when the host machine resumes
after suspend (Windows & Mac OS X hosts)  
* GUI: save the state of running or paused VMs when the host machine’s
battery reaches critical level (Windows hosts)  
* GUI: properly restore the position of the selector window when
running on the compiz window manager  
* GUI: properly restore the VM in seamless mode (2.0 regression)  
* GUI: warn user about non optimal memory settings  
* GUI: structure operating system list according to family and version
for improved usability  
* GUI: predeﬁned settings for QNX guests  
* IDE: improved ATAPI passthrough support  
* Networking: added support for up to 8 Ethernet adapters per VM  
* Networking: ﬁxed issue where a VM could lose connectivity after a
reboot  
* iSCSI: allow snapshot/diff creation using local VDI ﬁle  
* iSCSI: improved interoperability with iSCSI targets  
* Graphics: ﬁxed handling of a guest video memory which is not a power
of two (bug #2724)  
* VBoxManage: ﬁxed bug which prevented setting up the serial port for
direct device access.  
* VBoxManage: added support for VMDK and VHD image creation  
* VBoxManage: added support for image conversion (VDI/VMDK/VHD/RAW)  
* Solaris hosts: added IPv6 support between host and guest when using
host interface networking  
* Mac OS X hosts: added ACPI host power status reporting  
* API: redesigned storage model with better generalization  
* API: allow attaching a hard disk to more than one VM at a time  
* API: added methods to return network conﬁguration information of the
host system  
* Shared Folders: performance and stability ﬁxes for Windows guests
(Microsoft Ofﬁce Applications)

[下载 VirtualBox 2.1.0 for
Linux](http://www.virtualbox.org/wiki/Linux_Downloads)。
