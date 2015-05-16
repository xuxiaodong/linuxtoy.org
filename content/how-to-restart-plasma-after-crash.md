Title: KDE4 plasma 崩溃了怎么办？如何正确地重启 plasma
Date: 2009-09-01 11:59
Author: gmsh
Category: Apps
Tags: KDE, Plasma
Slug: how-to-restart-plasma-after-crash

KDE4 plasma 崩溃了怎么办？如何正确地重启 plasma 才稳定?

尽管现在 KDE4 华丽且易用，但是 KDE4 并不是那么稳定，尤其是 plasma。  
如果在一次 plasma 崩溃之后，你有幸保留了一个 Shell 或者能调出 Krunner
的话，有一定的几率可以通过以下脚本重启 plasma：

  

*原载：<http://blog.gmsh.pp.ru/2009/08/how-restart-plasma-after-crash/>*

`kbuildsycoca4`

`kquitapp plasma-desktop`

`kstart plasma-desktop`

这样启动 plasma 要比 `killall plasma-desktop && plasma-desktop`
要更合乎规范。因为系统配置缓存需要重建，而且把 plasma 的关闭和重启交由
KDE 处理更加稳定。

注：以上是 KDE 4.3 的脚本，KDE 4.3 之前的脚本需要把所有的
`plasma-desktop` 换成 `plasma` 。

*[图]并不怎么稳定的 plasma*

[![并不怎么稳定的Plasma](http://i.linuxtoy.org/images/2009/09/plasmacrash-400x198.jpg)](http://i.linuxtoy.org/images/2009/09/plasmacrash.jpeg)

*希望对您有用。by [John Smith](http://blog.gmsh.pp.ru/about/)*
