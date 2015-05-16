Title: Vuze 4.X 系列简体中文汉化版
Date: 2009-02-07 00:29
Author: lovenemesis
Category: BitTorrent Client
Tags: vuze
Slug: vuze4-series-simplified-chinese

Vuze（ Azureus），是一款在 BitTorrent 发展历史中做出过重大贡献的
BitTorrent
软件。现在已经发展为一体化的高清视频发布平台。本人在原有汉化文件的基础上，针对新的
Vuze 4.X
系列做了大量的修订（尚未100%完成）。现将本地化文件分享出来，欢迎大家测试并提出宝贵建议。

**使用方法：**  
1. 因为 Vuze 是一个基于 Java SWT 的程序，所以需要 Java 运行时环境。  
一个选择是前往 [Sun
开发者中心](http://java.sun.com/javase/downloads/index.jsp) 或者
[Java.com](http://www.java.com/zh_CN/) 下载并安装对应系统的Java
运行时环境即可。前者的版本通常较新些，不过对于用户来讲区别甚微。  
**注：**在 Linux 平台下如果要正确显示中文的话，需要在 Java 运行时环境的
lib/fonts 目录下建立一个 fallback 目录，并将所需字体复制一份到 fallback
目录下。  
如果使用的是较新的 Linux 发行版，就可以选择安装开源的 OpenJDK
版本。使用发行版的软件管理工具搜索并安装 openjdk 即可。  
如 Fedora 10 的朋友可以在终端使用

`su -c 'yum install java-1.6.0-openjdk'`

安装。

2.下载并安装 Vuze 4。  
可以选择从 [Vuze.com](http://www.vuze.com/) 或者
[SourceForge.net](http://azureus.sourceforge.net/) 上。  
Windows 下和 Mac OS X 的安装无需多说。  
Linux 版本下载后得到一个 tar.bz2 包，解压到任意位置，生成一个名为 vuze
的文件夹(这个目录就是 Linux 版本的“安装目录”)，使用双击其中的 vuze
脚本，选择运行即可启动程序。

**注：** Vuze 需要 Adobe Flash Player 才可以显示 Vuze HD Network
门户站点的一些内容。在 Fedora 10 系统上会在
/usr/lib/xulrunner-1.9/plugins 目录下查询 libflashplayer.so
文件。而通常情况下 Flash Player 会安装到 /usr/lib/mozilla/plugins/
下，所以需要创建一个相应的符号联结，在终端使用以下命令：

`su -c 'ln -vs /usr/lib/mozilla/plugins/libflashplayer.so /usr/lib/xulrunner-1.9/plugins/libflashplayer.so'`

另外，Vuze 4 可以使用系统上已经安装的 Mozilla Firefox 3
进行页面渲染，在“工具”-“选项”-“界面”-“显示” 中可以指定 Firefox 3
的安装路径，Linux 系统下推荐使用稳定的 /usr/lib/xulrunner-1.9/
，而不是经常变化的 /usr/lib/firefox-3.0.{4,5,6}/

**记得在防火墙上打开相应端口！**  
Fedora 10 GNOME
的用户可在“系统”-“管理”-“防火墙”中的“其他端口”中添加需要打开的，Vuze
使用的端口号可在 “工具”-“选项”-“连接”中找到。

Vuze
有很多的插件，提供了各种各样的功能，有兴趣的朋友可以在“工具”-“插件”中探索。在此推荐一款名为
Mainline DHT 的插件，添加了对主流 DHT 协议的支持。

3.下载语言文件

**目前简体中文汉化已经进入 Vuze 4.2.X
的官方安装包中，只需要直接下载即可拥有简体中文界面！**

~~从以下链接下载语言文件，将解压后得到的
MessagesBundle\_zh\_CN.properties 放置在 Vuze 的安装目录中，保持与
Azureus2.jar 文件在同一目录下。重新启动 Vuze 即可看到简体中文版本了。~~

汉化效果见下图(Fedora 10 + OpenJDK IcedTea 1.4)：  

[![](http://i.linuxtoy.org/images/2009/02/screenshot-vuze.png)](http://i.linuxtoy.org/images/2009/02/screenshot-vuze.png)

~~**PS:**  
其实这个东西早都汉化好了，但是本人通过各种途径都无法引起 Vuze
项目组的注意，所以目前都还没有进入官方包中，也因此**在翻译人员列表中并没有本人ID**。在此将它“提前”分享给诸位也是希望能让国内的朋友更多的接触到这个高清视频发布平台，并对本人的翻译提出意见。~~

**为了避免不必要的口水，在此多罗嗦几句：**  
1. 对于 Java 抱有非理性偏见的朋友不要尝试；  
2. 如果您仅仅是需要一款 BitTorrent
下载软件的话，它对您来说有太多又不上的功能，Deluge 和 Transmission
是更好的选择；  
3. 如果您的机器配置较低内存小于256M，不推荐，它需要大约150M的内存；  
4. 如果您对于高清视频并没有太大兴趣， [Miro](http://www.getmiro.com/)
也是一个不错的选择 。
