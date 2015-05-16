Title: QEMU-KVM 0.12.2 发布
Date: 2010-01-23 16:22
Author: toy
Category: Apps
Tags: KVM, Qemu
Slug: qemu-kvm-0-12-2-released

{ 撰文/[liangsuilong](http://www.liangsuilong.info) }

[QEMU-KVM](http://linux-kvm.com) 项目最近发布了 0.12.2  
的新版本，从版本号上看，此次更新主要是为增强 KVM 和修复  
Bug 而发布的。不过在 Phoronix  
上得到的消息是，这个版本引入了 Block Migration (块迁移)  
的特性。

众所周知，虚拟机实现实时迁移，需要有共享存储 (Shared Storage)  

服务器，把虚拟媒体文件如虚拟磁盘、虚拟光盘等放置在该服务器上，也需要连接到始发机和目标机。引入块迁移以后，则可以在进行实时迁移的时候，同时把虚拟磁盘从始发机迁移至目标机。使用这个特性时，QEMU
首先会把虚拟磁盘文件完全地传送目标机，然后把在迁移过程中虚拟磁盘发生改变的部分也迁移到目标机。QEMU-KVM  

有了这个特性以后，那么共享存储就不再是实时迁移的必要条件，从而降低了进行实时迁移的难度。

另外，QEMU 也发布了 0.13 版本的特性列表：

+ gPXE support for virtio-blk  
+ helper based network setup  
+ balloon driver statistics  
+ Fully supported QMP  
+ Live migration protocol support for subvendor version  
+ virtio-console  
+ vhost-net  
+ vepa networking  
+ kvm irqchip  
+ guest SMP support

[QEMU-KVM 0.12.2
下载地址](http://sourceforge.net/projects/kvm/files/qemu-kvm/0.12.2/qemu-kvm-0.12.2.tar.gz)。

{ Thanks liangsuilong. }
