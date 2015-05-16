Title: OpenGL 4.2 for Linux
Date: 2011-08-11 14:45
Author: lovenemesis
Category: Drivers
Tags: AMD, NVIDIA, OpenGL
Slug: opengl-42-for-linux

在本月 8 号 Khronos 组织发布跨平台 3D 标准 OpenGL 4.2
之后，今天两大显卡厂商在 Linux 平台下的闭源驱动都已经准备就绪。

OpenGL 4.2 的新特性有：

-   允许 Shaders
    的原子化计数器，将单一材质的读取-修改-写入操作和并入一层。
-   捕获 GPU
    表面纹理操作，并在一次变换操作中绘制多个线程，允许在绘制复杂对象中有效的重新定位。
-   允许改变一个指定区域内的材质，而无需重新下载整个材质，，有效的提升了
    GPU 性能。
-   将多个 8 位和 16 位操作整合为一个 32 位操作来提升 Shader 的效率。

[英文详细介绍和发布公告](http://www.khronos.org/news/press/khronos-enriches-cross-platform-3d-graphics-with-release-of-opengl-4.2-spec)

[NVIDIA OpenGL 4.2 Linux 280.10.01.02
驱动](http://developer.nvidia.com/opengl-driver)

[AMD Catalyst OpenGL 4.2 Preview Linux
驱动](http://support.amd.com/us/kbarticles/Pages/AMDCatalystOpenGL42BetaLinux.aspx)

*消息来源：*
[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=OTc4MA)
