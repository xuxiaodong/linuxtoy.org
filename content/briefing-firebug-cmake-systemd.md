Title: 短消息：Firebug CMake Systemd
Date: 2014-06-12 11:35
Author: lovenemesis
Category: News
Tags: cmake, firebug, systemd
Slug: briefing-firebug-cmake-systemd

短消息三则，分别关于 Web, 构建系统和 init。

**兼容最新 Firefox 30 的 Firebug 发布 2.0 版本**，新版本完全迁移到了
Firefox JSD2
调试引擎，实现了语法高亮、代码阅读模式、自动补全等大量新功能，同时亦完成了本地化和扩展的更新。[官方详细功能说明](http://blog.getfirebug.com/2014/06/10/firebug-2-0/)

**跨平台构建工具 CMake 3.0 发布，**移除了对 2.4.X 之前版本的兼容，新增了
CodeLite 和 Kate
生成器并优化了编译器支持。[邮件列表详细说明](http://www.cmake.org/pipermail/cmake/2014-June/057793.html)
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTcxNjk)

**引导系统 Systemd 发布
214**，带来文件系统级别的沙箱支持，且支持从零重建 /var
分区方便整体迁移，网络组件 networkd 及 resolved 也将以独立用户运行无需
root
权限。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTcxNzc)
