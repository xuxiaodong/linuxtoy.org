Title: smem: 内存占用报告
Date: 2009-05-06 17:26
Author: toy
Category: Apps
Tags: Python, smem
Slug: smem

smem 能够为你报告内存的占用情况，提供
PID、User、Command、Swap、USS、PSS、RSS
等信息。除了一般的文本信息报告外，smem 也可以生成条状或饼状图。

![smem](http://i.linuxtoy.org/images/2009/05/smem.png)

通过 `smem --help` 可以获得它的使用说明。

smem 要求 Kernel 2.6.27/Python 2.4 及以上版本、matplotlib 库。

[smem](http://www.selenic.com/smem/)
