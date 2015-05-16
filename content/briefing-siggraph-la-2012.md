Title: 短消息：SIGGRAPH LA 2012
Date: 2012-08-06 23:53
Author: lovenemesis
Category: News
Tags: astc, Khronos, OpenGL
Slug: briefing-siggraph-la-2012

正在洛杉矶举行的 [SIGGRAPH 2012
大会](http://s2012.siggraph.org/)上标准的制定者 Khronos 发布了新的
OpenGL 和 OpenGL ES 的新版本，以及无专利限制的材质压缩算法。

新的 OpenGL 4.3 以及标准带来：

-   允许在图像流水线上文中执行 Shader 并行运算。
-   材质参数查询。
-   标准 ETC2/EAC 材质压缩。
-   允许在程序开发阶段获取除错信息。
-   改善内存安全性。

依照传统，NVIDIA 放出了提供 [OpenGL 4.3 支持的 Beta
测试版本驱动](http://www.nvidia.com/content/devzone/opengl-driver-4.3.html)，AMD
方面也预期会很快释出支持的 Catalyst 驱动。Intel 方面则恐怕要等到至少
2014 年了，依赖 Mesa/Gallium3D 的其他开源驱动状况类似。

针对移动平台的 OpenGL ES 也升级到了 3.0 版本，吸取了 OpenGL 3.3 和
OpenGL 4.2 一些功能，并和 OpenGL ES 2.0 保持向后兼容。

更为激动人心的是，Khronos 公布了一款新高性能且无专利限制材质压缩算法
ASTC。Adaptive Scalable Texture Compression
自适应可缩放材质压缩可以通用于 OpenGL 和 OpenGL ES，以 Khronos
扩展的形式发布。它的独特之处在于会为图像中每一个单独的像素块的情况自动选择最为合适的压缩编码方法。

材质压缩是常见的提高显存利用效率的方法，但是不同的压缩算法效率上差异，图形处理器的支持情况也有不同。在
X86 世界常见的为来自 S3 图像的 S3TC
压缩算法，但是由于专利问题，该材质压缩算法无法被 Mesa
开源驱动默认支持。这是导致在性能之外导致很多闭源 3D
游戏无法在使用开源驱动的 Linux 系统上运行的重要原因。

在移动平台上，特别是 Android 系统上，由于存在多个不同的 SoC GPU
解决方案，材质压缩算法也是多种多样。这也是为什么有些 3D
游戏会按照机型区分资源包的原因之一。

ASTC 的出现很有可能会改变现在这个局面。

由于没有专利风险，开源 Mesa/Gallium3D
驱动可以毫无顾虑的增加该算法支持，提供了闭源驱动类似的材质压缩选项；移动领域针对不同机型准备不同材质包给开发者和使用者带来的麻烦也会用于统一的
ASTC 而不复存在。

目前 ARM、AMD、Imagination 和 NVIDIA 已经在发布会上表示支持 ASTC
并鼓励开发者使用，著名 3D 引擎 Unity3D 的开发者也对新压缩算法大为称赞。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTE1NTA)
