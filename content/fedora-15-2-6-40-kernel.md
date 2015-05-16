Title: Fedora 15 专用的 2.6.40 内核
Date: 2011-07-30 11:33
Author: liangsuilong
Category: Distros, Funny
Tags: Fedora, Kernel, Linux
Slug: fedora-15-2-6-40-kernel

Linus 大神早前已经说了 Linux 内核的版本号太长了，在 2.6.39
内核后直接跳上了 3.0 内核，并且已经发布了新的版本。但是 Fedora
某部分维护者似乎有所不甘。

不甘的原因是他们不想 Fedora 15 整个生命周期都只能使用 2.6.38
内核，而无法享受 3.0 内核带来的新特性。但是如果直接使用 3.0
内核，因为版本号的问题可能会出现兼容性问题，而且工程量大。于是维护者们就把
3.0 内核的版本号更改为 2.6.40 内核。本质上 2.6.40 内核和 3.0
内核没有任何区别。

[![](http://linuxtoy.org/img/2011/07/linux-2640.png)](http://linuxtoy.org/img/2011/07/linux-2640.png)

2.6.40 内核暂时还有一小部分兼容性的
Bug，稍后会逐一解决。短期内将会推送到 updates-testing
以供测试。此内核只会特供 Fedora 15 使用。Fedora 16 和已经指向至 Fedora
17 的 Rawhide 将会使用 3.x 内核。
