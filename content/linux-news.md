Title: Linux 相关消息一束
Date: 2008-10-13 18:44
Author: toy
Category: News
Slug: linux-news

[撰文/guest]

以下是本人最近在网上浏览到的一些 Linux
新闻。单拿出一个来恐怕不够一个主题，所以就集合在一起说吧。

1 GCC 4.4.0 正在开发当中，其中的改进有对 C++ 0x
标准的进一步支持（详细特性支持列表请参阅
<http://gcc.gnu.org/gcc-4.4/cxx0x_status.html>）。一方面是需要程序员的具体实现，另一方面是
C++ 0x 标准仍然没有完全定下来（但是 TR1
已经得到支持）。另一个有意思的是在“新的目标平台及特定平台的改进”中的这句：

GCC now supports STMicroelectronics' Loongson 2E/2F processors. The
canonical -march= and -mtune= names for these processors are loongson2e
and loongson2f.

也就是针对龙芯平台的优化参数。因为龙芯隶属 mips 指令体系，所以支持 mips
的 GCC
自然支持龙芯，但是优化参数包括了龙芯，应该是说明对龙芯的支持更进一步。虽然离大众视线还很远，但应该是个好消息吧。

2 OpenGL 公布了 3.0
标准。这已经是很长时间前的事情，不过相应的驱动还都没有跟上，所以只是空中楼阁。最近
nv 的 Windows 的 β 驱动 177.89 加上 nvemulate 可以支持 opengl3。Linux
下则发布了 177.80 版驱动，有消息称这是 17x 版本的最后一次发布，下次将是
18x 版本驱动，18x 版本将加入 opengl3.0 支持。但是坏消息来自于 nv
的说明：需要 8000 系列显卡才行....

3 Linux 2.6.27-git3 中提到，ext4 终于被认可为足够稳定，并将去掉 ext4dev
的 dev 后缀，正式成为 ext4，进入内核。自 2.6.24 开始我就一直用 ext4dev
作为 root 分区，感觉不错。早在一年前的测试中，ext4dev 就已经与 reiser4
不相上下了，加上最近的几个补丁的加入，ext4 完全有实力成为主流。至于
reiser4 吗...在 zen-sources
上是有开发的，我也用过的，虽然没有测试过具体数据，但是 fsck 的时候
ext4dev 对 reiser4 是绝对的胜出的，超快...

4 fedora 10 引入了一个新的图形化启动进程显示器 Plymouth，据在 thinkpad
上的视频看来，启动不但快速，而且从 grub 到 X
启动，只有一次黑屏闪动，其他时刻是全图形显示的，一改往日 Linux
启动时反复闪动，内核信息刷屏的形象。查了些资料，说明如下：过去的 Linux
图形子系统是内核先设置好硬件一次，然后到了 X
启动，又将重置硬件，即使是注销时，X
也将重置硬件，造成闪动不止。而且现在的 X
的显卡驱动都是在自己完成资源管理，造成代码重复。于是一些开发者希望由内核来完成基本的显卡资源管理，这在
Linux 圈中还引发了很大争论。因为有些人认为把图形功能放入内核，就会像
Windows 一样有很多问题。这个我也不大懂，有兴趣的人可以去 kerneltrap
看看这些人的讨论。不论如何，现在的情况是 Intel 提出了一个叫 GEM
的解决方案，这个 GEM 来管理显卡的资源，且很有可能进入 2.6.28内核。X 的
DRI2 也将围绕 GEM API 进行开发。现在内核中已经有了 direct render manager
选项。正是借助 kernel mode-setting + intel 显卡驱动支持，fedora 10 的 X
才能直接重用内核已经设定好的硬件上下文，进行无缝的切换。在 X 的 wiki
中提到，在 SSD 硬盘上，从 grub 启动内核到 X 启动，可以只用 2
秒(2秒!?)。而且 GEM 还能大幅提高 Linux 下的 2D 3D 性能。intel 的测试表明
GEM 模型下，glgear 和 openarena (就是 quake3 的一个 mod 吧) 有 50%-60%
的性能提升。X 加速模式将会有新的"UXA" 。

5 eeepc 启动到 Linux 桌面只用 5s，开发人员称还能更快。开发的预读补丁
sreadahead 已经提交给内核。
