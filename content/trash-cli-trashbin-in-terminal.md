Title: trash-cli: 终端版回收站
Date: 2014-07-10 21:42
Author: lovenemesis
Category: Cli
Slug: trash-cli-trashbin-in-terminal

终端下的删除操作也可以有后悔药吃！trash-cli 提供对 FreeDesktop.org
标准兼容回收站的终端访问方式。

功能特性有：

-   与 GNOME, KDE，XFCE 等桌面环境共用一个回收站。
-   可以正确记录删除的原位置、时间及权限，完美恢复。
-   基于 Python 2.7。

**PS:** 或许您也想用这个作为 `rm` 的 `alias`？
程序作者并不建议这么做，因为 `trash-put` 有些行为和 `rm` 并不一样。

[项目 Github 主页](https://github.com/andreafrancia/trash-cli)

Fedora 中安装：

`pkcon install trash-cli`
