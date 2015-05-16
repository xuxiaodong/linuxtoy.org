Title: Fedora 17 中的 KDE Plasma 桌面小程序自动依赖解决
Date: 2012-05-17 16:43
Author: lovenemesis
Category: Desktop Stuff
Tags: Fedora, KDE
Slug: fedora-17-kde-plasma-widget-automatic-dependency-resloving

包含大量创新性功能的 Fedora 17 也不会忘记 KDE 用户群体，率先实现了 KDE
Plasma 桌面小程序控件的依赖关系自动解决。

Plasma 桌面小程序具有两种不同的形式：

-   使用 C++ 撰写的小程序只能通过发行版打包或者自己编译的方式安装。
-   使用各式脚本语言并遵循[开放互联服务标准(OCS)](http://www.freedesktop.org/wiki/Specifications/open-collaboration-services)的可以通过
    Plasma 内置的下载对话框进行安装和管理。

为了实现小程序的正常运行，又有两方面的东西需要安装：

-   脚本引擎：如果小程序是用脚本语言编写，那么对应语言的脚本引擎是必需品，否则小程序将抛错拒绝工作。
-   数据引擎：各种提供应用程序所需要的数据内容的组件，若是没有则小程序运行异常。

目前各类发行版对于以上这些问题的处理方式有：

-   仓库中的小程序由发行版打包者人工处理依赖关系，但是问题是工作量巨大且容易出错。
-   对于互联网提供的诸多小程序则完全交由最终用户去解决依赖关系问题，不可避免会遇到很多异常和抛错。

在 Fedora 17 中通过 KPackageKit/Apper 与 KDE
上游社区的合作，**三种途径同时发力去解决 Plasma 的依赖关系**：

-   上游要求 Plasma 小程序在元数据中明确指定依赖关系。
-   安装过程中 KPackageKit/Apper 从源代码中抓取依赖关系。
-   在小程序运行时再下载所缺失的依赖关系。

于是乎 Fedora 17 KDE 的用户将从此告别 Plasma
小程序依赖关系所带来的烦心问题了。

秉承 Fedora
一贯坚持的上游紧密合作传统，该功能已经合并入上游，很快**所有使用
PackageKit 的 KDE 发行版**都将可以享受到它带来的便利（使用 aptdaemon 的
Kubuntu 于此无缘）。

[该功能详细说明](http://fedoraproject.org/wiki/Features/Plasma_PackageKit_Integration)
