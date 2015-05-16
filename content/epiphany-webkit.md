Title: Webkit 引擎的 Epiphany 可用于 Ubuntu 7.10 
Date: 2007-11-21 11:14
Author: toy
Category: Apps
Slug: epiphany-webkit

Webkit 是 Apple 基于 khtml 的浏览器引擎，被用在 Safari、gPhone
上。我尝试在 Ubuntu 7.10 编译了 WebkitGtk 的
[Epiphany](http://www.gnome.org/projects/epiphany/) 浏览器，deb
包临时放在 <http://linuxfire.com.cn/~huahua/soft/webkit/>，让大家可以在
Ubuntu “使用” Safari 了。

[![Epiphany-webkit](http://i.linuxtoy.org/i/2007/11/epiphany-thumb.png)](http://i.linuxtoy.org/i/2007/11/epiphany.png)  
*Webkit 引擎的 Epiphany 网络浏览器截图*

Webkit 在 Linux 下也非常快，Epiphany-webkit 看 map.google 和 ditu.google
明显比 Firefox 和 Opera 流畅。只是现在 Epiphany-webkit 和 WebkitGtk
还没整合好，渲染速度很快，但是好些应有的功能用不了，比如无法在网页里打开新窗口，网页里无法用右键菜单，网页里无法激活输入法，感觉上成熟度不如
QtWebkit 的浏览器。不过既然 GNOME 2.22 要默认用
Epiphany-webkit，估计这些很快都会修好的。

**关于 Webkit**

Webkit 被设计成可以用多种 GUI toolkit，包括 aque，Qt，wx 等，往 Gtk
的移植比较起来似乎没有 Qt 那么成熟，下载网页依然用的 libcurl，TW 的
jserv 说虽然现在已经可以多线程下载网页，可是效能上还有好大优化空间。

[撰文/华华]
