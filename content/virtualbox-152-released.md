Title: VirtualBox 已更新到 1.5.2 版
Date: 2007-10-19 09:10
Author: toy
Category: Apps
Slug: virtualbox-152-released

开源[虚拟机软件 VirtualBox](http://linuxtoy.org/search/virtualbox)
在昨日已更新到了 1.5.2 版。这只是一个 bug
修订版本，主要解决了在图形用户界面、BIOS、VGA、VMM、网络、以及 VRDP
等方面的问题。此外，VirtualBox 1.5.2 也包括些许改进，如改进了在 Linux
主机上的键盘处理、NLS、与 Linux KVM 的兼容性、MAC 地址处理，在 VM
关闭对话框中增加了 ACPI 关机选项，支持其他的 RDP 客户端，Linux
附加程序支持 X.org Server 1.4 等等。

![VirtualBox](http://i.linuxtoy.org/i/2007/10/virtualbox.png)

以下是引用自 VirtualBox 1.5.2 的完整更新记录，供大家参考：

- Windows Installer: fixed installation on Windows 2000 hosts  
- Windows Installer: proper warning when installing a 32-bit VirtualBox
version on 64-bit Windows and vice versa  
- Linux Installer: no longer require license acceptance during install,
instead at first GUI startup (addresses issues with hanging installer on
Debian based distributions)  
- GUI: added user registration dialog  
- GUI: fixed crashes on 64-bit Linux hosts  
- GUI: several fixes and improvements to seamless mode  
- GUI: fixed DirectDraw mode with certain video cards (e.g. Intel
i915)  
- GUI: fixed incorrect guest resolution after leaving fullscreen mode  
- GUI: improved keyboard handling on Linux host  
- GUI: show fatal VM aborts (aka "Guru Meditation")  
- GUI: fixed crashes due to a display update race condition on some
systems  
- GUI: added ACPI shutdown option to the VM close dialog  
- GUI: NLS improvements  
- BIOS: fixed floppy boot menu  
- BIOS: expose the VM UUID in the DMI/SMBIOS area  
- VGA: fixed CGA video modes  
- VGA: fixed 8-bit DAC handling (Solaris setup)  
- VMM: fixed issue with VT-x on Windows 64-bit hosts  
- VMM: improved compatibility with Linux KVM  
- VMM: fixed issues with Fedora 8 guests  
- VMM: fixed fatal errors while installing Windows guests when using
AMD-V  
- VMM: fixed sporadic hangs when minimizing VM window and using
VT-x/AMD-V  
- VMM: fixed high load of ksoftirq on tickless Linux hosts  
- VMM: fixed Windows 2000 guests hangs related to IRQ sharing  
- VMM: fixed sporadic errors during openSUSE 10.3 installation  
- VMM: fixed issue with Linux 2.6.23 guests  
- VMM: fixed issues with Solaris guests  
- VMM: fixed stability issue related to incorrect relocations  
- Serial: significantly reduced CPU utilization  
- Network: fixed issues with FreeBSD guests  
- Network: added MII support (100MBit detection fix)  
- Network: improved MAC address handling  
- Network: added PXE release logging  
- IDE: large reads from CD could exceed the I/O buffer size  
- Audio: load ALSA dynamically on Linux (i.e. do not fail when ALSA is
not present)  
- VRDP: support additional RDP clients (SunRay, WinConnect, Mac OS X)  
- VRDP: fixed issues when client color depth is higher than server
color depth  
- VRDP: make PAM authentication service name configurable  
- VRDP: increased stack size to deal with stack consuming PAM library
calls  
- Additions: various fixes and enhancements to clipboard handling  
- Windows Additions: fixed issues with Additions on NT 4 guests  
- Windows Additions: added support for 8-bit video modes  
- Windows Additions: allow specifying custom resolutions for secondary
screens  
- Windows Additions: several fixes and improvements for DirectDraw  
- Windows Additions: improved the mouse filter driver compatibility
with other mouse drivers  
- Linux Additions: several fixes and enhancements to Shared Folders  
- Linux Additions: added support for X.org Server 1.4  
- Shared folders: fixed MS Powerpoint access issues (Linux host)  
- API: fixed RPC\_E\_CHANGED\_MODE startup error on Windows hosts<  
- API: fixed SMP race condition on Linux hosts  
- API: fixed stability issues on Windows hosts in low memory conditions

- [Download VirtualBox 1.5.2](http://www.virtualbox.org/wiki/Downloads)
