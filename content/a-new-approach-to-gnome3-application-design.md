Title: GNOME 3 应用程序设计新趋势
Date: 2012-02-14 15:46
Author: lovenemesis
Category: Reviews
Tags: design, GNOME
Slug: a-new-approach-to-gnome3-application-design

参与 [GNOME 设计的 Allan Day](http://afaikblog.wordpress.com/about/)
近期在博客上分享一些 GNOME 3 应用程序设计的新趋势。

首先 Allan 表示随 GNOME 3.2 发布的“Documents 文档”和“Contacts
联系人”将会迎来新成员
[Boxes(虚拟化和远程桌面工具)](https://live.gnome.org/Design/Apps/Boxes)、[Web(网页浏览器)](https://live.gnome.org/Design/Apps/Web)
和
[Clocks(世界时钟)](https://live.gnome.org/Design/Apps/Clock)。目前**设计小组正在撰写用户界面设计指南
HIG，本文仅是一些前瞻性的内容**。

[更多 GNOME 应用程序设计](https://live.gnome.org/Design/Apps/)

**最大化窗口**

[![](http://linuxtoy.org/img/2012/02/maximised-windows.png "maximised-windows")](http://linuxtoy.org/img/2012/02/maximised-windows.png)

如上图所示的 Web
程序，在多数情况下窗口将最大化显示，并且将隐去标题栏，这样可以尽可能的有效利用屏幕空间显示内容。其中：

-   并不是所有程序都会最大化显示，诸如计算器之类的小应用程序，并不会最大化显示。
-   尽管会默认最大化显示，程序依然可以取消该状态，执行窗口平铺等操作。
-   对于在超大屏幕上显示的时候，会有另外的策略处理以便更佳合理的利用空间。

**视图元素**

[![](http://linuxtoy.org/img/2012/02/views.png "views")](http://linuxtoy.org/img/2012/02/views.png)

如上图的 Music 程序所示，GNOME 3
程序的一个窗口中将包含多个视图这一界面元素，每个视图将只显示和当前所从事活动相关的内容。意味着用户将可以更加关注当前的活动，而不被界面上无关的其他元素困扰。

**主工具栏**

[![](http://linuxtoy.org/img/2012/02/primary-toolbars.png "primary-toolbars")](http://linuxtoy.org/img/2012/02/primary-toolbars.png)

如上图的 Clocks 程序所示，GNOME 3
的主工具栏风格将变得简洁，内容上也是强调在不同程序间的共通性，同时支持各种对齐点，美观的精确调整更容易。

此外 GNOME 3
的主工具栏还将取代窗口标题栏承担导航的功能，成为用户界面的顶层元素，提供关键性的交互功能。

**选择和上下文操作**

[![](http://linuxtoy.org/img/2012/02/selections-and-contextual-actions.png "selections-and-contextual-actions")](http://linuxtoy.org/img/2012/02/selections-and-contextual-actions.png)

GNOME 3
将引入触屏友好的文件选择和上下文操作菜单，通过进入特殊的上下文视图来实现操作。这种方法一方面避免了传统使用
Shift 的辅助键操作的不变，同时也方便布局仅限上下文菜单的内容。

可以通过设计者创建的[交互站点](http://jimmac.fedorapeople.org/gnome3/boxes/overlay-toolbar2/)来体会新的上下文操作方式。

**搜索**

[![](http://linuxtoy.org/img/2012/02/search.png "search")](http://linuxtoy.org/img/2012/02/search.png)

便于搜索是 GNOME 3
应用程序中的核心理念之一，只要光标不是位于文本输入框或者文档中，那么只要用键盘开始输入，便会立即启动搜索。

同时搜索框也可以通过在列表或网格向下滑动的方式呈现出来，这样可以减少空间浪费。同时，应用程序作者也可以针对自身程序内容的特点，添加一些过滤器到搜索中，通过搜索框下拉菜单访问。

以上介绍的 GNOME 3
应用程序设计的新趋势眼下正在不断的打磨和修订之中，欢迎各方面的意见和建议，最终将成型
GNOME 3 应用程序用户交互指南。

[英文原文](http://afaikblog.wordpress.com/2012/02/10/a-new-approach-to-gnome-application-design/)
