Title: SMPlayer 0.6.0 Final 发布(更新0.6.1)
Date: 2008-05-17 10:23
Author: lovenemesis
Category: Movie Player
Tags: mplayer
Slug: smplayer-060-final-%e5%8f%91%e5%b8%83

5月14日，MPlayer 的跨平台图形前端 SMPlayer 发布了 0.6.0 Final 版本。
SMPlayer 致力为所有平台的用户提供图形化的从基本的播放视频、DVD、VCD
到调整滤镜等高级设置的 MPlayer 功能。

5月29日，SMPlayer 发布了0.6.1版本，进行了小幅度改进。

**0.6.1 版本包括如下更新：**

-   精简模式下依然保持窗口外观，而不是以前的只有黑色边框。
-   在“首选项－杂项”中增加了一个 “GUI 选项”，可以允许用户选择 "Mini GUI"
    模式，该模式下仅显示最基本的控制按钮。
-   修正了使用Qt 4.4 编译时 设置－FAQ 中帮助菜单失效的Bug。
-   (Windows) 修正了使用 DirectX 作为视频输出时缩放工作不正常的Bug。
-   添加了加泰隆语翻译。

**0.6.0 final 版本包括如下更新：**

-   修正打开一个文件时同时运行两个 MPlayer
    进程的问题，以前这个问题可以导致 Windows Vista 的 Aero 特效被禁用。
-   时间轴浏览功能现在工作的更流畅了。
-   可以将目录中包括子目录在内的文件一次性添加到播放列表中。
-   为播放列表增加了一个首选项菜单。
-   鼠标右键的功能可以自定义配置。
-   (Linux) 文件管理器应该会显示一个把文件添加到 smplayer
    播放列表的选项。
-   修正在启动时播放列表会自动显示一会儿的问题，以前这个问题在 compiz
    会导致窗口无法隐藏。
-   修正 Qt 4.4 下无法显示logo的问题。
-   更新了部分本地化文件，包括 Simplified-Chinese, Italian, Ukrainian,
    Dutch, French, Romanian, Portuguese, Polish, Russian, Japanese,
    Spanish and German。
-   现在 Install.txt 包含了更新后的 smplayer 编译和安装指南。

下载及更新日志见[这里](http://www.qt-apps.org/content/show.php/SMPlayer?content=61041)。

**附：Fedora 8 X86\_64 下如何编译及安装**

1.  确定安装了qt4开发包。使用 yum install qt4-devel.x86\_64 即可完成。
2.  解压 smplayer-0.6.0final.tar.bz2 得到 smplayer-0.6.0final
    目录，进入该目录。
3.  使用 make QMAKE=qmake-qt4 PREFIX=/usr/ 编译。
4.  使用 root 权限安装 su -c 'make install'
5.  接下来就可以在"多媒体"中找到 SMPlayer 了。

