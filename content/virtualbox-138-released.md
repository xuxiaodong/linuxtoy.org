Title: VirtualBox 1.3.8 发布
Date: 2007-03-18 19:15
Author: toy
Category: Apps
Slug: virtualbox-138-released

InnoTek 在几天前发布了一个 [VirtualBox](http://www.virtualbox.org/)
的维护更新版 1.3.8。该版本包括许多改善和修正，且针对 Red Hat Enterprise
Linux 4 (RHEL4) 和 Mandriva 2007.1 提供了专用的安装包。

VirtualBox 1.3.8 的更改情况如下（引用自官方）：

> * Windows installer: fixed installation problem if UAC is active  
>  * Linux installer: added RPM for rhel4 and Mandriva 2007.1  
>  * Linux installer: remove any old vboxdrv modules in
> /lib/modules/*/misc  
>  * Linux installer: many small improvements for .deb and .rpm
> packages  
>  * Linux installer: improved setup of kernel module  
>  * GUI: Host-Fn sends Ctrl-Alt-Fn to the guest (Linux guest VT
> switch)  
>  * GUI: fixed setting for Internal Networking  
>  * GUI: show correct audio backend on Windows (dsound)  
>  * GUI: improved error messages if the kernel module is not
> accessible  
>  * GUI: never fail to start the GUI if the kernel module is not
> accessible  
>  * VMM: fixed occasional crashes when shutting down Windows TAP
> device  
>  * VMM: fixed issues with IBM's 1.4.2 JVM in Linux guests  
>  * RDP: fixed color encoding with 24bpp  
>  * BIOS: zero main memory on reboot  
>  * BIOS: added release logging  
>  * USB: fixed parsing of certain devices to prevent VBoxSVC crashes  
>  * USB: properly wakeup suspended ports  
>  * USB: fixed a problem with unplugged USB devices during suspend  
>  * Audio: fixed crashes on Vista hosts  
>  * NAT: allow configuration of incoming connections (aka port
> mapping)  
>  * Network: hard reset network device on reboot  
>  * iSCSI: fixed a hang of unpaused VMs accessing unresponsive iSCSI
> disks  
>  * Linux Additions: support Xorg 7.2.x  
>  * Linux Additions: fixed default video mode if all other modes are
> invalid  
>  * Linux Additions: set default DPI to 100,100  
>  * Linux Additions: fixed initialization of video driver on X server
> reset

Download [VirtualBox 1.3.8](http://www.virtualbox.org/wiki/Downloads)
