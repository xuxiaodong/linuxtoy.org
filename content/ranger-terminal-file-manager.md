Title: Ranger: 控制台下的文件管理器
Date: 2010-10-04 20:18
Author: lovenemesis
Category: File Manager
Tags: ranger, Vi
Slug: ranger-terminal-file-manager

[Ranger](//wiki.archlinux.org/index.php/Ranger)
是一个控制台下的文件管理器。*感谢 gDD 来稿！*

Ranger 用 Python 完成，默认为使用 Vim 风格的按键绑定，比如
hjkl（上下左右），dd（剪切），yy（复制）等等。功能很全，扩展/可配置性也非常不错，介绍一下几个主要特点：

-   Vi 风格的按键绑定。
-   类似MacOS X下Finder（文件管理器）的多列文件管理方式。
-   支持多标签页。
-   实时预览文本文件和目录。
-   可以使用S键退出并转至最后浏览的目录。

[![](http://linuxtoy.org/img/2010/10/screenshot-ranger.png)](http://linuxtoy.org/img/2010/10/screenshot-ranger.png)

另外man和帮助文档（主界面按“?”）也很完善，喜欢Vi风格的千万别错过了。

Arch Linux 用户可以通过 `AUR/ranger-git `获取。

Fedora 用户可以通过 `pkcon install ranger` 安装。

另外 Vi 粉丝们也可以尝试基于 WebKit
引擎的浏览器：[Vimprobable](http://www.vimprobable.org/)。
