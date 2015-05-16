Title: Yum 未来展望
Date: 2011-08-06 11:33
Author: liangsuilong
Category: Package Manager
Tags: Fedora, RPM, yum
Slug: yum-future

Yum 3.2 不知不觉已经用了三四年，一直在 x.y.z 版本号的 z 不断更新。最近
Yum 跳上了 3.4 版本了。

Yum 3.4 在今年的四月份就已经开始了，现在还处于整理代码和 API
阶段，并没有增加多少新功能。但是在 Yum
的官方网站列出了它的路线图。按照原定计划，Yum 会在 2011
年增加相当多功能。部分特性如下：

-   并行下载
-   后台下载
-   Updater 和 safe-update 插件
-   若干 API 和文档的整理

其中并行下载和后台下载是他们认为比较难实现的功能，不过他们会力争在 2011
年内实现，这似乎是他们自己定的硬指标。

此外他们也列举了一部分广大人民群众希望他们能够实现的功能，但是这些功能不会是硬指标，看看开发者什么时候有空再折腾。有几个特性会

-   Metadata
    的增量更新（个人认为这个功能相当重要，但是开发者认为难度很大。）
-   Presto 插件合并到 yum 的核心层，并且可以处理 installonly
    选项和非安装包
-   Python 3 的支持
-   使用 xz 压缩格式打包 metadata 以减小压缩下载体积

详情可以看 <http://yum.baseurl.org/wiki/YumFuture>

PS1：某老外在两年前 YY 过 yum-emerge
的东西。<https://fedoraproject.org/wiki/User:Baard/Yum_Emerge>

PS2：最近 Fedora 15 的 yum-3.2.29
有所调整，可能会导致在安装新软件包和更新的时候出现错误。如果遇到这种问题又解决不了的话，可以到
Koji 下载最新的包安装。
