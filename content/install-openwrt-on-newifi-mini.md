Title: Newifi Mini 安装 OpenWrt
Date: 2015-12-29
Author: lovenemesis
Category: Embedded
Tags: openwrt
Slug: install-openwrt-on-newifi-mini
Summary: 最近偶然入手 Newifi Mini 一枚，既然号称智能路由，当然要装上 OpenWrt 来试一试咯～

根据其他媒体及其产品页面介绍，[Newifi Mini](http://www.newifi.com/product_newifi_mini.shtml) 身世复杂，简单的说就是本土化 OpenWrt 系统 + 联想出资做硬件 + 百度深度植入。其最近官方固件貌似又扯上了京东和搜狐，远离了百度……

不谈那扯不清理还乱的强国 IT 圈不谈，还是看下这款设备吧。和近两年雨后春笋般冒出的所谓智能路由产品一样，Newifi Mini 亦是使用 MediaTek MT7620A SoC + MT7612E 5G 方案的产品。那么这款产品又什么特别的呢？

* 相比某数字和五谷厂商的同类型产品，此款的 U-boot 并未锁
* 散热孔设计相对合理些
* 表面的镜面处理是个绝佳指纹收集器（误）
* 可控制的 LED 稍多些

其他的硬件特性为：

* 2x2 3db 外置天线
* 2.4GHz 802.11n 300M + 5GHz 802.11ac 866M
* 两个百兆 LAN 及一个百兆 WAN 口
* 16M Flash
* 128M DDR2 内存
* 具备一个 USB 2.0 接口

**** 官方系统

根据网上流传的早期固件版本评测，该设备官方固件使用需要百度账号，所以在下完全跳过了……不知道现在版本固件的内容如何。了解官方版本宣传的功能可参考其[产品页面](http://www.newifi.com/product_newifi_mini.shtml)。

**** 安装 OpenWrt

前面说过这款设备的 U-boot 并没有锁，所以您完全可以直接刷入 OpenWrt 系统的，方法如下：

1. 前往 OpenWrt 官网下载对应固件，设备实际型号[名为 Lenovo Y1](http://downloads.openwrt.org/chaos_calmer/15.05/ramips/mt7620/openwrt-15.05-ramips-mt7620-Lenovo-y1-squashfs-sysupgrade.bin)
2. 通过有线连接设备，并将 PC 端设备 IP 设定为 192.168.1.11，子网掩码 255.255.255.0，网关 192.168.1.1 。
3. 拔下路由器后面的电源，拿在手里，然后再次通电，之后**迅速按下 RESET 按钮**，若是设备上出现两个蓝灯连续闪烁，代表已经进入 U-boot 恢复模式。
4. 在浏览器中输入 192.168.1.1 进入恢复模式页面，选择之前下载的 bin 文件即可开始刷机
5. 将 PC 端设备 IP 重置为自动获取模式，即可开始常规 OpenWrt 配置了

**** 开启 5G 网络

这款设备的 OpenWrt 固件生成依然是遵循了极简原则，于是需要在配置好网络连接后自行安装 5G 网络驱动模块。其 MT7612E 5G 芯片被包含在 `kmod-mt76` 软件包中

`opkg update && opkg install kmod-mt76`

之后重新启动路由器，便可以在 LuCI 中看到 5G 网络的 radio 选项了。

**** 总结

和使用 Qulcomm Atheros 方案或者更高档次的 MT7621 双核方案相比，这个百兆双无线的无线路由器的价格优势显著，配合良好的 OpenWrt 支持及便利的刷机方式，那个 USB 2.0 接口可以玩转很多有趣的事情。


[OpenWrt Wiki: Lenovo Y1](https://wiki.openwrt.org/toh/lenovo/lenovo_y1_v1)
