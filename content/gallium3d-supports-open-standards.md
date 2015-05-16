Title: Gallium3D 近期开发支持多个开放加速标准
Date: 2009-06-05 10:04
Author: toy
Category: News
Slug: gallium3d-supports-open-standards

{撰文/guest}

进入了 Mesa 3D 的 Mainline Code 的 Gallium3D
近期开发活跃，将提供对于多个开放加速标准的支持（都是 Khronos
工作组相关的，也差不多都是 OpenGL 相关的），具体内容如下：

1. 将支持 OpenGL ES 1.x 和 2.x：为嵌入式设备设计的低 profile 版的
OpenGL，与 OpenGL 基本相同。比如在 iPhone 和 Android 中都使用 OpenGL ES
作为 3D API 接口。  
2. 将支持 OpenVG：为向量图设计的 API，比如可对 Flash（矢量部分）和 SVG
进行加速。根据 （我翻墙看的）的说明，将在未来的 Mesa 3D 7.6 版中包含
OpenGL ES 和 OpenVG 的支持。  
3. Hopefully soon（翻译成预期中即将？）支持 OpenCL 和 OpenGL
3.1：如标题，暂时还是空头支票，不过既然是 hopefully
soon，还是很有希望的。

附加说明：[Khronos](http://www.khronos.org/)
是多媒体制作和加速的开放标准的工作组，其管理的标准包括
OpenGL、OpenCL、OpenGL ES、OpenVG、COLLADA、EGL
等。其目的是要建立一套完整开放的标准（比如 OpenCL 可操作 OpenGL
内部数据；EGL 可操作 OpenGL 和 OpenVG，共享内部对象和
surface，缓存等）。在上面的 Blog
中作者提到，以对这些开放标准的支持程度来看，Mesa 3D 已经快成为 Khronos
的 SDK 了。

现在看来，这个开放标准＋开源开发的案例，也算是很强势了，有兴趣的也可以去看看与之竞争的
DirectX 10 和 DirectX Compute。

新闻来源：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=NzI3NQ)
