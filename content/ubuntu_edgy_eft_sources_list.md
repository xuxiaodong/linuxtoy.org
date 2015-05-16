Title: Ubuntu Edgy Eft 的源列表
Date: 2006-10-08 23:31
Author: toy
Category: Tutorials
Slug: ubuntu_edgy_eft_sources_list

以下是 [Ubuntu](http://www.ubuntu.com) Edgy Eft
的[源列表](http://ubuntuguide.org/wiki/Ubuntu_Edgy#How_to_add_extra_repositories)，记一个备用，同时供有需要的同学参考。

    deb http://archive.ubuntu.com/ubuntu edgy main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu edgy main restricted universe multiverse

    deb http://archive.ubuntu.com/ubuntu edgy-proposed main restricted universe multiverse

    ## 主要的 Bug 修正更新
    deb http://archive.ubuntu.com/ubuntu edgy-updates main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu edgy-updates main restricted universe multiverse

    ## Ubuntu 安全更新
    deb http://security.ubuntu.com/ubuntu edgy-security main restricted universe multiverse
    deb-src http://security.ubuntu.com/ubuntu edgy-security main restricted universe multiverse

    ## Backports 仓库
    deb http://archive.ubuntu.com/ubuntu edgy-backports main restricted universe multiverse
    deb-src http://archive.ubuntu.com/ubuntu edgy-backports main restricted universe multiverse

    ## PLF 仓库，包括 Skype、GoogleEarth、W32codecs 等
    deb http://packages.freecontrib.org/plf edgy-plf free non-free
    deb-src http://packages.freecontrib.org/plf edgy-plf free non-free

需要注意两点：

1.  sources.list 位于 /etc/apt/sources.list，编辑需要 sudo
    权限，且最好备份。
2.  在 archive.ubuntu.com 之前可以加 cc.（cc
    即国家代码）以便使用本地镜像，如 cn.archive.ubuntu.com。

