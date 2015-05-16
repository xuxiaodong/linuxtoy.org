Title: GNOME 3.2 Web Apps
Date: 2011-09-01 09:28
Author: lovenemesis
Category: Desktop Stuff
Tags: Epiphany, GNOME, web
Slug: gnome-32-web-apps

在即将到来的 GNOME 3.2 中增加了创建 Web Apps 的支持。

该功能通过 [Epiphany
浏览器](http://projects.gnome.org/epiphany/)中的一个新菜单项实现（快捷键
Ctrl-Shift-A）：

[![](http://linuxtoy.org/img/2011/09/gnomewebapp-saveas.png "gnomewebapp-saveas")](http://linuxtoy.org/img/2011/09/gnomewebapp-saveas.png)

之后会被提示输入名称和图标：

[![](http://linuxtoy.org/img/2011/09/gnomewebapp-create.png "gnomewebapp-create")](http://linuxtoy.org/img/2011/09/gnomewebapp-create.png)

然后会有提示告诉你程序创建完成：

[![](http://linuxtoy.org/img/2011/09/gnomewebapp-notify.png "gnomewebapp-notify")](http://linuxtoy.org/img/2011/09/gnomewebapp-notify.png)

之后你就可以看到这个 Epiphany Web App 模式了：

[![](http://linuxtoy.org/img/2011/09/gnomewebapp-app.png "gnomewebapp-app")](http://linuxtoy.org/img/2011/09/gnomewebapp-app.png)

**Web App 模式的特点**为：

-   仅仅保留标题栏这一个 UI 元素。
-   在该模式下不可访问其他域名，如果试图通过点击超链接的方式打开其他站点，其请求将在正常浏览器进程中打开。
-   该域名下的 cookies
    将从浏览器配置文件中继承（这样就无需重复输入密码），但其他域名的将是独立的。
-   在独立的进程运行，所以若是正常浏览器进程崩溃了，将不会影响这个 Web
    App 。

Web App 和其他本地应用程序一样，可以在 Alt+Tab
的**应用程序切换器中出现**：

[![](http://linuxtoy.org/img/2011/09/gnomewebapp-switch.png "gnomewebapp-switch")](http://linuxtoy.org/img/2011/09/gnomewebapp-switch.png)

当然也会在应用程序列表中出现了，所以也可以**添加到收藏**：

[![](http://linuxtoy.org/img/2011/09/gnomewebapp-dash.png "gnomewebapp-dash")](http://linuxtoy.org/img/2011/09/gnomewebapp-dash.png)

[消息来源](https://twitter.com/#!/gnome/status/109000352463986688)：
[Iocane Powder
及图片版权所有](http://blogs.gnome.org/xan/2011/08/31/web-application-mode-in-gnome-3-2/)
