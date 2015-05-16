Title: FreeBSD 10.0 正式发布
Date: 2014-01-21 09:28
Author: toy
Category: Distros
Slug: freebsd-10

知名 BSD 发行版 FreeBSD 于近日发布了 10.0 的正式版本。FreeBSD 10.0  
主要包含如下变化：

* clang 代替 GCC 成为默认编译器  
* Unbound 已被导入到 base 系统作为本机缓存 DNS 解析器  
* BIND 已从 base 系统移除  
* 使用来自 NetBSD 项目的 bmake 替换了 make  
* pkg 现在是默认的包管理工具  
* pkg\_add、pkg\_delete 及其相关工具已被移除  
* 对虚拟化进行了主要增强  
* 针对 SSD 的 TRIM 支持已被添加到 ZFS  
* 高性能 LZ4 压缩算法已被添加到 ZFS

对于 FreeBSD 10.0 的更多更改细节，可参阅其[发行注记][n]。FreeBSD 10.0
提供  
包括 amd64、i386、ia64、powerpc(64)、sparc64
等多种架构版本，可从其官方网站  
的[下载页面][d]获取。

[a]:
http://lists.freebsd.org/pipermail/freebsd-announce/2014-January/001532.html  
[n]: http://www.freebsd.org/releases/10.0R/relnotes.html  
[d]: http://www.freebsd.org/where.html  
[l]: http://lwn.net/Articles/581314/

{ via [LWN][l] }
