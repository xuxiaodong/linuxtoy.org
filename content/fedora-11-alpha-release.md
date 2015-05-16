Title: Fedora 11 (Leonidas) Alpha  发布
Date: 2009-02-06 01:38
Author: lovenemesis
Category: Distros
Tags: Alpha, Fedora
Slug: fedora-11-alpha-release

Fedora 项目组在短暂的延期后于近日发布了 Fedora 11 Alpha
版本，供公众测试并提交 Bug 。

*以下内容是对发行日志的简化翻译*

Fedora 11 Alpha的新功能：

-   Windows Cross Compiler：无需 Windows 即可在熟悉的 Linux
    环境下编译跨平台程序
-   Ext4 File System：使用 Ext4 作为默认文件系统
-   Btrfs File System：增加对于 Btrfs
    下一代文件系统的支持，需要在引导时添加 `icantbelieveitsnotbtr` 参数
-   New Volume Control：重新设计的 GNOME 音量管理控件
-   PackageKit Firmware Support：PackageKit 支持依据需要安装固件
-   GNOME 2.26：包含了 GNOME 2.26 开发快照
-   KDE 4.2 Release Candidate 2：包含了 KDE4.2 RC2版本。4.2
    最终版将以升级方式提供。
-   Xfce 4.6 Beta ：包含了 Xfce 4.6 Beta 版本。
-   NetBeans 6.5 ：将 NetBeans 升级到最新的 6.5 版本
-   Python 2.6 ：将对于所有使用 Python 的程序将兼容 Python 2.6
    版本。这是向不提供向后兼容的 Python 3.X
    迈进的第一步（译注：对此感到困惑的朋友请参考下面的留言）
-   X Server ：默认禁用 Ctrl-Alt-Backspace 杀死 X
    Server，如果要启用该功能的话在 xorg.conf
    中增加` Option "DontZap" "false"`到 ServerFlags 字段。
-   Git 1.6.1.1 ：升级到 Git 1.6.1.1 ，依照建议，git-*
    命令现在并不包括在 `PATH` 变量下。

*翻译结束*

Fedora 11 Alpha 提供 LiveCD 版本镜像，也可以使用 livecd-tools
工具将其转化为 USB 镜像使用，所以无须安装到硬盘上即可进行测试。

为了预期与2009年5月24日发布的 Fedora 11
的正式版本能以最佳的状态展现在最终用户面前，希望有兴趣的朋友能积极参测试并提交
Bug 。

[FedoraForum Alpha/Beta/RC 测试专区  
](http://forums.fedoraforum.org/forumdisplay.php?f=66)  

[英文发行日志](https://fedoraproject.org/wiki/Fedora_11_Alpha_release_notes)  
[发布时间表](https://fedoraproject.org/wiki/Releases/11/Schedule)  
[官方下载](http://fedoraproject.org/get-prerelease)
