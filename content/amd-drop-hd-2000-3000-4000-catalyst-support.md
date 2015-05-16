Title: AMD 即将放弃 Radeon HD2000/3000/4000 系列显卡的驱动支持
Date: 2012-04-21 15:06
Author: liangsuilong
Category: Apps
Tags: AMD, Catalyst
Slug: amd-drop-hd-2000-3000-4000-catalyst-support

根据
[Phoronix](http://www.phoronix.com/scan.php?page=article&item=amd_catalyst_legacy2)的消息称，AMD
即将不再为 Radeon HD 2000/3000/4000 系列显卡提供驱动更新。

如同三年前的 Catalyst 9.4 不再支持 DirectX 9 显卡一样，AMD 也即将放弃
DirectX 10 的显卡驱动支持。现在 AMD 还没有正式宣布这个决定，根据
Phoronix 收到 AMD 的内线消息，大约在 12.7 起，Catalyst 不再支持 Radeon
HD 2000/3000/4000 显卡。在此之后，AMD 不会为这批显卡提供新的 X Server 和
Linux Kernel 提供支持，只会在重大 Bug Fix 才会再发布修复性驱动。

暂时尚不清楚是仅仅放弃 Linux 驱动的支持，还是 Windows 和 Linux
一并放弃驱动支持。Catalyst 驱动在 Windows 和 Linux
上共用了大部分代码，如果 AMD 放弃 Linux
的驱动支持，那么也很大机会同时放弃在 Windows
平台的支持。如果你打算使用这一世代的显卡顺利过渡到 Windows
8，那么你需要衡量能否有驱动支持的风险。

或许 AMD DirectX 10 显卡失去催火剂 Catalyst 驱动支持对 Linuxer
来说，是一种解脱，在今年下半年更新的 Linux 发行版，如 Fedora 18，Ubuntu
12.10 里，你将只能为你的显卡选择开源驱动。即将到来的 Mesa 8.1， R600
开源驱动将会得到 OpenGL 3.0 的支持，还有可能存在的基于 Gallium3D VPDAU
视频硬件加速。

相比起 AMD，NVIDIA 在放弃一批显卡支持以后，还会继续在 Legacy
驱动上及时增加新的 X Server 和 Linux Kernel 的支持。

 
