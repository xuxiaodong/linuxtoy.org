Title: VirtualBox 1.5.4 发布
Date: 2007-12-30 09:54
Author: toy
Category: Apps
Slug: virtualbox-154-released

innotek 在近日发布了开源虚拟机软件
[VirtualBox](http://linuxtoy.org/archives/virtualbox.html) 的 1.5.4
版。自 [VirtualBox
1.5.2](http://linuxtoy.org/archives/virtualbox-152-released.html)
推出以来，VirtualBox 1.5.4 的主要改进包括：支持 USB 2.0、添加了
PulseAudio 后端、改善了 FreeBSD 客户机的兼容性等。推荐使用 VirtualBox
的朋友及时更新。

![VirtualBox](http://i.linuxtoy.org/i/2007/10/virtualbox.png)

以下为 VirtualBox 1.5.4 的完整更改日志，谨供参考：

- USB 2.0 support  
- PulseAudio backend  
- GUI: ﬁxed accelerators in German translation  
- GUI: ﬁxed registration dialog crashes  
- GUI: allow to enter unicode characters to the name of the
registration dialog  
- GUI: pre-select attached media in the disk manager when opened from
the VM settings dialog  
- GUI: remember the last active VM  
- GUI: don’t accept empty paths for serial/parallel ports in XML  
- GUI: ﬁxed NumLock / CapsLock synchronizazion on Windows hosts  
- GUI: don’t start the kernel timer if no VM is active (Linux host)  
- VMM: improved compatibility with FreeBSD guests  
- VMM: properly restore CR4 after leaving VT-x mode  
- VMM: patch code and disassembler updates  
- VMM: with VT-x a pending interrupt could be cleared behind our back  
- VMM: workaround for missed cpuid patch (some Linux guests refuse to
boot on multi-core CPUs)  
- VMM: ﬁxed code for overriding CPUID values  
- API: don’t crash when trying to create a VM with a duplicate name  
- API: don’t crash when trying to access the settings of a VM when some
other VMs are not accessible  
- API: ﬁxed several memory leaks  
- ATA/IDE: ﬁxed SuSE 9.1 CD read installer regression  
- Floppy: ﬁxed inverted write protect ﬂag  
- USB: virtualize an EHCI controller  
- USB: several minor ﬁxes  
- Network: ﬁxed MAC address check  
- Network: host interface ﬁxes for Solaris guests  
- Network: guest networking stopped completely after taking a snapshot  
- Network: don’t crash if a network card is enabled but not attached  
- PXE: ﬁx for PXE-EC8 error on soft reboot  
- NAT: update the DNS server IP address on every DNS packet sent by the
guest  
- VGA: reset VRAM access handers after a fullscreen update  
- VGA: don’t overwrite guest’s VRAM when displaying a blank screen  
- ACPI: implemented the sleep button event  
- VRDP: ﬁxed crash when querying VRDP properties  
- VRDP: netAddress ﬁxes  
- VRDP: ﬁxed the Pause/Break keys over VRDP  
- VRDP: sync NumLock / CapsLock sync over VRDP  
- VRDP: workaround for scrambled icons with a guest video mode of
16bpp  
- VRDP: reset modifer keys on RDP\_INPUT\_SYNCHRONIZE  
- VRDP: reset RDP updates after resize to prevent obsolete updates  
- Clipboard: Windows host/guest ﬁxes  
- Clipboard: ﬁxed a SEGFAULT on VM exit (Linux host)  
- Clipboard: ﬁxed a buffer overﬂow (Linux host)  
- Shared Folders: ﬁxed memory leaks  
- Linux installer: remove the old kernel module before compiling a new
one  
- Linux host: compatibility ﬁxes with Linux 2.6.24  
- Linux host: script ﬁxes for ArchLinux  
- Linux host: load correct HAL library to determine DVD/ﬂoppy
(libhal.so.1 not libhal.so)  
- Linux host: make sure the tun kernel module is loaded before
initializing static TAP interfaces  
- Windows additions: ﬁxed hang during HGCM communication  
- Windows additions: ﬁxed delay when shutting down the guest  
- Linux additions: added sendﬁle support to allow HTTP servers to send
ﬁles on shared folders  
- Linux additions: make additions work with Fedora 8 (SELinux policy
added)  
- Linux additions: sometimes ARGB pointers were display incorrectly  
- Linux additions: several small script ﬁxes

除源代码外，VirtualBox 1.5.4 针对 Ubuntu、Debian、openSUSE、SUSE Linux
Enterprise Server、Fedora、Mandriva、Red Hat Enterprise
Linux、PCLinuxOS、Xandros Desktop 等 Linux
发行版提供有预编译的二进制包，你可以从 [VirtualBox
的官方网站](http://www.virtualbox.org/wiki/Downloads)下载。
