Title: Ubuntu 6.10 Beta（附升级攻略）
Date: 2006-09-29 09:55
Author: toy
Category: Distros
Slug: ubuntu_6_10_beta

[Ubuntu](http://www.ubuntu.com) 6.10 Beta
版已经发布。其主要发布亮点包括：

-   桌面版
    -   GNOME 2.16
    -   OpenOffice.org 2.0.4 RC 2
    -   X.org 7.1
-   服务器版
    -   具有易装的 mail 服务器、web 服务器等任务选择
    -   包含即将出现的 LTSP 5.0 预发布版

更为详细的发布注记，可查看[这里](https://wiki.ubuntu.com/EdgyEft/Beta)。其实，里面的很多东西，我们以前曾经报道过，读者朋友不妨翻阅以前的相关文章。

需要全新安装 Ubuntu 6.10 Beta
的朋友，可到[这里](http://releases.ubuntu.com/6.10/)下载。为了达到更快的下载速度，可选择以下镜像：

-   [美国](http://us.releases.ubuntu.com/6.10/)
-   [荷兰](http://nl.releases.ubuntu.com/6.10/)
-   [德国](http://de.releases.ubuntu.com/releases/6.10/)
-   [意大利](http://it.releases.ubuntu.com/releases/6.10/)
-   [台湾](http://tw.releases.ubuntu.com/6.10/)

对于目前正在使用的 Ubuntu 6.06 用户，可通过以下方法升级。

方法一：在你喜欢的终端输入下列指令：

    gksu "update-manager -c -d"

如果有 alternate 安装 CD，也可使用这个命令：

    gksu "sh /cdrom/cdromupgrade"

方法二：首先，编辑 /etc/apt/sources.list 文件，将其中的 dapper
全部替换为 edgy。

接着，在终端执行下面的指令：

    sudo apt-get update && sudo apt-get dist-upgrade

如果在升级过程中出现问题，则执行下列命令：

    sudo apt-get -f install
    sudo dpkg --configure -a

最后，重启系统即可。
