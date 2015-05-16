Title: Fluxbox 1.0 RC 3
Date: 2007-03-21 10:03
Author: toy
Category: Apps
Slug: fluxbox-10-rc-3-released

[Fluxbox](http://www.fluxbox.org/) 1.0 RC 3
于昨日放出，据了解，这是最后一个 RC 版，紧接着将要发布的是 1.0.0
稳定版。此版本引入了一些新特性，如：keys
文件现在支持鼠标按钮、添加了自动更新配置文件的工具等。另外，许多 bug
也得到了修正。

以下是 Fluxbox 1.0 RC 3 的更新记录：

> * Introduced support for mouse buttons in the keys file  
>  - Mouse buttons are bound to new `keys' Mouse1, Mouse2, etc.  
>  - Also a new modifier `OnDesktop' to specify actions that should
> take place  
>  when you click on the desktop -- without this, mouse bindings are
> global  
>  * Added a utility to the project that automatically updates
> configuration  
>  files when we change the syntax -- your current mouse bindings on
> the  
>  desktop will be added to your keys file automatically  
>  * Introduced new key command: HideMenus  
>  * Introduced a key command to display a menu stored in an arbitrary
> file:  
>  CustomMenu /path/to/file  
>  * More extended wm hints support:  
>  * \_NET\_WM\_MOVERESIZE\_CANCEL (new in version 1.4.draft-1),  
>  * \_NET\_REQUEST\_FRAME\_EXTENTS  
>  * \_NET\_WM\_WINDOW\_TYPE\_MENU  
>  * \_NET\_WM\_WINDOW\_TYPE\_TOOLBAR  
>  * Little simplification of data structure for keybindings  
>  Side effects:  
>  - "Mod4 a b" now behaves like "Mod4 a None b" -- in fact, "None" is
> now  
>  completely obsolete  
>  - You can press "Escape" to cancel any Emacs-style keychain in
> progress  
>  (unless it's bound to something else)  
>  - If there is a conflict between bindings, the first one in the file
> wins  
>  - Fixes handling of keychains like "Mod4 a Mod1 b"  
>  - Should fix some issues with "None" modifier  
>  * Updated following translations:  
>  pt\_PT, es\_ES, es\_AR, pt\_BR, de\_DE, nb\_NO  
>  * Support per-window transparency settings.  
>  ( sf.net patch #1511042, feature #1108692 )  
>  - new "Transparency" menu in the window menu  
>  - new apps file attribute:  
>  [alpha] {int int} (or just {int})  
>  Where numbers represent focused and unfocused transparency,  
>  respectively. One number only will be used for both.  
>  - Also, show toggle status for shade and stick in window menu.  
>  * Introduced new key command: SetAlpha [[+-] [[+-]]]  
>  - with no arguments, returns the focused window to default settings  
>  - with one argument, changes both focused and unfocused settings the
> same  
>  way  
>  - with two arguments, the first changes the focused alpha, and the
> second  
>  changes the unfocused alpha  
>  E.g. SetAlpha 127 +5 will set the focused alpha to 127 and increment
> the  
>  unfocused alpha by 5 (until it reaches 255)  
>  * Added resource and menu item for maximizing over external tabs  
>  * Renamed session.screen*.iconbar.deiconifyMode to  
>  session.screen*.userFollowModel (Mark)  
>  This resource is used for:  
>  - clicking a window on a different workspace in the iconbar  
>  - \_NET\_ACTIVE\_WINDOW messages where the source is a pager  
>  - clicking a client in the workspace menu (and the opposite is used
> for  
>  right clicks)  
>  Possible values are:  
>  - Follow: go to the workspace of the selected window  
>  - Current: bring the window to the current workspace  
>  - SemiFollow: act like Current for iconified windows, else Follow  
>  - Ignore: leave it alone  
>  * Added support for negative arguments to the `Tab' key command to
> count  
>  backwards from the last tab in the group  
>  * Added option to :Minimize key command to lower all windows in the
> same  
>  layer as the focused window,syntax is :Minimize (layer)  
>  * Several changes for background style option:  
>  - now support `background: mod' to coincide with fbsetroot -mod --  
>  In addition to `background.color' and `background.colorTo', this
> option  
>  must also set `background.modX' and `background.modY' to integers  
>  - added `background: none' for styles that do not include a
> background  
>  - fixed bug with style backgrounds not getting set when changing
> styles  
>  - updated default styles to be valid wrt background options  
>  * Made some changes to the way autogrouping in the apps file works  
>  - Introduced new syntax [group] (workspace) to group new windows only
> with  
>  windows on the current workspace.  
>  * XEMBED support for systemtray.  
>  * Added typeahead support to menus (patch by Philipp Goedl, modified
> by Mark  
>  and Matteo Galiazzo)  
>  - Added new style item menu.frame.underlineColor: for displaying  
>  matching items  
>  * session.screen.defaultDeco now allows same strings as apps file

Download [Fluxbox 1.0 RC 3](http://www.fluxbox.org/download.php)
