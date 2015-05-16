Title: GIMP GEGL 迁移工作基本完成
Date: 2012-04-19 01:45
Author: lovenemesis
Category: Image Editor
Slug: gimp-gegl-porting-nearly-done

在担心为何 GIMP 2.8 迟迟不见正式发布？原来他们在忙于 GEGL
的迁移工作，原本以为要很久的工作在三周的疯狂 coding 中完成了！

根据 Mitchs 博客上的说法，原本计划一周的 Hackfest 活动变成了三周的 GEGL
移植工作，**90% 的 GIMP 程序核心已经迁移到了 GEGL 上**，仅剩适用于图层的
`GeglOperations `部分。当 GIMP 2.8 正式发布后 GIMP 2.9/2.10 Master
将迁移至 100% GEGL 的分支上。

插件开发者们则可以通过 libgimp 中**新增加的 GEGL
的缓冲平铺后端**简单的享受 GEGL 带来的性能提升。

这项工作还带来了其他一些优势，比如将容易的实现**更高颜色深度的支持(16-bit)**；现在**对于索引图片也可以进行绘制和色彩修正**工作了。

*消息来源：*[GimpFoo
博客](http://gimpfoo.de/2012/04/17/goat-invasion-in-gimp/)
