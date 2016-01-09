Title: 如何在 Linux 平台下看蓝光影碟
Date: 2013-04-05 00:20
Author: lovenemesis
Category: Featured
Tags: Blu-Ray, MakeMKV, VLC
Slug: howto-watch-bluray-movie-on-linux

随着蓝光光驱的价格逐步走低，这一未来高容量光存储介质也得到了更多人的认识。蓝光影碟更以它清晰的画面博得了电影发烧友的青睐。那么如何在 Linux 平台上欣赏蓝光影碟带来的视觉盛宴呢？

首先介绍下朝内通常能见到的几种蓝光影碟：

-   不具备任何版权保护的蓝光。这包括了蓝光个人影像光盘，和以 Blu-ray Ultra 为代表的 D 版蓝光。前者可能来自于 Nero Media Home 等多媒体剪辑软件的输出并刻录，一般目录结构为 AVCHD 或者 BDAV；而后者目录结构多为 BDMV。Blu-ray Ultra 实际上是使用特殊软件从正版蓝光提取出来，除去了版权保护机制，然后写入 BD-R 载体，有些甚至还放在山寨正版的包装盒中蒙骗消费者。不过相比于以双层 DVD 为载体的 Real Blu-ray 伪蓝光而言，Blu-ray Ultra 的真正蓝光介质至少在一定程度上保证了有足够的容量放下未经二重压缩的视频和音轨。若是制品者不是太坑的话，原盘中的幕后花絮和交互式内容也可能保留。
-   只有 AACS 加密的正版蓝光，仅见于海淘、音像店角落及收藏家手中，价格难以界定。属于早期蓝光制品，在 AACS 被爆掉之后就已经不再生产了。
-   使用 BD+ 和 AACS 加密的正版蓝光，当下主要的正版蓝光影碟，见于各大电商和蓝光形象店。尽管朝内土地在蓝光分区时被归于 C 区，不过为了考虑到朝内复杂的蓝光回放设备来源，实际上不少在朝内正规渠道发行的蓝光影碟都是没有区域码的。不过相对在其他地区发行的版本，在附加内容上就有一些缩水了。

下面以 Fedora 23 64bit 系统，[先锋 BDC-207BK 蓝光康宝](http://www.amazon.cn/Pioneer-%E5%85%88%E9%94%8B-BDC-207BK-%E8%93%9D%E5%85%89%E5%BA%B7%E5%AE%9D%E9%A9%B1%E5%8A%A8%E5%99%A8/dp/B00ABDWP7W/ref=sr_1_1?s=pc-components&ie=UTF8&qid=1365000933&sr=1-1)为例介绍如何在 Linux 下实现回放上面介绍的三种蓝光影碟。

在开始之前，请确保您的 Fedora 系统已经[启用了 RPMFusion 仓库](http://rpmfusion.org/Configuration)，并安装了 VLC Player：

`sudo dnf install vlc`

**无版权保护的蓝光影碟**

VLC 从 2.0 开始已经可以理解蓝光影碟所用的 BDMV 和 BDAV
的结构，只是到目前为止蓝光交互式菜单的一直没有实现。于是对于不包含版权保护的蓝光影碟是可以直接播放的。

[![](http://lt-file.b0.upaiyun.com/files/2013/04/vlc-bluray-295x250.png "vlc-bluray")](http://lt-file.b0.upaiyun.com/files/2013/04/vlc-bluray.png)

如上图，在 VLC 文件菜单中选择打开光盘，格式选择为 Blu-ray，勾选上 “No discs menu” 即可。注意若忘记勾选后者的话可能会导致 VLC 崩溃哦～

**仅使用 AACS 加密的蓝光影碟**

播放仅包含 AACS 加密的蓝光影碟需要两个额外部分组件，一是**公钥库文件**，可以从[这里下载](http://vlc-bluray.whoknowsmy.name/)（最后更新 2012 年 4 月 20 日），然后放置到 `$HOME/.config/aacs/` 目录下即可。

另一个组件是 AACS 的开源实现动态链接库，可以从 rpmfusion 仓库里获得：

`sudo dnf install libaacs`

之后即可使用和打开 Blu-ray Ultra 同样的方式在 VLC 中播放仅有 AACS 加密的蓝光影碟了。

**带有 BD+ 和 AACS 蓝光影碟**

对于增添了 BD+ 保护的蓝光影碟情况则要复杂很多，要求一个可供 BD+ 虚拟机来运行版本验证程序，实现检查播放环境是否满足 HDCP 的安全播放要求的工作。目前来看只有来自 [GuinpinSoft 的 MakeMKV](http://www.makemkv.com/) 可以比较完美的在 Linux 系统下模拟一个 BD+ 虚拟机并同时实现 AACS 解密。MakeMKV 是一款共享软件，其中 DVD 和 AVCHD 的流媒体及转码是免费的，对于蓝光则有 30 天体验的限制。不过目前它尚在 Beta 测试阶段，**所有功能完全免费使用**，在此获得[Beta 期间注册码](http://www.makemkv.com/forum2/viewtopic.php?f=5&t=1053)即可。

MakeMKV 由开源的设备驱动及图形界面，和闭源二进制的 BD+ 虚拟机实现等核心功能两部分组成。Linux 用户可以在[官方论坛](http://www.makemkv.com/forum2/viewtopic.php?f=3&t=224)免费下载到这两部分，分别为 `makemkv-oss` 及 `makemkv-bin`。

接下来需要安装一些编译所依赖的软件包。官方论坛中[列出了 Ubuntu 下的软件包](http://www.makemkv.com/forum2/viewtopic.php?f=3&t=224)，新版本已经支持使用 Qt5 构建。对于 Fedora 23 系统则可以使用如下命令安装：

`sudo dnf install gcc-c++ glibc-devel openssl-devel expat-devel ffmpeg-devel mesa-libGL-devel qt5-qtbase-devel`

然后分别解压之前的 `makemkv-oss` 和 `makemkv-bin` 压缩包，分别在各自的目录上执行以下命令，注意先从 `makemkv-oss` 开始 ：

`./configure`

`make`

`sudo make install`

然后再进入 `makemkv-bin` 目录：

`make`

`sudo make install`

从 MakeMKV 1.8.5 开始增加了一个 [libmmbd库](http://www.makemkv.com/forum2/viewtopic.php?f=10&t=7008)，模拟 libaacs/libbdplus 的接口，从而使得支持后两者的播放器可以在后台调用 MakeMKV 实现解码，实现直接播放，非常方便。具体实现方式如下，以 MakeMKV 默认安装位置为例：

若您已经安装了 AACS，请先移除：

`sudo dnf remove libaacs`

之后创建 libaacs/libbdplus 到 libmmbd 的符号链接：

`cd /usr/lib`

`sudo ln -vs libmmbd.so.0 libaacs.so.0`

`sudo ln -vs libmmbd.so.0 libbdplus.so.0`

至此 MakeMKV 安装配置完成，剩下的操作就非常简单了。像播放无 DRM 的蓝光光碟一样，在 VLC 文件菜单中选择打开光盘，格式选择为 Blu-ray，勾选上 “No discs menu” 即可。

注意**首次使用前**需要先启动 MakeMKV 程序，在帮助中填写获得的[注册码](http://www.makemkv.com/forum2/viewtopic.php?f=5&t=1053)。之后直接用VLC 播放即可。

使用华纳在朝内正版发行的哈利波特蓝光全集测试，所有影片均可正常播放，中文字幕亦可调出。

除了可以将蓝光回放以外，MakeMKV 如同名字所示还支持从蓝光影碟生成 MKV 格式的文件，实现 **BDRip备份**的功能。另外根据不完全测试结果显示它还可以**绕过蓝光区域码的限制**。甚至还可以架设成媒体服务器，实现远程回放，使用 VLC for Android 即可，不过注意需要千兆网络才可流畅。

MakeMKV 支持 Win32/64，Linux 32/64 及 OS X x86 以上操作系统，也是**目前OS X 和 Linux 系统下唯一能曲线实现正版蓝光影碟全区回放的方案**。未来 Beta 测试结束之后[50 欧元的注册费用](http://www.makemkv.com/buy/)贵不贵，则由您自己考量咯～

**总结**

作为高清影片的指定光学载体，当下蓝光影碟在 Linux 系统上的回放仍有相当长的道路要走。MakeMKV 作为 OS X 和 Linux 下的唯一可行方案，仍有一定的上手难度。尽管当下免费，但未来稍微偏高的注册授权费用，也是需要谨慎考虑的。
