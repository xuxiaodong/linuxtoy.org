Title: AMDKFD 合并入 3.19 内核
Date: 2014-12-04 13:50
Author: lovenemesis
Category: News
Tags: AMD, hsa, OpenCL
Slug: amdkfd-drivers-pulled-in-kernel-3-19

作为 AMD 开源 HSA 异构计算核心的重要部分之一的 AMDKFD 内核驱动被纳入
Linux 3.19 内核，标志着 Linux 平台上的 HSA 计算基础架构完成。

本次合并入的 `amdkfd` 可以理解为在 DRM 子系统中提供了 CPU 与 GPU
沟通的快速通道，使得两者可以平等的访问内存资源而无需额外拷贝。结合前端时间同样[开源的
HSA DRM
用户态组件](http://www.phoronix.com/scan.php?page=news\_item&px=MTgzODY)改善，现有的
RadeonSI 开源驱动及 Mesa OpenCL State Tracker，Kaveri 系列 APU
即可实现异构计算。

另一方面，[AMD
统一化驱动](https://linuxtoy.org/archives/amd-announce-unified-gpu-driver-stack.html)尚需时日完善，预期将在
Linux 3.20 完成。届时应该能赶上 2015 H1 的[Carrizo 系列 SoC APU
](http://www.anandtech.com/show/8742/amd-announces-carrizo-and-carrizol-next-gen-apus-for-h1-2015)发布。

*消息来源*：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTg1MzE)
