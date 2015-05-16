Title: HTC Tattoo 两三事
Date: 2009-12-04 05:21
Author: lovenemesis
Category: Funny
Tags: Android
Slug: something-about-htc-tattoo

在观望了很久智器的 V5 后，本人一周前用省吃俭用的钱入手了 HTC
Tattoo。折腾了这么一周，在这里随便聊聊这个基于 Linux
核心的设备。**提醒：软文，慎入！**

HTC Tattoo 是 HTC 公司推出的入门型 Android 系统手机，目前固件版本
1.6，基于 **Linux 2.6.29**
核心。[详细硬件配置](http://www.htc.com/europe/product/tattoo/specification.html)

**开机速度**

在入手前，在视频中就发现这个机器开机速度不是一般的慢。自己的两年前购买的
Turion 64 X2 本本，运行 Fedora 12 i686 ， 加载 VBox 和 Nvidia
官方驱动，bootchart 的时间为 32 秒；而 Tattoo
的时间在**50秒**左右，可能跟需要加载 HTC 定制的 HTC Sense
有关。幸好开机过程中出现 Android 的小绿人还是比较 Cute
的（女友说它是**绿虫子**……）。

**声音、视频与多媒体**

开机过程中声音是无法关闭，有些恼人……

声音部分应该是用的 ALSA，不知道有没有像 Palm WebOS 一样使用
[PulseAudio](http://www.pulseaudio.org/)
这样的事件驱动的音频服务器，不过至少它可以针对不同的音频源（来电、消息、邮件、提醒、媒体）单独调节音量。

视频部分大家都知道 **Android 没有使用 X Window** 架构，不再赘述。3D
方面支持 **OpenGL ES**，不过 Tattoo 运行经典的 Qualcomm NeoCore
测试程序有严重的贴图错误，可能是兼容性问题。

Android 系统的多媒体框架是由 PacketVideo 提供的
[openCORE](http://www.pv.com/products/android/index.html)。从目前的状况来看距离
[gstreamer](http://www.gstreamer.org/) 和
[xine](http://www.xine-project.org/home)
这两个多媒体框架差距不小，分离器和解码器都少的可怜。

我可以很负责的说，**开源音频格式 ogg** 是可以播放的，尽管在 HTC
的详细参数里根本没有提到。硬盘上 6G 的 ogg 音乐可以挨个听了~  
FLAC 没有试，不过没有看到库文件，应该不行。

单纯的播放器来言，目前作为绝大多数开源播放器解码器部分的 ffmpeg 的
Android 实现才起步不久，常见的 AVI (Xvid+MP3)，mkv(x264＋AC3) 和 RMVB
完全没戏。

目前在 openCORE 框架下能播放的视频局限在 **MP4 (H264+AAC)**，用一个叫
[Meridian Player
Noble](http://andappstore.com/AndroidApplications/apps/Meridian_Player_Noble)
可以获得字幕支持。理论上讲 [Avidemux](http://avidemux.org/)
应该可以很好的转码，但是 Fedora 12 rpmfusion 里的 Avidemux 并没有包含
FAAC 编码器，在加上 x264 的编码速度，我就不折磨本本了……

另外 HTC 说自己支持 WMV9，当然我是绝对不会去试的……

**蓝牙**

Tattoo 所用的 Android 1.6
系统的**蓝牙是个残废**，不支持文件传输，也不支持声音服务器……  
~~[GNOME
2.28](http://library.gnome.org/misc/release-notes/2.28/#rnusers.bluetooth)
里对蓝牙管理器的改进在 Tattoo 上完全体现不出来……~~ 用 GNOME
的蓝牙管理器没有办法给 Tattoo 传送文件。

幸好 Android 2.0 有改善，静候固件……

**办公软件**

Android 比较诡异的是没有开源的 **txt 文本编辑器**，免费的也没有…… 很怀念
Palm Zire72 上的 cardTXT ……

[DocumentsToGo](http://www.dataviz.com/products/documentstogo/android/index.html)
支持 M$ 系列文档查看编辑和 PDF 查看，12月6日前购买仅需 $10。

OpenOffice.org 在可见的未来是不会有
[Android](http://user.services.openoffice.org/en/forum/viewtopic.php?f=49&t=10305)
版本的（但不是[完全无望](http://eric.bachard.free.fr/news/2009/10/android-openofficeorg-port.html)）。目前
Android 仅有一款支持 ODS 数据表格式（还不是更常用的 ODT 文档）的软件
[Androffice](http://www.androffice.com/)。

辞典方面，有一款名为
[ColorDict](http://andappstore.com/AndroidApplications/apps/ColorDict_Universal_Dictionary)
的软件，支持**星际译王的辞典**，支持 QuickSearch
整合，相当优秀，很不错~就是不能真人发音……

**文件系统**

由于 Tattoo 暂时还没有第三方固件，**无法获得 root
用户权限**，查询不了更多的信息。不过根文件系统用的 ext 系列的（ext3
应该）没什么问题，因为有 tune2fs 工具。

郁闷的是存储卡上放置一般数据的分区只能是 vfat，我将 microSD
卡在本本上格式化成 ext3 放入后直接提示错误。看来是 fstab
部分限定了首个分区类型……  
**我要 ext4 ！！！我要和 M$ 不兼容！！！**

**软件市场**

Android Market
按地区划分这点我之前完全不知情，以为现在把软件还按地区划分只有 Nintendo
能做的出……  
更加郁闷的是由于 Tattoo 的分辨率比其他 Android 小(**320*240**)，所以
Market 会把指定屏幕最小分辨率的程序都过滤掉了……  

其实大多数程序也是可以运行的（下面没有了……），不过就要通过其他途径去获得了，颇费周折……

另外不象 AppsStore，Android Market
只能通过**手机访问**，无法通过网络下载。意味着如果不适用第三方软件，固件升级后的软件重装将是流量噩梦……

**GPL 协议**

Google 在这方面还是做到了。在系统的设置菜单里很容易就能找到 Android
系统所用的**开源组件的相关协议**，包括 Linux
Kernel、SQLite、Vorbis、Gzip、bz2、iptables、wpa\_supplicant、dhcpd、pppd、png、FreeType、WebKit
等。不知道 Palm 新的 WebOS 在这方面做的如何。

HTC 自己的部分组件也以 **APL 2.0
协议**开源了，比如相册、相机和媒体播放器。

**开发环境**

本站介绍过如何安装和配置 [Android
SDK](http://linuxtoy.org/archives/howto-set-sup-android-sdk-under-fedora.html)，经过测试对于最新的
Eclipse 和 Android SDK 2.0 依然适用。

不过要注意的是，新的 udev 对于 **Android
的设备权限处理**有问题，如果像上文中将 Android SDK
安装在用户目录下，必须用 `su` 获得 root 权限（`su -`
不行的，原因自己想啦~）才可以使用 adb 。

目前看到两个 Android 平台下的开源项目，觉得还不错，一个是**飞信客户端**
[AnFetion](http://code.google.com/p/anfetion/)，一个是提供很多基础应用（比如文件管理器）的
[OpenIntents](http://code.google.com/p/openintents/) 。

**Java 和 Dalvik （口水警告）**

Android 目前主要开发语言是 Java，所有程序都运行在与 **JavaME 不兼容**的
Dalvik 虚拟机上。逛了几个论坛，不少人对此有异议，认为让 Dalvik
垃圾收集器管理内存会影响性能和耗电，于是论坛上很火的帖子是XX版的任务管理器，认为手动结束进程就能释放内存，提高性能并省电。

在此不想多说什么，只是自己印象中的 **Linux
内核内存管理**（阅读陈莉君老师的书,2.4
内核），并不是进程终结了就立即将进程对应内存页交换出去的。于是乎上面那种手动结束进程的方式似乎并不能起到“提高性能并省电”的效果。

并不确定现在 2.6.29 内核是什么样子， Android
所用的内核是不是又在内存管理方面有变化，以上只是推测。不过个人装了不少程序，很少手动结束进程（通过某国产的文件管理器），互相切换并没有感觉到什么延迟。

**结束语**

作为开源狂热者，我对这台 HTC Tattoo 还是基本满意的，希望以后 Android
在办公软件和文件系统上能做的更好，至少让 microSD 用户分区**支持 ext4**
！！！

目前热切期待 **Firefox for Android** 中……

[Firefox Mobile 主页及宣传视频](http://www.mozilla.com/en-US/mobile/)

[Gecko Android port Wiki](https://wiki.mozilla.org/Android)
