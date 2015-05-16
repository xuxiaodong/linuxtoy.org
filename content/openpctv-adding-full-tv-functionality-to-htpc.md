Title: OpenPCTV - 让你的HTPC拥有更全面的电视功能
Date: 2013-09-09 15:17
Author: lovenemesis
Category: Distros
Slug: openpctv-adding-full-tv-functionality-to-htpc

OpenPCTV 是一款支持 DVB-S2 卫星、DVB-C 有线、DVB-T
地面波电脑接收设备（PCI/PCIE/USB）的接收及播放的 Linux 发行版。*感谢
Yinghong.Liu 来稿*

**功能介绍：**

-   完美支持原汁原味的 CHC HD、CCTV 3/5/6/8 HD 及多个省级卫视高清频道的
    1080p
    全高清硬解输出，5.1声道及多种音频设备（模拟、数字、HDMI）即时切换输出。
-   集成 XBMC 12.2 Frodo, VDR 2.0.2 和 Enigma2PC（一款被移植 DM8000HD
    机顶盒的系统）三大平台。
-   支持全球超过 60 多种语言支持，一次切换 XBMC/VDR/Enigma2 的语言界面。
-   提供原生完整的 EPG 支持。
-   支持OScam, vdr-sc 和 TTscam 解密支持。
-   无需手动编辑配置文件，采用对话菜单样式可完成大部分的配置。
-   将 iso 文件拷到U盘即可正常使用(将在U盘上建立一个 loopdisk.img
    虚拟磁盘文件，U盘的容量不得少于1G)
-   三大平台均支持 Intel(vaapi)/AMD(vdpau via UVD)/Nvidia(vdpau)
    显卡硬解码。
-   使用内核直接驱动遥控接收设备，一般的遥控设备无需任配置就可以直接支持。
-   对市面上大多数的DVB设备提供了支持。
-   XBMC 已安装 xvdr 插件，默认即可在 XBMC 观看 vdr 的电视节目。
-   OpenPCTV 遵循 GPL 开源协议，公开所有源码。采用 opkg
    软件包管理，可在线升级。系统以 iso
    光盘镜像格式发布，按年月日不定期滚动发布。

**环境要求：**

-   Intel显卡支持 Intel G45主板集显、Intel
    第一代核芯显卡及其后的SNB、IVB、Haswell 等核芯显卡。
-   AMD 显卡得益于最新 AMD 内核及 mesa 开源驱动得以支持 vdpau
    硬解码模式。可支持 HD4xxx（或785G/880G/890G等集显，但仅支持 mpeg2
    1080p 硬解，暂不支持 mpeg4/h.264/vc-1 硬解码），HD5xxx 与
    HD6xxx（这两个系列可以提供完美支持，注意第一代 APU 即 FM1 及 E350
    的集显是 HD6xxx），HD7xxx 与
    HD8xxx（目前第二代APU采用这两个系列，注意这个系列在XBMC的OSD界面显示不正常，HDMI
    音频输出爆音，这是开源驱动的问题，如果采用主板音频输出及只使用
    Engima2 和 VDR 也可以）
-   Nvidia 系列显卡较为广泛。具体的显卡型号为 GF8400 以上即 08
    年及以后的 Nvidia
    显卡基本都支持，注意显存必须不少于256M（不是TC256M）
-   DVB卡的支持情况：理论上 Linux 能支持的卡 OpenPCTV
    都可以使用。一般情况下 OpenPCTV
    可直接支持较为通用的Prof、Tevii、DVBWorld、DVBSky、TBS等设备。同时还提供
    s2-liplianin 及 TBS
    两个驱动包提供更多的DVB设备支持。第一次使用请进入配置模式可以进行调正驱动。注意部分部分以
    cx88 的 pci 卡及基于 cx23885 的 pcie
    可能存在偶发性不能顺利驱动的情况，你可以在配置模式中指定你的 dvb
    卡型号。
-   遥控支持情况: 基本上内核能支持的遥控就可以直接驱动，如部分主板自带的
    CIR 遥控、标准的 MCE 遥控及 DVB
    卡自带遥控，你要做的只是需要指定默认的 Lirc 遥控设备即可。推荐使用
    CIR 及 MCE 遥控。DVB
    卡自带遥控可能某些键位需要重新定义。这需要依具体设备而定。注意有些非通用遥控如“遥酷”可能需要特别的配置（写
    udev 规则），这些可以另外讨论。
-   显示及音频设备：推荐使用可支持 1080p 的电视机或投影仪。音箱设备推荐
    5.1 声道自带 AC3 解码（浙江卫视、CCTV3568 及 CHC HD
    有时候发送5.1音频通道，显示分辨率输出及音频通道选择均可在配置模式中进行设置。
-   其它设备要求：cpu 至少 E350 就可以完美使用了，内存 1G
    也够了。如果直接使用 U盘的话至少也要 16G
    吧（要录像的话这容量也不够），最好是主板及
    U盘均支持USB3（市面上很多采用 slc 芯片的USB3 U盘读写速度可达到
    200MB/s以上），安装到硬盘的话视情况而定，如果需要录像的话当然是越大越好了。值得注意的是用来作系统盘话对U盘要求还是比较高的。有些
    U盘平常用可能没发现什么问题，但用来作系统盘可能有坏块而产生一些未知的错误。

**使用形式**

OpenPCTV 目前提供三种使用形式。

-   LiveCD 运行形式，即将 iso 刻录成光盘，然后从光盘启动
    OpenPCTV。因为系统需要配置，并且光盘系统重启后所有数据会复位。因此只推荐需要安装系统时才刻录光盘。（即从光盘启动安装
    OpenPCTV）
-   U盘模式，这种使用模式近似于硬盘正式安装使用。所有配置重启后自动保存而不会消失。只要U盘容量大（32G及以上），速度快（U盘和主板均是
    usb3 接口，读写达到
    50MB/s以上）也可以获得和安装一样的速度体验。下面会分别介绍如何在
    windows/Linux 下将 iso 安装到U盘（U盘使用 fat3 2格式，U盘中可存除
    OpenPCTV 外其它文件）
-   硬盘安装，在启动介质（光盘或U盘）启动时选择进入 Install OpenPCTV to
    disk 安装模式，即可将 OpenPCTV
    安装到你的硬盘上。这里值得注意的是需要你对硬盘分区比较熟悉，最好是预留一个分区给
    OpenPCTV，在安装中可以选择安装到这个分区中。这个安装程序最终将安装
    Grub2 到硬盘中（可选择是否安装到硬盘的
    mbr），理论上说可以正常识别硬盘上其它的操作系统如windows 及其它
    Linux等，同时也会将这些启动项加入到这里。安装完后第一次启动也请进入”Setup
    Mode”进行初始化配置。

**启动 U 盘制作**

下面说说如何制作U盘启动盘（也可作安装介质），分 Windows 与 Linux
两个平台分别介绍。注意很多U盘在出厂时量产程序产生的分区表可能不适合作系统盘，这种分区表在Linux下
/dev/sdb（假设sdb就是U盘设备）就是整个U盘（USB-FDD模式），我们需要重新建立一个/dev/sdb1（即USB-HDD模式）的主分区。当然我们可以在
Windows 下直接使用 Ultraiso
工具，它会直接对U盘分区表作重新调整。制作完成的 U 盘既可作 OpenPCTV
启动，也可作它用，但请保持其至少1G以上的空闲容量。

*Windows 两种办法:*

1.  可以使用Ultraiso工具直接将iso写入U盘
2.  先用 7zip
    等工具将iso内的所有内容解压到U盘，然后打开Windows的命令行窗口（注意
    Windows7/8 需要打开管理员模式的命令行窗口），再依次执行：
    1.  `F: ` 假设 F 为U盘盘符。
    2.  `cd boot` 进入boot目录
    3.  `bootinst ` 执行bootinst.bat
    4.  再按两次回车。

*Linux:*

1.  建立 openpctv-*.iso 光盘文件挂载点：`mkdir /tmp/iso`
2.  挂载 openpctv-*.iso
    光盘文件：`mount -o loop /where/is/you/openpctv-*.iso /tmp/iso`
3.  将iso中的所有内容拷入你的U盘，假设/media/usb
    是你的U盘挂载点：`cp -a /tmp/iso /media/usb`
4.  进入U盘的/boot目录：`cd /media/usb/boot`
5.  执行syslinux引导安装程序`bash bootinst.sh`

**运行配置**

-   第一次启动请进入"Setup
    Mode"完成所有初始化配置。配置过程将采用中文对话模式。期间包括语言设置、默认启动项设置、网络设置、DVB
    卡驱动配置、Lirc
    红外遥控选择、显示设备分辨率设置、音频设置、卫星参数自动下载、CAM
    解密模块选择、DiSEqC 配置（只针对
    VDR/XBMC，Enigma2需要进入其界面设置）、自动频道扫描（同样只针对
    VDR/XBMC，Enigma2 的同样须进入其界面）。值得说明的是对于广泛使用的
    CCcam 帐号你只需要将 CCcam.cfg
    丢到U盘中，系统启动时将会自动读入配置。
-   Enigma2/VDR/XBMC均运行在 tty4，你可以在任何时候按 `Ctrl+Alt+F1...F3`
    切换并以 root:root
    登录到shell，你可以运行setup继续进行配置。但要注意的是如果当前
    vdr.service
    正在支持，则所有针对vdr的修改均将无效，这里需要停止vdr进程，如：

    -   当前进入的是VDR：`systemctl stop vdr`
    -   当前进入的是XBMC：`systemctl stop vdr-backend`

    配置完后可重新启动系统或再直接启动vdr进程：

    -   `systemctl restart vdr`
    -   `systemctl restart vdr-backend`
-   你可以使用ssh远程登录到运行中的OpenPCTV，帐号root，密码root
    也可以使用ftp传送文件，帐号密码均为openpctv
-   Enigma2偶然存在死锁的情况，这里我定义了MCE遥控器上的"RECORD"按键为强制重启enigma2进程，这样你可按此键不不需要重新启动计算机来重启Enigma2

**相关链接：**

[项目主页](https://sourceforge.net/projects/openpctv)

[下载](https://sourceforge.net/projects/openpctv/files/release/)

获得源代码：`git clone git://git.code.sf.net/p/openpctv/code openpctv-code`
