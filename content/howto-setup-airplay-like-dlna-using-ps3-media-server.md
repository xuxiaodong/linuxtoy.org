Title: 使用 PS3 Media Server 构建 DLNA 家庭媒体网络
Date: 2012-08-17 17:38
Author: lovenemesis
Category: Featured, Server
Tags: dlna
Slug: howto-setup-airplay-like-dlna-using-ps3-media-server

羡慕 [Win7 中的 Play
To](http://windows.microsoft.com/en-us/windows7/products/features/play-to)？
眼馋 [OS X 的 AirPlay](http://www.apple.com/itunes/airplay/)？ 您的
Linux 工作站也可以做到！

一年前本站介绍了 [DLNA 技术在 Linux
平台上的一些应用](http://linuxtoy.org/archives/linux-dlna.html)，这次将通过实例的方式说明如何使用
[ps3mediaserver](http://www.ps3mediaserver.org/) 架设 DLNA
服务，并允许家庭网络中各种设备浏览照片、音乐和视频。

**[PS3 Media Server](http://www.ps3mediaserver.org/) 介绍**

PS3 Media Server 是一款兼容 DLNA 协议的 UPnP 媒体服务器，使用 Java
实现跨平台图形界面和服务器进程，调用本地化的
[MEncoder](http://www.mplayerhq.hu/design7/news.html)、[FFmpeg](http://ffmpeg.org/)、[tsMuxeR](http://www.videohelp.com/tools/tsMuxeR)
实现媒体转换和重封装操作。

最初目标是为 PS3 提供媒体服务支持，现在已经成为全范围支持的 DLNA
媒体服务器，内置**适用于 XBox 360、Nokia N900、Android
手机、三星/索尼/飞利浦旗下电视以及各类进口/国产机顶盒的预置文件**，同时对前文中所介绍过的
XBMC 也有良好支持。

**PS3 Media Server
最强大的地方在于可以调用系统平台原生的转码和封装工具，将针对播放设备的特征在必要时进行格式实时转换，特别适合于影音文件类型复杂的用户。**

[![](http://linuxtoy.org/img/2012/08/pms-main.png "pms-main")](http://linuxtoy.org/img/2012/08/pms-main.png)

上图为同时连结了 XBMC、Sony 电视、PS3 和 Android 手机的 PS3 Media Server
。在 [1.6.0
版本](http://www.ps3mediaserver.org/forum/viewtopic.php?f=8&t=14861)中收录由在下**完全重做的简体中文本地化**，希望能进一步降低上手难度。

**[PS3 Media Server](http://www.ps3mediaserver.org/) 安装及配置**

这里以在 [Fedora 17 64
位系统](https://fedoraproject.org/zh_CN/get-fedora)为例。

在[配置好 RPMfusion
仓库](http://rpmfusion.org/)后，需要安装一些必要的软件包，可以在终端输入以下命令或者在添加/删除中搜索对应软件包：

`pkcon install java-1.7.0-openjdk ffmpeg mencoder`

当然后两者也完全可以自行从各自官网下载并编译。

在运行之前，根据情况需要打开 mDNS 防火墙的端口，Fedora
用户可以[参考该文中](http://linuxtoy.org/archives/howto-remote-control-linux-desktop-vlc-player-from-android-mobile.html)的“设置防火墙策略”部分。

PS3 Media Server 提供通用版本的预编译压缩包（内置 tsMuxer）和适用于 Deb
包管理系统的软件包，这里以通用版本为例。

双击解压后的目录中的 PMS.sh
文件，即可运行。第一次使用，可以到第三个标签页 General 那里设置下语言：

[![](http://linuxtoy.org/img/2012/08/pms-general.png "pms-general")](http://linuxtoy.org/img/2012/08/pms-general.png)

重启后生效。

默认情况下 PS3 Media Server 会将整个文件系统共享出来(当然依然遵循 Linux
文件权限)，这显然不是想要的。于是需要在“浏览/共享设定”页面中**将包含有视频、音乐和照片的目录**添加到共享列表中，如下图所示：

[![](http://linuxtoy.org/img/2012/08/pms-share.png "pms-share")](http://linuxtoy.org/img/2012/08/pms-share.png)

如果有需要调整编码器的设置，可以在下图的“转码设定”标签页中进行，不过默认的设置已经足够了：

[![](http://linuxtoy.org/img/2012/08/pms-transcode.png "pms-transcode")](http://linuxtoy.org/img/2012/08/pms-transcode.png)

这个页面中左侧列表中按类别区分了很多编码引擎，可以用下方的**上下箭头按钮调整使用顺序**，越靠上面的引擎越优先使用。如果想/不想使用某个引擎的话，可以用点击下方那个插头样的按钮进行切换。

所有配置完成之后记得点击最上方的“**重新启动服务器**”。

服务器端的配置就这些了，下面就来看看处于**同一个局域网内的各种播放设备**该怎么配置吧。

**其他操作系统上 [XBMC](http://xbmc.org/download/) 配置**

跨平台的 XBMC 是可谓是应用最为广泛的 HTPC 系统了，当下代号为 Eden 的
XBMC 11 默认就启动的 DLNA 客户端模式。

[![](http://linuxtoy.org/img/2012/08/xbmc-dlna.png "xbmc-dlna")](http://linuxtoy.org/img/2012/08/xbmc-dlna.png)

如上图，在添加文件中选择 UPnP Devices 即可看到网络中的 PS3 Media
Server。分别在照片、音乐和视频中配置添加即可。

**PS3 配置**

PS3 的设置很简单：

1.  确保网络设置中：打开了 UPnP 支持；允许连接媒体服务器。
2.  在 XMB
    跨界菜单的视频、音乐或者照片的任意一个分类下选择搜索媒体服务器，此时应该很快就能看到
    PS3 Media Server 的图标。
3.  点击进入即可执行回放或者其他操作。

对于 PS3 来说，会在分享目录下看到一些以 `#` 号包围的特殊目录，这些是 PS3
Media Server 虚拟出来的特殊目录，可以通过选定的方式直接实时调整 DLNA
服务器的一些设置，无需起身操作电脑。

更多详情可以参考[官方手册](http://manuals.playstation.net/document/en/ps3/current/settings/connectdlna.html)。

**Sony Bravia 电视配置**

Sony 从 2011 年开始上市的电视已经标配
DLNA，使用起来也很方便。在保证正常连接网络的情况下，按菜单键打开 XMB
跨界菜单，在视频、音乐和照片中就可以看到 PS3 Media Sever 的图标了。

**[Android 手机客户端
UPnPlay](https://play.google.com/store/apps/details?id=cx.hoohol.silanoid)
配置**

Android 平台上支持 DLNA 的程序非常多，这里以 UPnPlay
这款简单小巧的控制端/播放端为例。在安装 UPnPlay
启动后的首个屏幕上**点击左下角的地球样图标即可看到 PS3 Media Server**

[![](http://linuxtoy.org/img/2012/08/screenshot_2012-08-17_1318.png "screenshot_2012-08-17_1318")](http://linuxtoy.org/img/2012/08/screenshot_2012-08-17_1318.png)

之后通过 UPnPlay
就可以直接浏览共享目录下的文件，点击即可进行播放。UPnPlay
的视频播放是通过调用系统第三方播放器实现的，所以要保证手机上至少安装有一个视频播放器哦。

注意默认情况下点击文件右侧的加号是添加到播放列表，点击文件名是用当前文件替代现有播放列表，所以它会有“是否删除播放列表”的提示。

UPnPlay 除了可以实现在本地播放以外，还可以实现**控制其他 DLNA
客户端的播放**。比如在 Android 手机上选择文件，但是在另一台电脑或者 PS3
进行回放，在一个房间遥控另一个房间的电视去播放第三个房间电脑中文件不再是奢望（好拗口）！

**性能参考**

对于目标设备支持的格式来说，播放性能仅取决于网络带宽。

对于目标设备不支持的格式来说，需要分情况而说。若是仅仅是不支持所用封装容器，例如
SONY 电视仅支持播放封装在 MP4 容器中的 H264/AVC1
视频，无法直接播放常见使用 H264/AVC1 编码的 720P MKV。此时 PS3 Media
Server
仅需要做**重新封装**的操作，而无需重新编码，画质也是毫无损失的。在笔者的本本上**重新封装几乎是瞬时完成，不到
5 秒钟在客户端影片就可开始播放**。

若是使用的视频编码格式不兼容，例如在尝试在不具备 VP8
解码功能的设备上进行 WebM 格式的格式，PS3 Media Server 则会调用
**menconder** 进行实时转码，此时速度会比较慢，而且存在画质损失。

当然，纯音频文件的实时转码则是很快的，例如在 PS3 上播放 Ogg 音轨时。

**总结**

从中可以看出使用 PS3 Media Server 搭建可供各类设备访问的 DLNA
数字家庭网络是一件十分简单的事情，它独特的实时转码重封装功能可以允许某些设备播放缺乏原生支持的文件，比如
WebM、Ogg Vorbis 和 MKV 。通过调整 `PMS.conf` 也可以实现无 GUI
的启动模式，可以参考[论坛中的分享](http://www.ps3mediaserver.org/forum/viewtopic.php?f=3&t=902)。

相比 AirPlay 的特定设备需求，兼容 DLNA
的设备非常多，覆盖电视、手机、蓝光机、机顶盒、NAS
在内的各类产品。如果您的多媒体设备是 2011
年左右购入的外资品牌产品(国产机顶盒也有良好支持)，那么很大可能性已经支持
DLNA；也可以使用[DLNA
官方设备查找程序及智能手机程序](http://www.dlna.org/consumer-home/look-for-dlna)进行查看。
