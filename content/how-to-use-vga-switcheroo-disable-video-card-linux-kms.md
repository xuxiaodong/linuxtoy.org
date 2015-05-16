Title: 用 vga_switcheroo 在 Linux 下(开启 KMS)彻底关闭某一可切换显卡的简单教程
Date: 2012-03-14 12:29
Author: lovenemesis
Category: Tips
Tags: kms
Slug: how-to-use-vga-switcheroo-disable-video-card-linux-kms

夏天不远了，如果您的本本使用开源驱动，且具备集显和独立显卡，那么赶紧通过此文为它降降温吧～*感谢
@ukyoi 来稿*

私在早先时记载过自己一直为一个问题所扰，就是私配备双显卡的 Ideapad Y460
在 BIOS 中仅支持“可切换”（switchable）和“独立”（原文为 discrete
graphic）两种模式。而当使用可切换模式进入 Linux
后，虽然只有集成显卡在使用，但两个显卡都会同时耗电，导致温度很高。虽然用独立显卡+催化剂（Ati
的商业驱动）可以获得不错的效果，但会有诸多麻烦事情，更何况这样一来集显的节能优势就消失了。

我曾在谷歌上粗略查找过很多彻底关闭独立显卡的方案，然而就目前我看到的中文解答来说，除了那个
ubuntu 关闭独显的脚本还靠谱外，基本都是不靠谱的答案。直到我最近从 Arch
的 Wiki 辗转到了 ubuntu documentation 才找到一个使用内核自带的

     vga_switcheroo

关闭显卡的方案。在此记述一下。

**声明：**本文只是记述了最主要的内容，详细内容可以从[这个页面](https://help.ubuntu.com/community/HybridGraphics)中找到。

下面进入正题：

首先，`vga_switcheroo`
是内核提供的组件，但有这一组件（或者说有下文提到的文件）并不代表其在您的机器上能够正常使用。此外[根据某些用户提供的信息](http://www.linuxsir.org/bbs/archive/index.php/t-370920.html)，`vga_switcheroo`
仅当在 KMS 开启状态下才用，所以请首先装好显卡的开源驱动并保持 KMS 开启。

**查看当前双显卡使用状态：**

终端中输入：

`cat /sys/kernel/debug/vgaswitcheroo/switch`

这步是要读出 `/sys/kernel/debug/vgaswitcheroo/switch`
这一文件的信息。不出意外您可能会看到类似下面（但不完全相同）的内容：

        0:IGD:+:Pwr:0000:00:02.0
        1:DIS: :Off:0000:01:00.0

其中“IGD”表示集成显卡，“DIS”表示独立显卡；加号（“+”）表示当前用作输出（或称“连接上”（connected））的显卡；“Pwr”代表正在供电，“Off”代表已关闭。如果看到两个显卡都显示“Pwr”，则说明都在消耗着电能。

**暂时性的关闭某一显卡**

注意：下面和内核的交互操作是通过操作
`/sys/kernel/debug/vgaswitcheroo/switch`
这个“虚拟文件”实现的，而这一文件每次开机会重新创建，所以您对其所做的修改都是暂时的，重启后会失效。

首先切换到root用户：

`su`

这步通常是必要的，不可用 sudo 取代（似乎是因为 sudo
如果不经设置，是没有“>”操作符权限的）。

打开所有的显卡：

`echo ON > /sys/kernel/debug/vgaswitcheroo/switch`

这步是给所有显卡加电，使其运行，但不改变当前输出的状态。

切换到集成显卡：

`echo IGD > /sys/kernel/debug/vgaswitcheroo/switch`

这步表示使用集成显卡作为输出（即“连接上”集成显卡）。同理，将其中的
“IGD”换成“DIS” 可使用独立显卡。

关闭未使用的显卡：

`echo OFF > /sys/kernel/debug/vgaswitcheroo/switch`

最后可以再运行一下
`cat /sys/kernel/debug/vgaswitcheroo/switch`，看一看自己的显卡状态。

**永久性的关闭某一显卡**

解决重启后失效的办法就是每次开机时都让它执行一遍，而且越早启动越好。对于这个问题，不同的发行版有不同的解决方案。例如在我所用的
Arch Linux 中有一个 `/etc/rc.local`
文件，把需要开机执行的命令写进去即可。对于 ubuntu，可以[参考 ubuntu
documentation
上的一个启动脚本](https://help.ubuntu.com/community/HybridGraphics#Script_for_use_during_bootup)。我没有尝试过加环境变量是否有用，但似乎也应该是可以的。

后记：3月12日帝都（室温约20度），开启 acpi 节能的情况下，我的 Ideapad
Y460 使用集显，打字、浏览网页等操作，CPU
温度不到37度，电池续航4小时以上，真是太舒爽了……

[作者博客原文地址](http://ukyoi.wordpress.com/2012/03/14/%E7%94%A8vga_switcheroo%E5%9C%A8linux%E4%B8%8B%EF%BC%88%E5%BC%80%E5%90%AFkms%EF%BC%89%E5%BD%BB%E5%BA%95%E5%85%B3%E9%97%AD%E6%9F%90%E4%B8%80%E5%8F%AF%E5%88%87%E6%8D%A2%E6%98%BE%E5%8D%A1%E7%9A%84/)
