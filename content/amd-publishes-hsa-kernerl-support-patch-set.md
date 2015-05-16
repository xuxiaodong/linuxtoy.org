Title: AMD 发布 HSA 内核支持补丁
Date: 2014-07-11 09:09
Author: lovenemesis
Category: Drivers
Tags: AMD, hsa
Slug: amd-publishes-hsa-kernerl-support-patch-set

AMD 发布了 83 个共计 1W+ 代码的补丁，为 Linux
内核增加了异构计算架构的支持，实现了 CPU/DSP/GPU 计算资源的通用。

HSA（Heterogeneous System Architecture）允许 CPU/DSP/GPU
共享内存页、用户态队列和平台级别的原子操作，本次发布的补丁实现了在 AMD
Kaviri/Berlin 系列 APU 和 Radeon Sea Islands GPU (R9 290/290X/290X2)上的
HSA 支持。除此之外，这系列补丁也是给 HSA 联盟的成员(特别是 ARM
阵营)用作参考实现的。

AMD 开发者 John Bridgman 在邮件列表中的发布公告中提到 Radeon Sea Islands
系列 GPU 会对 HSA 的指令在 GPUVM 和 IOMMUv2
之外提供硬件层面的验证操作，然后详细介绍了有哪些特别的操作。值得称赞的是，这些实现完全是以开源
radeon 驱动为范本的。

目前距离 Kernel 3.17 Feature Freeze 还有一段时间，意味着差不多年底前
Linux 用户既可以使用到 HSA 加速的 [Java
8](http://arstechnica.com/information-technology/2014/04/amd-demos-hsa-for-the-server-room-with-java-on-top/)
或 [C++
AMP](https://bitbucket.org/multicoreware/cppamp-driver-ng/wiki/Home)
程序了。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTczOTY)
