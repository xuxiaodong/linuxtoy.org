Title: 多合一小型 Linux 光盘
Date: 2008-08-12 17:15
Author: toy
Category: Distros
Tags: Live CD
Slug: nin1linuxcd

[撰文/muzuiget <[欢迎访问作者的
blog](http://muzuiget.blog.ubuntu.org.cn)>]

一个 7 个桌面 Linux，都是 LiveCD，顺便带一个
FreeDOS。[点击这里下载](http://ubuntu:ubuntuftp@ftp.ubuntu.org.cn/home/muzuiget/Nin1LinuxCD.iso)（MD5：be53e7635213e99533669e260d215fd7）。

搜集了几个小型的 Linux 的 LiveCD，本来就 600 多 m
的就不会考虑了。找些麻雀虽小，五脏俱全的，找到 7
个比较新的，中文支持最好，最好软件也不要重复。引导器自然首选是 Grub4DOS
啦，花些心思给每个发行版都弄了启动背景。

7 个 Linux 发行版为 Parted Magic、FanX、CDlinux、Damn Small
Linux、Puppy、slitaz、Nimblex。

[Grub4DOS](http://grub4dos.sourceforge.net/) 光盘引导菜单。

[![光盘引导菜单](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_grub4dos.png)](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_grub4dos.png "光盘引导菜单")

[Parted Magic](http://partedmagic.com/wiki/PartedMagic.php) 不够
50M，有了 Gnome Parted、Firefox、TestDisk、PhotoRec
等几个非常实用的工具，界面友好，急救系统恢复文件必备工具。

[![Parted
Magic](http://i.linuxtoy.org/i/2008/08/grub4dos_parted-magic.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_parted-magic.png "Parted Magic")

[FanX](http://fanx.org.cn/) 也就是 [Slax](http://www.slax.org/)
的中文版，有不错中文字体和输入法，使用 KDE
桌面环境的大部头，200m，软件不少，作为日常使用也是很不错的。

[![FanX](http://i.linuxtoy.org/i/2008/08/grub4dos_fanx.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_fanx.png "FanX")

[CDlinux](http://cd-linux.sourceforge.net/) 也是有中文版的，功能不如
FanX 多，不过也是只有 50 多 M，看看网页文档也就够了。

[![CDlinux](http://i.linuxtoy.org/i/2008/08/grub4dos_cdlinux.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_cdlinux.png "CDlinux")

[Damn Small Linux](http://www.damnsmalllinux.org/)，真他妈的小的
Linux，也是不够 50M，虽然界面有点简陋，不过软件很齐全。

[![Damn Small
Linux](http://i.linuxtoy.org/i/2008/08/grub4dos_dsl.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_dsl.png "Damn Small Linux")

[Puppy](http://www.puppylinux.org/) 只有 80 多
M，但是软件种类和界面做得很不错，ownlinux
[介绍](http://www.ownlinux.cn/2008/05/06/puppy-linux-400-experience/)过，也有一篇[硬盘安装方法和中文化](http://www.ownlinux.cn/2008/07/08/puppy-linux-40/)。

[![Puppy](http://i.linuxtoy.org/i/2008/08/grub4dos_puppy.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_puppy.png "Puppy")

[NimbleX](http://nimblex.net/) 也是用 KDE 的，某些软件跟 FanX
重复了，不过有Firefox，Gimp，Gpated
等几个重量级软件，急救日常使用都行，不过没中文。

[![Nimblex](http://i.linuxtoy.org/i/2008/08/grub4dos_nimblex.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_nimblex.png "Nimblex")

[SliTaz](http://www.slitaz.org/) 号称世界上最小的 Linux
桌面发行版，真的够小了，比 Damn Small Linux 还小，个头只有
28M，启动速度极快（以上几个 Linux 中最快），却有漂亮的界面，Firefox
这样的杀手级软件，还有
mplayer，音频播放器，开发环境，还有包管理软件和软件仓库令人爱不释手。目前找到个繁体中文了，不过那个繁体的字体真是难看，中英文不成比例，看起来很不习惯。

[![SliTaz](http://i.linuxtoy.org/i/2008/08/grub4dos_slitaz.png)](http://i.linuxtoy.org/i/2008/08/grub4dos_slitaz.png "SliTaz")

[FreeDOS](http://www.freedos.org/) 偶尔玩玩，加个 testdisk 也不错。

Linux 光盘怎么都得要有支持中文才行，不然实用性大打折扣。

-   FanX 和 CDLinux 启动后本身就是中文了，不需要操心。
-   Damn Small Linux，这个中文化起来太麻烦了，暂时放弃。
-   Puppy 是有人做出了中文包，一键安装，省心。
-   Parted Magic，Slitaz，Nimblex 这 3
    个最起码要支持中文字体和中文输入法。

安装字体好办，装一个文泉驿正黑就好了。输入法就麻烦了，要解包安装后之后就要重新打包，折腾过
Slitaz 安装
fcitx，结果老失败。结果找到一个简单方便又不需要重新打包的方法，因为这 3
个发行版都是有 Firefox 的，所以使用基于 Firefox
的扩展输入法就行啦，这个扩展叫“[Fireinput](https://addons.mozilla.org/zh-CN/firefox/addon/5420)”，中文叫“火输”。一直以为
Windows 下输入法这么多，怎么还有人有闲情去弄 Firefox
的输入法扩展呢，会有人用么？没想到这次派上用场了，那是因为可以跟 Firefox
一起跨平台使用，不用鸟什么操作系统，不用鸟什么语言桌面环境，有 Firefox
的地方就能用，值得一赞的是 Fireinput 还是一个开源软件。

有 Firefox 就万事好办，至于其它程序不能用 Firefox
的输入法扩展，用笨方法，复制粘贴过去就行了。用 Firefox
无所不能的扩展还能收邮件、RSS 阅读、FTP 下载、BT
下载、听歌、作笔记……结合在线服务更无敌了。什么都能在 Firefox
里干好了，整一个 LiveCD 就一个 Firefox
够了，装扩展基本上不用考虑平台兼容性。扯远了，说一下余下三个怎么设置中文字体和输入法。首先要挂载光驱，虽然说是光盘启动的。中文化文件我都放在“tools”目录下面。5
个文件：

-   wqy-zenhei.ttf.gz - 文泉驿正黑字体文件
-   Fxp.zip - Firefox 配置文件夹，里面预装了几个扩展，包括 Fireinput
-   copyfont.sh - 自动复制解压字体到家目录
-   copyFxp.sh - 自动复制解压 Firefox 配置文件夹到家目录
-   chinese\_pack\_total-0.2.6.pet - Puppy 的一步到位中文包

其中字体是复制解压到“~/.fonts”，不在需要任何设置，也可以手动复制解压。不过
Firefox 配置文件夹不是必须的，也可以进入桌面后用 Firefox
在官网重新下载安装。

**Parted Magic**

进入桌面后终端执行：

`mount /dev/cdrom /media/cdrom #或者点击桌面上的“Nin1LinuxCD”图标就自动挂载 cd /media/cdrom/tools/ ./copyfont.sh ./Fxp.sh #以 Fxp 文件夹为配置文件夹启动 Firefox firefox -profile ~/Fxp`

[![](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_parted_magic-thumb.png)](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_parted_magic.png)

**Slitaz**

进入桌面后终端执行：

`su #输入密码“root” mount /dev/cdrom /media/cdrom #退出 root 用户 exit #或者用主菜单里“System Tools”，“Mount devices”，挂载光驱。 cd /media/cdrom/tools/ ./copyfont.sh ./Fxp.sh firefox -profile ~/Fxp #以 Fxp 文件夹为配置文件夹启动 Firefox`

[![](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_slitaz-thumb.png)](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_slitaz.png)

**Nimblex**

光盘启动后就已经挂载好了，只需要打开终端，执行：

`cd /mnt/live/mnt/hdc/tools ./copyfont.sh ./Fxp.sh #以 Fxp 文件夹为配置文件夹启动 Firefox firefox -profile ~/Fxp`

[![](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_nimblex-thumb.png)](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_nimblex.png)

**Puppy**

点击桌面上的“mount”，把 CDROM
挂载，然后自动打开了文件管理器，进入“tools”目录，点击安装
chinese\_pack\_total-0.2.6.pet
文件，安装过程比较久，请耐心等待，等提示安装好了就打开主菜单，“Shutdown”，“Restart
X server”重启 X，然后就能用上中文环境了，输入法是 fcitx。

[![](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_puppy-thumb.png)](http://i.linuxtoy.org/i/2008/08/nin1linuxcd_puppy.png)

**注意事项**

-   所有 Linux 都是复制自官方光盘的，
    没有对文件解包重打包操作，只是简单整合。
-   光盘没有个人标记和水印（除了那个 Firefox
    配置文件夹一些个人配置外），下载后不满意菜单背景喜欢怎么改就怎么改。
-   光盘镜像一共 712 M，如果要刻录 CD
    就不够了，要对镜像修改一下，几个建议：
    -   删掉 12 M 的 Fxp.zip，就刚刚好 700M，刻盘就够了。
    -   删掉 50 M 的 Damn Small Linux（KNOPPIX 文件夹），因为没有中文。
    -   删掉 Nimblex，大部头，跟 FanX 软件有些重复，放置其它文件。
-   Puppy
    的最新一步到位中文包可以到[这个页面](http://puppy.cnbits.com/node/113)下载，直接替换即可。
-   Puppy 是很有潜力的发行版，还有更多中文 pet 软件包供选择，比如
    LinuxQQ，[浏览这里](http://puppy.cnbits.com/node/128)。
-   如果要光盘里面的发行版有更新，直接用官方的光盘里的文件或文件夹替换掉就行了。
-   Fireinput 只装了拼音版，如果需要五笔版到 [Fireinput
    官网](http://www.fireinput.com/wiki/Main_Page)下载
-   以 Live 模式安装到闪盘或硬盘也是可以的。

**相关链接**

FanX：[官网](http://www.fanx.org.cn/)，[支持论坛](http://www.linuxfans.org/bbs/forum-64-1.html)  

Puppy：[中文开发博客](http://puppy.cnbits.com/)，[支持论坛](http://puppy.cnbits.com/forum/4)  

Fireinput：[官网](http://www.fireinput.com/wiki/Main_Page)，[支持论坛](http://www.fireinput.com/forum/main.php)

其实 Linux LiveCD 整合非常简单，我都试过不少发行版了。只要是支持 Live
模式理论上都能整合，因为有 Grub4DOS 这个神器。如果用 DVD
空间就更多了，几乎就有多少空间就能整合多少个
Linux，Ubuntu、Fedora、openSUSE、Mandriva 这些都有
LiveCD，但是个头太大，启动太慢，一般都是做安装到硬盘用。而一些 300 M
以下的，本来就是做 LiveCD 用途的，常见的除了上边 7 个，还有
Tinyme，Partimage Is Not Ghost，Knoppix
等等。整合这么多玩玩而已，日常使用就 Ubuntu，分区急救就 Parted
Magic，其它很少用。

本文原文地址（如果以后有更新）：[《多合一小型Linux光盘》](http://muzuiget.blog.ubuntu.org.cn/2008/07/18/%e5%a4%9a%e5%90%88%e4%b8%80%e5%b0%8f%e5%9e%8blinux%e5%85%89%e7%9b%98/)，[《多合一小型Linux光盘下载及中文化说明》](http://muzuiget.blog.ubuntu.org.cn/2008/08/10/%e5%a4%9a%e5%90%88%e4%b8%80%e5%b0%8f%e5%9e%8blinux%e5%85%89%e7%9b%98%e4%b8%8b%e8%bd%bd%e5%8f%8a%e4%b8%ad%e6%96%87%e5%8c%96%e8%af%b4%e6%98%8e/)。
