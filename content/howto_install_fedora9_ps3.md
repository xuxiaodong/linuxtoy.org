Title: 如何在 Sony Playstation 3 安装 Fedora 9
Date: 2008-07-29 01:06
Author: lovenemesis
Category: Featured
Tags: Fedora, ps3
Slug: howto_install_fedora9_ps3

Sony 于 2006年底发售的游戏主机包含了各种高科技的玩意： Cell BE
处理器、蓝光光驱、HDMI接口、蓝牙/802.11g网络…… 一反常态，Sony
在发布前就宣布 PS3 支持 Linux 系统。下面就跟我以 Fedora 9
为例，一步一步地让憨态可掬的 Tux 企鹅“坐”在 PS3 上。

**必要工具**

1.  Sony Playstation3 任意地区任意版本皆可。本人使用的是新 40G 欧版。
2.  一个 PS3 支持的显示设备，比如电视机或者显示器，至少用色差分量。
3.  光盘刻录机及空白光盘
4.  剩余空间不少于300M的U盘一个(FAT32文件系统，NTFS 不可)
5.  USB 接口的键盘鼠标，或者免驱动的无线键盘鼠标。

**第一步：准备**

1.  由于 PS3 的中央处理器是 PowerPC(以下简称PPC) 而不是通常的 x86 或
    x86\_64 架构的，所以只能选择支持 PPC 架构的 Linux 发行版。像 Ubuntu
    8.04， ArchLinux 等仅有 i386 和 x86\_64
    的发行版是不行的。现在支持PPC的主流发行版是
    [Fedora](http://fedoraproject.org/get-fedora) 和
    [openSUSE](http://software.opensuse.org/)，下载相应的 PPC
    版本光盘镜像，强烈建议校验数据完整性。然后用你顺手的刻录软件刻录到光盘即可。注意，推荐下载
    DVD 版本，有些 PS3 专属的配置软件并没有包含在 CD
    版本的光盘镜像里。本文以 Fedora 9 PPC DVD 版本为例。
2.  在 PS3 上安装 Linux 操作系统要求 PS3 系统固件版本在 1.80
    以上。当前最新的系统固件版本是 2.41，可以通过用 PS3 网络升级或用
    [PC下载](http://www.us.playstation.com/PS3/About/SystemUpdate)
    好再用U盘传递到 PS3 的方式实现。
3.  安装引导程序。PS3自己并不能从光盘上启动相应的安装程序，于是我们需要一个引导程序。该引导程序将安装在
    PS3 系统 Flash
    部分，一旦安装将不可删除，但可以被其他引导程序覆盖，固件升级、格式化、或更换硬盘不会影响。因此，对你玩
    PS3 游戏看蓝光电影等在 Sony
    官方系统下的行为没有任何影响，可以放心大胆的尝试。目前有两种可用的引导程序，[kboot](http://www.kernel.org/pub/linux/kernel/people/geoff/cell/ps3-kboot/)
    和
    [petitboot](http://www.kernel.org/pub/linux/kernel/people/geoff/cell/ps3-petitboot/)，后者在前者的基础上提供了图形化的引导界面(仅仅是引导，与是否图形化安装没关系)，本文以
    kboot 为例。下载好之后，放在你U盘的 PS3/otheros/目录下，并重命名为
    otheros.bld（大小写敏感）。插入U盘到
    PS3，选择"设定"－"主机设定"-"安装其他系统"，按提示操作安装。其实这里所谓的“引导程序”本身就是一个小型的
    Linux
    系统，所以用“安装其他系统”的选项，不过这里我们只用它来引导安装光盘。
4.  格式化硬盘。如果你的 PS3
    已经使用了一段时间，上面一定有游戏存档之类的东西，用你的U盘或者FAT32格式的移动硬盘备份！备份之后，在
    PS3
    中选择"设定"－“主机设定”－“格式化硬盘”。很显然，"保留10Gb给游戏系统”是不够用的，选择“保留10Gb给其他系统”或者“自定义”。这里选择“保留10Gb给其他系统”，10Gb已经足够
    Linux 用了。之后等待格式化完成。

**第二步：开始安装**

1.  放入刻录好的安装DVD，插上你的鼠标键盘，在“设定”－“主机设定”－“优先启动系统”中选择“其他系统”，之后选择“是”，PS3将重新启动。
2.  如果你看到两个小企鹅出现，那么代表引导程序 kboot 运行成功。等待
    kboot 提示符出现后，输入 linux64 video=ps3fb:mode:0 引导光盘。这里的
    0
    代表自动检测显示输出模式。如果你清楚你的电视或显示器的输出模式，强烈建议按照下表将
    0 替换成相应数值。

-   YUV 60Hz 1: 480i 2: 480p 3: 720p 4: 1080i 5: 1080p
-   YUV 50Hz 6: 576i 7: 576p 8: 720p 9: 1080i 10: 1080p
-   RGB 60Hz 33: 480i 34: 480p 35: 720p 36: 1080i 37: 1080p
-   RGB 50Hz 38: 576i 39: 576p 40: 720p 41: 1080i 42: 1080p
-   VESA 11: WXGA 12: SXGA 13: WUXGA
-   在以上数值上增加 128 启动全屏模式，增加打开抖动修正 2048。

注：6是中国大陆地区普通电视PAL制式，我打开想抖动修正，于是该处的最终值为
6＋2048＝2054。所以我输入的是 linux64 video=ps3fb:mode:2054
本人没有高清电视，残念…… 如果实在不清楚该用什么，就用 0 自动探测吧。

之后的安装过程和通常的安装过程无两样。分区时你会被提示磁盘未初始化，放心选择“是”。所谓“整个磁盘”只是你在“第一步：格式化”中选择的给”保留给其他系统“的那部分，完全不影响游戏系统系统，所以用”删除全部分区并创建默认分区结构“是可以的，推荐使用LVM。

注意尽管 Fedora 9 PPC 光盘的可选软件包中有 XFCE
桌面环境，但**实际上并没有包含到光盘里面**，我选择的是
GNOME，并去掉了一部分不用的GNOME功能和Openoffice，最终有907个包需要安装，用时1小时。安装结束后光盘会自动弹出，记得取走，之后会自动重新启动。

首先会看到两只大的Tux，之后会再次看到 kboot
提示符，什么都不做，稍等一会儿，如果能再看到两只大的Tux(代表Cell
BE里双核的PPE)和六只小的Tux(代表Cell BE里可供使用的六个SPE)，表示找到
Fedoara
内核所在位置并开始加载。观察屏幕上的输出的话会发现在内核加载前有类似启动虚拟机的设备映射过程，的确，PS3
的 Linux 是运行于由 Sony
提供的硬件抽象层上的，以一种类似虚拟机的方式访问硬件设备，而 Cell BE
里的第七个 SPE 就被保留负责设备映射。

**第三步：优化配置**

1.  首先你会注意到 Fedora 9 “首次配置”的部分比以前版本有所精简，不再有
    SELinux 和声卡检测了，同时你也会在硬件配置文件部分发现内存只有
    191M！ 知道做为“KDE控”的我为什么之前不选择 KDE4 了吧……
2.  如果你显示输出在先前使用的是 0 自动探测的话，这里我们可以用
    ps3videomode 工具测试出来正确的数值。用Ctrl+Alt+F1
    打开一个新的终端（该工具不可在X工作的终端使用），以root用户的登陆，在
    ps3videomode -v ＃
    测试（#位置为上表中数值）。如果一个不正确的数值导致电视黑屏了，此时用上箭头使用
    bash
    的命令回溯功能调出上一条命令，然后用Backspace键删去错误的值，再输入上一个已知的可以工作的值。
3.  经过上一步的尝试，你应该已经得出了适合你的显示设备的值了。于是用文本编辑器比如
    vim 打开 /etc/yaboot.conf，找到 append="video=ps3fb:mode:# rhgb
    quiet"（#位置为之前在引导时所用数值），将#替换为新值。此时我们还可以在此行通过
    ps3fb=#M 限制 ps3fb
    所用内存，将更多的内存留给系统，根据其他人的测试，2M 足够 480i
    使用，4M 足够 720P 使用了。于是我的该行是
    append="video=ps3fb:mode:2054 ps3fb=4M rhgb quiet”。注意该行还有
    root=
    部分，那是代表你硬盘的UUID，切不可删除或修改！保存退出。重新启动后会发现可用内存已经增加到211M了。
    /etc/yaboot.conf 就是在 PPC 架构上 Linux 系统的引导程序
    yaboot，相当于 X86 架构上的 GRUB 和 /etc/grub.conf。为什么不用 GRUB
    是因为它只有 i386 版本。
4.  关闭AIGLX，避免运行一些 OpenGL 程序时的崩溃问题。用文本编辑器打开
    /etc/X11/xorg.conf 文件，在其中的 Device 段中增加一行 Option  
    "AIGLX" "0"  ，保存退出。
5.  你会发现没有你的GNOME是没有声音的，需要调整下 pulseaudio
    才行。用文本编辑器比如 vim 打开 /etc/pulse/default.pa，找到并取消
    load-module module-oss device="/dev/dsp" sink\_name=output
    source\_name=input 的注释，接着找到并注释掉 load-module
    module-suspend-on-idle 。保存退出。之后新建一个 /etc/asound.conf
    文件，内容如下：
6.  pcm.!default {  
    type pulse  
    }  
    ctl.!default {  
    type pulse  
    }
7.  记得赋予 /etc/asound.conf 可执行权限 chmod o+x /etc/asound.conf
    。确认已经安装了 pulseaudio-esound-compat
    (默认GNOME是安装的)，注销并重新登录后就能听到声音了。
8.  关闭SELinux。用文本编辑器打开 /etc/sysconfig/selinux
    文件，按照其中的注释说明将 enforcing 改成 disabled 保存退出即可。
9.  关闭不必要的服务。有些服务对于 PS3
    来讲是不必要的，可以关闭以节省内存。包括 auditd, httpd, ip6tables,
    isdn, sendmail, anacron, cpuspeed, cups, iprinit, iprdump,
    iprupdate, mdmonitor, nfslock, pcscd, restorecond, rpcbind, rpcgssd,
    rpcimapd, setroubleshoot, smartd, sshd。 用 chkconfig [service] off
    或者用"设置"-"系统" －“服务”关闭。
10. 删除不需要的显示驱动 rpm -e xorg-x11-drivers xorg-x11-drv-palmax
    xorg-x11-drv-voodoo xorg-x11-drv-trident xorg-x11-drv-wiimote
    libwiimote xorg-x11-drv-sisusb xorg-x11-drv-sis
    xorg-x11-drv-diamondtouch xorg-x11-drv-nv xorg-x11-drv-i740
    xorg-x11-drv-ati xorg-x11-drv-savage xorg-x11-drv-nouveau
    xorg-x11-drv-i128 xorg-x11-drv-s3virge  。
    可以节省一定空间并降低更新量。
11. 无线网卡据说在 Fedora 9 中已经可以正常使用，但并不支持 WEP
    加密功能。因为没有无线路由，无法亲身测试，很抱歉……

![](http://i.linuxtoy.org/i/2008/07/fedora9ps3-340x271.png)

**如何从 Linux 返回 PS3 游戏系统？**

-   方法一：启动时，在 kboot 提示符处输入 game 。
-   方法二：进入 Linux 系统后，以 root 权限输入 ps3-boot-game-os 。
-   方法三：开机时，按住前面板的开机键不放，直到听到“滴”的一声，此时 PS3
    将以游戏系统启动，并且视频音频输出设置返回出厂状态(其他设置和硬盘内资料都不会变)。

**安装 Fedora 9 PPC 相比于 Sony 推荐的
[Yellowdog](http://www.terrasoftsolutions.com/products/ydl/intro.shtml)
6.0 各有什么优点？**

-   Fedora 9 包含了较新的应用软件，比如 Firefox 3.0 和 Openoffice 2.4
-   Fedora 9 可以方便的获得来自第三方资源仓库如 livna 的软件包。用 yum
    安装 mplayer 获得RMVB回放支持比自己编译要方便很多。
-   Fedora 9 默认安装了 ntfs-3g，可以在 Linux 下读写 NTFS
    格式的外置硬盘。
-   Fedora 9 具有更多更快的资源镜像。
-   Yellowdog 6.0 包含了来自 IBM 的 Cell SDK。
-   Yellowdog 6.0 安装后无需配置即可正常工作。

总而言之，如果你希望 PS3
成为你客厅里的电脑，主要上上网、看RMVB、用模拟器玩SNES或NEOGEO，那么推荐安装
Fedora 9；如果你仅仅需要一个 Cell BE 开发平台的话，那么就用 Yellowdog
6.0 吧！从安装到配置简单的几乎没的可说。

**嘿，我说，Ubuntu 哪里去了？**

Ubuntu 从 7.04 开始对PPC 架构的支持由官方支持转为社区支持了，于是 PPC
版本比 X86 版本的要晚很多发布，目前可用的版本是 [Ubuntu 7.10
Desktop](https://help.ubuntu.com/community/PlayStation_3) 。 社区的
Ubuntu PPC
版本存在一些问题，比如分区程序无法正确识别被映射的硬盘等。另外，很多镜像上都没有做
Ubuntu PPC 版本的资源仓库，下载软件速度也是一个问题。

**PS3 上的 Linux 运行速度如何？**

首先，目前绝大部分 Linux 程序都没有针对 PS3 使用的 [Cell
BE](http://en.wikipedia.org/w/index.php?title=Cell_BE&amp;redirect=no)
（Wikipedia 请自行翻墙 ）进行优化，于是实际上这些应用程序能使用的只有
Cell BE 里面 PowerPC 架构的双核 PPE 芯片，而六个具有超强浮点运算能力的
SPE
都处于闲置状态。只有优化过的程序比如[PS3GRID](http://www.ps3grid.net/)
才能调用那六个非通用计算的 SPE
。性能的差距可以这样比喻：一个是只有两个人拉的车，一个是两个人指挥六匹马拉的车。
这点理论上可以通过重新将全部源代码针对 Cell BE
进行优化解决，不过目前连针对 X86\_64
的优化都没做完，天知道什么时候才能轮到 Cell BE。

其次，目前 PS3 上 Nvidia 的 RSX GPU 被 Sony 屏蔽，无法用它对 Linux 下的
3D 程序进行加速，所以显示输出使用的驱动是 framebuffer 而不是
nv。这点除非破解了 Sony 的固件换用自制固件是别无他法的。 不过 GPU
被屏蔽了，显存并没有，所以目前有一些人在研究如何让 framebuffer 使用那
GDDR3 256M 的显存而不是系统主内存。

最后，为浮点流运算设计的 PS3 只有 XDR 高速内存只有 256M，而且可用的由于
Framebuffer 的原因还将更小。 对于目前的 Linux 图形桌面使用来讲，256M
以下的内存已经算捉襟见肘了，打开 Openoffice
已经比较费力了（所以还是用Abiword吧……），想用 GIMP ?  呃……

**友情提醒：**

本文假设读者已经有一定的 Fedora 或者其他 Linux
发行版的使用经验，并且能熟练操作PS3。 如果你是 PS3 或者 Linux
新手的话，请仔细阅读 PS3 的用户手册，并阅读各大 Linux
论坛置顶基础知识帖。

**PS:** 在网上能找到一些如何在 PS3 上安装 Linux 的中文指南，但是估计购买
PS3 的核心玩家居多，没什么时间研究
Linux，这些指南或多或少都有些遗憾。另外无论是中文还是英文，都没有成形的
Fedora 9 在 PS3
上的安装指南。希望此文能弥补这些缺失，也希望没有让等待的诸多朋友们失望。

部分内容吸取自 [FedoraForum
PPC](http://forums.fedoraforum.org/forumdisplay.php?f=51) 的帖子

来自 PS3-Hacks 的 [Sony Playstation 3
详细硬件规格](http://www.ps3-hacks.com/forums/about1423.html)
