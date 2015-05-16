Title: Fedora 20 将会把 ARM 列为主要架构
Date: 2013-07-20 17:23
Author: liangsuilong
Category: Distros
Tags: arm, Fedora
Slug: fedora-20-will-set-arm-as-primary-arch

Fedora 工程委员会日前例行会议宣布，ARM 将会在 Fedora 20
列为首要架构，地位等同 i686 和
x86\_64。[详细介绍](https://fedoraproject.org/wiki/Changes/ARM_as_Primary)

应对 IT 行业对于绿色环保节能的需求，大批量廉价 ARM
运算设备亦在不断普及。传统上 ARM
在嵌入式设备和移动设备占据统治地位，近年 ARM 性能日益提升，ARM
也向传统运算设备领域迈进，比如桌面电脑，服务器。因此 Fedora 计划把
armv7l 架构作为首要架构推向 Fedora Koji 中心编译打包服务器。目前 Fedora
在美国凤凰城的数据中心有 96 个四核心 Calxeda EnergyCore
运算节点，有一部分依然用于编译打包 Fedora 18 和 Fedora 19
的后续更新，等到 Fedora 18 生命周期结束，用于 ARMv5
软浮点编译打包的计算节点将会重新分配用于其他任务。Fedora
负责基础架构团队对 ARM
的负载能力测试十分感兴趣，这些计算节点可能会分配用于质量保证以及其他工程项目。目前
Fedora 计划分配  24 个计算节点用于 Fedora 20 首要架构的 Koji 服务器。

当 Fedora 产品经理公开 ARM 作为 Fedora 20
的首要架构这一消息后，激烈的讨论蜂拥而至，毕竟这是 Fedora
近年来最重大的技术变动。有人认为 Fedora 加入 ARM
的支持只不过是顺应潮流；有人认为 ARM 性能实在太慢了，编译 Kernel 和
Eclipse 这些巨型组件需要多十倍八倍时间；也有人认为目前 ARM
移植版本完成度并不高，甚至比在 Fedora 13 剔除出首要架构的 PowerPC
还要低，Packager 也没有义务为 ARM 做更多的调试工作，但最终 ARM 被纳入
Fedora 20
的首要架构。[详细讨论](https://fedoraproject.org/wiki/Changes/ARM_as_Primary)

原来 Fedora ARM 次要架构时代共存 armv5tel 软浮点以及 armv7hfp
硬件浮点两架构，在 Fedora 19 时 armv5tel 已经被放弃，Fedora 18
将会是最后一个支持 armv5tel 的版本。而在 Fedora 20
升级到首要架构后，armv7hfp 将会被命名为 armhfp，该架构要求 ARMv7
芯片，而且需要包含 VFP 硬件浮点单元，不过 NEON SIMD
指令集则不是必须的。同样 armhfp 架构可以支持 LPAE 物理地址扩展技术，允许
32 位 ARMv7 架构支持超过 4GB 内存。Fedora 项目也会继续和 Linaro
项目沟通合作，加速 64 位 ARMv8 的 aarch64 架构移植工作，以满足未来 64 位
ARM 芯片的需求。（据说就是等 Linaro 项目的巨巨把 Linux
内核以及整套工具链移植到 ARMv8 架构芯片上咯。）

然而在 Fedora 20 开发周期里把 ARM 列为首要架构依然困难重重，是否作为
Fedora 20 最终发布的特性，需要根据 ARM 架构移植的进度而定。根据 Fedora
19 for ARM 的发行公告，Fedora 20 for ARM
可能会基于以下四款设备发布安装镜像：CompuLab TrimSlice（Tegra 2）、Texas
Instruments PandaBoard（OMAP 4）、Versatile Express（QEMU）以及 Calxeda
EnergyCore ECX-1000（HighBank）。Raspberry Pi 使用的 ARMv6
架构，不在支持设备名单内，但会有使用 ARMv6 VFP 硬件浮点的非官方的 Remix
版本。

注意：Calxeda EnergyCore 每一个计算节点包含一颗频率为 1.1GHz～1.4GHz
的四核心 Cortex-A9 核心处理器。该处理器功耗在 3.8W～5W 之间，包含 4MB
二级缓存以及 NEON SIMD 单元，提供有 PCI Express 2.0 x8 和 SATA 2.0
接口，也可支持 4GB miniDIMM ECC DDR3L 内存。另外 EnergeCore 有一个
10Gbps 光纤接口，用于多节点集群。发稿时 Calxeda
官方网站似乎故障了，资料来源于
[Anandtech](http://www.anandtech.com/show/6757/calxedas-arm-server-tested/)
和
[Phoronix](http://www.phoronix.com/scan.php?page=article&item=calxeda_ubuntu_pre)
的 Calxeda EnergeCore 评测。

除了 ARM 首要架构以外，Fedora 20 目前确认了以下特性：

-   Boost 1.54
-   Hadoop
-   KDE 4.11
-   SDDM 作为 KDE 默认显示管理器
-   Yesod Web 框架
-   共享证书工具
-   通过 libvirt 工具管理和运行 x86 上的 ARM 虚拟机
-   virt-manager 的虚拟机快照界面

[特性详情](https://lists.fedoraproject.org/pipermail/devel-announce/2013-July/001211.html)

补充：以下有一份数据表格对比在不同架构上编译所需的时间，数据来自 Fedora
Koji 中心编译服务器，在 ARM 架构上编译著名的集成开发环境 Eclipse
需要比在 x86 上多使用大约 15
个小时。[数据表格](http://scotland.proximity.on.ca/~jon/koji.times.html)
