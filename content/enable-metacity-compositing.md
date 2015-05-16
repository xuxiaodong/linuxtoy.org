Title: 小技巧: 打开 Metacity 的混合特效
Date: 2008-04-03 10:45
Author: toy
Category: Tips
Tags: Metacity, Tips
Slug: enable-metacity-compositing

我们知道在 [GNOME
2.22](http://linuxtoy.org/archives/first-look-at-the-gnome-222.html)
中的 Metacity
窗口管理器已经具有了混合特效，但是默认情况下这些混合特效并没有被打开。如果你已经安装了
GNOME 2.22，且当前所用的显卡也支持，那么可以使用以下方法来打开 Metacity
的混合特效。

[![Metacity
Compositing](http://i.linuxtoy.org/i/2008/04/metacity-compositing-300x141.png "metacity-compositing")](http://i.linuxtoy.org/i/2008/04/metacity-compositing.png)

1.  按 Alt + F2，打开“运行应用程序”对话框。输入 gconf-editor，并按回车。
2.  导航到 Apps->metacity->general，并选中 compositing\_manager。

你也可以执行下面的终端命令来打开 Metacity 的混合特效：

`gconftool-2 -s '/apps/metacity/general/compositing_manager' --type bool true`

要关闭 Metacity 的混合特效则执行：

`gconftool-2 -s '/apps/metacity/general/compositing_manager' --type bool false`

[via
[Tombuntu](http://tombuntu.com/index.php/2008/03/31/enable-metacity-compositing-in-gnome-222/)]
