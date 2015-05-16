Title: NVIDIA 337.12 Beta
Date: 2014-04-09 12:33
Author: lovenemesis
Category: Drivers
Tags: NVIDIA
Slug: nvidia-337-12-beta

NVIDIA 发布适用于 Linux 平台的 337.12 Beta
闭源显卡驱动，带来了显卡超频支持。

本次 Beta 版本驱动带来的变化有：

-   支持 Geforce 400/500/600/700 系列 GPU 的超频。
-   新增了不少 EGL 扩展支持。
-   降低在使用 EGL 时 GPU 和 CPU 的占有率。
-   新增了对 GeForce GT 705、GT 720、830M、840M、845M、GTX 850M、GTX
    860M、GTX 870M 和 GTX 880M 的支持。
-   其他少量 Bug 修复。

最引人关注的超频支持需要在 xorg.conf 文件中增加
`Option "Coolbits" "integer"` 开启，具体数值配置可以参考 README
文件。之后进入 NVIDIA 控制面板，在同意免责条款后，即可看到对应选项。

[官方下载](http://www.nvidia.com/download/driverResults.aspx/74888/en-us)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTY1ODg)
