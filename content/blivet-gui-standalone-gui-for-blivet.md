Title: blivet-gui：blivet 存储管理独立 GUI
Date: 2014-09-09 11:12
Author: lovenemesis
Category: Tools
Tags: blivet
Slug: blivet-gui-standalone-gui-for-blivet

Red Hat 系 RPM 发行版 Fedora/CentOS/RHEL
长久以来在一直安装过程中使用称为 [blivet
的存储管理库](https://fedoraproject.org/wiki/Blivet)。现在这个功能强大存储管理库将拥有自己独立的图形界面。

blivet-gui 的特点有：

-   通过 blivet 库实现完整企业级别 LVM2、RAID、Btrfs
    功能支持，包括分卷管理及 LUKS 加密等。
-   向 GParted 看齐的队列式处理逻辑，方便上手。
-   支持通过 XEmbed 协议嵌套入其他 GTK 或 Qt 应用程序。
-   可以生成 Kickstart 配置文件共 Anaconda 安装器使用。

[![blivet-gui-1](http://lt-file.b0.upaiyun.com/files/2014/09/blivet-gui-1-294x250.png)](http://lt-file.b0.upaiyun.com/files/2014/09/blivet-gui-1.png)

[项目首页及 Copr 仓库](http://blog.vojtechtrefny.cz/blivet-gui)

[邮件列表发布公告](https://lists.fedoraproject.org/pipermail/devel/2014-September/202105.html)

**PS：**[Slashdot
的相关报道](http://hardware.slashdot.org/story/14/09/07/2218229/fedora-to-get-a-new-partition-manager)言过其实，bliver-gui
并未打算取代使用不同后端的 GParted 。
