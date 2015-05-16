Title: VirtualBox 的实时迁移试验
Date: 2010-01-23 16:34
Author: toy
Category: Apps, Reviews
Tags: VirtualBox
Slug: virtualbox-teleportation

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

自 VirtualBox 发布 3.1 版本以来，Sun 赋予了 VirtualBox  
实时迁移的能力。当然 Sun 没有称自家的实时迁移技术为 Live  
Migration，而是叫 Teleportation。按照它自家的说法就是  
Teleportation 比 Live Migration 更高级。

实现实时迁移的条件之一就是要先把虚拟机存储文件存放在公共的存储空间，因此需要设定一个共享存储  
(Shared Storage)  

的空间，让实现迁移的两台实体主机都能够连接到共享存储空间上的虚拟媒体文件，包括虚拟磁盘、虚拟光盘和虚拟软盘。否则，即使迁移完成以后，也会因为无法启动迁移后的虚拟机。实时迁移实际上把虚拟机的各个配置文件封装在一个文件，然后透过高速网络，把这个封装文件和内存运行状态从一台实体机迅速传送到另外一台实体机上，期间虚拟机一直保持运行状态。在现有技术条件下，大多虚拟机软件，如  
VMware、KVM、Hyper-V、Xen 都需要共享存储。VirtualBox 支持 NFS 和
SMB/CIFS  
协议的网络文件系统，也可以支持 iSCSI 连接到 SAN  
网络。选用哪一种网络文件系统，则需要根据具体情况而定。SMB/CIFS 在
Windows  
和 Linux 都设置简便。NFS 在 Windows 则略显繁复。

    Source 机
    CPU: Pentium E2160
    RAM: 2GB
    OS: Fedora 12 x86_64

    Target 机
    CPU: Athlon 64 X2 4200+
    RAM: 2GB
    OS: Windows 7 Ultimate x64

    Guest 机
    Name: XP
    CPU: Virtual Single-Core Processor without VT
    RAM: 1GB
    OS: Windows XP Professional

首先架设一个共享存储环境，我就选用了 SMB/CIFS 协议，在  
Source 机架设了 Samba  

服务。如果把共享存储服务放置在第三台电脑上会更好，但是我由于条件所限只能把共享存储服务安装在  
Source 机上。具体方法就不再详述了。然后移动 Source  
机上的虚拟磁盘文件到共享存储服务器上。重新注册到  
Source 机上的 VirtualBox，并重新连接到 Guest 机，即可启动 Guest  
机。

在 Target 机上新建一个虚拟机。虚拟机的配置和特性要求与  
Source 机上的 Guest  
机完全一致。随后把共享存储上的虚拟磁盘文件连接到这台虚拟机上。随后在  
Target 机运行如下命令：

VBoxManage modifyvm --teleporter
on --teleporterport --teleporterpassword

以我的试验为例：

VBoxManage modifyvm XP --teleporter on --teleporterport
1234 --teleporterpassword 123456

若是在 Windows 上使用 VBoxManage  
命令行，则需要在命令提示符进入 VirtualBox 的安装目录，用  
VBoxManage.exe 替代 VBoxManage，使用效果是一样的。

以上命令瞬间执行完毕，然后启动 Target 机上的 Guest  
机。此时 VirtualBox  
弹出等待迁移的窗口。若取消迁移，可以按下窗口上的关闭键。

![等待迁移](http://dl.dropbox.com/u/1352061/photo/teleportation-1.jpeg)

然后在 Source 机运行迁移命令：

VBoxManage controlvm teleport --host // --port --password

以我的试验为例：

VBoxManage controlvm XP teleport --host 192.168.1.3 --port
1234 --password 123456

![迁移中](http://dl.dropbox.com/u/1352061/photo/teleportation-2.jpeg)

Source 机和 Target 机的 VirtualBox 控制台同样出现了正在  
Teleporting 的状态：

![正在迁移](http://dl.dropbox.com/u/1352061/photo/teleportation-3.jpeg)

迁移过程实际上是很短暂的。VirtualBox  
把虚拟机的配置文件封装并与虚拟机内存运行状态一并从  
Source 机传送到 Target 机即可。按照我家里的网络情况，TP-Link  
百兆家用路由器搭建的局域网，大约 20  
秒的时间就可以完成迁移过程。VirtualBox  
显示的剩余时间实际上是没有意义的。迁移前段 VirtualBox  
进行文件校验应该会花费不少时间。实际所需要的时间是根据网络情况与  
Source 机和 Target 机的性能配置而定。

当迁移完成以后，Source 机上的 Guest 机自动关闭，而 Target  
机上的 Guest 自动启动并且恢复到 Guest  
机关闭前的那一刻状态。此时VirtualBox 控制台就会显示  
Teleported 状态。

![完成迁移](http://dl.dropbox.com/u/1352061/photo/teleportation-4.jpeg)

当 Guest 机下一次在 Target  
机上启动前，需要把实时迁移的功能关闭，否则就会出现等待迁移的界面。

VBoxManage modifyvm XP --teleporter off

至此，整个实时迁移的试验宣告完成了。此外我更换了 Target  
机的 OS，改为与 Source 机一样的 Fedora 12  
x86\_64，似乎迁移的稳定性会更加好。以上截图大多数取自第二次迁移试验。

**注意事项：**

1. 在 VirtualBox 上运用实时迁移功能，Source 机和 Target  
机的硬件配置越接近越相似出现错误的机会就会越少。如果  
Source 机和 Target  

机硬件配置一致，那么出现兼容性的问题就非常地小。特别是两台机器的处理器，尽量要相近的型号。型号差异过大，则非常容易导致出错，尤其是  
Guest  

机内运行着专门为特定处理器优化的软件。当在两台处理差异过大的机器上进行实时迁移，特别是在跨品牌处理器之间(主要是  
AMD 与 Intel)  
的迁移，那么建议用户关闭虚拟处理器的筛选器。命令如下  
(后面<>为命令选项)：

VBoxManage modifyvm --cpuid

2. 实施迁移前，一定要确保 Source 机和 Target 机上的 Guest  
机硬件配置和设置都是一样的，特别是 System 和 Display  
的选项一定要保持一致，同样也需要采用相同的虚拟网卡。VirtualBox  
的实时迁移功能并不需要依赖 VT 技术，但是不能在一台没有  
VT 的 Guest 机和一台开启 VT 的 Guest  
机之间迁移，否则就会出现错误。

3. 最好配备有千兆局域网或者更好的网络条件，因为 Guest  

机的磁盘操作需要较高的速率，如果仅仅靠百兆局域网，那么速率上的限制和操作上的延时则极大地影响文件操作的效率和适用体验。

**总结**

VirtualBox 3.1  

带来了实时迁移能力，实在让人惊喜。这应该是第一款跨处理器品牌跨平台的虚拟机软件，能够在  
Windows、Linux、Mac OS X 和 Solaris  
平台上进行实时迁移。良好的易用性，一直都是 VirtualBox  
的优点。不过看起来，实时迁移对于 VirtualBox  

而言还是刚刚起步，还有很远的路要走。没有为实时迁移这种重量级的特性配备图形化操作界面对  
VirtualBox  
这款以易用闻名的虚拟机来说，不得不说是一个遗憾。

最后，限于条件，我没有带有 VT 技术的 Intel  
处理器。如果哪位热心朋友有这样的条件，可以进行一次带有  
VT 的 AMD 与 Intel  

的实时迁移试验，将会更有挑战性，因为这种情况下更容易出现处理器兼容性的问题。

{ Thanks liangsuilong. }
