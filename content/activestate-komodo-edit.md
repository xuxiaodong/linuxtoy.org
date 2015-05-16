Title: ActiveState Komodo Edit：好用的跨平台免费编辑器
Date: 2007-06-24 16:23
Author: toy
Category: Apps
Slug: activestate-komodo-edit

作为一个
Coder，如果能够找到适合自己所用的编辑器，则往往能起到事半功倍的效果。得
Livid 的推荐，[ActiveState Komodo
Edit](http://www.activestate.com/Products/komodo_edit/)
或许就是你正在寻找的那款工具。Komodo Edit
具有免费、支持多种语言、以及跨平台（可用于 Windows、Mac OS X 和
Linux）等特点。

[![Komodo
Edit](http://i.linuxtoy.org/i/2007/06/komodo-edit_s.jpg)](http://i.linuxtoy.org/i/2007/06/komodo-edit.jpg)  
*ActiveState Komodo Edit 屏幕截图*

当前，Komodo Edit 具有下列功能：

-   既支持 Perl、PHP、Python、Ruby、Tcl 等服务端语言，也支持
    CSS、HTML、JavaScript、XML 等。
-   在使用 Komodo Edit
    编写代码时，通过其提供的自动完成、调用提示、语法纠正、代码片断等功能可以充分提高你的编码效率，助你写出高质量的代码。
-   如果你已经是 Vi 或 Emacs 拥趸，那么可以试试 Komodo Edit 的 Vi 模拟和
    Emacs 键盘绑定功能，相信这能够让你平滑过渡。
-   Komode Edit 还提供项目管理功能，使你的开发过程清晰而充满条理。

Komodo Edit 目前稳定版本为 4.1，在下载后可按照以下步骤安装：

1.  在 Linux 上，Komodo Edit 要求 glibc 为 2.1 或更高版本、libjpeg.so.62
    或更高版本、libstdc++5
    或更高版本。在安装之前，你应当检查你的系统是否满足上述要求。
2.  使用 `tar zxvf Komodo-Edit-4.1.0-278996-linux-libcpp6-x86.tar.gz`
    解开安装包。
3.  转到上一步所解开的目录，执行 `./install.sh`
    安装脚本，然后按提示操作即可。
4.  在安装完成后，依次执行
    `ln -s <installdir>/komodo /usr/local/bin/komodo` 和
    ` export PATH=<installdir>:$PATH`，注意你需要将 installdir 替换为
    Komodo Edit 实际的安装位置。

现在，从终端执行 `komodo` 就可以运行 Komodo Edit
了，你也可以建立一个快捷方式方便启动它。

Komodo 还有一个收费版的 IDE，其功能与 Edit
相比，更为丰富，你可以从二者的[功能比较页面](http://www.activestate.com/Products/komodo_edit/edit_vs_ide.plex)了解详细情况。

- [Download ActiveState Komodo Edit
4.1](http://www.activestate.com/store/komodo_edit/download/)

[[via](http://www.v2ex.com/topic/view/13476.html)]
