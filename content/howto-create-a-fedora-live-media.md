Title: 如何自制 Fedora Live 介质
Date: 2014-07-31 13:43
Author: lovenemesis
Category: Tutorials
Tags: Fedora, live-respin
Slug: howto-create-a-fedora-live-media

包含重大变化的 Fedora 21 延期到了 11 月份，意味着 Fedora
用户群体将不得不坚守去年底发布的 Fedora 20
长达一年。可是，若是遇到新硬件，老的 Live
介质中的内核太早不支持，怎么办？

自己动手呗！其实自己构建包含最新更新的 Fedora Live
介质是个很简单的事情。

本文[基于官方
Wiki（亦有中文版）](https://fedoraproject.org/wiki/How_to_create_and_use_a_Live_CD)，捡要点简单叙述下。

*安装必要工具*

`pkcon install livecd-tools spin-kickstarts`

`livecd-tools` 中包含了创建 LiveCD 以及将 LiveCD 制作成 USB 的工具，而
`spin-kickstarts` 中则包含了构建用的[大量 KS
模板](https://git.fedorahosted.org/cgit/spin-kickstarts.git/tree/)。

和安装介质不同，Live
介质的构建思路是将指定的软件包安装到一个特定目录，再将其目录转换成运行根目录。于是这个过程使用和
Fedora 无人值守安装一样的 KS 文件进行定制。

*准备工作*

构建 LiveCD 就要用
`livecd-creator`，不过这个工具工作过程特殊，需要在开始前暂时禁用
SELinux。

`su -c 'setenforce 0'`

若是感兴趣，可以仔细浏览下 KS 模板们：`/usr/share/spin-kickstarts/`  
里面包含了各种 Live
介质，从名字可以看出包含依赖关系，比较重要的几个基础类别 KS 有：
fedora-live-desktop.ks、fedora-live-base.ks 和 fedora-repo.ks 。

`开始构建`

若想直入主题，构建包含最近更新的 LiveCD，那么进入想要存放生成 ISO
文件的目录，执行以下命令：

`su -c 'livecd-creator --verbose --config=/usr/share/spin-kickstarts/fedora-livecd-desktop.ks --fslabel=F20_x86_64-Latest --cache =/var/cache/live'`

参数的用途可以从名字看出，无需多解释。换个 cache
目录后亦可以用普通用户执行，

从输出可以看到其先在 /tmp 临时目录创建多个伪 ext 分区并挂载，然后依据 KS
文件通过 yum 从镜像抓取 RPM
包，之后安装至伪分区，且会执行一部分脚本操作进行诸如清理 man 数据库。F20
的 Desktop 镜像大小在 1G 左右，所以具体用时取决于网络速度。

接下来转换伪分区至 squashfs 的过程比较费时，因为涉及压缩，在本人
A10-5800K 的机子上，满载五分钟才完成，不愧是炎炎夏日中的保暖极品……

*写入 USB*

耐心等待后，一个全新的 LiveCD ISO 就完成了。若是直接依据官方 KS
文件，那么无需担忧，可以直接制成 LiveUSB 使用。

插入一个 FAT32 分区格式的 U 盘，umount
掉自动挂载的分区，执行以下命令即可

su -c 'livecd-iso-to-disk --reset-mbr F20\_x86\_64-Latest.iso /dev/sdb1'

上面的命令假设 U 盘上对应为 sdb1，请根据实际情况替换。

*结语*

其实，在 Linus 吐槽 Fedora 不发布更新版本安装镜像之后，Fedora 就开始提供
[Live-Respins](http://alt.fedoraproject.org/pub/alt/live-respins/)。Respins
没有太固定的更新周期，基本上每月会有一次。所以若是等不及的话，还是参照本文中的方法自己构建吧～

由此入门，还可以尝试融合 rpmfusion 的 ks
实现更多的订制，留待诸位童鞋自行研究。
