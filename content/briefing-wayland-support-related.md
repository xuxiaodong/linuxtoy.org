Title: 短消息：Wayland 支持相关
Date: 2013-03-19 20:41
Author: lovenemesis
Category: Desktop Stuff
Tags: enlightenment, wayland, weston
Slug: briefing-wayland-support-related

短消息三则，关于 Wayland 支持方面的进展。

**GTK+ 已将对于 Wayland 客户端装饰支持合并入主线**，将在今年 9 月份随着
GTK+ 3.10 发布。和 X11 不同，在 Wayland 环境下的混成管理器 Weston
允许由客户端完成窗口装饰工作，GTK+ 对于该功能的支持已经由来自 Intel 的
Kristian Høgsberg 和 Rob Bradford
实现并合并入主线。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTMyOTk)

**Enlightenment 发布了自身用于 Wayland 协议条件下的混成管理器**
，目前该管理器尚处于原型阶段，不过依然可以传达出一个信息：Enlightenment
项目不打算 Weston 混成管理器。[演示视频](http://youtu.be/dfnvYAKKPZI)
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTMzMDI)

**Arch Linux 宣布开启 GTK3 的 Wayland 后端支持**，由于 GTK3
具备运行时动态后端切换的功能，这代表着未来 Arch 下所有使用 GTK3
的软件无需重新编译均可在 X11 和 Wayland
两种环境下使用。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTMzMTA)
