Title: VirtualBox 1.6.4 发布
Date: 2008-08-02 08:48
Author: toy
Category: Apps
Tags: VirtualBox, VM
Slug: virtualbox-164-released

[虚拟机软件 VirtualBox](http://linuxtoy.org/archives/virtualbox.html)
已经发布了 1.6.4 版。这是一个维护版，主要将 rdesktop 客户端更新到了
1.6.0、改进了 NLS、添加了 SMBIOS header 以使 Solaris 和 Vista 识别 DMI
数据、兼容于 Linux 内核 2.6.27、以及修订了大量 bug。

下面引用官方的更新记录，供大家参考：

> * AMD-V, VT-x: stability fixes  
>  * Shared Folders: fixed host crash (Solaris host only, bugs #1336,
> #1646)  
>  * Shared Folders: fixed BSOD when debugging with Visual Studio (bug
> #1627)  
>  * Shared Folders: fixed BSOD when compiling on a shared folder (bug
> #1683)  
>  * Shared Folders: several fixes/stability improvements  
>  * SATA: fixed a race that could cause an occasional Windows guest
> system hang  
>  * SATA: fixed spurious BIOS log messages  
>  * Networking: fixed NIC tracing with NAT interfaces (bug #1790)  
>  * USB: fixed crash under certain conditions when unplugging a USB
> device (bug #1295)  
>  * Settings: fixed bug when converting 1.5.x settings  
>  * RDP: fixed enabling the RDP server during runtime  
>  * RDP: properly detect the rdesktop 1.6.0 RDP client  
>  * RDP: fixed RDP crash (bug #1521)  
>  * RDP: updated modified rdesktop client to version 1.6.0  
>  * GUI: NLS improvements  
>  * BIOS: added SMBIOS header to make Solaris and Vista recognize the
> DMI data  
>  * ACPI: properly hide a disabled floppy controller  
>  * VMM: small fixes to protected mode without paging  
>  * VMDK: fixed handling of .vmdk images without UUIDs  
>  * Windows hosts: fixed driver parameter validation issue in
> VBoxDrv.sys that could allow an attacker on the host to crash the
> system  
>  * Windows hosts: installer now contains web service examples
> mentioned in the manual  
>  * Linux hosts: properly deregister the Linux kernel module before
> uninstalling a Linux deb/rpm package  
>  * Linux hosts: kernel module works now with Linux 2.6.27  
>  * Linux hosts: fixed a typo in the vboxnet setup script for host
> network interfaces (bug #1714)  
>  * Linux hosts: fixed usage of tar in installer (bug #1767)  
>  * Linux hosts: fixed long guest shutdown time when serial port is
> enabled  
>  * Solaris hosts: refuse to install in Sun xVM hypervisor dom0  
>  * Solaris hosts: accept Solaris raw disks when for raw disk access  
>  * Windows additions: made installation of shared folders more
> robust  
>  * Windows additions: improved installation  
>  * Linux additions: accept every user-defined guest video mode in
> /etc/X11/xorg.conf  
>  * Linux additions: fixed startup order for recent Linux
> distributions (e.g. openSUSE 11)

[下载 VirtualBox
1.6.4](https://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_SMI-Site/en_US/-/USD/ViewProductDetail-Start?ProductRef=innotek-1.6-G-F@CDS-CDS_SMI)。

[感谢 yu 朋友提示]
