Title: 跨平台飞信 LibFetion V1.2.0 发布
Date: 2009-11-29 21:22
Author: lovenemesis
Category: Instant Messenger
Tags: LibFetion
Slug: libfetion-v120-released

跨平台的第三方飞信客户端 LibFetion 最近发布了 v 1.2.0
版本，带来了全新的界面，并修正了定时短信的问题。

**该版本解决了以下问题（摘自[发布日志](http://www.libfetion.cn/VersionInfo%5CV1.2.0.txt)）：**

-   解决了移动服务器变更,手机号失败的问题(2009.11.17号出现的)。
-   解决V1.1内存泄漏问题。
-   解决V1.1出现奇怪分组"un set group"的bug。
-   解决V1.1好友积分显示错误的BUG。
-   解决V1.1程序设置字体问题。
-   增加给自己群发/定时短信。
-   解决Linux 64位系统崩溃问题，增强64位系统的稳定性。
-   屏蔽陌生人消息,彻底屏蔽那烦人的广告。
-   增加搜索好友功能,增加好友备注为空功能。
-   整理优化代码结构,提供程序性能。
-   完善程序界面皮肤,解决1.2测试版皮肤的各种小问题，解决提示框字体大的BUG。
-   同步完善苹果版本。

[Win 32
版本下载](http://libfetion-gui.googlecode.com/files/win-LibFetionV1.2_release.zip)

[Mac OS X
版本下载](http://libfetion-gui.googlecode.com/files/MacFetion_V1.2.0_Test.zip)

[Linux
版本源代码下载](http://libfetion-gui.googlecode.com/files/linux_fetion_v1.2.tar.gz)

[Fedora 12 i686 RPM
下载](http://dl.dropbox.com/u/464139/linux-fetion-1.2-1.fc12.i686.rpm)

[Fedora SRPM
下载](http://dl.dropbox.com/u/464139/linux-fetion-1.2-1.fc12.src.rpm)

**附: 源代码编译指南**

以 Fedora
系统为例，参考[此文](http://www.libfetion.cn/Docs-dve%5CBuild-LibFx-on-Fedora.txt)：

**1.** 安装编译依赖库

`su -c 'yum install qt-devel, libcurl-devel, gcc, glibc-devel, openssl-devel, gcc-c++, libstdc++-devel'`

**2.** 下载并解压缩上面的源代码包。

**3.** 进入解压缩后生成的目录，**依据架构分别运行** 以生成编译配置文件：

32 位： `qmake-qt4`

64 位： `./64_libfetion.sh && qmake-qt4`

**4.** 编译

`make`

**5.** 安装

`su -c './install.sh'`
