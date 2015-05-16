Title: XorgTablet: 用 Android 平板当绘图板
Date: 2013-01-18 10:32
Author: lovenemesis
Category: Android
Tags: Android, GIMP, x11
Slug: xorgtablet-transform-android-tablet-into-wacom

来自 GIMP 社区的 [redforce](http://www.gimpusers.com/users/redforce)
开发了基于 X11 协议的网络绘图板驱动程序，配合对应客户端，允许用户将
Android 平板当作绘图板使用。

要实现这个功能，大致的步骤为：

-   一台装有 Linux 系统且有局域网连接的主机。
-   下载客户端 [XorgTablet 的
    APK](http://sourceforge.net/projects/xorgtablet/files/XorgTablet/XorgTablet-16012013.apk/download)
    并安装到 Android
    平板，亦可自行从[源代码编译](https://github.com/rfc2822/XorgTablet)。
-   下载 [xf86-networktablet
    的源代码](https://github.com/rfc2822/xf86-networktablet)并编译安装。
-   编辑 `/etc/X11/xorg.conf` 或在
    `/etc/X11/xorg.conf.d/`中增加如下内容：

        Section "ServerLayout"
            Identifier     "DefaultLayout"
            InputDevice    "NetworkTablet0"
        EndSection

        Section "InputDevice"
            Identifier     "NetworkTablet0"
            Driver         "networktablet"
        EndSection

    之后重启 X Server。

-   在终端使用 `xinput list` 查看是否已经有名为 `NetworkTablet0`
    的设备。
-   配置 Linux 系统主机防火墙，允许 UDP 40117 端口的访问。
-   在 Android 平板上启动 XorgTablet 客户端，将默认主机地址修改为您
    Linux 系统的 IP。
-   在 GIMP 中使用 Edit -> Input Devices -> Network tablet -> Mode:
    set to Screen 即可，支持压感。

[视频演示](http://www.youtube.com/watch?v=QgTm2TEt4Yc)（[朝内镜像](http://v.youku.com/v_show/id_XNTAzNDg5NjIw.html)）

[作者博客及详细说明](http://blog.dev001.net/post/40681591705/x-org-use-your-android-tablet-as-a-graphics-tablet)

*消息来源：* [XDA
Developer](http://www.xda-developers.com/android/android-gains-x11-support/)
