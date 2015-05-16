Title: NVIDIA 宣布 Wayland/Mir 及 KMS 支持策略
Date: 2014-10-11 13:50
Author: lovenemesis
Category: Drivers
Tags: kms, NVIDIA, wayland
Slug: nvidia-announces-waylandmir-kms-support-strategy

在 XDC [AMD
宣布主打开源的统一化驱动策略](https://linuxtoy.org/archives/amd-announce-unified-gpu-driver-stack.html)的第二天，NVIDIA
亦在 XDC 上宣布了其闭源驱动接下来的发展方向，包括 Wayland/Mir 支持。

不出意外的，NVIDIA 方面依然是主导闭源驱动，其新策略要点有：

* 他们的确在努力实现其闭源驱动对于 Wayland/Mir 的支持。

* 重写其内核模块，使其能以类似当前 PRIME 支持的方式关联到 DRM KMS
ioctls 上，可供 `xf86-video-modesetting` 使用。不过其将不会直接使用
KMS API。

* 在用户态实现不依赖 X 的 EGL 支持，预期在今年秋季的 346.XX
上实现。不过由于内核态 KMS 的重写没完成，所以 Wayland/Mir 还是暂不可用。

* 相比 GBM，NVIDIA 更倾向于使用 EGLStreams
来处理帧缓存，从而减少分发自己 libgbm 的需要且兼容无 DRM 平台（如
QNX）。

* NVIDIA 并未公布具体完成时间点，不过估计在明年。

更多细节及演示内容，请参考下面的消息来源。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTgxMDE)
