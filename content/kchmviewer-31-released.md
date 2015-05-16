Title: KchmViewer 3.1 发布
Date: 2007-06-17 21:30
Author: toy
Category: Apps
Slug: kchmviewer-31-released

[KchmViewer](http://www.kchmviewer.net/)，很不错的 CHM
类格式电子文档阅读工具。这个 3.1 更新版在昨天发布。该版本为 bug
修订版，无新功能增加。追求稳定可靠的朋友可及时升级。

![KchmViewer](http://i.linuxtoy.org/i/logo/kchmviewer.jpg)

此版本主要解决的 bug 包括：

1.  为 Gentoo 修正了区域和 .desktop 安装目录的问题。
2.  提升了搜索引擎索引的速度。
3.  修正了使用 URL 从浏览器调用 KchmViewer 的问题。
4.  修正了 CHM 文件中使用 Unicode 编码的索引/主题文件名的问题。
5.  修正了 64 位平台的兼容性问题。

总体上看，新的 KchmViewer 版本将更加稳定。另据开发者称，此版本也将作为
Qt3 支持的最后一个版本。下一个版本将基于 Qt4，版本号将为 4.0。

KchmViewer
以源码包形式发行，在使用它之前，你需要编译它。下面是简略编译介绍：

1.  检查你的 Linux 系统是否安装有 qt3-devel 包，如果没有，请安装它。
2.  如果你要编译 KDE 版本，则请检查是否安装 kdelibs3-devel 包。
3.  编译独立版本，执行 `./configure && make`。
4.  编译 KDE 版本，执行 `./configure --with-kde && make`。

- [Download KchmViewer
3.1](http://sourceforge.net/project/showfiles.php?group_id=135500)
