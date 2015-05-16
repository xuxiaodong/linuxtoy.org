Title: Mesk：简洁而朴实的音乐播放器
Date: 2007-04-22 11:52
Author: toy
Category: Apps
Slug: mesk

在 Linux 中，我已经使用过好几个音乐播放程序，但在看到
[Mesk](http://mesk.nicfit.net/)
的那一瞬，我还是愿意花些时间来作些尝试。Mesk 最近刚刚发布了 0.3.0
版，我的体验过程正是以此版本为基础而展开的。

从下载 Mesk 的源代码到最终完成编译安装颇费了一些时间。由于 Mesk 使用
PyGtk 开发，后端又采用的是 GStreamer
多媒体框架，所以在[准备依赖时相关的包](http://trac.nicfit.net/mesk/wiki/README)是必不可少的。

[![Mesk](http://i.linuxtoy.org/i/2007/04/mesk_s.png)](http://i.linuxtoy.org/i/2007/04/mesk.png)  
*Mesk 主界面截图*

在使用 Mesk 时，它让我感觉到除了像能够播放 mp3、ogg vorbis
等格式的音乐文件及
CD、支持播放列表、可以随机或者重复播放等基本的功能之外，还具有以下一些好的特性：

-   Mesk
    的界面足够简洁，其布局仅包含一些基本的元素，显得十分紧凑。另外，Mesk
    包含一个更加精简的界面模式，该模式可以使用 Alt+C 打开。
    [![Mesk Compact
    Mode](http://i.linuxtoy.org/i/2007/04/mesk-compact_s.png)](http://i.linuxtoy.org/i/2007/04/mesk-compact.png)  
    *Mesk Compact 模式截图*
-   Mesk
    支持标签页的播放列表，这使你能够随时在多个播放列表中切换。而且，播放列表可以导入/导出。在
    Mesk
    的播放列表中还有一个比较有意思的功能，那就是你可以把想要优先播放的歌曲添加到播放队列中。这样，那些队列中的歌曲就会先于列表中的其他歌曲而播放。你也可以搜索播放列表，按
    / 可以激活此功能。
-   Mesk 包含可以扩展其现有功能的插件系统。目前，在 0.3.0
    版本中自带的插件包括：Audioscrobbler 插件（为了支持 last.fm）、Album
    Artwork 插件（可通过 Amazon.com 下载缺少的专辑封面）、以及 Gajim
    Status 插件（改变 Gajim 状态信息）。
-   Mesk
    可以显示专辑封面，并具有系统托盘等功能。前者可以为听者增加更多的情趣和对于歌者的感性认识；而后者无疑能够节省桌面空间，以便更好的开展其他方面的工作。

总体看来，Mesk
并没有华丽的面孔，它显得有些朴实。在功能方面，尚有一定的扩展空间，如增加更多音乐文件格式的支持、引入对于
iPod 的支持等。

[![Mesk
About](http://i.linuxtoy.org/i/2007/04/mesk-about_s.png)](http://i.linuxtoy.org/i/2007/04/mesk-about.png)  
*Mesk 关于对话框*

Download [Mesk 0.3.0](http://mesk.nicfit.net/releases/)
