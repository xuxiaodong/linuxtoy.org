Title: Fedora Packages & Tagger
Date: 2012-01-17 10:28
Author: lovenemesis
Category: Web App
Tags: Fedora, packages, tagger
Slug: fedora-packages-tagger

提供在线软件包信息查找的 [Fedora
Packages](http://community.dev.fedoraproject.org/packages/)
和软件包元数据标签加注的 [Fedora
Tagger](http://community.dev.fedoraproject.org/tagger/) 测试版上线。

**[Fedora Packages](http://community.dev.fedoraproject.org/packages/)**

[![](http://linuxtoy.org/img/2012/01/fedora-packages.png "fedora-packages")](http://linuxtoy.org/img/2012/01/fedora-packages.png)

Fedora Packages
提供在线软件包信息搜索和查询的功能，相比现有直接在[远程构建平台
Koji](http://koji.fedoraproject.org/koji/) 查询的方式有如下优点：

-   支持对于软件包名、软件包标签（下面会提到）和软件包描述的**模糊搜索**。
-   直观的软件包依赖及层级关系图。
-   一站式的在线查看构建日志、更新日志、软件包内部文件、**补丁及 SPEC
    文件内容**。

下一步计划[和 openSUSE
社区合作](http://blog.linuxgrrl.com/2011/07/29/fedora-package-social-networking/#comment-5760)，进一步完善对于上游项目元数据的抓取。

目前 Fedora Packages 尚处于测试阶段，欢迎反馈意见～

**[Fedora Tagger](http://community.dev.fedoraproject.org/tagger/)**

[![](http://linuxtoy.org/img/2012/01/fedora-tagger.png "fedora-tagger")](http://linuxtoy.org/img/2012/01/fedora-tagger.png)

上面提到了 Fedora Packages 支持模糊搜索软件包标签，也就是和 yum
工具一样可以访问[Fedora
软件包数据库](http://admin.fedoraproject.org/pkgdb)里记录的软件包标签。那么这个标签是从哪里来的呢？
Fedora Tagger 就是提供给社区在线添加、评分软件包标签的工具（游戏？)。

使用（游戏？)规则如下：

-   Tagger 会随机呈现一个软件包。
-   社区成员可以查看软件包详情，为已有的标签评分，或者添加新标签。
-   每一个评分或者新添加的标签，都会影响自己的贡献点数，点数最终会影响显示排行榜中的名次。
-   登录使用 FAS 账户，支持 Gavatar 头像显示。

下一步的计划包括更好的与 PackageKit 及 GNOME Shell 整合（直接在 Shell
搜索框获取远程软件包信息），引入 [Mozilla Open
Badges](https://wiki.mozilla.org/Badges)
显示（开放式的徽章/奖杯系统）等。

目前 Fedora Tagger 尚处于测试阶段，欢迎反馈意见～

*消息来源：*[Máirín Duffy
博客](http://blog.linuxgrrl.com/2012/01/16/announcing-fedora-packages-and-fedora-tagger/)
