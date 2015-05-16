Title: Arch Linux 2012.07.15 放出
Date: 2012-07-22 19:53
Author: toy
Category: Distros
Slug: arch-linux-2012-07-15

Arch Linux 开发团队已发布 2012.07.15 版本。其 ISO 映像现在可从 Arch
Linux  
官方网站的[下载页面][d]获取。

下面是 Arch Linux 2012.07.15 的更改情况：

* 因为 AIF（Arch Installation
Framework）缺少维护和贡献，已被去掉；同时，  
代之以一些简单的[安装脚本][i]替换  
* 安装映像是签名的，可通过 `pacman-key -v .sig`  
验证；不过不用担心签名的问题，这在安装系统上是开箱即用的  
* 仅提供单一 ISO，支持 i686 及 x86\_64 架构  
* 可通过 PXE 引导  
* 包含 Kernel 3.4.4

进一步的信息，可查看 Arch Linux [官方新闻][n]。

[d]: https://www.archlinux.org/download/  
[i]: https://wiki.archlinux.org/index.php/Arch\_Install\_Scripts  
[n]: http://www.archlinux.org/news/install-media-20120715-released/
