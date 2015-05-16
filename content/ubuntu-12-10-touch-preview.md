Title: Ubuntu 12.10 Touch Preview
Date: 2013-02-22 09:16
Author: lovenemesis
Category: Distros
Tags: Ubuntu
Slug: ubuntu-12-10-touch-preview

Canonical 放出了将在 MWC 2013 展示的 Nexus 系列手机和平板的 Ubuntu 12.10
触屏预览版本，可供爱好者自行刷机。**内附独家 Galaxy Nexus 测试体验**。

支持的设备有：

-   Galaxy Nexus
-   Nexus 4
-   Nexus 7
-   Nexus 10

目前实现的功能有：

-   界面和部分核心应用。
-   可连接至 2G GSM 网络，实现通话和短信。
-   通过 WiFi 连网。
-   前置和后置摄像头。
-   可通过 adb 连通。

[详细刷机指南（请注意备份资料，刷机有风险！）](https://wiki.ubuntu.com/Touch/Install)

[镜像下载](http://cdimage.ubuntu.com/ubuntu-touch-preview/quantal/mwc-demo/)

[源代码](https://launchpad.net/ubuntu-touch-preview)

**Galaxy Nexus 测试体验**

按照 Canonical 的教程，成功将 Ubuntu 12.10 for Touch 安装到 Galaxy Nexus
上。以下是个人体验：

-   没有系统启动屏幕，按下电源后需要耐心等待，之后突然一亮直接进桌面。
-   系统中包含了大量假的聊天记录、联系人、图片等信息，其实都不可用……
-   所谓核心应用，**只有电话、拍照和相册可用**，没有短信程序，向目标手机发短信无响应。
-   **其余应用皆为静态图片，连计算器都是……**，Facebook 和 Gmail
    就是普通触屏手机网页版。Ubuntu One
    能看到登录界面，因无帐号故未进一步测试。
-   Dash 搜索不可用，所显示内容皆为静态图片。
-   浏览器 HTML5test.com 得分 386 + 16，UA 为 Safari on iOS 5.0
    。尽管宣称支持 HTML5 音视频，但都不可用。不支持 WebGL。
-   不支持中文显示及输入。
-   顶部提示条的设计从音量图标位置向下滑动，显示音量控制；从 WiFi
    的图标向下滑动，显示 WiFi 控制。这种方式或许在 Nexus 7 或者 10
    上会稍好些，但是在 Galaxy Nexus 的“小屏幕”上，很容易滑错。
-   **主界面上下滚动操作比较流畅**以外，其余操作都很卡，包括左右滑动切换应用程序。从拍照界面进入相册，到看到刚拍摄的照片，大约需要等待1分钟。
-   耗电飞快，机子也比较容易过热。死机频繁，常常需要卸电池。

可能这个固件的主要目的是展现 Unity for
Touch，至少这是固件中唯一能勉强看的部分。应用方面对于一个以静态图片为主的固件，我真的不知道该说什么……
其他的诸如缓慢、死机和过热的问题，可能是 Galaxy Nexus
配置“过于孱弱”无法满足 Ubuntu 12.10 for Touch
的胃口吧。时间所限，未能测试 Nexus 4
上的情况。如有童鞋依然愿意尝试，不妨也在此分享下～

**PS:** [根据 Phoronix
的报道](http://www.phoronix.com/scan.php?page=news_item&px=MTMwODg)，Ubuntu
12.10 for Touch 使用的显示服务器并非 Wayland 或 X11，而是直接用的
Android 的 SurfaceFlinger 。
