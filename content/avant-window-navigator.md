Title: Avant Window Navigator：Dock 类的窗口导航方式
Date: 2007-01-30 17:53
Author: toy
Category: Apps
Slug: avant-window-navigator

目前，我们在 GNOME 桌面环境中导航窗口主要是通过窗口列表的形式来进行。而
[Avant Window
Navigator](http://code.google.com/p/avant-window-navigator/)
则采用一种新的方式来导航窗口，使用者可以从 Dock
栏中已被跟踪的打开窗口来进行切换。说到这里，你可能已经想到了，在 Mac OS
X 系统中不正是这样吗？没错，我猜想作者的创意也正源于此。

[![Avant](http://i.linuxtoy.org/i/2007/01/avant_s.png)](http://i.linuxtoy.org/i/2007/01/avant.png)

Avant Window Navigator 使用 libwnck
来保留已跟踪的打开窗口，并使其行为就像窗口列表一样。比如，点击 Dock
栏中的图标就可以切换窗口，再次点击则会最小化该窗口；右击图标会显示一个菜单，其中包括最大化、最小化、关闭窗口等项目；另外还可以将一些东西拖曳到图标上，那样的话就会自动激活窗口。

除此之外，你也可以定制该 Dock
栏的外观，如选择不同的引擎、更改边框的颜色、以及活动窗口图标的背景等等。

Avant Window Navigator 仍旧在开发当中，不过作者已经发布了 0.1.1
版的源代码，供有兴趣的朋友尝试。

Download [Avant Window Navigator
0.1.1](http://code.google.com/p/avant-window-navigator/downloads/list)
