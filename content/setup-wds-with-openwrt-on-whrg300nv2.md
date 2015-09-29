Title: WHR-G300N V2 上使用 OpenWrt 构建 WDS 无线网络扩展
Author: lovenemesis
Date: 2015-09-25
Category: Tutorial
Tags: openwrt, wds
Slug: setup-wds-with-openwrt-on-whrg300nv2
Summary: OpenWrt 15.05 中基于 Atheros 方案的 WDS 网络扩展成熟起来，这里介绍如何使用两台 Buffalo WHR-G300N V2 组成 WDS 网络，适用于在结构奇葩或者错层大宅等房间环境下的网络部署。

#### 刷入 OpenWrt

Buffalo WHR-G300N V2 的硬件和 WHR-G301 一样，所以可以直接使用针对它的固件。若是还没有在 Buffalo WHR-G300N V2 刷入 OpenWrt 或者更新至 15.05 的话，可以参照下面的方式操作：

1. 前往 OpenWrt 官网下载 WHR-G301 的固件：[从官方固件升级](http://downloads.openwrt.org/chaos_calmer/15.05/ar71xx/generic/openwrt-15.05-ar71xx-generic-whr-g301n-squashfs-factory.bin) 或者 [自 OpenWrt 升级](http://downloads.openwrt.org/chaos_calmer/15.05/ar71xx/generic/openwrt-15.05-ar71xx-generic-whr-g301n-squashfs-sysupgrade.bin)
2. 确保使用有线方式连接路由器，还是因为 OpenWrt 默认不开无线网络……
3. 前往官方固件的 `Admin` 或者 OpenWrt 固件的 `Reflash` 更新便可以了。
4. 等待 WHR-G300N V2 上红色的 DIAG 灯熄灭后，便可以在浏览器中通过 `192.168.1.1` 访问 Web 管理界面了
5. 重复这个步骤，对两台 WHR-G300N V2 都更新至 OpenWrt 15.05 版本

#### WDS 无线网络扩展

WDS 是一个非标准的 IEEE 802.11 无线网络扩展，允许两台路由器通过无线的方式连接起来形成一个内网环境，连接至路由器 A 的主机可以透明的访问的连接至路由器 B 的主机。

由于是非标准的方案，各个厂商的实现机制都有所差异，所以在官方固件基本上只允许同品牌甚至同型号的产品之间组成 WDS 网络，有的还有数量限制，比如 WHR-G300N V2 的官方固件仅允许两台同型号。得益于 OpenWrt，只要所用芯片一样，不同品牌的之间也可以组成 WDS 网络，也打破了无谓的数量限制。

选定刷好 OpenWrt 的路由器中的一台作为**主访问点**，这个访问点的 WAN 接口需要连接 ADSL/Fiber 猫或者更上一级网络。其余的路由器称为 **次访问点**，这些路由器按照 WDS 的说法起到扩展主访问点覆盖范围的功效。

##### 主访问点的配置

1. 使用有线方式连接主机和主访问点，通过 `192.168.1.1` 在 Web 管理界面在 `Interface` 中完成 WAN 相关的配置，PPPoE 或者 DHCP(Client) 什么的
2. 确保之后可以通过这台路由器访问互联网或者上级网络
3. 前往 `Wifi` 设定，开启无线网络，注意 `Access Type` 需要选择 `Access Point(WDS)`，然后像通常一般指定 SSID、加密方式和访问密钥。
4. 拔掉主机和主访问点的连线，确保现在可以通过这台路由器的无线节点上网。

主访问点配置完成

##### 次访问点的配置

1. 使用有线方式连接主机和次访问点，通过 `192.168.1.1` 在 Web 管理界面在 `Interface` 的 LAN 中**禁用 DHCP 服务**，因为很显然只需要主访问点的 DHCP 服务就可以了，改为静态地址。这个地址需要和主访问点同一个子网，但又在其 DHCP 地址池的分配范围之外，在 OpenWrt 中这一般在 100 以内，比如 `192.168.1.2`。
2. 拔掉主机与次访问点的连接，将主访问点和次访问点的两个 LAN 连接起来，主机应该可以通过新指定的 IP 地址打开次访问点的 Web 配置界面。
3. 前往 `Wifi` 设定，开启无线网络，注意 `Access Type` 需要选择 `Client(WDS)`，然后再下方**指定主访问点的** SSID、加密方式和访问密钥。**重要**
4. 稍等一会儿，WDS 的连接建立需要大约 1 分钟。之后将主机的无线网络暂时禁用，再次使用有线方式连接次访问点，此时应该可以正常上网了。
5. 如果上一步没问题，再次前往 `Wifi`页面，在无线网络设备的页面点击 `Add` 按钮添加一个虚拟访问节点（VAP），这个节点将用于无线连接次访问点。
6. 点击新创建的 VAP 开始配置，可以发现诸如网络制式和频道之类是无法调整的，毕竟共用一个天线嘛。下面的 `Access Type` 选择 `Access Point`，类似一般的指定 SSID 和加密方式即可。这里的 SSID 并不特别要求和主 SSID 的一样，允许不同。个人经验是不同的 SSID 可以方便手动选择当前信号最佳的节点，因为有些设备（PS Vita）选择 WiFi 信号时太愚蠢了……
7. 断开主机和次访问点的有线连接，重新启用无线网络，此时应该能通过次访问点的节点正常上网了。

次访问点配置完成

如果有更多的路由器，可以参照上述方式添加到 WDS 网络中即可。

#### 参考文献

[OpenWrt Wiki: Atheros and MAC80211 WDS to implement a wireless network bridge (wireless repeater)](http://wiki.openwrt.org/doc/recipes/atheroswds)

[OpenWrt Wiki: Buffalo WHR-G300N V2](http://wiki.openwrt.org/toh/buffalo/whr-g300nv2)

[DD-WRT Wiki: WDS Linked router network](http://www.dd-wrt.com/wiki/index.php/WDS)