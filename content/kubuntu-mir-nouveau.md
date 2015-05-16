Title: 短消息：Kubuntu Mir 和 Nouveau
Date: 2013-06-29 17:29
Author: liangsuilong
Category: Desktop Environment, Distros
Tags: canonical, Kubuntu, mir, nouveau, Ubuntu, XMir
Slug: kubuntu-mir-nouveau

短消息三则，内容是 Kubuntu、Mir 和 Nouveau。  

**首先是 Kubuntu，Canonical 日前宣布 Ubuntu 13.10 将会默认使用 Mir
服务器**，而 Unity 7 将会运行在 Mir 服务器的 X 兼容层
XMir。如果没有图形驱动支持会后退到 X Server 模式。到了 Ubuntu 14.04
LTS，Mir 会有完整的驱动支持，XMir 继续作为默认的会话模式，但后备的 X
Server 模式将会被移除。Ubuntu 14.10 和以后的版本，Mir
原生模式将成为默认，Unity 8 成为默认的桌面环境，通过 XMir 支持依赖 X
的应用程序。[消息来源自 Ubuntu
官方开发者列表](https://lists.ubuntu.com/archives/ubuntu-devel/2013-June/037401.html)

**不过 Kubuntu 并不会跟随 Canonical 这一条迁移路线图**，Kubuntu
宣布并不打算计划迁移到 Mir 或 XMir，原因是 KDE 上游短期内并不打算支持
Mir。Kubuntu 在 13.10 和 14.04 LTS 继续使用 X
Server，而后续的版本将会寻求办法向 Ubuntu 仓库添加和维护 Wayland，以及把
Kubuntu 向 Wayland 迁移。 [消息来自 KDE
官方博客](http://blogs.kde.org/2013/06/26/kubuntu-wont-be-switching-mir-or-xmir)

**Phoronix 日前完成了 Mir 的性能测试**，测试环境是 Ubuntu 13.10
最新版本以及 Unity 7，GPU 则来自 Intel，采用开源驱动。测试结果对比了 X
Server 原生模式和 XMir 模式下的 3D 和 2D 性能水平。3D
性能方面，除了一小部分测试 XMir 能够和 X Server
原生模式持平以外，大部分测试 XMir 都明显落后于 X Server 原生模式。而在
2D 性能测试和 3D 性能测试相若，XMir 大部分测试落后于 X  Server
原生模式。消息来源自 Phoronix [3D
测试](http://www.phoronix.com/scan.php?page=article&item=ubuntu_xmir_benchmark)
[2D
测试](http://www.phoronix.com/scan.php?page=article&item=ubuntu_xmir_2d)

**最后一则消息来自 Nouveau**，前几天 Radeon 开源驱动进度喜人，Nouveau
显然不会让 Radeon 独舞。近日 Nouveau 开发者提交了新补丁，令 Nouveau
可以调用 GPU 的 PureVideo HD 硬件解码单元进行 H.264 和 MPEG-2，与类似
AMD 调用 UVD 硬解一样。目前这个补丁仅能用于 PureVideo HD VP2
解码单元中，使用 VP2 解码单元的大多是 GeForce 8000/9000
系列的中低端显卡以及 GeForce GT200
系列的高端旗舰显卡，[具体支持型号可参考维基百科](http://en.wikipedia.org/wiki/Nvidia_PureVideo)。硬解接口依然是基于
VDPAU，此外目前实现的代码扔在初期阶段，需要从 NVIDIA 闭源驱动中抽取
Firmware，以后开发者会重新编写开源 Firmware 替代闭源
Firmware。另有开发者计划打算基于这个补丁实现 Nouveau 的 VP4
硬件解码功能。开发者打算把 Nouveau 硬解补丁合并到 3.11
内核。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTM5ODE)
