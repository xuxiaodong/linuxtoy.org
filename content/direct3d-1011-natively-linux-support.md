Title: Direct3D 10/11 Linux 原生支持
Date: 2010-09-21 21:41
Author: lovenemesis
Category: Drivers
Tags: direct3d, Gallium3D
Slug: direct3d-1011-natively-linux-support

Direct3D 10/11 的 State Tracker 进入了 Mesa/Gallium3D
库，意味着依照该驱动架构开发的显卡在 Linux 平台将会具有 Direct3D 10/11
加速功能。

目前使用 Wine 运行的 Direct3D 程序是在将 Direct3D 10/11 的指令翻译成
OpenGL 的指令集，若是利用这个新加入的 State
Tracker，这一个翻译的步骤即可省略，效率预计将会有客观改善/

当下该 State Tracker 已经可以运行多个 Direct3D 10/11 的材质测试。尽管
Wine 项目上面尚未有对应的 DLL 发布利用该 State
Tracker，开发者表示实现这个功能的工作并不复杂。

如果一切顺利的话，不远的将来就可以已原生加速的方式在 Linux 平台上运行
Direct3D 10/11 游戏而无需 OpenGL 翻译。

值得注意的是，目前 Gallium3D 尚未实现 OpenGL 3/4 的 State Tracker。

*消息来源：*
[Phoronix](http://www.phoronix.com/scan.php?page=article&item=mesa_gallium3d_d3d11&num=1)
