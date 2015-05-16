Title: SE Android
Date: 2012-01-14 20:42
Author: lovenemesis
Category: Embedded
Tags: Android, selinux
Slug: se-android

Security Enhanced (SE) Android 是尝试识别并弥补 Android
系统上安全缺陷的项目，于最近发布了首个版本。

起初 SE Android 的目的是将 SELinux 应用在 Android
系统上，用来降低恶意程序的危害和强制施行应用程序隔离。不过 SE Android
项目的范畴并不局限于 SELinux。

SE Android 项目还将提供一个在 Android 底层软件中实现 SELinux
的参考方案，从而**提高 Android 面对 Root
溢出攻击和应用程序缺陷时的防御能力**。

SE Android 参考实现的功能：

-   Yaffs2 文件系统按文件的安全标注支持。
-   编译时文件系统(ext4 和 yaffs2)镜像安全标示。
-   Binder IPC 内核许可检查控制。
-   为由初始化进程生成的服务端口和端口文件进行安全标注。
-   为由 ueventd 生成的设备节点进行安全标注。
-   为应用程序及其数据目录提供灵活的可配置的安全标注。
-   使用 Zygote 执行用户态许可检查控制。
-   移植精简的 SELinux 用户态工具。
-   为 Android 工具集提供 SELinux 支持。
-   提供为 Android 重新编写的安全规范文件。
-   限定系统服务和程序到有限域中。
-   使用 MLS 分类来隔离应用程序。

SE Android 基于 [Android Open Source Project
(AOSP)](http://source.android.com/) 的源代码创建。

[项目详细 Wiki 主页以及 Fedora
平台编译指南](http://selinuxproject.org/page/SEAndroid)

[Linux 安全大会 2011 上关于 SE Android
的公开演讲](http://selinuxproject.org/~jmorris/lss2011_slides/caseforseandroid.pdf)

[消息来源](https://plus.google.com/u/0/114085224276669186297/posts/hCnfVbG7ma5)

**PS：**在 Android 玩家群体中常听到“获取 root
权限”实际上就是针对系统漏洞执行溢出操作从而取得 root 用户权限的过程。

**目前层出不穷的 root
大法在一方面方便了玩家执行一些特殊操作，另一方面也突显出 Android
系统在面对此类攻击时显得多么孱弱。**
