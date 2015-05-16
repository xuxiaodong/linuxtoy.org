Title: Fedora Copr
Date: 2014-01-15 10:15
Author: lovenemesis
Category: News
Tags: Fedora
Slug: fedora-copr

Fedora Copr（读作 /kä'pər/，意为 **Cool Other Package Repositories**
）新版上线，为 Fedora/EPEL/CentOS 社区带来了类似 PPA 的体验。

Copr 后端使用 [Fedora Koji
构建系统](http://koji.fedoraproject.org/koji/)，它不仅希望能简化第三方
RPM
仓库的创建，还希望能成为一个轻量级、易于维护且具备插件支持的构建环境。

使用 Copr 构建的软件包依然需要遵循 [Fedora
允许的分发类型](https://fedoraproject.org/wiki/Licensing)，依然不可以构建[严禁项目](https://fedoraproject.org/wiki/Forbidden_items)。

Copr 还提供了 [json 风格 API](http://copr.fedoraproject.org/api/)
及[命令行客户端](https://apps.fedoraproject.org/packages/copr-cli)，可以方便的供开发者使用。

至于为何未使用 SUSE 更为强大的 OBS
系统，是有一些[现实原因所限](https://lists.fedoraproject.org/pipermail/devel/2013-September/188751.html)。

[Fedora Copr
主页](http://copr.fedoraproject.org/coprs/)，其中已经包含不少有趣的内容，比如
[Firefox
GTK3](http://copr.fedoraproject.org/coprs/stransky/FirefoxGtk3/)、[KDE
5](http://copr.fedoraproject.org/coprs/dvratil/kde-frameworks/)、
[Drupal 8](http://copr.fedoraproject.org/coprs/siwinski/drupal8/)、[GIMP
GTK3](http://copr.fedoraproject.org/coprs/ryanlerch/gimp-gtk3-port/)、[Inkscape
GTK3](http://copr.fedoraproject.org/coprs/ryanlerch/inkscape-unstable-gtk3/)。

[更多关于 Copr 的 FAQ](https://fedorahosted.org/copr/wiki/UserDocs#FAQ)
