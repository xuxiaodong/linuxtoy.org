Title: Awesome 3.1 RC 1 发布
Date: 2008-11-08 09:20
Author: toy
Category: Apps
Tags: Awesome, WM
Slug: awesome-31-rc-1

即将到来的 Awesome 3.1 的第一个 RC
版在昨天晚上发布了。[Awesome](http://linuxtoy.org/archives/awesome.html)
是一个平铺式的窗口管理器，相比
[3.0](http://linuxtoy.org/archives/awesome-3.html)，新版本的变化还是蛮多的，让我们一起来瞧瞧。

-   窗口能够全屏了
-   原有的状态栏和标题栏已被新的 wibox 所取代
-   wibox 支持浮动，这意味着你现在能利用它写类似 Conky 的系统监视信息
-   窗口栈现在能更好的处理 dock、desktop 等特殊窗口
-   支持 \_NET\_WM\_STRUT\_PARTIAL，可将面板和 dock 自动放入屏幕
-   支持置顶窗口
-   新的全屏布局
-   新的 imagebox widget 可用来使用图像对象
-   新的 invaders
    模块，一个[太空侵略者游戏](http://linuxtoy.org/archives/space-invaders-for-awesome.html)
-   新的 naughty 模块，类似于 GNOME notification-daemon 的通知模块
-   命令选项 --check 可用来检查 Lua 语法

除了上述较为明显的变化，Awesome 在底层代码上也有所改动，比如使用 pango
来渲染文本、增加了一些新的函数等。更为详细的变化，你可以查看 [Awesome
3.1 RC 1](http://awesome.naquadah.org/news/version_3.1-rc1/) 发布公告。

你可以从这里下载 [Awesome 3.1 RC
1](http://awesome.naquadah.org/download/)。
