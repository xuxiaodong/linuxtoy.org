Title: OpenGL 及 OpenCL 的进展
Date: 2009-02-04 10:00
Author: toy
Category: News
Tags: OpenCL, OpenGL
Slug: opengl-and-opencl

[撰文/guest]

近期 OpenGL 有了新的发展，NVIDIA 发布了正式支持 OpenGL 3.0 规范的
[180.27](http://linuxtoy.org/archives/nvidia-release-18027-opengl3-officially-supported.html)
驱动（8 系列及之后系列硬件支持 OpenGL 3.0），ATI 方面则发布了 [Catalyst
9.1](http://linuxtoy.org/archives/ati-catalyst-91.html)，亦提供了 OpenGL
3.0 的支持（2400 系列及之后系列硬件支持 OpenGL 3.0）。OpenGL 3.0 相对于
OpenGL 2.0 的改变主要在于随着硬件可编程程度的增加，API 逐渐像 shader
编程方向转变，而逐渐淘汰固定功能管线渲染相关的功能。具体到应用上，就是将几何
shader（GS）扩展正式纳入核心部分（早在 3.0
规范前已有此扩展）。在这一点上，与 DirectX 10
的步伐基本是一致的。在此不想讨论 OpenGL 与 DirectX
的种种，有兴趣的可以去学学这两种 API，再看看计算机 3D
图形学和硬件相关的知识。

另外由 Apple 提出的 OpenCL 并行计算语言在早些日放出了 1.0
版规范，其可利用的计算设备不光有 GPU，还包括支持相关规范的 CPU、DSP
等。只是还没有相关的支持。最近在 GCC 的 Mail  
list 中出现了一贴，讨论 GCC 对 OpenCL
的支持问题，有兴趣者可看[原文](http://gcc.gnu.org/ml/gcc/2009-01/msg00591.html)。除去
GCC，还有 Mesa，准确的说是即将进入 Mesa 的 Gallium3D
的开发意向，[原文](http://zrusin.blogspot.com/2009/02/opencl.html)将开发
OpenCL 的支持。暂不讨论 OpenCL 与 CUDA、StreamSDK 孰优孰劣，假如
Gallium3D 支持
OpenCL，那么开源界将有一个通用的并行语言支持，而不是限制在 NV 或 ATI
的硬件上，总是件不错的消息。
