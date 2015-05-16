Title: Ubuntu 9.04 获得更快的系统启动速度
Date: 2009-01-14 11:07
Author: toy
Category: Distros
Tags: Jaunty Jackalope, Ubuntu 9.04
Slug: ubuntu-904-boot

Ubuntu 项目团队在制订 [Ubuntu 9.04（Jaunty
Jackalope）开发计划](http://linuxtoy.org/archives/ubuntu-904-release-schedule.html)时就表示过要改善系统的启动时间。现在看来，得益于
EXT 4 文件系统的引入，Ubuntu 9.04 的系统启动时间已经明显减少。据
Softpedia 测试，Ubuntu 9.04 完成系统启动过程仅花了 21.4 秒。

Softpedia 使用 Ubuntu 8.10 和 9.04 的 daily
build（20090112.1）进行对比测试，测试的硬件平台包括 AMD Sempron 1.8
Ghz、80 GB IDE 硬盘、512 MB DDR 内存及 Intel Core 2 Duo E4300 2.2
Ghz、250 GB SATA 硬盘、4 GB DDR2 内存两组。系统启动时间的计算则以从 GRUB
出现在屏幕上到显示登录管理器（login manager）时为准。最终测试结果如下：

-   Ubuntu 8.10，使用 EXT 3 文件系统：31.8 秒。（AMD Sempron 平台）
-   Ubuntu 9.04，使用 EXT 3 文件系统：28.3 秒。（AMD Sempron 平台）
-   Ubuntu 9.04，使用 EXT 4 文件系统：23.1 秒。（AMD Sempron 平台）
-   Ubuntu 9.04，使用 EXT 4 文件系统：21.4 秒。（Intel Core 2 Duo 平台）

更多信息，可阅读 Softpedia 的原文 *[Ubuntu 9.04 Boots in 21.4
Seconds](http://news.softpedia.com/news/Ubuntu-9-04-Boots-in-21-4-Seconds-101885.shtml)*。

想知道自己的系统启动到底有多快？你可以使用
[Bootchart](http://linuxtoy.org/archives/bootchart.html)
这个小工具来跟踪。
