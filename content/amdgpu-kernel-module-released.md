Title: AMDGPU 驱动模块发布
Date: 2015-04-21 11:26
Author: lovenemesis
Category: Drivers
Tags: AMD, amdgpu
Slug: amdgpu-kernel-module-released

作为 [AMD
统一化驱动策略](https://linuxtoy.org/archives/amd-announce-unified-gpu-driver-stack.html)的核心，`amdgpu`
驱动模块发布，协同对应的 Xorg 及 Mesa 补丁。

本次发布包括：

* `amdgpu` 内核模块，同时服务于开源及闭源驱动  
* 新的 `xf86-video-amdgpu` DDX 驱动，用作 2D 加速，推测应该仅是导向
GLAMOR 而已  
* 对应的 Mesa 补丁，从而 3D 部分依然使用现有成熟的 radeonsi 部分  
* UVD 硬解及 VCE 硬编码支持  
* 试验性的 Rx 300 支持

该驱动主要对象是即将发布的 Carrizo 系列 APU，不过依然包含 R9 285 Tonga
GPU 支持，后者当下缺少 DPM 支持，不过很快就会补上。

再次说明该驱动将无法兼容更早的产品，部分原因也是内核模块的限定，所以别妄想了……

[Git 分支](http://cgit.freedesktop.org/~agd5f/linux/log/?h=amdgpu)

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=AMD-AMDGPU-Released)
