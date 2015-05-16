Title: 简述 Linux 平台上浏览器的 GPU 加速
Date: 2011-11-29 00:08
Author: lovenemesis
Category: Featured
Tags: chrome, Firefox, gpu, Opera, webgl
Slug: brief-intro-gpu-acceleration-browser-on-linux

随着 HTML5 和 WebGL 逐步明朗化，浏览器开始寻求使用 GPU
加速的方式改善互联网体验。那么它在 Linux 平台的情况究竟是什么呢？

和其他桌面程序的显卡加速一样，**浏览器可以调用 GPU 实现的加速分为 2D 和
3D 两种**。

**3D 加速**

目前最常听到的是 3D 加速，也就是**显卡对于 WebGL 的支持**。WebGL 是
OpenGL ES 的一个子集，用于定义网页中的 3D 应用。

在 Linux 平台下，**Firefox 8** 对于 GPU 显卡 WebGL 加速的需求情况如下：

-   要求开源驱动 Mesa 版本在 7.10.3 以上，经典的 DDX 和 Gallium3D
    架构的驱动都可以。
-   NVIDIA 闭源驱动要求在 257.21 以上。
-   AMD Catalyst 闭源驱动需要实现 OpenGL 3.0 以上支持，10.6 以上即可。

**Google Chrome 15** 对于 GPU 显卡 WebGL 加速的需求情况如下：

-   要求开源驱动 Mesa 版本在 7.11 以上，暂不支持 Gallium3D 驱动(?)。
-   NVIDIA 闭源驱动要求 195.36.24 以上。
-   AMD Catalyst 闭源驱动暂不支持，可能需要等到 11.12 才行。

[WebGL
标准型兼容测试](http://www.khronos.org/webgl/wiki/Testing/Conformance)

[精彩 WebGL 应用：Lights](http://lights.elliegoulding.com/)

**2D 加速**

相比较与 WebGL，2D 加速的应用范围就广阔许多，已知的就有：

-   **YCbCr 到 RGB 的转换**(导致 Flash CPU 占有率居高不下的原因)。
-   HTML5 Canvas 的绘制。

理论上讲，所有元素都可以从 GPU 2D 加速中获益。

然而遗憾的是，**目前 Linux 平台上没有一款浏览器实现了 GPU 2D
加速**，原因是缺乏类似 Direct2D 一样的 API 以及目前驱动中普遍糟糕的
`texture_from_pixmap` 实现。

于是说目前 Linux 平台上的 2D
加速均是由软件后端的方式实现的，根据测试结果来看目前 Chrome 的 [Skia2
渲染后端](http://code.google.com/p/skia/)比 Firefox 的 [Azure(Cario)
后端](http://blog.mozilla.com/joe/2011/04/26/introducing-the-azure-project/)效率要高。

**花屏警告：**若是想强行尝试 2D 加速的话：

-   Firefox 中在 `about:config` 中设置
    `layers.acceleration.force-enabled=true` 。
-   Chrome 中在 `about:flags` 中启用“GPU 加速画布 2D” 和 “对所有网页执行
    GPU 合成“。

另一方面，[Opera 12 据说采取的 GPU
加速方式很特别](http://my.opera.com/desktopteam/blog/2011/10/12/hardware-acceleration)，将**有可能会是首个在
Linux 平台实现 2D 加速的浏览器**，十分值得期待。

[2D 加速测试](http://demos.hacks.mozilla.org/openweb/HWACCEL/)

[精彩 2D Canvas 应用：Particle
Acceleration](http://ie.microsoft.com/testdrive/Performance/ParticleAcceleration/)
