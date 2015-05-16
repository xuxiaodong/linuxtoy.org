Title: VirtualBox 更新到 3.0.2
Date: 2009-07-11 09:36
Author: toy
Category: Apps
Tags: VirtualBox, VM
Slug: virtualbox-updated-to-302

Sun 在今天将 VirtualBox 更新到了 3.0.2
版本。[VirtualBox](http://linuxtoy.org/archives/virtualbox.html)
是一个开源、跨平台的虚拟机软件，新的 3.0.2 版主要修正了
[3.0](http://linuxtoy.org/archives/virtualbox-30-released.html)
中的缺陷和回归问题。

参阅 VirtualBox 3.0.2
[Changelog](http://www.virtualbox.org/wiki/Changelog)：

* VMM: fixed network regressions (guest hangs during network IO) (bug
#4343)  
* VMM: guest SMP performance improvements  
* VMM: fixed hangs and poor performance with Kaspersky Internet
Security (VT-x/AMD-V only; bug #1778)  
* VMM: fixed crashes when executing certain Linux guests (software
virtualization only; bugs #2696 & #3868)  
* ACPI: fixed Windows 2000 kernel hangs with IO-APIC enabled (bug
#4348)  
* APIC: fixed high idle load for certain Linux guests (3.0
regression)  
* BIOS: properly handle Ctrl-Alt-Del in real mode  
* iSCSI: fixed configuration parsing (bug #4236)  
* OVF: fix potential confusion when exporting networks  
* OVF: compatibility fix (bug #4452)  
* NAT: fixed crashes under certain circumstances (bug #4330)  
* 3D support: fixed dynamic linking on Solaris/OpenSolaris guests (bug
#4399)  
* 3D support: fixed incorrect context/window tracking for
multithreaded apps  
* Shared Folders: fixed loading from saved state (bug #1595)  
* Shared Folders: host file permissions set to 0400 with Windows guest
(bug #4381)  
* X11 host and guest clipboard: fixed a number of issues, including
bug #4380 and #4344  
* X11 Additions: fixed some issues with seamless windows in X11 guests
(bug #3727)  
* Windows Additions: added VBoxServiceNT for NT4 guests (for time
synchronization and guest properties)  
* Windows Additions: fixed version lookup  
* Linux hosts: workaround for buggy graphics drivers showing a black
VM window on recent distributions (bug #4335)  
* Linux hosts: fixed typo in kernel module startup script (bug
#4388)  
* Installer: support Pardus Linux  
* Solaris hosts: several installer fixes  
* Solaris host: fixed a preemption issue causing VMs to never start on
Solaris 10 (bug #4328).  
* Solaris guest: fixed mouse integration for OpenSolaris 2009.06 (bug
#4365)  
* Windows hosts: fixed high CPU usage after resuming the host (bug
#2978)  
* OVF: accept ovf:/disk/ specifiers with a single slash in addition to
ovf://disk/ (bug #4452)  
* Fixed a settings file conversion bug which sometimes caused hardware
acceleration to be enabled for virtual machines that had no explicit
configuration in the XML.

你可以从这里[下载 Virtualbox
3.0.2](http://download.virtualbox.org/virtualbox/3.0.2/)。
