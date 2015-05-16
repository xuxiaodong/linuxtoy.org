Title: 10/GUI
Date: 2010-08-14 01:53
Author: lovenemesis
Category: Featured
Tags: 10gui
Slug: 10gui

现在口袋里的手机 GUI
全面步入多点触控时代了，可是桌面上放的和公文包里的电脑未来的 GUI
发展方向在哪里？ 某水果公司认为也是 Multi-Touch ！于是扔出施加了 i
魔法的某板子，虽说褒贬参半，倒也从信徒和送礼者手中赚得大把钞票。喧闹之余，不妨看看
[R. Clayton Miller](http://twitter.com/claymill) 是怎么想的。

**以下概念、截图取自 [10/GUI](http://10gui.com/) 。**

如果如同某水果公司那样，照搬手机上的多点触控，会有什么样的问题呢？

如果是显示屏依然像平时一样放置，那么长时间使用胳膊会感到不适。

[![](http://linuxtoy.org/img/2010/08/shot0001.png)](http://linuxtoy.org/img/2010/08/shot0001.png)

如果水平放置，不出多久脖子就会感到不适。

[![](http://linuxtoy.org/img/2010/08/shot0002.png)](http://linuxtoy.org/img/2010/08/shot0002.png)

并且在操作的时候手指尺寸会对屏幕上的信息阅读造成阻碍。

[![](http://linuxtoy.org/img/2010/08/shot0003.png)](http://linuxtoy.org/img/2010/08/shot0003.png)

相比之下，由于平放，传统的鼠标对胳膊和手腕的压力会小很多。

[![](http://linuxtoy.org/img/2010/08/shot0004.png)](http://linuxtoy.org/img/2010/08/shot0004.png)

眼睛可以直视屏幕，于是脖子也不那么容易酸痛。

[![](http://linuxtoy.org/img/2010/08/shot0005.png)](http://linuxtoy.org/img/2010/08/shot0005.png)

人的手被屏幕上小小的鼠标指针代替，不会阻碍信息阅读。

[![](http://linuxtoy.org/img/2010/08/shot0006.png)](http://linuxtoy.org/img/2010/08/shot0006.png)

那么有没有两全其美的方法？R. Clayton Miller 认为可以这样解决：

[![](http://linuxtoy.org/img/2010/08/shot0007.png)](http://linuxtoy.org/img/2010/08/shot0007.png)

如图所示，将交互的多点触摸从显示屏剥离并且平放，然后在屏幕上显示十个指头对应的指针。

下方的触摸屏通过多层感应的方式，可以做到感受到用户当前使用的那个手指。

[![](http://linuxtoy.org/img/2010/08/shot0008.png)](http://linuxtoy.org/img/2010/08/shot0008.png)

但是传统的层叠窗口管理依然是针对单点操作设计的：

[![](http://linuxtoy.org/img/2010/08/shot0009.png)](http://linuxtoy.org/img/2010/08/shot0009.png)

尽管有 Preview 和 Expose 等特效尝试改善，多窗口管理依然是个头疼的问题：

[![](http://linuxtoy.org/img/2010/08/shot0010.png)](http://linuxtoy.org/img/2010/08/shot0010.png)

[![](http://linuxtoy.org/img/2010/08/shot0011.png)](http://linuxtoy.org/img/2010/08/shot0011.png)

于是就有了名为 CON10UUM 的**连续式窗口管理**。

[![](http://linuxtoy.org/img/2010/08/shot0012.png)](http://linuxtoy.org/img/2010/08/shot0012.png)

[![](http://linuxtoy.org/img/2010/08/shot0013.png)](http://linuxtoy.org/img/2010/08/shot0013.png)

每个窗口都有可以左手激活的窗口管理菜单和用右手激活的全局管理。

[![](http://linuxtoy.org/img/2010/08/shot0015.png)](http://linuxtoy.org/img/2010/08/shot0015.png)

这个是连续式窗口管理的桌面，上面的 Widget 不是重点

[![](http://linuxtoy.org/img/2010/08/shot0016.png)](http://linuxtoy.org/img/2010/08/shot0016.png)

用右手从右侧拖出全局管理，可以从中启动各种应用程序。

[![](http://linuxtoy.org/img/2010/08/shot0017.png)](http://linuxtoy.org/img/2010/08/shot0017.png)

用左手从左侧拖出应用程序菜单，访问当前应用程序内的功能。

[![](http://linuxtoy.org/img/2010/08/shot0023.png)](http://linuxtoy.org/img/2010/08/shot0023.png)

在应用程序中，不同数目的手指操作被赋予了各自的功能，比如单手指是选择：

[![](http://linuxtoy.org/img/2010/08/shot0018.png)](http://linuxtoy.org/img/2010/08/shot0018.png)

如你所想，两个手指是缩放

[![](http://linuxtoy.org/img/2010/08/shot0019.png)](http://linuxtoy.org/img/2010/08/shot0019.png)

变化来了！通过三个手指的拖拽改变应用程序在连续式窗口中的位置。

[![](http://linuxtoy.org/img/2010/08/shot0020.png)](http://linuxtoy.org/img/2010/08/shot0020.png)

四个手指用来连续式窗口序列中滚动

[![](http://linuxtoy.org/img/2010/08/shot0022.png)](http://linuxtoy.org/img/2010/08/shot0022.png)

四个手指同时做抓取的动作可以将连续式窗口放大缩小，最终可以变为类似
Expose 的列表模式

[![](http://linuxtoy.org/img/2010/08/shot0024.png)](http://linuxtoy.org/img/2010/08/shot0024.png)

**10/GUI**
就是这样，由**手指敏感的多点触控板**、**连续式窗口管理器**和**层级式触摸事件捕捉**组成。  
它可以和现有的设备无缝的组合起来：

[![](http://linuxtoy.org/img/2010/08/shot0025.png)](http://linuxtoy.org/img/2010/08/shot0025.png)

就是这些了，具体内容可以查看[视频](http://10gui.com/video/)。它会是下一个
25 年人机交互的雏形么？
