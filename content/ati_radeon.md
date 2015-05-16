Title: ati 开源 RADEON 驱动双显支持
Date: 2006-10-23 08:50
Author: toy
Category: Tutorials
Slug: ati_radeon

fglrx 驱动在 edgy 下表现相当令人失望，升级到 edgy
这几天，基本上各种恼人的问题都是 fglrx 造成的。logout／suspend
时系统挂起；和 openoffice 的冲突；......除了眩目的 xgl3D 桌面外，fglrx
能给我的 edgy 带来的好处只剩下方便的双显支持了。今天稍作研究后搞定了 ati
开源 radeon 驱动的双头显示支持。效果完美，甚至好于 fglrx
驱动。第二显示器带来的屏幕扩展，很大程度可以替代 xgl3D
桌面带来的工作效率提高（窗口透明和桌面重整）。

实现方法步骤如下：

升级到 edgy。

在 /etc/modules 里注释掉 fglrx。

从[这里](http://mg.pov.lt/xorg.conf)下载 xorg.conf 文件替换
/etc/X11/xorg.conf #替换前做好备份

这个配置文件默认采用 MergedFB2
扩展桌面，支持两个显示器不同分辨率。窗口／鼠标在两个显示器间移动时自动调整坐标。（对宽屏笔记本用户很重要）

如果你不需要在两个显示器间采用不同分辨率，可以在 ServerFlags 节中把  
` Option "DefaultServerLayout" "MergedFB2Layout"`

行换成  
` Option "DefaultServerLayout" "MergedFBLayout"`

幸运的话重启 X 后就能完美的实现双显了。

如果你的主板/显卡在检测第二显示器时存在问题
（只有一个显示器被点亮），你可以用如下方法解决：

如果你采用 MergedFBLayout 找到 MergedFB 对应的 Device 节 （其中包含
Identifier "MergedFB ATI Technologies,...."）

在其中添加这行  
` Option "MonitorLayout" "LVDS, CRT2"`

如果你采用 MergedFB2，以此类推，在 MergedFB2 对应的 Device
节中添加上面一行。

保存文件，重启 X。

开源驱动虽然 3d 加速比不上 fglrx，但在我这里 mplayer -vo gl
全屏时是没问题的。最重要的，由 fglrx 引起的问题全部解决。依靠 linux
的稳定性和永不挂起的休眠，以后重启机器除了升级内核外，我找不到其他理由。

Pure Opensource ，Genuine Linux ...

（注：此文作者为
lvs，[原始链接](http://lvscar.blogspot.com/2006/10/atiradeon.html)，非常感谢
lvs 朋友对 linuxtoy 的支持）
