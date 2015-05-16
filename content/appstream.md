Title: AppStream
Date: 2011-01-27 13:14
Author: lovenemesis
Category: News
Tags: appstream
Slug: appstream

终于在最近的 FreeDesktop 会议上，Red Hat, Canonical, Novell, Debian,
Mageia 等重要的 Linux
发行版/厂商们坐下来开始实现**跨发行版的软件安装机制**。

简单来说，AppStream 跨发行版安装机制有四个部分组成：

-   打包服务器：从打包文件的desktop文件中抽取元信息，将包括软件图标在内的信息提交给镜像。
-   镜像：在各个仓库已有镜像的基础上添加 app-data.xml
    数据文件和包含软件图标的 app-data-icons.tar.gz
    文件。这些文件将会被客户端访问并使用。
-   客户端：以 **Ubuntu Software Center 为界面基础**，使用 **PackageKit
    为后端**执行软件包管理操作，并连接**本地 xapian
    文本搜索数据库实现内容搜索**，利用 **Zeitgeist 实现软件使用统计**。
-   OCS 服务器：通过 **OAuth 与客户端联系**，提供社会化评论及评分功能。

**AppStream 会**：

-   为各大 Linux
    发行版提供**便捷统一的安装流程**，用户在一个发行版上的安装经验可以平缓迁移到其他发行版。
-   提供一个**统一的元数据、评论、评分分享平台**。

**AppStream 不会**：

-   取代现有发行版的打包机制，而是利用 PackageKit
    的多后端支持将后台的模式封装起来。
-   为镜像服务器带来额外同步负荷，小尺寸图标文件和描述元信息很小。

[会议记录](http://distributions.freedesktop.org/wiki/Meetings/AppInstaller2011)

[**详细架构图**](http://distributions.freedesktop.org/wiki/AppStream/Implementation)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=OTA1MA)
