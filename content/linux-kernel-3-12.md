Title: Linux Kernel 3.12
Date: 2013-11-04 10:14
Author: lovenemesis
Category: Kernel
Slug: linux-kernel-3-12

过去的周末里 Linus 发布了 Linux 内核 3.12 版本，带来了新的 CPU
频率管理器。

详细的 [Kernel Newbie](http://kernelnewbies.org/Linux_3.12)
尚未就绪，[大体变化有](http://www.phoronix.com/scan.php?page=news_item&px=MTUwMjg)：

-   优化了 CPU
    频率管理器，更有效的实现动态调频功能，间接提升了部分开源和闭源驱动的性能。
-   进一步改善了 Radeon 开源驱动的动态电源管理。
-   增加了逆向工程出来的 Snapdragon/Adreno 显卡驱动。
-   支持 AMD 首个异构计算的 Berlin 系列服务器 APU。
-   小幅改善了 F2FS、XFS 和 Btrfs 文件系统。

[官方源代码下载](https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.12.tar.xz)

**友情提醒：**~~目前 NVIDIA 闭源驱动[尚未官方支持 3.11
及以上的内核](https://devtalk.nvidia.com/default/topic/628864/unix-graphics-announcements-and-news/num_physpages-and-support-for-3-11-and-later-kernels)，升级需谨慎。~~
[NVIDIA 闭源驱动需使用
331.20](http://www.nvidia.com/Download/driverResults.aspx/69372/en-us)
或以上版本，包含[对于 3.11+
内核支持的临时解决方案](http://www.phoronix.com/scan.php?page=news_item&px=MTUwNjA)。
