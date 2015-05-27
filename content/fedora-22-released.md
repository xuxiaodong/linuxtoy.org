Title: Fedora 22 发布
Author: lovenemesis
Date: 2015-05-27
Category: Distros
Tags: fedora
Slug: fedora-22-released
Summary: 经过几次预料之中的延期，Fedora 22 正式发布，带来了 Kernel 4.0 及众多开源新技术。

如果您想快速了解工作站版本的变化，不妨观看该[短片介绍](http://v.youku.com/v_show/id_XOTY1NDkxMDE2.html)。

Fedora.Next 引入了三个面向不同用户群体的版本，其中的一些共同的改善有：

* 上层软件包管理工具正式切换为 `dnf`，相应的过渡工具也已经就位。[点击此了解更多关于过渡的细节](http://dnf.readthedocs.org/en/latest/cli_vs_yum.html)。
* 引入开源分布式 RESTful 搜索引擎 [Elasticsearch](https://www.elastic.co/)。
* 使用 GCC5.1 作为默认编译器。

 
**工作站** 版本的变化有:

* 升级至最新的 GNOME 3.16 版本，带来改善的通知栏提示机制，可以处理包括命令行及 ABRT 工具的提示
* 众多来自 GNOME 3.16 的可用性改善
* 更好的集成 Boxes 和 Vagrant，方便构建开发测试环境


**服务器** 版本的变化有:

* 增加基于 PostgreSQL 的数据库服务角色，简化数据库服务搭建
* 默认文件系统切换至 XFS，将应用于 LVM2 以及一般磁盘分区方式
* Cockpit 服务管理工具将保持跨系统兼容性

**云计算** 版本的变化有:

* 包含最新的 Docker 镜像
* 包含 Vagrant Boxes，方便快速部署基于 Fedora 的开发环境
* 进一步优化 Atomic Host
* 增加 Dockerfiles

此外各个定制版也随着新版本做出了升级：

* KDE 定制版默认使用 **KDE5 Plasma 桌面环境**，引入全新的 Breeze 主题。
* Xfce 定制版升级至 4.12 版本，包含 HiDPI 和 GTK3 插件支持。
* 功能性定制版现在有了一个[专门的主页](https://labs.fedoraproject.org/)，内涵之前的创作套件版、开源游戏版和安全试验室版等
* ARM 也独立出来有了[自己的主页](https://arm.fedoraproject.org/)，可以下载上述各个定制版的 ARM 平台版本。


[项目首页及各版本下载](https://getfedora.org/zh_CN/)

**注意：**由于现在是下载高峰期，部分区域镜像可能也还在同步中，建议[通过 BT 下载获得最快速度](https://torrents.fedoraproject.org/)。

[消息来源](http://fedoramagazine.org/fedora-22-released)