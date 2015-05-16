Title: Fedora 19 Alpha
Date: 2013-04-24 09:52
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-19-alpha

代号 "Schrödinger's Cat" 的 Fedora 19 Alpha 发布，您准备好打开箱子了么？

[![](http://lt-file.b0.upaiyun.com/files/2013/04/f19alpha.png "f19alpha")](http://lt-file.b0.upaiyun.com/files/2013/04/f19alpha.png)

Fedora 19 Alpha 针对**开发者**带来的改善有：

-   开发者助手：采用直观的一条龙方式帮助首次使用 Linux
    作为开发环境的用户部署指定语言的开发环境、模板、样例，且允许创建和
    Github 的链接。
-   OpenShift Origin：自己搭建开放无限制的平台即服务 (PaaS) 云计算平台。
-   3D 建模及打印：增加对 OpenSCAD、Skeinforge、SFACT、Printrun 和
    RepetierHost 等 3D 建模及打印工具的软件包。
-   node.js：增加流行的服务器端 JavaScript 实现
    Node.js，以及其使用的包管理工具 `npm` 。
-   Ruby 2.0.0：增加新发布的 2.0.0 支持，已将保持提供对 1.9.3
    的向后兼容。
-   Scratch：一个新的图形化的编程语言，主要用于计算机教学使用。

针对**系统管理**带来的改善有：

-   增加可选的 **syslinux 引导选项**，允许在云端部署或者在 Kickstart
    中指定而不在使用 GRUB。
-   systemd 资源管理允许在**运行时修改服务的资源及控制参数**而无需重启。
-   增加**进程检查点和恢复**功能，允许创建进场检查点，使得在进程错误时可以从检查点恢复，方便除错及负载均衡。
-   增加 Virt 存储迁移功能，在虚拟机迁移时不再需要两主机间有共享空间。
-   增加对 OpenLMI 通用远程系统管理架构的支持。
-   延伸 corosync/pacemaker 的容器管理功能至虚拟机内部容器。

针对**桌面应用**带来的改善有：

-   可选 [GNOME 3.8
    桌面环境](https://help.gnome.org/misc/release-notes/3.8/)，带来了经典视图、
    ownCloud 云端存储整合、重新设计的应用程序预览视图及控制中心。
-   可选 [KDE 4.10
    桌面环境](http://www.kde.org/announcements/4.10/)，带来了新的打印和色彩管理工具，将更多的桌面控件使用
    QML 重写。
-   可选[MATE Desktop 1.6
    桌面环境](http://mate-desktop.org/2013/04/02/mate-1-6-released/)，增加了对
    `systemd-logind` 的支持和大量细节改善。
-   继续提供使用其他桌面环境的定制版，包括 XFCE 和 LXDE 等。

[预装 GNOME 或 KDE 或 XFCE 桌面环境的 ISO
下载](https://fedoraproject.org/zh_CN/get-prerelease)

[英文发布摘要](https://fedoraproject.org/wiki/F19_Alpha_release_announcement?rd=Fedora_19_Alpha_release_notes)

**注意：** 当下 Alpha 版本打开的内核除错选项，对性能有影响；此外
Anaconda 并未开启手动分区的支持。
