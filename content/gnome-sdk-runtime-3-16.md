Title: GNOME SDK Runtime 3.16
Date: 2015-04-01 12:38
Author: lovenemesis
Category: Desktop Stuff
Tags: GNOME
Slug: gnome-sdk-runtime-3-16

[GNOME 3.16](https://linuxtoy.org/archives/gnome-3-16.html)
带来了初步沙箱应用支持，其中的运行时环境在今天(美国时间3月31日，非愚人节)发布首个正式预览版了。

GNOME 沙箱化应用涉及多个方面，简单来说，应用程序在针对某个 GNOME SDK
版本开发后，既可以实现无关发行版的沙箱化运行，其中：

* GNOME SDK
定义了以沙箱化运行应用程序所需的最小环境以及与沙箱外系统其他部分沟通的
API  
* 最终形态的沙箱化应用将依赖诸如 KDBUS、cgroups、SELinux、Wayland
等组件  
* GNOME SDK
以完整版及运行时环境两种方式分发，后者仅包含运行程序所必需的 GNOME
库，而前者包含开发工具  
*
无论完整版还是运行时环境，都可以以用户态或者系统全局态安装，且支持多版本共存  
* 沙箱化程序的管理通过基于 [OSTree
技术](https://wiki.gnome.org/Projects/OSTree)的[xdg-app](https://github.com/alexlarsson/xdg-app)实现  
* 沙箱化程序在安装时根据元文件识别所需的 GNOME SDK
版本并将其拷贝到指定位置从而可以被系统识别  
* 沙箱化程序在分发时无需捆绑 SDK，不过可以在安装时请求安装缺失的 SDK。

如果感兴趣的话，不妨根据[详细步骤说明](https://blogs.gnome.org/alexl/2015/03/31/official-gnome-sdk-runtime-builds-are-out/)体验下吧！

[GNOME
沙箱化应用程序主页](https://wiki.gnome.org/Projects/SandboxedApps)
