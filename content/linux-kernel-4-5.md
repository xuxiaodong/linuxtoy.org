Title: Linux Kernel 4.5
Date: 2016-03-15
Author: lovenemesis
Category: Kernel
Tags: kernel
Slug: linux-kernel-4-5
Summary: Linux 内核 4.5 正式发布，带来了 ARM SoC 单一内核支持及 Raspberry Pi 3D 加速。

根据来自 [Phoronix 的总结](http://www.phoronix.com/scan.php?page=article&item=linux-45-features)来看，新版本内核包含的变化有：

* AMDGPU 支持 PowerPlay 重调频，支持 Tonga 和 Fiji 等新一代 GPU，不过仍然需要添加内核参数手动启用
* 历经五年的 ARMv6 及 ARMv7 指令集支持代码融合，终于可以创建适配于多种 SoC 的单一内核
* Raspberry Pi 的 3D 加速部分代码并入，实现完整的开源显示。
* 进程分组 Cgroup v2 升格为正式版
* Btrfs 引入新的空间缓存机制
* 其他安全更新

[详细更新日志](http://kernelnewbies.org/Linux_4.5)

[官方源代码下载](https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.5.tar.xz)
