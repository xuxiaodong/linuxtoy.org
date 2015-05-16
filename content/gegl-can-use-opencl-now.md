Title: GEGL 实现基于 OpenCL 的硬件加速
Date: 2012-03-22 02:30
Author: lovenemesis
Category: News
Tags: GEGL, GIMP
Slug: gegl-can-use-opencl-now

GIMP 的新图像处理核心 GEGL 获得了 OpenCL 加速支持，意味着可以使用 GPU
硬件加速部分图像操作。

目前以下这些操作合并入 GEGL 上游，将可以使用 GPU 加速渲染：

    gegl:opacity, gegl:threshold, gegl:over (Porter-Duff), color-temperature, invert, value-invert, whitebalance

该项目由 AMD 资助，由 Victor Oliveira 在 2011 年的 Google
暑期代码大赛中完成初始代码。

此外，位于吉林的 [Zhang Peixuan](https://github.com/peixuan) 在
[opencl-ops](http://git.gnome.org/browse/gegl/log/?h=opencl-ops)
中实现了更多的 OpenCL 加速操作，尚在审核并等待合并入主线：

    vignette, pixelise, noise-reduction, gaussian-blur, motion-blur, c2g (hell, yeah!), mono-mixer, snn-mean, gegl:bilateral-filter, edge-sobel, gegl:edge-laplace, gegl:levels

关于这些操作的具体用途[请参考
Wiki](http://www.gegl.org/operations.html#op_gegl:c2g)

另外最近 AMD 在[开源驱动的 OpenCL
支持方面](http://www.phoronix.com/scan.php?page=news_item&px=MTA3MjY)进展喜人，最终用户将**有希望在
2012 年末发行版比如 Fedora 18 上体验到开源的 GPU 硬件加速**。

*消息来源：*[Libre Graphics
World](http://libregraphicsworld.org/blog/entry/new-hardware-acceleration-code-landed-to-upstream-gegl)
