Title: Fedora 11 值得期待──新特性简介
Date: 2009-03-11 09:59
Author: gcell
Category: Distros
Tags: Fedora, Fedora 11
Slug: fedora-11-new-features

[撰文/[gcell](http://gcell.yo2.cn/)]

Fedora 10 的推出好评不断，即将推出的 Fedora 11
又将带来更加丰富的新特性和更好的用户体验，作为许多新技术的激进先行者，Fedora
11 值得期待！

**软件更新**

Fedora 11 包含以下软件的更新，带来了许多 bug 修正和功能改进。Firefox
3.1、GCC 4.4、GFS 2、GNOME 2.26、IBus、[X Server
1.6](http://linuxtoy.org/archives/x-server-160-released.html)、Python
2.6、Thunderbird 3、TigerVNC、[KDE
4.2](http://linuxtoy.org/archives/kde-420-released.html)、[Xfce
4.6](http://linuxtoy.org/archives/xfce-460-released.html)、Evdev
2.2、xorg-x11-drv-synaptics 1.x……其中 IBus 将取代 SCIM
成为默认的输入法，TigerVNC 将成为默认的 VNC 客户端。另外，Fedora 11
重新构建了 KDE 4.2，添加了 PolicyKit-KDE、NetworkManager Plasma
插件等新鲜内容。

**驱动程序**

除去内核中驱动的更新，Fedora 11 默认启用了 Intel 图形芯片的 KMS（kernel
modesetting）特性，Nouveau 成为 NVIDIA 图形芯片的默认驱动，升级了 Radeon
r100/r200 3D 驱动，并开启了 kernel modesetting 和 DRI 2。

-   DRI 2 得到更新，提升了直接渲染的能力。
-   InputDeviceProperties──X server 1.6
    输入设备提供了一个通用组件用于实时改变驱动设置，同样的组件也被应用程序用于直接在设备上存储信息。
-   Anaconda 存储管理代码重写，新的 Anaconda 将使用 Udev
    来探测块设备，重写了分区管理、LVM、软
    RAID、块设备加密等模块。代码重写不会改变用户接口界面。

**用户体验**

-   上一个版本中未实现的 20 秒启动将在 Fedora 11 中实现，加速 Fedora
    开关机，其目标是尽量控制启动到登录窗口的时间在 20
    秒以内，并尽可能的加快登录后的桌面加载速度。
-   DeviceKit 是一个简单的，模块化的系统服务，用于管理设备和部分取代
    Hal。用户得到了一个图形化的磁盘管理程序
    palimpsestwhich，并且很好的整合到了桌面。
-   改进的音量控制：通过一种更容易理解和富有弹性的音量控制模式提升了
    Fedora 用户的多媒体体验。
-   允许桌面程序自动安装应用、字体、多媒体解码器和矢量素材（图标？）。
-   Evdev 2.2 的引入，使得输入设备的识别和配置更加智能和便利。
-   Ext4 将成为默认的文件系统，用户将可以体验到性能的提升和便利。
-   ABRT bug 自动报告工具继续改进，帮助新手提交 bug
    报告，只需简单的点击几次鼠标即可完成 bug 提交过程。
-   Presto 继续改进，作为 yum 的插件实现增量更新，提升 yum
    的更新下载速度。
-   提升了指纹识别验证功能的用户体验。
-   提升了对电源管理当前状态的检测和显示。
-   OpenChange 提供了原生的访问 Microsoft Exchange 应用。

**程序开发**

-   添加了 Eclipse 配置工具：添加了大量原生配置工具进入 Eclipse
    IDE，并与其他工具一起整合到了开发环境中，尤其是 Linux
    Tools、OProfile 及 Valgrind等。
-   Archer 进入 Fedora，Archer 是专注于提升 C++ 支持的 gdb
    开发分支，同时也包含了 Python 脚本功能支持。
-   liblvm 提供了用户空间的 LVM API。
-   NetBeans 6.5 作为一个十分有意义的更新将纳入 Fedora 11。
-   提供了全特性的跨平台编译 Windows 程序功能，在 Fedora 环境下无须
    Windows 即可编译和测试 Windows 程序。

**系统安全**

-   改进的组控制：允许系统管理员划分系统资源到不同的子组，同时根据不同程序的的需要分配子组的资源。
-   DNSSEC (DNS SECurity) 提供了真实可靠的 DNS 信息，改善了 DNS
    的安全性。
-   提升了 DBus 设置的安全性。
-   其他大量安全方面的更新和加强，为系统安全提供更可靠的保障。

虚拟机和虚拟化方面的更新也很多，在这里未做归纳，如有需要，请移步
<https://fedoraproject.org/wiki/Releases/11/FeatureList> 获得详情。

Fedora 11 此次的新特性条目总数达到 56
项，力度很大，覆盖很广，以上特性多数已经完成或者已完成大部分，但整体尚不完整且有疏漏或错误之处，详细一手信息敬请访问：
<https://fedoraproject.org/wiki/Releases/11/FeatureList>。

如有问题，请不吝指出，我将随时更正！

**延伸阅读**

-   [Fedora 11
    5大新功能简介](http://linuxtoy.org/archives/fedora-11-five-new-features.html)
-   [Fedora 11
    发布计划](http://linuxtoy.org/archives/fedora-11-release-schedule.html)

