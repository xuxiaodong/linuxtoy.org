Title: AMD 宣布统一 GPU 驱动架构
Date: 2014-10-09 13:50
Author: lovenemesis
Category: Drivers
Tags: AMD, amdgpu, Catalyst, Mesa, radeon
Slug: amd-announce-unified-gpu-driver-stack

在正在举行的 X.org Developer's Conference 上，AMD 宣布了统一化的 GPU
驱动架构，将当前开源的 radeon 及闭源的 fglrx
内核模块统一成单一的开源内核模块，将闭源部分限制在用户态。

新驱动架构的亮点有：

* 引入名为 `amdgpu` 统一新内核模块，替代现有的开源 `radeon` 及闭源
`Catalyst` 模块。

* 新架构将大量运用 Linux 系统中现有的图形组件，包括 TTM
图形内存管理、DRM 模式设定、DRI 缓存共享及 GLAMOR OpenGL 2D 驱动等。

* 新架构对于将同时支持 Mesa 开源驱动及 Catalyst
闭源驱动，意味着仅需要简单用户态的操作（甚至无需重启）即可在开源及闭源的
OpenGL 3D 及 OpenCL 通用计算实现之间切换。

* 新架构下 Catalyst 将仅局限于用户态，其 OpenGL 及 OpenCL
实现将依然保持闭源，不会开放。

* 新架构包括统一且开源的 HSA 异构计算支持，可供开源 Gallium3D Clover 及
Catalyst OpenCL 使用。

* 对于有特殊需求的行业用户，提供名为 FirePro
的闭源附加组件，同时相关的开源组件也需要做出修改以适应。

* 目前该新架构在针对即将发布的 Rx 300 "Pirate Islands" 系列 GPU
进行开发，没有支持现有 Rx 200 及更早 GPU 的计划。

对于最终用户来说，这些变革带来的好处有：

*
无需在为安装闭源驱动进行编译内核模块的操作，且无需担心新内核不兼容的问题。因为
`amdgpu` 作为上游内核模块，必须要考虑用户态兼容性。

* 在开源 Mesa 及闭源 Catalyst
之间的切换将非常简单，对系统改动也局限在用户态。

* 对于 Wayland 的闭源驱动支持将变得非常容易，仅需要实现要求的 EGL
即可。

* 通过现有的 DRI 架构可以流畅的实现双显卡切换。

[详细幻灯片说明](http://www.phoronix.com/scan.php?page=news\_item&px=MTgwODA)

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=article&item=amd\_bordeaux\_strategy#=3)
