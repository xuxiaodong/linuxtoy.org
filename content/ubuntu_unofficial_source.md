Title: 推荐一个不错的 Ubuntu 非官方源
Date: 2006-06-14 15:11
Author: toy
Category: Apps
Slug: ubuntu_unofficial_source

这个源支持 Ubuntu Breezy 和
Dapper，里面包括一些不错的应用程序，现介绍如下。

-   gnormalize：各种音频工具的 GUI 界面，既可以将 CD
    中的音频提取出来，也可以转换音频文件，支持 MP3、MP4 (M4A 或
    AAC)、MPC (MPP 或 MP+ - Musepack)、OGG、APE (Monkey's audio)、FLAC
    和 WAV 等格式。同时还能编辑元数据 tag。
-   kdocker：这个小工具可以将应用程序最小化到系统托盘，支持
    GNOME、KDE、Xfce 等桌面环境。
-   glipper：这是一个剪贴板守护程序，它会自动保存剪贴板中的内容，以供重复使用。
-   youtranslate：它可以使用一些在线的翻译服务，比如你可以利用它来查询某个单词的含义。
-   alltray：将应用程序最小化到系统托盘的工具，与 kdocker 类似。
-   zim：一个 WYSIWYG（所见即所得）的文本编辑器，它的目标是将 Wiki
    观念带入桌面。
-   d4x：功能强大的图形下载管理工具。
-   checkgmail：是一个供替代的 Gmail 通知程序。
-   chatsniff：是 AIM、ICQ、MSN、Yahoo! 和 Jabber
    即时消息程序的监视工具，可以截获其聊天内容。
-   gcolor2：一个屏幕颜色拾取程序，虽然小巧，但很有用。
-   xvidcap：是一个视频捕获程序。

附：如何使用源？

1.`sudo gedit /etc/apt/sources.list`

2.添加下列内容：

(1)对于 Breezy  

` deb http://asher256-repository.tuxfamily.org breezy main dupdate french deb http://asher256-repository.tuxfamily.org ubuntu main dupdate french`

(2)对于 Dapper  

` deb http://asher256-repository.tuxfamily.org dapper main dupdate french deb http://asher256-repository.tuxfamily.org ubuntu main dupdate french`

(3)对于 Edgy  

` deb http://asher256-repository.tuxfamily.org edgy main dupdate french deb http://asher256-repository.tuxfamily.org ubuntu main dupdate french`

3.`sudo apt-get update`

4.安装你喜欢的软件

2007.3.12 更新：添加了用于 Edgy 的源，感谢 zhuqin\_83。

（Via [Asher256's
Repository](http://asher256-repository.tuxfamily.org/)）
