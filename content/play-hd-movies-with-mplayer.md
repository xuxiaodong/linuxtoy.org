Title: Linux 下使用 MPlayer 观看高清电影的三种解决方案
Date: 2009-02-22 19:02
Author: toy
Category: Tips
Tags: mplayer
Slug: play-hd-movies-with-mplayer

最近，MPlayer 官方网站刊载了一篇名为《[Video Acceleration and
You](http://www.mplayerhq.hu/design7/news.html)》的文章，该文简述了使用
MPlayer 来观看 1080 H.264 高清电影的几种方案，兹摘录如下，并加以说明。

1.  **VDPAU**

    VDPAU 即 Video Decode and Presentation API for Unix 的简称，它是由
    NVIDIA 针对 GeForce 8 及更新的系列所设计的一套
    API，既有解码，也有解码后处理，可以大幅降低 CPU 的占用率。

    目前，MPlayer 的 SVN 版本已经提供了针对 VDPAU 的支持，你将需要通过
    Subversion
    版本控制工具来[获取其源代码](http://www.mplayerhq.hu/design7/dload.html)并自行编译。同时，在播放时需指定
    `-vo vdpau -vc ffh264vdpau` 选项和参数。

2.  **FFmpeg-mt**

    [FFmpeg-mt](http://gitorious.org/projects/ffmpeg/repos/ffmpeg-mt)
    是一个包含多线程实验性功能的 FFmpeg 新分支，它可以充分利用多核或多个
    CPU 的优势，从而加快视频解码过程。

    FFmpeg-mt 的源代码可由 Git 取得，编译及安装可使用以下命令：

    `git clone git://repo.or.cz/mplayer && cd mplayer && git checkout origin/mt && git submodule init && git submodule update && ./configure && make && make install`

    同样，播放时需指定相应选项和参数：`-lavdopts threads=N`，其中 N
    即线程数。

3.  **CoreAVC for Linux**

    [CoreAVC](http://www.coreavc.com/) 据说是 Windows 平台下最好的 H.264
    解码器，包含多线程、多核（专业版）等支持，其最大的特色是快。通过
    CoreAVC for Linux 可以在 Linux 下使用 CoreAVC。之前，该项目曾被
    CoreAVC 的开发商要求关闭，后来经过沟通在 Google Code
    上得已重新开放。

    关于 CoreAVC for MPlayer
    的安装，可以参考这篇[安装指南](http://code.google.com/p/coreavc-for-linux/wiki/MplayerInstallation)。

    得益于好友 Dark 的帮助，我目前使用的即是这种方案。我的体验是，1080P
    的片子可以流畅播放，CPU 占用率在 40%~70% 之间徘徊（我的是 Intel
    Pentium Dual-Core E2140 CPU）；720P 的更低一些，大约在 10%~40%。

综上，第一种方案针对显卡的要求要高一些，我的 GeForce 7300GT
目前便无福消受；第三种呢，CoreAVC 需要额外花钱购买，专业版要 15
刀；第二种方案倒是非常值得一试。
