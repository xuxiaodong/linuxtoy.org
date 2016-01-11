Title: 体验 Fedora Workstation 应用于桌面办公领域
Author: lovenemesis
Date: 2015-11-24
Category: Tutorial
Tags: fedora
Slug: trying-fedora-workstation-at-work
Summary: 可能您在工作中免不了接入一些 Windows 设备，甚至可能您的办公网络既是为了 Windows 环境考虑的，不过这是无法阻挡一颗向往 Linux 的心。

好吧，我承认本文是由于单位配发本本升级 Win10 后各种不爽而折腾的结果……
简而言之，本文阐述了如何将 Fedora 与 Win10 共存且配置一些常用办公软件的小技巧。

##### 安装 Fedora Workstation

这里以在**已经具备 Win 系统**上安装 Fedora Workstation 为例说明，其他发行版的方法类似。相信这也是大多数办公用机的现实状况。

现在的多系统引导需要了解您的机器是 BIOS 还是 UEFI 的，因为这影响着接下来的引导分区配置。一般来说若您的机器在 2010 年之后购置的，有很大机率是 UEFI 的，更早的则是 BIOS。

不过为了准确，可以[在 Win 系统下运行 msinfo32 查看](http://blogs.technet.com/b/home_is_where_i_lay_my_head/archive/2012/10/02/how-to-check-in-windows-if-you-are-using-uefi.aspx)，关注其 `BIOS Mode` 区域即可。

之后则需要在硬盘上腾出一片**未分配的空间**。在 Win 系统下可以使用自带的磁盘管理工具或者各类第三方工具实现，或者也可以稍后在 Linux 安装程序中操作。

接下来便需要重新启动至包含 Linux 安装介质了，比如 U盘。若是 BIOS 系统的话重启后留意提示按下指定键即可，若是 UEFI 的话则需要在 Win 的设置中选择高级工具。

在启动管理菜单中需要注意的是[选择与 Win 系统方式相同的方式引导 Linux 安装介质](https://docs.fedoraproject.org/en-US/Fedora/22/html/Multiboot_Guide/index.html)，特别是在 UEFI 的系统上可能出现 BIOS 兼容模式的情况下。若是您的 Win 是以 UEFI 方式引导，而您的 Linux 是以 BIOS 兼容模式引导且安装的，在默认 GRUB2 配置下安装后 Linux 后便无法再引导至 Win 了。反之亦然。

如果之前已经设定好了分区，那么 Linux 的安装过程便十分简单了，不再赘述。最后重新启动，使用在安装过程中创建的本地账户登陆即可。

##### 接入 Exchange/Kerberos 网络服务：

在 Fedora Workstation 下使用 GNOME 在线账户接入企业常见的 **Exchange/Kerberos 资源服务**很容易。

在`设置`中找到`在线账户`，在列表中分别可以找到 Microsoft Exchange 和 Kerberos 账户类型。Exchange 的填写信息可以参考原 Win 系统中 Outlook 等程序的配置。Kerberos 则简单很多，当下公司网络中的域服务器应该会直接出现在下拉菜单中，选择并填写用户名密码即可。

Fedora Workstation 版本防火墙默认配置允许扫描网络中可用资源，且预装了 SAMBA 客户端。于是在完成企业用户登录后，配置打印机和共享磁盘便简化成点点鼠标的事情了。若是使用的 HP 的打印机，那么驱动程序亦可以通过 PackageKit 自动联网下载。

不过暂时没有找到如何在 Linux 环境下更新 Exchange/Kerberos 域账户登录密码的方式……

##### 配置办公软件

随着 LibreOffice 和 Evolution 的改善，基本上可以替代 Office 办公套件了。不过若是想实现高精度的兼容，或者有要求使用特殊模版，那么也可以[使用 CrossOver 安装获得授权的 Office 套件](https://www.codeweavers.com/compatibility/crossover/microsoft-office-2010) 也是一个方案，一路有向导，不太可能出错。如果贵司有 Office365 企业级订阅的话，那么其实运行 Web 版本也很方便。

不过对于 MS 全家桶中的另外两大渣 Skype for Business 和 OneDrive for Business 情况则复杂一些。

先说 **Skype for Business**。别看它现在名字中包含了 Skype，其实还是那张新皮背后还是烂到渣的 OC/Lync，并不能使用 Skype for Linux 登录。此时需要借助 [SIPE 项目](http://sipe.sourceforge.net/) 才能实现。SIPE 在 Fedora 上提供了 purple 插件，也提供适用于 Pidgin 的配置界面。尽管也可以使用 Empathy/Telepathy 调用 purple 的插件用，不过有些功能尚缺乏访问接口，所以在直接 Telepathy 的插件推出前，推荐还是使用 Pidgin 版：

`sudo dnf install pidgin-sipe`

安装完之后启动 Pidgin，即可看到名为 Office Communicator 的新账户类型。配置页面中有不少选项可供调整，不过对于在下的环境来说仅需要按照[这篇博客](http://geekyschmidt.com/2013/05/18/microsoft-lync-on-linux)中所说**填上 Lync 2010 的UA**即可。

经测试群组聊天、联系人搜索、语音通话都可以正常工作，视频似乎还需要安装一些解码包才可，尚待研究。

最后剩下 **OneDrive for Business** 则真的是个坑了……

目前没有可以快速部署的 Linux 平台部署方案，现有的两个开源项目 [onedrive](https://github.com/skilion/onedrive) 和 [onedrive-d](https://github.com/xybu/onedrive-d)均不支持 OneDrive for Business。

不过 MS 自己的官方客户端也是区分个人用户和企业用户且互相不兼容的，实在没法奢求更多了……

我司常用的**会议软件新秀 Zoom** 则友好的提供了 Linux 平台原生版本（尽管只有 32 位版本），使用浏览器访问[其官方站点即可下载](https://www.zoom.us/download#client_4meeting)。体验保持了与其他平台一致的高水准，最近的更新也补上了创建会议的功能，继续完爆 Skype for Business N 条街。

##### 编译 Subversion 1.7

将 Fedora 配置为 Android 开发工作站十分简单，不需要多说什么。不过若是贵司也仍在使用古老的 **Subverion 1.7** VCS 的话……

Fedora 中仅有最新的 subversion 1.9 系列版本，Copr 仓库中亦没有 subversion 1.7 系列。固然可以使用较老版本的预编译包，不过为了安全更新和错误修复，在下选择了从源代码编译。

使用如下命令解决编译 subversion 所需的依赖关系：

`sudo dnf builddep subversion`

呃……是不是发现比预想中多？原因有默认包含了针对 Ruby、Python、Perl 的语言绑定，这里省事期间索性一并安装了，毕竟现在硬盘不值钱……

之后[前往 Apache 的存档](http://archive.apache.org/dist/subversion/)下载 [subversion-1.7.22](http://archive.apache.org/dist/subversion/subversion-1.7.22.tar.bz2) 版本，解压并执行 `./configure`，在过程中会发现**提示缺失 neon 库**（竟然不能自动检测并使用之前随着依赖安装的 libapr……），依照提示安装即可：`sudo dnf install neon-devel`。重新运行 `./configure` 后即可顺利开始 `make` 以及 `sudo make install` 了。

##### 结束语

整个过程比在下预想中顺利很多，MS 的被倒逼和开源软件这几年的成熟，使得在企业环境部署基于 Linux 的工作站不再是件头疼的事情。若是您的环境和工作性质允许，不妨试试吧！

##### 参考资料

[How to check in Windows if you are using UEFI](http://blogs.technet.com/b/home_is_where_i_lay_my_head/archive/2012/10/02/how-to-check-in-windows-if-you-are-using-uefi.aspx)

[Fedora 22 Multiboot Guide](https://docs.fedoraproject.org/en-US/Fedora/22/html/Multiboot_Guide/index.html)





