Title: Archlinux 向 KDE 4.1 进军
Date: 2008-07-30 13:00
Author: toy
Category: News
Tags: Archlinux, kde4
Slug: archlinux-kde-41

[撰文/max0000]

KDE 团队在 7 月 29 日发布 [KDE
4.1](http://linuxtoy.org/archives/kde41_release.html)，这是第一个 KDE 4
的可用版本。为让 [Archlinux](http://linuxtoy.org/tag/archlinux)
用户及时赶上这次盛事，[testing] 源已经准备好了。请大家试用，及时上报
bug。

**升级之前要注意以下提示：**

-   这次升级不会很顺畅。因为旧版的 KDE 设置文件与 KDE 4.1
    并不完全兼容。旧的放在 ~/.kde 里，新版在
    ~/.kde4。这些文件不会自动转过来。你可以试试手动拷贝过去，看看行不行。对
    Kmail、Konqueror 和其它一些程序是可行的，另外一些则会给搞坏。也许
    KDE 会出个转换工具什么的。
-   如果想要使用 KDE 桌面，一定要安装 kdebase-workspace，这里边有
    Kdm、状态栏等等东西。
-   如果 pacman 问你要不要替换文件，当然要答 YES:-)
-   目前并不是所有的 KDE-based 包都重新打包过，好可以在新 KDE
    下使用。如果你等不及，可以再安装kdelibs3，就应当可以让这些旧点的软件运行。不过当然，等到
    KDE 4.1 进了 [extra]，这些都会搞好的。
-   如果你用 inittab 启动 KDM，记得把 /opt/kde 改成 /usr
-   不要进行强制升级 (-f)，有情况请报告 bug。
-   如果你不喜欢桌面，可以移动或是删除 ~/Desktop。
-   第一次登录要一点时间，别担心，它在建立设置文件。
-   如果你用 Nvidia 卡，请阅读
    <http://techbase.kde.org/User:Lemma/GPU-Performance>
-   新功能请参考 <http://www.kde.org/announcements/4.1/>
    ([中文](http://linuxtoy.org/archives/kde41_release.html))

目前，Kde 4.1 已进 [extra] 源。另据 Archlinux 官方测试，没有发现什么
bug。别向后看了！

[[来源](http://www.archlinux.org/news/402/)]
