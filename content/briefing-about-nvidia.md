Title: 短讯：NVIDIA 相关
Date: 2012-06-19 13:59
Author: lovenemesis
Category: Drivers
Slug: briefing-about-nvidia

关于 NVIDIA 的三则短消息。

**Linus Torvalds 最近在阿尔托大学接受采访时对 NVIDIA
大爆粗口**，对于其在 Linux 平台上 Optimus
的支持颇为不满，称其为“最糟糕的公司”。[完整详细视频](http://is.gd/PURwzz)

似乎是为了相应 Linus 的批评，**NVIDIA 发布了 Linux 闭源二进制驱动 302.17
版本**，终于带来了 RandR 1.2/1.3 支持，新的 FSAA 抗锯齿模式，改善了
RENDER 位图文字的渲染，并且模式开启垂直同步。[64
位版本官方下载](http://www.nvidia.com/object/linux-display-amd64-302.17-driver.html)。

尽管 NVIDIA
依然拒绝提供任何支持给开源驱动开发者，通过社区努力逆向工程的**开源驱动
Nouveau 发布了 1.0 版本，并且在 Linux 内核 3.5 时离开 Staging
区域。**目前 Nouveau 已经可以实现对几乎全系列 NVIDIA 显卡的 3D
加速(部分需要手动提取固件)功能。由于缺乏文档，在电源管理方面支持缓慢。

**更新：**

NVIDIA 的公关部门今日[回应了 Linus
的说法](http://www.phoronix.com/scan.php?page=news_item&px=MTEyMjk)，要点如下：

-   Optimus 从一开始就仅为 Win7
    设计，以前没有，现在也没有在其他平台支持的计划。
-   已经在程序安装器和 README 文件中做了努力能和社区提供的解决方案
    Bumblebee 更好的协作。
-   能提供在新品发布当天 Linux 系统闭源驱动的支持。
-   NVIDIA 积极参与 Linux ARM 的工作。

最后 NVIDIA 公关部门表示他们的目标是为 “a consistent GPU experience
across multiple platforms for all of our customers” 。

**实在忍不住吐槽的 PS：**看来在 NVIDIA 眼中 Optimus 不属于 GPU
experience 的一部分啊……
