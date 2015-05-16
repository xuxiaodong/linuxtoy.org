Title: 聚集：Fedora 12 正式发布
Date: 2009-11-18 03:36
Author: lovenemesis
Category: Distros
Tags: Fedora
Slug: fedora-12-unite-golden-released

以技术创新驰名的 Fedora Project 今日发布了代号 Constantine 的 Fedora 12
，口号 Unite，取意“聚集开源软件智慧”。

**新特性**

-   性能优化：在 32 位平台上全部软件包**针对 i686 架构**重新编译，并对
    **Intel Atom** 处理器进行性能调优。
-   NetworkManager ：改善了对于**宽带、蓝牙和 IPv6**
    的连接配置过程。配合 PolicyKit
    ，网络配置只需要点击鼠标即可轻松完成。
-   下一代 Theroa 编码支持：Fedora 12 集成了最新的**开源视频编解码器
    Theora** 1.1
    版本（详情见本站[此文](http://linuxtoy.org/archives/how-to-use-thoggen-to-backup-dvd-video-under-fedora.html)）。
-   更好的显卡支持：针对 Nvidia Nouveau 驱动和 AMD R600/700 系列的
    **KMS** 支持，同时为 Intel 显卡引入 **DisplayPort** 支持。
-   虚拟化支持：改善了 KVM 性能，并提供**虚拟机磁盘镜像监控**工具
    guestfish。
-   自动臭虫汇报系统和 SELinux：新的崩溃收集程序 **abrt**
    只需要点击几下鼠标即可将遇到的软件或 SELinux 提交至
    Bugzilla，方便开发者修复。
-   新的 Dracut initrd 启动系统：并行、以事件为单位的 **Dracut**
    系统进一步加快启动速度。
-   PackageKit
    插件：当用户尝试运行一个包含在尚未安装的软件包中的命令时，PackageKit
    可以**自动提示安装**相应软件包。
-   按需蓝牙服务：蓝牙服务会根据需要**自动启动和停止**。
-   Moblin 桌面环境：增加了 **Moblin** 桌面环境软件包组以及Fedora Moblin
    Spin 。
-   PulseAudio ：增添了 **UPnP 和 DLNA** 支持，可以直接将音频流发送至
    PS3 等设备。同时改善了**热拔插和蓝牙设备**支持。
-   更加安全：降低了部分系统文件和进程的运行访问权限，避免使用 root
    权限访问。同时为 SELinux 增添了**沙箱**支持。
-   Broadcom 固件：默认包含了 **Open Broadcom** 固件，对部分 Broadcom
    无线网卡提供 out-of-the-box 支持。
-   混合 Live 镜像：现在只需要使用 dd 即可创建光盘或者 USB Live
    镜像，不过还是推荐使用 Livecd-tools 以获得诸如保留空间等功能。
-   更好的摄像头支持：改善了部分摄像头的成象质量，尤其是很多廉价摄像头。
-   GNOME 2.28：使用 **Gnote** 替代了 Tomboy 成为默认便签，用
    **Empathy** 替代了 Pidgin 成为默认即时通讯客户端。
-   GNOME-shell 预览：尽管 GNOME 3.0 延期了，但是依然可以在 Fedora 12
    中提前体验下 **GNOME Shell** 的。
-   KDE 4.3：升级版的 Air
    主题，可配置的快捷键支持，新的窗口管理器特效以及更好的红外线遥控支持。
-   开发者：Eclipse Galileo, Perl 6, PHP 5.3, Netbeans 6.7.1
-   管理员：**GFS2 集群** Samba 管理
-   X.org 1.7.1：包含支持**多指点设备支持**的 XI2。

[英文原文及详细贡献者](http://fedoraproject.org/wiki/Fedora_12_Announcement)

[官方镜像下载](http://fedoraproject.org/get-fedora.html)

[完整功能列表](http://fedoraproject.org/wiki/Releases/12/FeatureList)

[Fedora 12 常见 Bug
说明及部分解决方法](https://fedoraproject.org/wiki/Common_F12_bugs)

[中文PDF安装指南](http://fedora-zh.googlecode.com/files/Fedora%2012%20Installation%20Guide%20in%20Chinese.pdf)（[感谢嘉佑兄！](http://pengyulong.com/yy/406.times)）

[英文配置命令集锦](http://digitizor.com/wp-content/uploads/2009/11/Fedora_12_Cheat_Sheet.pdff)（[再次感谢嘉佑兄！](http://pengyulong.com/yy/410.times)）
