Title: Gtk+ 3.2 HTML5 后端
Date: 2011-03-18 10:39
Author: lovenemesis
Category: News
Tags: Firefox, GTK
Slug: gtk-32-html5-backend

GTK+ 3.X 的渲染后端支持达到一个全新的境界，增加 HTML5 渲染后端支持。

实现在浏览器中渲染 GTK+ 3.X 程序，只需要满足以下条件：

-   使用 Mozilla Firefox 4 浏览器（未来会有更多浏览器的支持）。
-   打开默认禁用的 WebSocket 支持。
-   编译 **GTK+ 3.2** 时打开 HTML5
    后端支持：`–enable-x11-backend –enable-broadway-backend`。
-   使用`GDK_BACKEND=broadway your-application` 启动你的 GTK+ 程序。
-   在 Firefox 中指向测试机的 8080 端口 IP 地址，比如
    `http://127.0.0.1:8080/`

赶紧前往作者博客观看[视频演示](http://blogs.gnome.org/alexl/2011/03/15/gtk-html-backend-update/)吧！

[**朝内版本**](http://v.youku.com/v_show/id_XMjUxNjM5MjA4.html)

**FAQ：**  
Q：这有什么用途？  
A：意味这只需要使用浏览器，就可以远程运行另外一台机器上的 GTK+
程序，不再需要 VNC 客户端和 ssh X 转发了。

Q：似乎它缺少一个窗口管理器。  
A：的确，准备用 JavaScript 实现一个。

Q：哇！那么可以在 Firefox 里再运行一个 Firefox 么？  
A：不可以，Firefox 里包含相对多的本地 X 调用，不是单纯的 GTK+ 运用。

Q：可不可以实现远程程序和本地程序之间的复制粘帖、或者拖拽？  

A：目前不可以，现在甚至连键盘输入都还存在一些问题，不过相信以后会实现这些功能的。
