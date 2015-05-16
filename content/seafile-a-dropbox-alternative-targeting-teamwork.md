Title: Seafile，面向团队的开源 Dropbox
Date: 2013-01-29 09:21
Author: lovenemesis
Category: Cloud
Tags: seafile
Slug: seafile-a-dropbox-alternative-targeting-teamwork

Seafile 是一个面向团队的文件同步和协作平台。它有 Dropbox
类似的文件同步功能，但是针对团队文件同步和协作做了优化。*感谢 freeplant
来稿*

-   [产品主页](http://seafile.com)
-   [Github 项目主页](https://github.com/haiwen/seafile)

你可以用它在你自己的服务器上搭建文件 同步和协作服务。Seafile
同时也提供公共的云服务。

Seafile 是第一个能够在产品功能上和稳定性上能与 Dropbox 相比的开源项目。
它同时提供了 Dropbox 所不具有的**协作功能**。Seafile 的创新特色包括:

1.  群组功能，用户可以创建和加入群组, 在群组中共享文件。在 Dropbox
    中，用
    户一般是通过创建公共的账号来做多人协作。群组功能使得多人协作更加的直观流畅。
2.  同步和协作结合更自然。Seafile 中，文件组织成资料库，每个资料库可以单
    独共享到多个群组和多个用户。用户可以选择性的单独同步一个资料库到一台电脑上。
3.  在线文件协作，包括文件在线预览、评论、推荐等等。 Markdown, text,
    源代 码等文本格式可以直接在线编辑。
4.  端到端数据加密，Seafile 中用户可以创建加密的资料库，密码不在服务器上
    保存，这样甚至系统的管理员可无法读取私有数据。
5.  分布式同步，用户可以同时使用多个服务器，比如把公司的资料放在企业内部
    的服务器上，把对外交流的资料放在 Seafile 公共服务器上。

Seafile 采用了类似 GIT
的数据模型和分布式同步技术，但是针对自动同步和**大文件管理**做了优化。

同其他的开源项目 (SparkleShare, Owncloud) 相比，Seafile 有以下的优势：

1.  有成熟和稳定的同步算法
2.  并不是 Dropbox 克隆，Seafile 是一个针对团队协作设计的新产品。

目前客户端支持所有主流平台，包括 Windows, Linux, Mac，Andoird 和
iOS。服务器支持 Linux 平台，可以跑在 Raspberry Pi 平台上。

Seafile 项目最初是希望解决在没有服务器的情况下社团成员之间共享文件资料的
问题。所以 Seafile 项目包括了一个 Ccnet 子项目。Ccnet 是一个 P2P
的网络应用框架，实现了网络节点间的连接管理、消息通信、RPC
等功能。后来，Seafile
项目才逐步的演化成一个分布式的架构，并加入了文件同步的功能。

Seafile 目前的项目目标是成为团队文件资料管理、协作和共享的统一性的平台，
并成为一个世界级的一流产品。

**PS:** 项目负责人 freeplant 在刚刚举行的 [Fedora 18 Release
Party](http://linuxtoy.org/archives/fedora-18-release-party-announcement.html)
上对于 Seafile 做了专题介绍，预知详情敬请期待近日发布的活动报告。
