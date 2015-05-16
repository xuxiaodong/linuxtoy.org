Title: Radeon 开源驱动电源管理
Date: 2011-05-23 22:39
Author: lovenemesis
Category: Tips
Tags: radeon
Slug: power-management-for-open-sourced-radeon-driver

这个夏日，您使用开源驱动的 AMD 显卡也可以享受在 2.6.35
内核引入的电源管理功能了。

在 **2.6.35 内核**中引入了 AMD 开源驱动的电源管理，目前实现了 **GPU
核心频率调整、显存频率调整、电压调整和温度监控支持**。

具体的电源管理策略有两种：

-   **动态调整**(仅支持单显示器，偶尔闪屏)：`echo dynpm > /sys/class/drm/card0/device/power_method`
-   **配置文件**：`echo profile > /sys/class/drm/card0/device/power_method`
    1.  默认(使用显卡默认频率不做调整)：`echo default >/sys/class/drm/card0/device/power_profile`
    2.  自动(使用电池为“中”，连接电源为“高”，屏幕关闭为“低”)：`echo auto >/sys/class/drm/card0/device/power_profile`
    3.  低(慎用，可能在部分本本上造成显示问题)：`echo low >/sys/class/drm/card0/device/power_profile`
    4.  中(中速运转，屏幕关闭为“低”)：`echo mid >/sys/class/drm/card0/device/power_profile`
    5.  高(全速运转，屏幕关闭为“低”)：`echo high >/sys/class/drm/card0/device/power_profile`

电源管理功能支持**全系列 Radeon 显卡**，需要**至少 2.6.35 内核**。

注意这个设置**仅在当前运行时立即生效**，若是想要开机自动启用的话，将对应的更改加入
`/etc/rc.local` 文件即可。

KDE 用户还可以在[这里](ttp://is.gd/ytBHes)下载对应的桌面小程序。

*参考来源*：[X.org Wiki](http://wiki.x.org/wiki/RadeonFeature)
