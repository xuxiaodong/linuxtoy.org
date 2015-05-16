Title: 利用 Zsync 更新已有的 Ubuntu ISO 镜像
Date: 2009-10-31 14:36
Author: Yunkwan
Category: Tips
Tags: Ubuntu, Zsync
Slug: use-zsync-to-update-existing-iso-images

{ 撰文/[Yunkwan](http://kwanlife.yo2.cn) }

对！是升级 ISO
镜像，不是升级系统。从旧的镜像升级到新的镜像。可能有点迟了~大家都 Down
好了镜像~我现在才有心情和时间写 Blog 哦~由 Alpha 的 ISO
升到正式版都可以。呃~当然，估计由 Alpha
开始的话，下载量也与直接下载正式版区别不大~这么多人下载，速度当然会慢喇~用
Zsync 来升级镜像减少了下载量也是一个不错的方法哦~

首先要安装 Zsync 喇~

sudo aptitude install zsync

然后，就是把你原有的 ISO 镜像，重命名，无论是 Alpha，Beta，还是 RC，估计
daily-build 也可以哦~都重命名为正式版的名字：

mv ubuntu-9.10-rc-desktop-i386.iso ubuntu-9.10-desktop-i386.iso

(当然，你不用命令行也可) 当然终端的工作目录要 cd
到原镜像所在目录~只要你找到发布镜像的地址，该镜像又有 *.zsync
的就可以了。

命令使用：

zsync *.zsync

(不是运行这个哦~ 这个是使用方法)

然后，你使用以下的命令就可以升级 ISO 镜像了~ Zsync 会自动帮你搞定的~

    ========================32 位桌面版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-desktop-i386.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-desktop-i386.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-desktop-i386.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-desktop-i386.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-desktop-i386.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-desktop-i386.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-desktop-i386.iso.zsync

    ========================64 位桌面版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-desktop-amd64.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-desktop-amd64.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-desktop-amd64.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-desktop-amd64.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-desktop-amd64.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-desktop-amd64.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-desktop-amd64.iso.zsync

    ========================32 位 Alternate 版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-alternate-i386.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-alternate-i386.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-alternate-i386.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-alternate-i386.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-alternate-i386.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-alternate-i386.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-alternate-i386.iso.zsync

    ========================64 位 Alternate 版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-alternate-amd64.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-alternate-amd64.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-alternate-amd64.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-alternate-amd64.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-alternate-amd64.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-alternate-amd64.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-alternate-amd64.iso.zsync

    ========================32 位上网本(Netbook Remix)版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-netbook-remix-i386.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-netbook-remix-i386.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-netbook-remix-i386.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-netbook-remix-i386.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-netbook-remix-i386.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-netbook-remix-i386.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-netbook-remix-i386.iso.zsync

    ========================32 位服务器版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-server-i386.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-server-i386.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-server-i386.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-server-i386.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-server-i386.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-server-i386.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-server-i386.iso.zsync

    ========================64 位服务器版=================================

    zsync http://mirrors.cat.pdx.edu/ubuntu-releases/9.10/ubuntu-9.10-server-amd64.iso.zsync
    zsync http://ftp.usf.edu/pub/ubuntu-releases/9.10/ubuntu-9.10-server-amd64.iso.zsync
    zsync http://mirror.as29550.net/releases.ubuntu.com/9.10/ubuntu-9.10-server-amd64.iso.zsync
    zsync http://mirror.anl.gov/pub/ubuntu-iso/CDs-Ubuntu/9.10/ubuntu-9.10-server-amd64.iso.zsync
    zsync http://ubuntu.osuosl.org/releases/9.10/ubuntu-9.10-server-amd64.iso.zsync
    zsync http://mirrors.xmission.com/ubuntu-cd/9.10/ubuntu-9.10-server-amd64.iso.zsync
    zsync http://ubuntu.inode.at/cdimage/karmic/ubuntu-9.10-server-amd64.iso.zsync

{
[Source](http://kwanlife.yo2.cn/articles/use-zsync-to-update-existing-iso-images.html).
Thanks Yunkwan. }
