Title: Fedora 19 Beta
Date: 2013-05-29 10:10
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-19-beta

代号 [“薛定谔的猫”](http://youtu.be/IOYyCHGWJq4) 的 Fedora 19 发布了
Beta 版本，增加了搭载 Mate 桌面环境和适用于云端服务的镜像。

相比之前发布的 [Alpha
版本](http://linuxtoy.org/archives/fedora-19-alpha.html)，本次 Beta
版本的变化有：

-   内核升至 3.9.4 版本并关闭影响性能的除错选项，Anaconda
    安装器手动分区完善。
-   [受 PackageKit
    上游影响](https://fedorahosted.org/fesco/ticket/1115)，默认允许具有管理员权限的用户安装来自
    Fedora 官方仓库的软件包而无需确认。在最终版将不再如此。
-   引入 [Federated VoIP](http://www.opentelecoms.org/federated-voip)
    支持，允许自由无障碍的语音通话。
-   更新打印服务器 **CUPS** 至最新版本，转而使用 PDF 作为基本文档类型。
-   在云端镜像使用 syslinux 实现启动引导，并且支持在 `kickstart`
    无人值守安装中调用，计划在未来在 Anaconda 中增加隐藏选项。
-   Kerberos 网络认证系统得到升级，可以提供支持两步验证的 FreeIPA 环境。

[预装 GNOME 或 KDE 或 XFCE 或 LXDE 或 SoaS 或 MATE-Compiz
桌面环境或云端服务的 ISO
下载](https://fedoraproject.org/zh_CN/get-prerelease)

[英文发布公告](http://fedoraproject.org/wiki/F19_Beta_release_announcement)
