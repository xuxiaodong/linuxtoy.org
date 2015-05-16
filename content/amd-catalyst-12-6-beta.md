Title: AMD Catalyst 12.6 Beta
Date: 2012-06-01 23:51
Author: lovenemesis
Category: Drivers
Tags: Catalyst
Slug: amd-catalyst-12-6-beta

AMD 改变了其 Catalyst 闭源显卡驱动的发布策略，这次于 12.5 之前带来了
12.6 Beta 驱动。

Catalyst
显卡驱动将不再按照原先的每月发布的方式进行，而是在有切实用户体验改进的时候再发布，比如有新
3D 游戏/程序需要支持时。AMD
表示此举将免于用户不断的每个月更新驱动，却感受不到太多跟自己有关的变化。

另一方面，AMD 改善了驱动质量的反馈渠道，将提供更多公开测试的 Beta
版本驱动，上线了新的[问题汇报站点](http://www.amdsurveys.com/se.ashx?s=5A1E27D20B2F3EAC)。

回到这次发布的 12.6 Beta 版本，尽管官方的发布日志尚未出现，不过[根据
Phoronix
论坛的反馈](http://phoronix.com/forums/showthread.php?71284-AMD-Catalyst-12-6-Beta-improvements)来看的确有很大的变化：

-   仅支持标号 Radeon 5XXX 系列以及以后的显卡和 APU 产品。
-   大幅度改善了 GNOME Shell
    的稳定性，修复了随机崩溃和开启抗锯齿之后的花屏问题。
-   改善了 KWin 的直接渲染支持。
-   修复了 Chromium/Chrome 的 WebGL 支持。
-   支持应用程序配置文件。
-   Linux 3.3 kernel 和 X.Org Server 1.12 的支持。
-   引入新的 ShadowPrimary 2D 加速，使用
    `aticonfig --set-pcs-u32=DDX,ShadowPrimary,1` 启用。
-   改善了 XvBA 硬件解码的支持，优化了和 XBMC 的兼容性。

[官方驱动下载](http://support.amd.com/us/kbarticles/Pages/AMDCatalyst126beta.aspx)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTExMTU)

**PS:** 经测试该驱动在 Fedora 17 中工作良好，简述配置过程：

1.  安装最新的 `kernel-devel` 和 `gcc` 软件包。
2.  在保存有驱动程序 run 文件的目录执行它，根据屏幕提示完成安装。
3.  参照[此文](http://linuxtoy.org/archives/fedora-16-amd-proprietary-driver-installation-guide.html)编辑并重新生成
    GRUB2 以及 X.org 配置文件。SELinux 标签此次正确，无需修改。

