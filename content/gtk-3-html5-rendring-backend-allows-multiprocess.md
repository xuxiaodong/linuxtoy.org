Title: GTK+ 3 HTML5 渲染后端实现多进程支持
Date: 2012-12-28 12:08
Author: lovenemesis
Category: Desktop Stuff
Tags: GTK+, html5
Slug: gtk-3-html5-rendring-backend-allows-multiprocess

在 [GTK+ 3.2 引入的 HTML5 渲染后端
Broadway](http://linuxtoy.org/archives/gtk-32-html5-backend.html)
再度进化，现在允许多进程支持，颇有远程 X 会话的风范了。

[视频演示](http://www.youtube.com/watch?v=hhMFD3ZCrIc&feature=player_embedded)（[朝内镜像](http://v.youku.com/v_show/id_XNDk0MTgxMDA0.html)）

相比 GTK+ 3.2 时，现在的 Broadway 后端有了多项改善：

1.  支持键盘和鼠标事件。
2.  **在一个网页中打开多个 GTK3+ 程序**
3.  **支持嵌套性打开**，比如在通过网页打开的 GNOME Web
    浏览器中再次渲染一个 GTK+ 3 程序。
4.  支持复杂的 GTK+ 3 程序，比如针对 GTK+ 3 编译的 GIMP 2.99 开发版本。

本项支持将合并入明年初发布的 GTK+ 3.8 中，现有 GTK+ 3
程序无需更改即可使用 Broadway 渲染引擎在支持 HTML5
的本地或者远程浏览器中使用，本次的多进程支持将这一技术的实用性大大增强。

*消息来源：*[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=MTI2Mjg)
