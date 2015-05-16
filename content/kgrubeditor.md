Title: KGRUBEditor: 可视化的 GRUB 编辑器
Date: 2008-02-19 09:46
Author: toy
Category: Apps
Slug: kgrubeditor

KGRUBEditor 是一款适用于 KDE 4 桌面环境的小工具，它为 GRUB
提供可视化的配置编辑器。使用 KGRUBEditor，你不仅可以跟随向导对 GRUB
的引导菜单进行编辑，而且能够设置 GRUB
的各种选项，例如默认菜单、密码、背景图片、颜色等等。此外，KGRUBEditor
也支持对各种存储设备的挂载点进行编辑。

**安装 KGRUBEditor**

KGRUBEditor 移植自 QGRUBEditor，仅支持 KDE 4，当前版本为
0.5b。在[下载其源代码](http://www.kde-apps.org/content/show.php/KGRUBEditor?content=75442)并解包后，可使用如下指令编译安装：


    mkdir build
    cd build
    cmake ..
    make
    sudo make install

注意，在编译前需要准备好相关依赖及工具，如 KDE 4 开发包、CMake 等。

**运行 KGRUBEditor**

在安装完成后，通过向终端输入 `kgrubeditor` 即可启动 KGRUBEditor。

[![KGRUBEditor](http://i.linuxtoy.org/i/2008/02/kgrubeditor1-thumb.png)](http://i.linuxtoy.org/i/2008/02/kgrubeditor1.png)

在 GRUB Entries
页面，可对已存在的菜单条目进行编辑，也可添加新的菜单条目。

[![KGRUBEditor](http://i.linuxtoy.org/i/2008/02/kgrubeditor2-thumb.png)](http://i.linuxtoy.org/i/2008/02/kgrubeditor2.png)

GRUB Settings 页面提供有关 GRUB 设置的各种选项，可在此对 GRUB 进行配置。

[![KGRUBEditor](http://i.linuxtoy.org/i/2008/02/kgrubeditor3-thumb.png)](http://i.linuxtoy.org/i/2008/02/kgrubeditor3.png)

GRUB Device Naming 显示存储设备的挂载情况。

如果你使用 GNOME 桌面环境，那么可以选择我们之前介绍的 [Bootloader
Manager](http://linuxtoy.org/archives/bootloader-manager.html)，或者
[StartUp
Manager](http://linuxtoy.org/archives/startup-manager.html)，它们也能对
GRUB 进行编辑和配置。
