Title: Wine 使用技巧两则
Date: 2008-03-13 19:00
Author: toy
Category: Tips
Slug: wine-tips

对于那些想要在 Linux 系统中运行 Windows 程序的人来说，Wine
算是一个不错的解决方案。最近，在使用 Wine
的过程中，我学到了两个使用技巧，现介绍给使用 Wine 的朋友分享。

**改善外观**

熟悉 Wine 的朋友可能都知道，所 Wine 出来的程序的默认外观与 Linux
系统中的原生程序看起来不太一致和协调。很多朋友对此也颇有抱怨。好在 Wine
支持安装 Windows 主题文件 (*.msstyles)，因此我们可以利用这一点来改善
Wine 程序的外观，使之与 Linux 环境融为一体。

具体操作步骤如下：

1.  执行 Wine 配置程序 winecfg，并切换到 Desktop Integration 选项卡；
2.  点击 Install theme 按钮选择已下载的主题文件；
3.  当主题安装成功后，可从 Theme 下拉框中选择；
4.  点击 OK 确认。

![Wine 配置](http://i.linuxtoy.org/i/2008/03/wine1.png)  
*应用主题后的效果*

在 deviantART 上可以找到许多与 Linux 桌面一致的 Windows 主题，如 [Ubuntu
Human](http://fioressj.deviantart.com/art/Human-for-Windows-37743373)、[GNOME
Clearlooks](http://ksaad.deviantart.com/art/ClearLooks-2-RC1-27877459)
等。

值得注意的是，在我应用主题后，在程序性能上有所影响。正所谓，鱼与熊掌不可兼得呀。

**设置背景**

当你使用桌面模拟功能 (该功能可通过 winecfg 配置程序打开，启用 Graphics →
Emulate a vistual desktop 选项即可)
时，你可以使用以下技巧来设置一个窗口背景。

1.  将 bmp 格式的壁纸文件复制到 ~/.wine/drive\_c/ 目录，假设其名称为
    SkyBlue.bmp；
2.  使用文本编辑器打开 ./wine/drive\_c/windows/win.ini
    文件，并加入下列内容：

        [Desktop]

        Wallpaper=c:\SkyBlue.bmp

![Wine 背景](http://i.linuxtoy.org/i/2008/03/wine2.png)  
*设置背景后的效果*

[via
[PolishLinux](http://polishlinux.org/apps/window-managers/wine-improving-look-and-feel/)]
