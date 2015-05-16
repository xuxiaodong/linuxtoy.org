Title: GNOME 2.21.2 发布
Date: 2007-11-16 09:59
Author: toy
Category: Apps
Slug: gnome-2212-released

GNOME 开发团队在今天发布了 GNOME 2.21.2，即 GNOME 2.22
的第二个开发版。该版本对既有的软件和组件进行了更新，添加了一些新的特性，并修正了许多
bug。这主要包括 Metacity、GDM、GNOME 主题引擎及主题、GNOME
游戏、Totem、Vino 等等。

![GNOME](http://i.linuxtoy.org/i/logo/gnome-apps.png)

-   Metacity：添加了 --sync
    选项，当窗口最大化时将不保存其位置，修正了内存泄漏问题等。
-   GDM：在注销时关闭会话，执行 Xsession，重做 XAuth
    处理，编译时不再需要 x11.pc 等。
-   GNOME 主题引擎及主题：主要改进了 Clearlooks 主题引擎、Gummy
    样式、以及图标主题。
-   GNOME 游戏：其中的 Chess 和 Sudoku 有所改进。
-   Totem：改进了播放列表功能及浏览器插件。
-   Vino：添加了新的 gconf 键及更多的选项。

关于此版本的详细更新情况，你可以查阅其
[NEWS](http://ftp.gnome.org/pub/GNOME/desktop/2.21/2.21.2/NEWS)
文件。根据计划，GNOME 2.22 预定于 2008 年 3 月 12 日发布。

[GNOME 2.21.2
的源代码](http://ftp.gnome.org/pub/GNOME/desktop/2.21/2.21.2/)可到这里下载。若要编译它，你可以使用
[GARNOME](http://www.gnome.org/projects/garnome/)。
