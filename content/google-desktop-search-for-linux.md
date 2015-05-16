Title: 体验 Google 桌面搜索 Linux 版
Date: 2007-06-28 21:27
Author: toy
Category: Apps
Slug: google-desktop-search-for-linux

正如之前消息所说的一样，[Google 桌面搜索 Linux
版在今天正式推出](http://googlechinablog.com/2007/06/linux-beta.html)了。目前发布的是
1.0 测试版，其版本号为 1.0.1.0060。相信有些 Linux
朋友已经在使用这个搜索工具了。笔者在下班之后，也对 Google
桌面搜索进行了体验。

**安装 Google 桌面搜索**

运行 Google 桌面搜索要求你的 Linux 系统至少满足下列条件：

-   Linux 内核 2.4.x 及更高版本
-   glibc 2.3.2 及更高版本
-   XFree86-3.3.6 及更高版本
-   gtk+2.2 及更高版本
-   fontconfig/xft
-   Mozilla Firefox 1.5.0.1 或更高版本
-   /home 分区具有 1 GB 可用空间

要在你的 Linux 系统中安装 Google
桌面搜索软件，可以采用以下三种方式之一：

1.  如果你所用的 Linux 发行版基于 RPM 的包管理工具，那么在下载 .rpm
    包后，可以执行下列指令安装：
    `sudo rpm -U google-desktop-linux-1.0.1.0060.rpm`
2.  假如你使用 Debian/Ubuntu Linux 发行版，则可以下载 .deb
    包并通过下列指令安装：
    `sudo dpkg -i google-desktop-linux_1.0.1.0060_i386.deb`
3.  或者你也可以使用 Google Linux 软件库，并通过该库来安装 Google
    桌面搜索。

    Debian/Ubuntu 可以使用下列源：

    `deb http://dl.google.com/linux/deb/ stable non-free`

    并添加密钥：

    `wget -q -O - http://dl.google.com/linux/linux_signing_key.pub | apt-key add -`

Google 桌面搜索软件默认的安装位置为 /opt/google/desktop/。

**Google 桌面搜索的使用**

你可以在终端中输入 `gdlinux` 指令来执行 Google
桌面搜索软件。程序启动后会在系统托盘显示图标，并开始利用计算机的空闲时间编制索引。此过程会消耗一段相当漫长的时间。

Google
桌面搜索软件的核心功能是搜索，它不仅支持搜索一般的文件、OpenOffice.org
文档、音乐、图片、邮件（包括
Gmail、Thunderbird）、网络历史记录，而且也支持对源代码、PDF、man、info
等进行搜索。这儿有两种方法对所需的信息进行搜索：

1.  使用 Google 桌面搜索主页。右击 Google
    桌面搜索在系统托盘中的图标，并选择“显示主页”菜单条目可以打开 Google
    桌面搜索的主页。这个主页看上去与 Google
    的默认搜索界面并无二致。相信接下来的操作无需我再绕舌。

    [![Google
    桌面搜索](http://i.linuxtoy.org/i/2007/06/gdl01_s.jpg)](http://i.linuxtoy.org/i/2007/06/gdl01.jpg)  
    *Google 桌面搜索主页*

    *小技巧：将地址栏中的 en\_US 更改为 zh\_CN，可以把英文界面的 Google
    桌面搜索即时切换为简体中文界面。*

    [![Google
    桌面搜索](http://i.linuxtoy.org/i/2007/06/gdl02_s.jpg)](http://i.linuxtoy.org/i/2007/06/gdl02.jpg)  
    *使用 Google 桌面搜索软件搜索文件*

    如果你需要实现更为精准的搜索结果，那么可以使用 Google
    桌面搜索所提供的高级搜索选项。

    [![Google
    桌面搜索](http://i.linuxtoy.org/i/2007/06/gdl03_s.jpg)](http://i.linuxtoy.org/i/2007/06/gdl03.jpg)  
    *Google 桌面搜索的高级搜索选项*

    你也可以根据自己的使用偏好来对 Google 桌面搜索进行定制。

    [![Google
    桌面搜索](http://i.linuxtoy.org/i/2007/06/gdl04_s.jpg)](http://i.linuxtoy.org/i/2007/06/gdl04.jpg)  
    *Google 桌面使用偏好*

2.  使用快速搜索框。只需按下 Ctrl 键两次，你便可以打开此 Google
    桌面快速搜索框。部分搜索结果会即时呈现在你的面前。
    [![Google
    桌面搜索](http://i.linuxtoy.org/i/2007/06/gdl05_s.jpg)](http://i.linuxtoy.org/i/2007/06/gdl05.jpg)  
    *Google 桌面快速搜索框*

**小结**

整个体验下来，感觉 Google 桌面搜索相当不错。Google
桌面搜索在计算机空闲时从后台编制索引，这对于系统资源的占用并不高。搜索的过程让人感到非常人性化，很注重用户体验。尤其是快速搜索框的设计也增色不少。但这并非说
Google
桌面搜索就没有任何缺点，如使用偏好中不能更改语言界面，对于其他浏览器（特别是
Opera 一族）或支持不佳或未予支持等。希望 Google
桌面搜索软件能够得到进一步地完善。

- [Download Google Desktop for Linux 1.0
Beta](http://desktop.google.com/zh/linux/download.html)
