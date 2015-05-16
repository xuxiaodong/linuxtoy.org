Title: 使用 VMware Player 测试 Linux 发行版
Date: 2006-08-01 14:29
Author: toy
Category: Tutorials
Slug: using_vmware_player_to_test_linux_distributions

原著：Francesco Arillotta　  
翻译：xxd　  
原文：[Using VMware Player to test linux
distributions](http://www.linuxforums.org/applications/using_vmware_player_to_test_linux_distributions.html)

[VMware](http://www.vmware.com)
是一家从事虚拟技术的专业公司，它提供的软件可以在一个操作系统之内运行另外一个操作系统。几个月前
VMware 发布了一个免费的虚拟机运行程序 VMware
Player，你可以用它来运行预先建立好的虚拟操作系统。

**系统**

宿主机（实际的操作系统）：Ubuntu Dapper Drake (build
20060323)。你可以从[这里](http://cdimage.ubuntu.com)下载。

客户机（我们即将安装的虚拟操作系统）：Underground Desktop
(022)。从[这里](http://www.ludos.org)下载。

**VMware Player安装**

从[这里](http://www.vmware.com/download/player/)下载 VMware Player 的
tar.gz 版。

安装与你目前运行的内核相匹配的 Ubuntu
内核头文件：`` sudo apt-get install linux-headers-`uname -r` ``。

同时安装编译 VMware
内核模块所需要的包：`sudo apt-get install gcc make`。

解压 VMware
Player，并转到新的目录：`tar xvzf VMware-player-1.0.1-19317.tar.gz`，`cd vmware-player-distrib`。

现在安装它：`sudo ./vmware-install.pl`。

安装程序将询问有关配置的问题，只需接受默认回答即可（按 ENTER
键）。同时授权协议也会显示，阅读后按 q 键，如果你接受它，输入 yes。

现在 VMware Player 应该安装好了。让我们尝试安装一个客户操作系统。

**安装客户操作系统**

创建一个新的目录用来保存你的客户操作系统：`mkdir  ~/GUEST`，`cd  ~/GUEST`。

现在你需要一个 VMware 格式的虚拟硬盘。另一个模拟器 Qemu
能提供创建它的方法。所以，安装 Qemu（你必须启用 Ubuntu universe
仓库）：`sudo apt-get install qemu`。

现在让我们创建一个8 GB
的磁盘映像，它将用于客户操作系统：`qemu-img create -f vmdk hd.vmdk 8G`。

然后创建一个名叫 vm.vmx 的虚拟机配置文件。

[php]  
#!/usr/bin/vmplayer

config.version = "8"  
virtualHW.version = "3"  
guestOS = "other26xlinux"  
memsize = "320"  
MemAllowAutoScaleDown = "FALSE"  
MemTrimRate = "-1"  
uuid.action = "create"  
hints.hideAll = "TRUE"  
tools.syncTime = "TRUE"  
usb.present = "TRUE"  
usb.generic.autoconnect = "FALSE"  
sound.present = "TRUE"  
sound.virtualdev = "es1371"  
isolation.tools.hgfs.disable = "FALSE"  
isolation.tools.dnd.disable = "TRUE"  
isolation.tools.copy.enable = "TRUE"  
isolation.tools.paste.enabled = "TRUE"  
ethernet0.present = "TRUE"  
ethernet0.virtualDev = "vlance"  
ethernet0.connectionType = "nat"  
ethernet0.addressType = "generated"  
ethernet0.generatedAddress = "00:0c:29:2e:30:2d"  
ethernet0.generatedAddressOffset = "0"  
floppy0.present = "TRUE"  
floppy0.startConnected = "FALSE"  
floppy0.autodetect = "TRUE"  
ide1:0.present = "TRUE"  
ide1:0.deviceType = "cdrom-image"  
ide1:0.startConnected = "TRUE"  
ide1:0.fileName = "underground\_022.iso"  
displayName = "UNDERGROUND"  
ide1:0.autodetect = "TRUE"  
ide0:0.present = "TRUE"  
ide0:0.fileName = "hd.vmdk"  
ide0:0.mode = "persistent"  
ide0:0.startConnected = "TRUE"  
ide0:0.writeThrough = "TRUE"  
ide0:0.redo = ""  
uuid.location = "56 4d 5d 61 35 03 9a 16-0d b2 b6 b2 92 2e 30 2d"  
uuid.bios = "56 4d 5d 61 35 03 9a 16-0d b2 b6 b2 92 2e 30 2d"  
[/php]

如果你的虚拟机需要超过320 MB 的内存，那么请更改此文件中的：

[php]  
memsize = "320"  
[/php]

同样，更改这两行：

[php]  
ide1:0.fileName = "underground\_022.iso"  
displayName = "UNDERGROUND"  
[/php]

以适合你用来安装的客户操作系统的 ISO 映像，及显示名称。

既如此，将已经下载的 Underground Desktop（我自己建立的 Linux
发行版）的安装 ISO 映像与 vm.vmx 和 hd.vmdk 一起放到~/GUEST 中。

现在运行 VMware Player：`vmplayer vm.vmx`。

虚拟机将从 CD
映像引导，并开始安装过程。完成下面的安装步骤，然后重启。你的客户操作系统就安装好了。

为了访问物理 CDROM，你可能要更改这行：

[php]  
ide1:0.deviceType = "cdrom-image"  
[/php]

为：

[php]  
ide1:0.deviceType = "cdrom-raw"  
[/php]

和这行:

[php]  
ide1:0.fileName = "underground\_022.iso"  
[/php]

为：

[php]  
ide1:0.fileName = "auto-detect"  
[/php]
