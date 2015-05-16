Title: K3b 1.0.3 发布
Date: 2007-07-23 20:46
Author: toy
Category: Apps
Slug: k3b-103-released

这个适用于 KDE 桌面环境的光盘烧录软件 [K3b](http://www.k3b.org/)
在今天推出了 1.0.x 稳定系列的 1.0.3 版。据 K3b
的开发者宣称，这将有望成为 1.0.x 系列的最后一个版本。K3b
的下一个版本将向 1.1 Alpha 挺进。

![K3b](http://i.linuxtoy.org/i/2007/07/k3b.jpg)

K3b 1.03 是一个新的 bug 修订版本，其更改情况如下：

> # Reverted to old behaviour of reloading medium before verification.
> Not enough testing had been done before introducing this and some
> systems fail to read the medium before reload (Bugs 147297, 147328,
> 147420, 147698).  
>  # Do not crash when the currently playing audio project item is
> removed (Bug 147548).  
>  # Added desktop actions to handle empty media with K3b.  
>  # Fixed read retry when reading data tracks (Bug 147778).  
>  # K3b's dialogs now honor the global button layout setting (Bug
> 147799).  
>  # Do not crash on mp3 files without tags if compiled with taglib
> support (Bug 142651).  
>  # Do not allow to copy a rewritable media to itself.  
>  # Fixed crash on startup with devices that return bogus GET
> PERFORMANCE data (Bug 147676).

- [Download K3b 1.0.3](http://k3b.plainblack.com/download)
