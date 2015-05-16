Title: D3D9/10/11 支持将通过 Gallium3D 登陆 Linux
Date: 2010-02-09 09:18
Author: toy
Category: News
Tags: Gallium3D
Slug: gallium3d-supports-d3d

{ 撰文/guest }

Gallium3D 是当前 Linux 图形部分的一大亮点，Gallium3D 提出的 3D
驱动模型得到了社区的认可，Gallium3D
本身的发展也引人瞩目。最近，一名开发者为 Gallium3D 开发了 D3D9 支持。

根据介绍，此实现可为 Wine 提供基于硬件的 D3D9 加速功能。  
代码地址为 。

之后根据另一位 Zack Rusin 的介绍，当前正在开发中的 Gallium3D 新特性包括  
OpenCL1.0、D3D10/10.1/11。

至此 Gallium3D 所支持的 API 达到一个新高度（当然很多还在开发当中）：  
OpenGL/ES、EGL、OpenVG、OpenCL、D3D。  
与 NV/ATI 的 Windows 驱动所支持的相比已经是只多不少了（多了 OpenVG 和  
EGL，没提到 DirectCompute）。  
加之最近的 Wine 在 D3D10 支持上的开发，也许不久后我们能够在 Linux  
上得到基于硬件加速的全部 API。

{ via
[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=Nzk2OQ).
Thanks guest. }
