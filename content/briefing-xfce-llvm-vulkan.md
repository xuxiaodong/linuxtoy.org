Title: 短消息：Xfce LLVM Vulkan
Date: 2015-03-03 13:38
Author: lovenemesis
Category: Desktop Environment
Slug: briefing-xfce-llvm-vulkan

短消息三则，发生在刚刚过去的那个周末。

**轻量级桌面环境 Xfce 终于发布 4.12
版本**，此时距离上个版本发布已经过去了将近三年时间。新发布尽管并未完成向
GTK3+ 的迁移，不过依然带来了包括客户端渲染、HiRes
屏幕支持、多屏幕支持等更新；此外大量组件也得到了重写，增添了不少功能：

* Thunar 文件管理器现在支持标签页  
* Xfburn 增加蓝光碟写入  
* 类似 GNOME Shell 风格的 xfdashboard  
* 剪贴板管理器增加 QR 码生成

更多详情请参考[官方发布公告](http://www.xfce.org/about/news/?post=1425081600)。[消息来源](http://www.phoronix.com/scan.php?page=news\_item&px=Xfce-4.12-Released)

**编译器集合 LLVM 发布 3.6
正式版本**，根据[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=LLVM-Clang-3.6-Features)的报道，此次发布的改善有：

* 大幅度改善对于 MIPS 的支持  
* 更多用于 AMD GPU 的优化  
* 进一步向着编译 Linux 内核努力，现在仅需一小部分补丁即可  
* 增加 Go 语言绑定  
* Clang 3.6 改善在 Win 平台上的支持  
* 默认 C 语言支持版本升级到 C11，完整的 C++14 支持，同时带来 C++17
初步支持

[官方发布公告](http://lists.cs.uiuc.edu/pipermail/llvm-announce/2015-February/000057.html)

**备受瞩目的下一代 OpenGL 标准（或其继任者）名字是 Vulkan**，Khronos
打算将其打造为横跨多个平台（从桌面到手机到嵌入式设备）的高性能图形/计算
API。作为一个新的靠近底层的 API，其定位和 OpenGL
不相同，后者仍将继续存在。更多的信息将在明天举行的 GDC 2015
公布。[消息来源](http://www.phoronix.com/scan.php?page=news\_item&px=Khronos-Vulkan-Graphics-API)
