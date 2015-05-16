Title: VirtualBox 更新到 1.5.6
Date: 2008-02-20 10:51
Author: toy
Category: Apps
Slug: virtualbox-updated-to-156

开源虚拟机软件
[VirtualBox](http://linuxtoy.org/archives/virtualbox.html) 已更新到了
1.5.6
版。其中，一些有意思的更改内容包括：修正了无缝模式和全屏模式的问题，改善了
Solaris 客户机的性能，支持只读共享文件夹，支持 E1000 设备模拟，与 Kernel
2.6.24 的兼容性更好，等等。

![VirtualBox](http://i.linuxtoy.org/i/2007/10/virtualbox.png)

VirtualBox 1.5.6 的完整更改记录如下：

* GUI: ﬁxed several error messages  
* GUI: ﬁxed registration dialog crashes once and for all  
* GUI: really ask before resetting the VM  
* GUI: release mouse and keyboard before the host activates the
screensaver  
* GUI: ﬁxed issue with license display on big screens  
* GUI: added setting for network name for internal networks  
* GUI: added setting for network device type  
* GUI: keyboard ﬁxes  
* GUI: seamless mode and fullscreen mode ﬁxes  
* GUI: ﬁxed soaked hostkey keyup event under certain conditions  
* GUI: more informative message dialog buttons  
* GUI: VM selector context menu  
* VBoxSDL: added -termacpi switch  
* VBoxSDL: ﬁxed automatic adaption of the guest screen resolution to
the size of the VM window  
* VMM: under heavy guest activity, for example when copying ﬁles
to/from a shared folder, the VM could crash with an assertion  
* VMM: added an option to select PIIX4 (improves compatibility with
Windows guests created by VMware)  
* VMM: ﬁxed a bug which could lead to memory corruption under rare
circumstances  
* VMM: improved performance of Solaris guests  
* VRDP: ﬁxed a 1.5.4 regression: VRDP client and server were
out-of-sync if the VM was started using the GUI  
* VRDP: proper error handling if the VRDP library could not be loaded  
* VBoxManage: ﬁxed crash during clonevdi  
* VBoxManage: added ’list runningvms’ command  
* VBoxManage: improved the compatibility when reading the partition
table of a raw disk  
* Shared Folders: added support for read-only shared folders  
* Shared Clipboard: several ﬁxes  
* Network: experimental support for E1000 device emulation  
* iSCSI: better check for misconﬁgured targets  
* iSCSI: allow to directly attach to internal networks with integrated
mini IP stack  
* PulseAudio: don’t hang during VM initialization if no sound server
is available  
* VDI: ﬁxed sized virtual disk images are now completely written
during creation to workaround buggy sparse ﬁle handling on some OS (e.g.
Vista)  
* VDI/VMDK: prevent indexing of .vdi and .vmdk ﬁles on Windows hosts  
* RDP: ﬁxed compilation of the Linux rdesktop client on newer Linux
kernels  
* RDP: install rdesktop-vrdp on Linux hosts  
* ACPI: added sleep button event  
* Serial: proper handling of inaccessible host devices  
* Windows installer: allow smooth upgrade without deinstallation  
* Linux installer: ﬁxed Slackware detection regression  
* Linux installer: updated VBoxTunctl allowing to assign a tap device
to a group on Linux kernels > 2.6.23  
* Windows additions: several ﬁxes, in particular for Windows NT4  
* Linux additions: ﬁxed installer for Kubuntu 8.04  
* Linux additions: add default video mode for handling video mode
hints from the host  
* Linux host: compatibility ﬁxes with Linux > 2.6.24

- [下载 VirtualBox 1.5.6](http://www.virtualbox.org/wiki/Downloads)
