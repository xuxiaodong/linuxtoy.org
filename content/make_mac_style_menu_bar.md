Title: 打造 Mac 风格的菜单栏
Date: 2006-12-22 20:36
Author: toy
Category: Tutorials
Slug: make_mac_style_menu_bar

有很多朋友虽然十分喜欢 Mac 系统的风格，但是却无缘享用 Mac
系统。没有关系，使用 Linux，我们完全可以凭着自己的喜好来定制一个与 Mac
系统相类似的风格。以下即为一例。

[![Mac Style
Menu](http://i.linuxtoy.org/i/2006/12/macmenustyle_s.png)](http://i.linuxtoy.org/i/2006/12/macmenustyle.png)  
*Mac 风格的菜单栏*

在 Ubuntu 6.10+Gnome 环境中打造 Mac
风格的菜单栏，可以按照以下的步骤执行：

1.  到[这里](http://chrislord.net/files/gtkmenubar/)下载需要的包，经过我的测试，只需
    libgtk2.0-0\_2.10.6-0ubuntu1+macmenubar1.0.11\_i386.deb、libgtk2.0-bin\_2.10.6-0ubuntu1+macmenubar1.0.11\_i386.deb、libgtk2.0-common\_2.10.6-0ubuntu1+macmenubar1.0.11\_all.deb、libgtk2.0-0-dbg\_2.10.6-0ubuntu1+macmenubar1.0.11\_i386.deb、gnome-macmenu-applet\_1.0.11-1\_i386.deb
    这 5 个包。为了简便安装，执行 `sudo dpkg -i *.deb`。
2.  在使用 Mac 风格的菜单之前，你需要对 Gnome
    上方的面板作一些清理，以便为显示菜单腾出空间。我仅保留了一个主菜单，你可以根据自己的情况酌情处理。现在，右击
    Gnome 上面板，在弹出的菜单中选择“Add to
    panel”，然后在打开的窗口中选择“Mac Menu”，单击“Add”即可把 Mac
    风格的菜单栏应用组件添加到 Gnome 的面板中。
3.  好了，如果你之前打开了程序的话，那么现在关闭它们，并重新打开吧。注意观看
    Gnome 的上面板，已经可以显示应用程序的菜单栏了。

在使用过程中，感觉有些程序对于 Mac 风格的菜单栏支持得很好，如
Azuerus、Evince、Gaim、gFTP、Nautilus、Terminal
等，但也有些程序不支持，如
Firefox。更为严重的是，甚至某些程序会因此崩溃，如 Acrobat Reader
7。另外，菜单栏中的 Alt+[A-Z] 热键也无法正常工作。总之，目前看来，这个
Mac 风格的菜单栏还有好些缺点。

对于使用 Xfce 环境的朋友来说，同样有一个支持显示 Mac
风格菜单栏的[面板小应用程序](http://ubuntuforums.org/showpost.php?p=1586951)可用。

如果需要从补丁源码开始安装，可以详细查看 Ubuntu
英文论坛上面的[帖子](http://ubuntuforums.org/showthread.php?t=241868)。

PS.此文应内存不足网友的请求而写。
