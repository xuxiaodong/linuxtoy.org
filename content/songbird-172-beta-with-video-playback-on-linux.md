Title: Songbird 1.7.2 Beta Linux 版本带来视频回放支持
Date: 2010-04-24 19:52
Author: lovenemesis
Category: Music Player
Tags: Songbird
Slug: songbird-172-beta-with-video-playback-on-linux

自从 Songbird 宣布将[研发重心转移到 Win32 和 OS X
平台后](http://linuxtoy.org/archives/shortnews-audacity-songbird-firefox.html)，不少
Linux 用户纷纷转移到其他播放软件。在下也是在昨天 Rhythmbox
不断僵死之后才又决定试下前段时间低调发布的 Songbird 1.7.2 Beta
，结果惊喜！

1. 原先跟 **gstreamer python 绑定冲突的问题解决**了，解压后直接
./songbird 即可运行。

2. 启动速度得到提升，**跟 Rhythmbox 启动速度接近**。不知道是不是更新到
xulrunner 新版本的缘故（？）。

3. 经过测试，**支持 OGV 和 MP4 视频回放**， 看截图：

[![](http://i.linuxtoy.org/images/2010/04/songbird_video_ogv-300x187.png)](http://i.linuxtoy.org/images/2010/04/songbird_video_ogv.png)

[![](http://i.linuxtoy.org/images/2010/04/songbird_video_mp4-300x187.png)](http://i.linuxtoy.org/images/2010/04/songbird_video_mp4.png)

个人猜测 MP4 回放可能需要本地安装相应的 gstreamer
解码器，不过相信诸位都懂得，不赘述……

除此之外，该 Beta 版本还带来了 Win7 平台支持和对于 SD 卡的同步功能。

[其他平台的视频回放支持格式信息](http://wiki.songbirdnest.com/Docs/Video_Codec_Support)

[英文博客原文](http://blog.songbirdnest.com/2010/04/15/songbird-1-7-b1-available-for-download/)

[1.7.2 Beta 1
全平台下载地址](http://wiki.songbirdnest.com/Developer/Articles/Builds/Nightly_Builds)

**PS**: 这篇 Linux Magazine 上关于 [Songbird 和 Linux
的评论](http://www.linux-mag.com/cache/7761/1.html)文章值得一读。
