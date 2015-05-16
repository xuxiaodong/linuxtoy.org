Title: aria2 — Linux 下的高速下载工具
Date: 2007-09-09 08:00
Author: toy
Category: Apps
Slug: aria2

[aria2](http://aria2.sourceforge.net/) 是 Linux
下一个不错的高速下载工具。由于它具有分段下载引擎，所以支持从多个地址或者从一个地址的多个连接来下载同一个文件。这样自然就大大加快了文件的下载速度。aria2
也具有断点续传功能，这使你随时能够恢复已经中断的文件下载。除了支持一般的
http(s) 和 ftp 协议外，aria2 还支持 BitTorrent
协议。这意味着，你也可以使用 aria2 来下载 torrent 文件。

**安装 aria2**

aria2 目前已被包含到许多 Linux
发行版中，因此你可以通过所用的系统直接加以安装。例如，在 Debian/Ubuntu
中，你可以在终端执行如下指令来安装 aria2：

`sudo apt-get install aria2`

如果你使用 Fedora Core，那么可以使用下列命令：

`sudo yum install aria2`

你也可以获取 aria2 的源代码，自行编译安装。当前 [aria2 的最新版本为
0.11.2](http://sourceforge.net/project/showfiles.php?group_id=159897)，可从这里下载。

**aria2 的使用方法**

aria2 是命令行程序，使用非常简单。

-   一般使用

    使用 aria2 下载文件，只需在命令后附加地址即可。如：

    `aria2c http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.22.6.tar.bz2`

-   分段下载

    利用 aria2
    的分段下载功能可以加快文件的下载速度，对于下载大文件时特别有用。为了使用
    aria2 的分段下载功能，你需要在命令中指定 s 选项。如：

    `aria2c -s 2 http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.22.6.tar.bz2`

    这将使用 2 个连接来下载该文件。s 后面的参数值介于 1~5
    之间，你可以根据实际情况选择。

-   断点续传

    在命令中使用 c 选项可以断点续传文件。如：

    `aria2c -c http://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.22.6.tar.bz2`

-   下载 torrent 文件

    你也可以使用 aria2 下载 BitTorrent 文件。如：

    `aria2c -o gutsy.torrent http://cdimage.ubuntu.com/daily-live/current/gutsy-desktop-i386.iso.torrent`

关于 aria2 的更多用法，可以通过 man aria2c 查阅。
