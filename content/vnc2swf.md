Title: Vnc2swf：Linux 中的 Flash 录制工具
Date: 2006-08-01 14:50
Author: toy
Category: Apps
Slug: vnc2swf

[Vnc2swf](http://www.unixuser.org/~euske/vnc2swf/index.html)
是一个很酷的玩具，使用它你可以把当前屏幕上的操作录制下来，保存成 swf
格式，俗称 Flash 动画，与他人分享。这种东西在 Windows
里都有些泛滥了，不过作为跨平台的 Vnc2swf，确有介绍的必要。

当前，Vnc2swf 包括两个版本：

-   Python 版，其最新版本号为0.8.2，从个人角度而言，我推荐使用这个版本。
-   C 版，其最新版本号为0.5.0。

要正常使用 Vnc2swf，你的系统可能至少需要满足下列要求（注意：我是就
Python 版本来说的）：

-   Python 2.3 以上版本。
-   Pygame 1.6 以上版本。
-   至少要安装一个 VNC 服务器，我使用的是 vncserver。

让我们来看一个 Vnc2swf 的屏幕录制过程：

首先，你可能需要配置“System -> Preferences -> Remote
Desktop”，打开“Sharing”下面的两个选项，以允许其他用户查看并控制你的桌面。

然后，在终端中敲入“vncserver“来启动VNC服务器。

接着，使用“./vnc2swf.py”来启动 Vnc2swf，此时会打开 Vnc2swf
的界面，保持默认选项，点击“Save
As”保存文件，再点击“Start”就可以开始录制了。当录制完成后，使用“Stop“来停止。

之后，在 Vnc2swf 的目录里就可以找到你录制的动画了，包括 swf 和 html
两个文件，打开 html 则可以观看录制的动画。

如需了解 Vnc2swf
的详细用法，请阅读其[使用说明](http://www.unixuser.org/~euske/vnc2swf/pyvnc2swf.html)。此外，Vnc2swf
除了包括录制的工具外，还包括可以编辑的 edit.py 和播放的
play.py，具体用法可查看上述链接。
