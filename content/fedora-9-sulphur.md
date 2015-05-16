Title: Fedora 9 (Sulphur) 发布摘要：引领潮流（独家中文首发）
Date: 2008-05-14 19:00
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-9-sulphur

美国东部时间5月13日，Fedora社区正式发布了代号"硫磺"的发行版 Fedora 9
(Sulphur) 。

Fedora 9
代号"硫磺"，是因为硫磺在神话中可以用来驱逐狼人，而"狼人"恰好就是 Fedora
8 的代号。

该版本有如下更新：

-   **PackageKit :** PackageKit
    是一个跨发行版的包管理系统，目前拥有完整的 yum
    后端。该软件的目标是统一所有发行版上的图形化包管理系统，所以采用了一些最新的技术如
    PolicyKit 和 D-Bus。
-   **GNOME 2.22：**GNOME 2.22带来了诸多升级。其中之一是由 Fedora
    的开发者[AlexanderLarsson](https://fedoraproject.org/wiki/AlexanderLarsson)
    完成的GVFS 和 GIO，它们被用来取代了陈旧的GNOME VFS。 GVFS
    提供了性能上提升，队列式多文件传输，并协同 PolicyKit
    提高了安全性。PolicyKit同样由 Fedora 开发者
    [DavidZeuthen](https://fedoraproject.org/wiki/DavidZeuthen)
    开发并维护，并首先于Fedora 8 中引入。GNOME 2.22
    还带来了样式新颖的世界时钟桌面小程序，可以同时显示不同时区的时间和天气情况。另一个在该版本
    GNOME 引入的变化是新设计的 GNOME
    登陆管理器(GDM)。新功能包括对登陆屏幕的电源管理支持，动态显示支持，以及对
    PolicyKit 的整合.
-   **KDE Desktop 4.0.3：**KDE Desktop 4.0.3 将全部 KDE 核心组件升级到了
    Qt4 接口上，从而引入了一系列全新的框架：多媒体API
    Phonon；硬件整合框架 Solid； 全新的桌面及面板
    Plasma；整合式桌面搜索；KWin 的混合特效和一个全新的视觉主题
    Oxygen。在 Fedora 9 的生命周期里， KDE
    将会持续得到来自上游项目的补丁升级，最终 Fedora 9
    将包括今年7月发布的 KDE 4.1。
-   **NetworkManager ：**Fedora 开发者 Dan Williams 使 NetworkManager
    变得比以前更加好用。
    新功能包括：多个设备的同时激活；方便与周围无限设备建立网络的 Ad-hoc
    支持；支持通过 GSM/CDMA 手机卡的 PPP 拨号以及 PolicyKit
    的管理方式的支持。
-   **Firefox 3 Beta 5：** Firefox 3 Beta 5
    带来了与当前桌面环境相一致的本地化视觉体验。其他改进包括整合了历史和收藏夹功能的地址栏，改进的收藏夹管理器。同时，浏览器引擎
    XULRunner
    也与用户界面分拆来，为其他有网页渲染需求的应用程序提供了一个独立于浏览器稳定接口。
-   **SELinux :** SELinux
    现在可以将浏览器插件置于安全限定区域内执行，从而避免了由于不安全的浏览器插件导致的安全问题。Fedora
    SELinux 开发者
    [DanielWalsh](https://fedoraproject.org/wiki/DanielWalsh) 在他的
    [blog post](http://danwalsh.livejournal.com/15700.html#cutid1)
    对此有详细描述。
-   **Java：**OpenJDK6 这一由 Sun 在开放源代码协议下发行的 Sun Java SDK
    将成为默认的 Java 开发环境。极少的OpenJDK 私有产权代码被来自
    [IcedTea](http://icedtea.classpath.org/wiki/Main_Page)
    项目的代码取代。现在，更多的 Java 程序无需任何额外设置就可以运行了。
-   **Xorg 升级：**X
    的启动和关闭现在只需要大约一秒钟！同时还有更方便的显示配置，以及热拔插支持。
-   **统一化辞典：**现在，OpenOffice.org，Firefox，Thunderbird，GNOME 和
    KDE 将共享同一个拼写检查辞典，这项改进将大幅度减少资源及内存消耗。
-   **蓝牙功能强化：**用蓝牙发送、接受文件，以及通过ODBX访问周边蓝牙设备将更加简单。
-   **Anaconda 安装器：**Fedora
    系统安装器，Anaconda，得到不少强化，其中包括：支持安装时调整
    ext2，ext3 和 NTFS 分区大小；支持创建和安装加密文件系统； 对 ext4
    文件系统的安装时支持(需要添加 `ext4` 引导选项来启动该功能)；支持
    GRUB 在 EFI x86\_64
    设备上的原生安装；引入支持网络安装和系统恢复功能的安装小镜像 
    netinst.iso 。
-   **无缝升级：**如果你已经安装了 Fedora 7或 Fedora
    8，现在可以通过图形化的
    [PreUpgrade](http://fedoraproject.org/wiki/Features/PreUpgrade)
    工具安全、方便的升级到Fedora 9。  

    [![](http://i.linuxtoy.org/i/2008/05/preupgrade-340x237.png)](http://i.linuxtoy.org/i/2008/05/preupgrade.png)
-   **永久性USB Live支持：** 全新的 LivdCD 工具包支持将 LiveCD
    镜像转化为自启动U盘 Live
    系统，并且不会丢失原先U盘上的数据。而且对U盘中 Live
    系统的改变可以永久储存在预先定义的空间内。现在，你可以将 Fedora
    系统与文档随身携带，还可以对 Live 系统进行升级。同时，通过
    [liveusb-creator](https://fedorahosted.org/liveusb-creator) 也可以在
    Windows 系统下制作Fedora Live U盘了。  

    [![](http://i.linuxtoy.org/i/2008/05/liveusb-340x335.png)](http://i.linuxtoy.org/i/2008/05/liveusb.png)
-   **Jigdo 下载支持：**Fedora 9 的镜像可以通过 jigdo 或者
    jigsaw下载。如果你所处地区有站点镜像或者你自己还保存有先前版本的光盘镜像，使用该方法将大大节省下载光盘镜像所需流量。
-   **FreeIPA：** FreeIPA 提供了对 Fedora Directory
    Server，FreeRADIUS，MIT Kerberos，NTP 和 DNS 服务的集中式的 Web
    及命令行界面配置，它可以使网络管理员快速、方便的进行认证、确认、策略处理等工作。
-   **Upstart 进程管理：**Fedora 9 使用 Upstart 进程管理取代了System V
    进程管理。这个变化帮助 Fedora 大幅度提升启动和关闭进程的速度。
-   **系统级应用程序升级：**包括GCC升级到4.3，Perl升级到5.10，Kernel升级到2.6.25-rc5，以及用TeXLive取代了Tex。
-   **中文相关：**默认中文字体包中增加了文泉驿正黑，默认包括了scim-python，并用scim-python-pinyin取代了原先的scim-pinyin。默认的中文输入法启动按键为Ctrl＋Space。

英文正式发布摘要见[这里](https://fedoraproject.org/wiki/Releases/9/ReleaseSummary)。

英文正式发布说明见[这里](http://docs.fedoraproject.org/release-notes/f9/en_US/)。

下载见[这里](http://fedoraproject.org/get-fedora)。

**下载完后一定要检验完整性！**目前 FedoraForum
上很多抱怨安装失败的人都是因为没有检验下载文件完整性。

如何检验见[这里](http://fedoraproject.org/zh_CN/verify)。

PS：目前中文版本的正式发布摘要还没有就绪，这里应该是首发:)
转载请注明，谢谢。

本人的 Fedora 本地化小组加入申请已经通过，正在等待Wiki编辑审核……寒……
