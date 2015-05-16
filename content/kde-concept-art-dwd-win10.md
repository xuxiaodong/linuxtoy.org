Title: KDE 设计概念图：DWD 及 Win10
Date: 2014-10-27 13:42
Author: lovenemesis
Category: Desktop Environment
Tags: dwd, KDE
Slug: kde-concept-art-dwd-win10

KDE 团队设计师 Ken Vermette 近日释出两篇博客，附带多个概念设计图，阐述了
Dynamic Window Decoration （动态窗口装饰）构思及 Win10
设计思路。这两篇关于设计的文章新意十足，值得一看。

### [Presenting DWD, a Candidate for KDE Window
Decorations](http://kver.wordpress.com/2014/10/25/presenting-dwd-a-candidate-for-kde-window-decorations/)

前段时间 KDE 社区在经过严肃的讨论后决定继续在 KDE5 中使用
SSD（服务器端装饰）的方式且达成共识。这些讨论同时激发了 Ken
的新思路，称为动态窗口渲染。简单来说，这个新的渲染方式的分为两部分：

1.
一个核心协议，应用程序可以以广播方式告知自己所需要的控件风格、需求及组织方式；

2. 多个 DWD 终端，负责响应广播中的请求，在指定的位置按照需求绘制控件。

Ken 希望通过这种方式弥补 CSD (客户端装饰)及 SSD
两种方式的不足，实现应用程序和窗口管理器之间的良好分工。既允许应用程序指定在窗口边框的内容，又使得窗口管理器保留诸如处理僵死程序的权利。

[![multiformfactor-01](http://lt-file.b0.upaiyun.com/files/2014/10/multiformfactor-012-300x200.png)](http://lt-file.b0.upaiyun.com/files/2014/10/multiformfactor-012.png)

此外，这种处理方式也给 Plasma 小程序及 KDE Connect 等应用更大的灵活度。

**注意**：当前 DWD 尚处于构思阶段，无任何实现计划。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTgyMjk)

### [What if… KDE Used Windows 10 Design
Components?](http://kver.wordpress.com/2014/10/25/what-if-kde-used-windows-10-design-components/)

Ken 在这篇文章中分析了 Win8+ 开始的设计思路，并以 KDE5
为模板尝试了下仿效 Win10 的 Consumption 设计思路。

[![win10-dictionary](http://lt-file.b0.upaiyun.com/files/2014/10/win10-dictionary-300x158.png)](http://lt-file.b0.upaiyun.com/files/2014/10/win10-dictionary.png)

包括将 Plasma 小程序独立启动，小程序嵌入 K 菜单等概念图。

**注意**：仅是概念构想试验，不代表未来 KDE 的发展方向。

消息来源：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTgyMjU)
