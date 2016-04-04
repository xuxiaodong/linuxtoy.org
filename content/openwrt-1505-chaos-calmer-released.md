Title: OpenWrt 15.05 Chaos Calmer 发布
Author: lovenemesis
Date: 2015-09-22
Category: Embedded
Tags: openwrt
Slug: openwrt-1505-chaos-calmer-released
Summary: 针对路由器环境的第三方固件 OpenWrt 发布了 15.05 正式版，带来了内核 3.18 及大量安全更新。

新版本的变化有：

* 更新内核至 3.18.20 版本
* 包含 openssl、curl 等组件的安全更新
* 新增大量 3G/4G 猫的支持
* 增加对 SQM QoS、AQM 和 Traffic Shaping 的支持
* 更好的支持 DNSSEC
* 新增 `sunxi`，支持全志系列设备
* 新增 `mxs` ，支持 Freescale 系列设备
* 新增 `mt7621`，支持联发科 802.11AC 的 SoC 设备
* brcm2708 模块增加对 Raspberry Pi 2 的支持

[详细更新日志](https://forum.openwrt.org/viewtopic.php?pid=291233#p291233)

[多平台下载](http://downloads.openwrt.org/chaos_calmer/15.05/)

#### 关于 TL-WR703N 的额外说明


如果您跟随本站早先[折腾文将 TL-WR703N 刷成 OpenWrt](https://linuxtoy.org/archives/howto-install-openwrt-on-tl-wr703n.html)了，那么请注意在升级之后需要**重新创建在外置 USB 存储设备上的根分区**。
此外由于 15.05 版本相比上一个版本固件大小有所增加，无法正常通过 `opkg` 安装必要的软件包，于是建议通过自定义镜像的方式构建，方法如下：

1. 下载适用于该架构的 [ImageBuilder](http://downloads.openwrt.org/chaos_calmer/15.05/ar71xx/generic/OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64.tar.bz2)
2. 在一个 Linux 64bit 系统上解压，使用如下命令构建自定义镜像：
    `make info` 找到自己的设备预置文件名称，比如这里要使用的是 "TLWR703"
    `make image PROFILE="TLWR703" PACKAGES="block-mount kmod-fs-ext4 kmod-usb-storage-extras"`
3. 之后新的镜像即在 `ImageBuilder` 的 `bin` 目录下生成，包含适用于升级的 `sysupgrade` 镜像。


