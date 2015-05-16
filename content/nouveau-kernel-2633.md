Title: Nouveau 的 DRM 组件将（可能？）进入 Kernel 2.6.33
Date: 2009-12-12 11:38
Author: toy
Category: News
Tags: Kernel, nouveau
Slug: nouveau-kernel-2633

{ 撰文/guest }

Nouveau 是一个开源的 Nvidia 显卡驱动。相比之下 Nvidia  
的官方驱动不是开源的，而开源的 xf86-video-nv
功能又很弱。对比官方驱动，Nouveau  
的优势在于支持新内核的 Kernel Mode Setting 特性。在 Fedora 12 中，使用
Nouveau  

驱动启动内核后会第一时间直接进入显示器的最佳分辨率，启动界面（不论文本还是图形）与  
X、GDM 之间的切换、用 Ctrl+Alt+Fn 在 X 和终端间切换完全的"flicker  
free"，使用体验大大增强。

但是其 DRM 模块部分一直没有进入内核的代码树。昨天在 Phoronix  
网上看到一则消息，大意是说 Linus 看 Fedora 提供 Nouveau
已经很长时间了，希望  
Nouveau 的 DRM 也进入内核。Nouveau 的维护者和 Fedora  
的维护者则解释说主要是由于 Nouveau 是依靠反向工程来了解 NV GPU  
的某些内部机制的，使用了一些 Microcode，而这些 Microcode  
相关的代码进入内核可能有版权问题。Linus 回复说这些理由都是 BS(从几次
Linus  
的发言来看这位还真是"牛气"啊)，Fedora  
是不是完全没有版权问题的发行版？是那么上述理由就是
BS，否则以后发布就别分发  
Nouveau 驱动。

今天又看到上面一则消息，这件事的下文是这样：红帽公司的 David Airlie 和
Ben  
Skeggs 对 Nouveau 的内核部分代码进行了修改，Microcode 将使用内核的
Firmware  
接口来加载。这样就避免了版权问题。

接下来引用一句原文：

> In this pull request, there is the Nouveau driver that is set to go
in the  
> Linux 2.6.33 kernel under the staging area

也许 2.6.33 中，我们就能用上正式进入内核的 Nouveau
驱动，获得各种新特性了。

PS: NV 官方驱动虽然不支持 KMS，但是支持 OpenCL(G80+)，视频加速方面支持
XvMC(G80-)和 Vdpau(G80+)。对于这些功能，Nouveau 并没有支持。实际上连 3D
功能 Nouveau 也不直接支持。现在的发展趋势是由 Mesa 和其中的 Gallium3D
来提供 OpenGL（也许甚至是 D3D）、OpenVG、、OpenCL
的支持。显卡驱动仅仅完成与显卡的基本交互。最近 Kernel
的图像部分发展成为了亮点，page flipping ioctl 进入
2.6.33（"据说"不论对于 X 还是 Wayland 都很有用），现在 Intel/ATI/NV 的
KMS 驱动又都不断完善，Linux 用户的图形体验必将逐步增强。

{ Thanks guest. }
