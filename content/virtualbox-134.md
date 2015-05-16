Title: VirtualBox 1.3.4
Date: 2007-02-12 21:41
Author: toy
Category: Apps
Slug: virtualbox-134

InnoTek 公司在今天宣布了旗下的虚拟软件
[VirtualBox](http://www.virtualbox.org/) 1.3.4
发布的消息。据了解，这是一次非常重要的更新。大量来自 VirtualBox
用户社区的反馈，大约超过 800 个的改进被整合到了新的版本中。同时，InnoTek
也同意了 Ubuntu 官方打算把 VirtualBox 整合到 Ubuntu 7.04 ("Feisty Fawn")
的请求。

以下是来自 VirtualBox 1.3.4 的更改列表，可供参考：

> * General: fixed unresolved symbol issue on Windows 2000 hosts  
>  * General: added warnings at VirtualBox startup when there is no
> valid Linux kernel module  
>  * General: fixed problem with unrecognized host CDROM/DVD drives on
> Linux  
>  * General: fixed compatibility issue with SELinux  
>  * GUI: improved USB user interface, easier filter definitions, menu
> to directly attach specific devices  
>  * GUI: added VM settings options for VRDP  
>  * GUI: fixed GDI handle leak on Windows hosts  
>  * GUI: worked around issue in the Metacity window manager (GNOME)
> leading to unmovable VM windows  
>  * GUI: show an information dialog before entering fullscreen mode
> about how to get back  
>  * GUI: several fixes and improvements  
>  * VMM: fixed occasional crashes when shutting down a Windows guest  
>  * VMM: fixed crash while loading Xorg on openSUSE 10.2  
>  * VMM: fixed problems with OpenBSD 3.9 and 4.0  
>  * VMM: fixed crash while loading XFree86 in SUSE 9.1  
>  * VMM: fixed Debian 3.1 (Sarge) installation problem (network
> failure)  
>  * VMM: fixed crash during SUSE 10.2 installation  
>  * VMM: fixed crash during Ubuntu 7.04 RC boot  
>  * VMM: fixed crash during ThinClientOS (Linux 2.4.33) bootup  
>  * ATA/IDE: pause VM when host disk is full and display message  
>  * ATA/IDE: fixed incompatibility with OpenSolaris 10  
>  * VDI containers: do not allocate blocks when guest only writes
> zeros to it (size optimization when zeroing freespace prior to
> compacting)  
>  * CDROM/DVD: fixed media recognition by Linux guests  
>  * Network: corrected reporting of physical interfaces (fixes Linux
> guest warnings)  
>  * Network: fixed IRQ conflict causing occassional major slowdowns
> with XP guests  
>  * Network: significantly improved send performance  
>  * Audio: added mixer support to the AC'97 codec (master volume
> only)  
>  * Audio: added support for ALSA on Linux (native, no OSS emulation)  
>  * iSCSI: improved LUN handling  
>  * iSCSI: fixed hang due to packet overflow  
>  * iSCSI: pause VM on iSCSI connection loss  
>  * Linux module: never fail unloading the module (blocks
> Ubuntu/Debian uninstall)  
>  * Linux module: improved compatibility with NMI watchdog enabled  
>  * Windows Additions: fixed hardware mouse pointer with Windows 2003
> Server guests  
>  * Linux Additions: compile everything from sources instead of using
> precompiled objects  
>  * Linux Additions: better compatibility with older glibc versions  
>  * Linux Additions: when uninstalling, only delete the files we put
> there during installation, don't remove the directory recursively to
> prevent unwanted data loss  
>  * Linux Installer: added support for Slackware  
>  * Linux Additions: added support for Linux 2.4.28 to 2.4.34  
>  * RDP: fixed sporadic disconnects with MS RDP clients  
>  * RDP: fixed race condition during resolution resize leading to rare
> crashes

Download [VirtualBox 1.3.4](http://www.virtualbox.org/wiki/Downloads)

(Thanks MKB!)
