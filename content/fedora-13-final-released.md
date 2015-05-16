Title: 腾飞：Fedora 13 正式发布
Date: 2010-05-25 22:15
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-13-final-released

经过已经习以为常的一周延期，Fedora 项目组今天正式发布了代号为 Goddard 的
Fedora 13 。

Fedora 13 带来为桌面用户、开发者和系统管理员带来了哪些新功能呢？

首先从**桌面用户**开始：

-   **流水线式安装器** Anaconda
    安装工具的用户界面得到改善，简化了安装时对于存储设备和分区的管理。
-   **打印机驱动自动安装** RPM 和 PackageKit
    得到改善，当你连接打印机时将自动搜索软件仓库并安装对应驱动。
-   **新的桌面应用程序和改善** 预装了 Shotwell 照片管理，Deja-dup
    数据备份，Pino Identi.ca/Twitter 客户端和 Simple Scan
    扫描工具。另外现在也可以用 Palimpsest 磁盘设备程序方便的管理 LVM 和
    RAID 了。
-   **NetworkManager 添加移动宽带、蓝牙和命令行管理界面支持**
    NetworkManager
    现在是一站式的网络连接配置中心，无论使用何种联网方式。这次它不仅可以显示移动宽带信号强度，还添加对于蓝牙拨号的支持。所以这些功能都可以通过改进的图形化界面或者新增加的命令行界面访问。
-   **色彩管理** 通过全新的 gnome-color-manager
    组件，可以对打印机、扫描仪以及显示器的色彩进行调整，保证打印或扫描的色彩和在显示器上看到的一致。
-   **改善 iPod 系列设备支持** 新的 Apple iPod 、 iPod Touch 和 iPhone
    都得到了libimobiledevice 的支持，可以使用照片管理软件和音乐播放器如
    Rhythmbox 进行管理了。
-   **改善 Totem 流媒体和缓冲支持** 新的磁盘改善了 Totem
    播放高清视频和互联网 Podcast 时的流畅性。
-   **ATI 显卡 (R600 和 R700) 开源驱动 3D 加速支持** 默认启用了
    R600/R700 系显卡的 3D 加速支持，并且启用了 R800 的 2D
    驱动支持（无任何加速）也已经添加。
-   **Nvidia 开源驱动 Nouveau 的实验性 3D 加速支持** 可以通过安装
    mesa-dri-drivers-experimental 软件包来体验。
-   **KDE 进一步改善** KDE 进一步强化了 Fedora
    中的最新技术进步的联系。在这次发布中，通过进一步整合 PulseAudio 和
    Phonon 及KMix ， KMix
    可以对单独应用程序进行音量控制以及在不同硬件设备间切换。最新的
    PolicyKit 授权框架的也得到整合。此外，还将 KOffice、K3b 和 KDevelop
    IDE 迁移到 KDE4 框架下，不再需要 KDE3 兼容库了。
-   **改善 DisplayPort 支持** 在 Fedora 12 中增加 Intel 显卡的
    DisplayPort 支持后， 对于 NVIDIA 和 ATI 显卡的 DisplayPort
    支持也在本次发布中加入。
-   **实验性的用户管理界面** 用户帐号管理工具得到了完全的重新设计。

Fedora 13 还为**开发者**们带来了如下变化：

-   **SystemTap Static Probes** SystemTap 添加了对于 Java, Python, 和
    Tcl 运行环境，以及用户态应用程序的程序 PostgreSQL
    的支持。在未来，Fedora 将为更多的用户态应用程序提供 SystemTap
    支持，将极大的帮助需要对应用程序进行效能监控的开发者们
-   **简化的 Python debug** gdb 对 Python and C/C++
    混合型应用程序将提供更完整的 Debug 信息。
-   **并行安装 Python 3** 方便程序员同时在 Python 2.6 和 Python 3
    环境下测试代码。
-   **NetBeans Java EE 6 支持** NetBeans 6.8 ，首个完全实现 Jave EE6
    要求的 IDE， 也被包含在本次发布中。
-   **IntelliJ IDEA Community Edition, Java IDE** 继 Eclipse 和 NetBeans
    之后，Fedora 又添加了一个流行的 Java IDE 环境。

最后，是为**系统管理员**们带来的改进：

-   **boot.fedoraproject.org (BFO)**. BFO
    允许用户下载一个可放进软盘的微型镜像，使用它就可以通过网络安装当前和未来所有版本的
    Fedora 而无需再度下载。
-   **系统安全服务守护进程(SSSD)** SSSD
    将功能扩展到管理登录域中，包括离线授权。这意味着用户依然可以在未链接到公司网络的时候登入使用公司笔记本。
-   **领先的 NFS 功能** 本次发布 Fedora 默认使用 NFS4 协议，并且添加
    IPv6 支持。
-   **Zarafa 开源群组套件** Zarafa Open Source edition
    是一个完全免费并开源的 M$ Exchange
    替代品，实现网页邮箱、日历、协作和任务管理。功能包括 IMAP/POP 和
    iCal/CalDAV ，原生手机支持，并且可以和现有 Linux
    邮件服务器整合，完整的可编程接口和利用 Ajax
    技术实现的现代化操作界面。
-   **Btrfs 快照支持** Fedora 13 提供一个 yum-plugin-fs-snapshot
    插件为每次 yum 操作创建一个 Btrfs
    轻量级系统快照，方便管理员在更新出现问题时快速将系统回滚到原先状态。Btrfs
    还是处于实验性的文件系统，需要在安装时添加 "btrfs"
    安装选项才能使用，注意该选项不适用于 LiveCD 介质。
-   **进一步改善虚拟化**. KVM 添加了 Stable PCI Addresses 和 Virt Shared
    Network Interface 技术。Stable PCI addresses
    允许虚拟机保留在主机上的 PCI
    地址。共享网络接口允许虚拟机使用和主机同一个物理网卡。此外，得益于
    VHostNet KVM 网络加速和
    Virtx2apic，虚拟机的运行效率也得到了改善。Virtio-Serial
    是另一个重要改善，它为虚拟机提供了多个简单的字符设备接口，方便虚拟机和主机在用户态的沟通。
-   **Dogtag 认证系统** Dogtag 是一个企业级的开源 Certificate Authority
    (CA)，支持各类认证生命周期管理，包括密钥归档、OCSP 和智能卡 管理。

关于 **PowerPC 架构支持**：  
随着 Apple 迁移到 x86 架构和 Sony 移除 PS3 主机上的 Other System 功能，
Fedora 13 将 PowerPC 列为第二支持架构，转为社区支持。第一支持架构包含
x86 和
x86\_64。软件包只要求保证在第一支持架构通过，将不会因为在第二架构编译失败而无法进入软件仓库。

[Fedora 支持架构说明](https://fedoraproject.org/wiki/Architectures)

[简洁的 Fedora 13
单页图文发布摘要](http://fedoraproject.org/wiki/F13_one_page_release_notes)

[Fedora 13
完整功能列表](http://fedoraproject.org/wiki/Releases/13/FeatureList)

[Fedora 13 常见问题](https://fedoraproject.org/wiki/Common_F13_bugs)

[点击这里进入 Fedora 13 下载](http://get.fedoraproject.org/)
