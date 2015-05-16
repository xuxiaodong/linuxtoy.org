Title: Xfce 稳定版更新：4.4.3
Date: 2008-10-29 08:56
Author: toy
Category: Apps
Tags: DE, Xfce
Slug: xfce-443

在开发 4.6 新版本的同时，Xfce
项目开发小组也没忘给目前的稳定分支更多关爱。近日，针对 4.4.x
稳定分支系列，Xfce 项目组发布了维护版本 4.4.3。Xfce 4.4.3
仅仅对窗口管理器 xfwm4、桌面管理器 xfdesktop、面板组件 xfce4-panel
中的缺陷进行了修正，并没有添加其他新特性。此外，这个版本也更新了一些翻译。

**Xfce 4.4.3 changelog**

> Panel (xfce4-panel):
>
> * Quite a bit code changed in the dnd code. Mostly to fix a segfault
> in FreeBSD-amd64, but more problems were discovered and a lot of code
> was simplified.  
>  * Don't respond the uri drags, we don't use it and it only causes
> problems like hiding the panel when a file was dragged over the panel
> (Bug #3815).  
>  * Fix crash with xrandr 1.2 (Bug #3620)
>
> Desktop Manager (xfdesktop):
>
> * Make menu panel plugin honor CustomizeDesktopMenu kiosk setting
> (Bug #1026).  
>  * Fix incorrect initial desktop font size when setting custom font
> size if a custom font was never set before (Bug #3957).
>
> Window Manager (xfwm4):
>
> * Fix automaximize on move  
>  * Remove trailing \\0 in UTF-8 strings, that causes libwnck to
> rightfully complain that NET\_WM\_NAME contains invalid UTF-8  
>  * Exit on SelectionClear event so that xfwm4 exits even with WM who
> do not send a ClientMessage event such as Openbox (Bug #2374)  
>  * Backport overlay and compositor support from trunk (Bug #3849)  
>  * Filter out grab/ungrab events so we don't end up redrawing the
> frame twice  
>  * Set monitor when positionning menu (Bug #4162)  
>  * Reduce flickering during resize (Bug #4283)  
>  * Fix NET\_WM\_STATE claiming maximization vertical and horizontal
> even if only horizontal of vertical is actually set (Should fix Bug
> #3969)  
>  * Loosen the rule that prevents an application from iconifying
> itself when skip\_taskbar is set (Bug #4434)  
>  * Rework visual depth selection of the frame window (Bug #4452)  
>  * Add support for NET\_MOVERESIZE\_WINDOW  
>  * Take gravity bit into account in configure resize only requests to
> comply with standard (Bug #3634)  
>  * Add client windows to save set to avoid loosing all windows in
> case of crash  
>  * Use guint32 instead of Time internally to avoid potential issues
> in 64bits  
>  * Add a "--replace" command line option to replace ICCCM2 compliant
> window managers (Bug #3731)

[下载 Xfce 4.4.3](http://www.xfce.org/download/)

寻找下一个 Xfce 版本 4.6？请参考：

-   [Xfce 4.6 ALPHA "Pinkie"
    发布](http://linuxtoy.org/archives/xfce-46-alpha-pinkie.html)
-   [Xfce 4.6 ALPHA
    截图预览](http://linuxtoy.org/archives/xfce-46-alpha-screenshots.html)
-   [Xfce 4.6 BETA-1 "Fuzzy"
    发布](http://linuxtoy.org/archives/xfce-46-beta-1-fuzzy.html)

