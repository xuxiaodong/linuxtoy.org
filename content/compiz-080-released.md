Title: Compiz 0.8.0 发布
Date: 2009-02-21 11:52
Author: toy
Category: Apps
Tags: Compiz
Slug: compiz-080-released

Compiz 的新版本 0.8.0 现已发布。自上一版 0.7.8 推出以来，Compiz 0.8.0
主要增加了新的 commands 和 gnomecompat 插件、支持 GNOME 2.24、调整了
gtk(kde4)-window-decorator、以及修正了一些内存泄漏问题。

*参阅 [Compiz 0.8.0
Changelog](http://lists.freedesktop.org/archives/compiz/2009-February/003299.html)*

> New plugin "commands" that handles the bindings for arbitrary commands
> that previously were handled in core. In addition to the previously
> present key bindings button and edge bindings were added as well.
>
> New plugin "gnomecompat" which handles bindings that are exclusively
> used in the Gnome desktop environment and removed the corresponding
> bindings from core. This change fixes main menu and run dialog
> bindings for KDE users as those previously were conflicting between
> compiz and KDE. Gnome users upgrading should make sure to enable this
> plugin.
>
> Added support for \_NET\_WM\_FULLSCREEN\_MONITORS EWMH hint.
>
> Added support for reading the icon hint from the WM\_HINTS property if
> \_NET\_WM\_ICON is not available.
>
> Update Gnome support for Gnome 2.24.
>
> Added options to scale plugin that allow "toggle type" behaviour for
> key and button bindings.
>
> Several memory leak fixes.
>
> Adjusted gtk-window-decorator for newer libmetacity-private versions.
>
> Fixed gtk-window-decorator display for RTL languages.
>
> Adjusted kde4-window-decorator for KDE 4.2 API.
>
> Large number of minor bug fixes, especially in resize handling and
> stacking code.
>
> Translation updates

[Compiz](http://releases.compiz.org/core/) [via
[Phoronix](http://www.phoronix.com/scan.php?page=news_item&px=NzA3OQ)]
