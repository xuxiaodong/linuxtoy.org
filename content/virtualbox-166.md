Title: VirtualBox 发布 1.6.6 修订版
Date: 2008-09-03 18:53
Author: toy
Category: Apps
Tags: VirtualBox, VM
Slug: virtualbox-166

[VirtualBox](http://linuxtoy.org/archives/virtualbox.html)，一个跨平台的虚拟机软件。该软件于今日发布了一个
Bug 修订版本 1.6.6。VirtualBox 1.6.6
并没有添加任何新的功能，主要修正了过度生成日志、与 gcc-4.3 编译器及
Linux 内核 2.6.27 的兼容性、AMD-V 稳定性、剪贴板服务不启动等问题。

下面引用 VirtualBox 官方的更新日志，供大家参考：

> * VMM: ﬁxed excessive logging (bug #1901)  
>  * VMM: AMD-V stability ﬁxes (bug #1685)  
>  * GUI: added support for Ctrl+Caps reversed keyboards (bug #1891)  
>  * SATA: ﬁxed BSODs of Windows guests on a SATA disk (bug #1941)  
>  * SATA: ﬁxed hard disk detection on Solaris 10 U5 (bug #1789)  
>  * VBoxHeadless: don’t start the clipboard service (bug #1743)  
>  * VBoxHeadless: added -vrdp parameter which allows to start the VM
> session without VRDP (bug #1960)  
>  * VBoxManage: ﬁxes to creating raw disk/partition VMDK ﬁles, now
> accepts removable media on Windows (bug #1869)  
>  * VRDP: ﬁxed communication with MS Remote Resktop Connection on
> MacOS X (bug #1337)  
>  * VRDP: clipboard ﬁxes (bug #1410)  
>  * VRDP: ﬁxed crash during PAM authentication (bug #1953)  
>  * Shared Folders: ﬁxed a regression introduced in version 1.6.2: the
> shared folders service was sometimes not properly installed (Windows
> guests only, bug #1915)  
>  * Shared Folders: don’t deny to load a VM if a shared folder is not
> accessible (bug #822)  
>  * BIOS: allow to specify empty DMI strings (bug #1957)  
>  * OSE archive: added missing Makeﬁles (bug #1912)  
>  * Linux hosts: workaround for buggy gcc-4.3 compilers (e.g. openSUSE
> 11)  
>  * Linux hosts: one more ﬁx for compiling the kernel modules on Linux
> 2.6.27 (bug #1962)  
>  * MacOS X hosts: shared folders unicode ﬁx  
>  * Solaris hosts: ﬁxed link issue (bug #1840)  
>  * Windows additions: allow to downgrade the package  
>  * Windows additions: ﬁxed corrupted installer icon on Windows 2000
> (bug #1486)  
>  * Windows additions: ﬁxed bug when creating intermediate directories
> (bug #1870)  
>  * Windows additions: implemented /xres=, /yres= and /depth= switches
> for the installer (bug #1990)  
>  * Linux additions: properly unregister the misc device when
> unloading the kernel module  
>  * Linux additions: ﬁxed startup order for recent Linux distributions
> again (e.g. openSUSE 11)  
>  * Linux additions: attempt to ﬁx the autostart issue of !VBoxClient
> with Mandriva guests (bug #1699)  
>  * Linux additions: ﬁxed detection of patched Linux 2.6.18 kernels of
> RHEL5 / FC6 / CentOS 5.2 (bugs #1899, #1973)  
>  * Linux additions: added new mount ﬂags dmode, fmode, umask, dmask
> and fmask allowing to override the ﬁle mode (bug #1776)  
>  * Documentation: added a note that jumbo frames don’t work (bug
> #1877)  
>  * Documentation: document special host interface names on openSUSE11
> (bug #1892)

**参考**

1.  <http://www.virtualbox.org/wiki/Changelog>
2.  [下载 VirtualBox 1.6.6](http://www.virtualbox.org/wiki/Downloads)

