Title: 折腾：给 TL-WR703N 安装 OpenWrt
Date: 2015-02-20 23:00
Author: lovenemesis
Category: Featured, Gadget
Tags: OpenWrt
Slug: howto-install-openwrt-on-tl-wr703n

在下的[树梅派2](http://www.raspberrypi.org/products/raspberry-pi-2-model-b/)不幸被延期到年后才能发货了，[春节没的折腾了怎么办](http://zone.guokr.com/area/SpringFFFFFFFestival/)？无意中在
Rpi2 的报道中读到了关于 TL-WR703N
的消息，才想到还剩在箱底的她。思索着既然是春节，就做个好事情，将 OpenWrt
介绍给她！

### 主角介绍

[TL-WR703N](http://www.amazon.cn/gp/product/B005J29SSE) 是 TP 在 2011
年推出的一款便携式 3G 路由器，具备一个可连接 3G 上网卡的标准 USB
口，802.11N 150M 无线网络，microUSB 供电接口，搭载 Atheros AR7240 CPU 及
Atheros AR9331 芯片组。小巧省电，不到手掌心大，功耗不及 0.5W。

[OpenWrt]则是面向路由器等小型嵌入式设备的 Linux 发行版，可以使用 opkg
包管理器轻松扩展功能。截止本文发表时最新版本为[代号是 Barrier Breaker 的
14.07 Final
版](https://lists.openwrt.org/pipermail/openwrt-devel/2014-October/028346.html)，使用
Linux Kernel 3.10 。

### 初次见面

单纯刷入 OpenWrt 固件相当简单，OpenWrt 提供了针对 TL-WR703N
的预编译镜像。大致步骤如下：

1. 从 OpenWrt 官网下载对应型号的固件，由于这个时基于 AR7240 CPU
的，所以在[名为 ar71xx
的目录下](http://downloads.openwrt.org/barrier\_breaker/14.07/ar71xx/generic/)寻找
wr703n 即可。

2. 首次从官方固件转换到 OpenWrt 固件，需要使用
[factory](http://downloads.openwrt.org/barrier\_breaker/14.07/ar71xx/generic/openwrt-ar71xx-generic-tl-wr703n-v1-squashfs-factory.bin)镜像。另外的[sysupgrade](http://downloads.openwrt.org/barrier\_breaker/14.07/ar71xx/generic/openwrt-ar71xx-generic-tl-wr703n-v1-squashfs-sysupgrade.bin)用于从老版本的
OpenWrt 升级，这里无须操心。

3. 使用**有线方式**连接 WR703N 与电脑，然后在浏览器中输入 WR703N
的网络配置
IP。验证用户名和密码后，在左侧选择`固件升级`，然后选择刚才下载的
OpenWrt
镜像，确认写入。若是固件不识别，尝试将固件名称缩短些，比如重命名为
`openwrt.bin`。

4. 耐心等待，大概快五分钟后，它会自动重启，此时迎接您的就是 OpenWrt 的
[LuCI 管理配置界面](http://luci.subsignal.org/)了。

根据 Wiki 上的说明，似乎 V1.7
版的官方固件存在兼容性问题，刷入困难。笔者手上的 V1.2
版倒是一切顺利，此外 14.07 Final 版的代号早已远高于报告有问题的
Trunk，应该无须担忧。

### 轻度调教

在呈现的登陆提示框下设定了 root 账户密码后，名为
[dropbear](https://matt.ucc.asn.au/dropbear/dropbear.html) SSH
服务器就可以使用了。用任意 SSH 客户端即可登陆进行配置工作

记得之前强调要用有线方式链接么？因为 OpenWrt 的无线网络默认是关闭的……

接下来根据个人需要分别设定无线网络和有线网络接口的功用，PPPoE、DDNS
什么的都有，如有必要还可以配置下防火墙什么。

如果您仅是想要 WR703n 继续乖乖的做一个路由，至此就可以了。

如果想要进一步挖掘它的其他潜能，请继续往下读。

### 想要更多

顺便浏览下 opkg 软件仓库及 OpenWrt 的
Wiki，这款小小的设备的处理器还有很大的潜能。不过若是想要更多的话，首先要解决存储空间的问题，否则一两个额外软件包就能占满其仅有
4M 的闪存。而扩充容量最直接的方式就是插一个 U 盘！接下来要做的就是将
`/` 分区迁移到大容量的外接 U 盘上。

找一个**空闲的 USB2.0 接口的 U 盘**，注意太老的 USB 1.1
不认，格式化成 ext4 格式，插到 USB 接口上，然后在通过 SSH
在终端中执行以下步骤为系统添加外部 USB 大容量存储设备支持：

`opkg update`  
`opkg install kmod-usb-storage block-mount kmod-fs-ext4`

亦可在 LuCI 的 Software 面板中操作。Wiki 中还建议在 U
盘中顺道创建一个交换分区，可以根据您的接下来的具体应用考量。

然后用 `mount` 简单尝试下能否正常挂载，若是没问题话，继续。  
假设 U 盘挂载到了 `/mnt/sda1`

mkdir -p /tmp/cproot  
mount --bind / /tmp/cproot  
tar -C /tmp/cproot -cvf - . | tar -C /mnt/sda1 -x  
umount /tmp/cproot

之后用 `vi` 编辑 `/etc/config/fstab` 文件，仿照如下字段修改或添加：

config mount  
option target /  
option device /dev/sda1  
option fstype ext4  
option options rw,sync  
option enabled 1  
option enabled\_fsck 0

保存退出，然后重启 WR703n，然后用 `df` 看看 `/`
分区容量是不是增大了呢？

除了这里描述的将整个 `/` 迁移到 U 盘的方法以外，还有一种仅将包含系统的
`/overlay` 分区迁移的方法，效果类似，不再赘述。

### 分享彼此

既然通过扩容获得了足够的空间，可以折腾的空间就大很多了，比如您首先可能想要的就是中文支持：

`opkg install kmod-nls-utf8 luci-i18n-chinese`

接下来就任凭您想像了。有趣的是，不知出于何种原因中文论坛有不少人求该款设备的应用，这里还是建议直接从官方仓库在线安装比较好。

这里，首先介绍使用 Samba 供局域网分享文件。

为了方便管理及配置，可以安装 LuCI 的 Samba 管理模块：

`opkg install luci-app-samba`

它会依着依赖关系安装 Samba 3.6 版的服务器端。此外在 LuCI 界面上增加了
Service 分类，点击下面的 Network Share 开始配置。

General Settings
下的内容非常直观，主要是指定要共享的文件夹目录以及新文件权限。值得修改的是
Edit Template 标签中的内容。以下是几个推荐修改的选项

unix charset = UTF-8 #中文支持  
security = share #方便本地访问

Wiki
页面上用了不少篇幅在说明防火墙的配置，似乎并不适用于最新版本的默认防火墙配置：它默认就已经是仅允许局域网访问。

### HTTP下载

在测试 Samba
可以良好的实现包括手机、高清播放机及电脑之间的文件共享之后，我琢磨着要不再用它做下载好了。

HTTP 当然首选 `aria2`
，内存占用少，支持多线程及后台运行，直接从仓库里安装即可。

`opkg install aria2`

之后按照 RPC 方式将 aria2 以守护进程方式运行：

`/usr/bin/aria2c --enable-rpc --rpc-listen-all -D -d [DOWNLOAD
FOLDER]`

省事期间，可以直接将这一句写道 `/etc/rc.local`
中实现开机后自动运行，可以通过终端或者 LuCI 的 Startup 标签页操作。

[aria2](http://aria2.sourceforge.net/)有不少前端，电脑上可以用[WebUI](https://github.com/ziahamza/webui-aria2)，Android
手机则可以用[Transdrone](https://play.google.com/store/apps/details?id=org.transdroid.lite)，配置都非常简单，无需赘言。

若是将下载目录指定为上述的 Samba
共享目录的话，更可以实现下载内容整个局域网可见。

### BT 下载

其实上面的 `aria2` 也可以支持 BT 下载的，只是 OpenWrt
仓库里的版本出于某种原因编译时没开启。所以就选择 `transmission`
好了。它提供了 LuCI 管理界面，可以直接在 Service 下配置：

`opkg install luci-app-transmission`

`transmission` 的远程管理工具一抓一大把，从 Web、GTK+、Qt 到 Android
手机版，不再赘述了。

### 性能及测试

借助 OpenWrt，WR703n 的性能得以充分发挥，在经过了如上配置后，同时两个
HTTP 下载及 Samba 大文件拷贝也不过仅仅消耗了其 50% 的 CPU 及 35%
的内存，意味着它还有不少潜力可以发挥。这一切都仅仅需要不到 0.5W
的功耗，实在是环保节能啊。

若是您手上也恰好这样一个小设备，不妨也试试用 OpenWrt 折磨它吧～

### 参考阅读

[OpenWrt Wiki:TP-Link
TL-WR703N](http://wiki.openwrt.org/toh/tp-link/tl-wr703n)

[OpenWrt Wiki:USB
Storage](http://wiki.openwrt.org/doc/howto/usb.storage)

[OpenWrt Wiki:Rootfs on External
Storage](http://wiki.openwrt.org/doc/howto/extroot)

[OpenWrt Wiki: Samba](http://wiki.openwrt.org/doc/howto/cifs.server)
