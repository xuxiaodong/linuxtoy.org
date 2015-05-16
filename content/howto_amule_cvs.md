Title: 如何编译安装aMule 2.21 CVS
Date: 2008-07-23 19:51
Author: lovenemesis
Category: Apps
Tags: amule
Slug: howto_amule_cvs

跨平台的ED2K客户端 aMule 于上6月11日发布了期待已久的aMule
2.21版本。然而由于该版本的过渡性质，将不会有官方二进制版本发布。本篇文章主要介绍如何在
Linux 系统下编译安装 aMule 2.21 及 aMule CVS 版本。

aMule 2.21版本相比 aMule 2.13版本有以下变化（当前的 aMule CVS
版本相似），遗憾的是，依然不支持Low2Low。

-   模糊协议支持
-   UPnP 通用即插即用支持
-   网络协议升级至 eMule 0.49a (包括超大文件支持)
-   Kad 网络升级至 2.0 版本
-   增强了外观皮肤支持和国家旗帜显示功能
-   支持在 MS Visual Studio 下编译

下面以 aMule CVS 版本为例介绍如何从源代码编译安装，aMule
2.21版本类似。所用平台为 Fedora 8 X86\_64，其他 Linux 平台亦可参考。

**准备依赖库文件**

1.  首先确定已经安装了必要的编译工具，基本上有 gcc, make, pkgconfig,
    autoconf, automake, ccache就够了，以下命令安装 su -c 'yum install
    gcc make pkgconfig autoconf automake ccache'
    。或者用以下命令安装全部开发用工具 su -c 'yum groupinstall
    'Development Tools'' 。
2.  之后安装需要的库文件，依然用 su -c 'yum install wxGTK-devel
    GeoIP-devel libupnp-devel zlib-devel'。其中 wxGTK-devel 推荐使用
    updates-testing 资源库里的 2.8.7 版本， su -c
    'yum --enablerepo=updates-testing wxGTK-devel' 。
3.  aMule 需要的一个库文件 cryptopp 并不在 Fedora
    的软件仓库里，需要自己编译安装。从文末地址下载得到cryptopp552.zip
    文件后解压缩到一个目录并进入。如果你的 CPU 支持 SSE2
    扩展指令集并且所用 gcc 版本高于3.3，用任意文本编译器打开该目录下的
    GNUmakefile ，找到 ＃CXXFLAGS += -msse2
    把该行的注释去掉，打开SSE2支持，**显著提升**对共享文件的MD4和AICH速度（至少在我的
    Turion 64 X2 上如此）。 之后运行 make 编译， 用 su -c 'make install'
    安装到 /usr 目录下。

**编译安装aMule**

1.  从文末地址下载 aMule CVS 或 aMule 2.21，解压缩到并进入生成的目录。
2.  输入
    ./configure --prefix=/usr --enable-geoip --disable-debug --enable-optimize --enable-profile --enable-ccache 
    生成编译配置文件，如果没有问题的话将给出一个表格显示相关编译信息。如果需要远程控制或以守护进程方式运行的话，运行
    ./configure --help ，依据给出帮助信息添加相关选项。
3.  输入 make 编译，没有错误的话使用 su -c 'make install' 安装到 /usr。

**配置及建立 Firefox 下载关联**

1.  打开 Firefox 并在地址栏输入 about:config 右键点击下面任一键值，选择
    New －> Boolean，在 Preference Name 中输入
    network.protocol-handler.external.ed2k ，Value
    选择true。依照此法，New -> String， Preference Name 输入
    network.protocol-handler.app.ed2k ， Value 输入
    /usr/bin/ed2k。之后在你首次点击ed2k连接的时候 Firefox
    会弹出一个打开方式窗口，此时选择该窗口下方的的 Remember my choice
    即可完成 ed2k 下载关联的设置。
2.  aMule
    并不预置获取服务器地址的列表文件位置，需要自己设置。中文用户推荐在“网络”->ED2k
    的服务器列表文件地址处输入
    http://www.emule.org.cn/server.met，点击左侧的小箭头更新；“网络”->Kad
    的服务器列表文件地址处输入
    http://emule-inside.net/nodes.dat，点击左侧的小箭头更新。
3.  在防火墙中打开 aMule 默认使用的TCP 4662 UDP 4665和UDP
    4672端口。Fedora 8 在“设置”－“防火墙”－“其他端口”中添加， Kubuntu
    可以使用 guarddog 添加“自定义协议”。
4.  记得在 aMule 的设置-常规中输入自己的昵称！其余设置和 Win32 平台下的
    eMule 相似，不再赘述。

**下载地址**

[cryptopp552.zip](http://www.mirrorservice.org/sites/download.sourceforge.net/pub/sourceforge/c/cr/cryptopp/cryptopp552.zip)

[aMule 2.21  
](http://www.amule.org/files/download.php?go=2&file=170&mirror=262)

[aMule 2.21 非官方二进制包](http://forum.amule.org/index.php?board=69.0)

[aMule 每日 CVS 源代码包](http://www.hirnriss.net/?area=cvs)
