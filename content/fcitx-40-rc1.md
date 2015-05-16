Title: FCITX 4.0 RC1
Date: 2010-11-09 18:51
Author: lovenemesis
Category: Desktop Environment
Tags: Fcitx
Slug: fcitx-40-rc1

小企鹅输入法 fcitx 4.0 rc1 发布，带来**换肤和多词库**支持！。

相对于 3.6.X 系列，本次 4.0 系列带来如下**全新功能**：

-   皮肤支持，采用cairo做绘制，pango负责字体，界面支持真透明；
-   拼音支持多个词库：利用createPYMB创建的词库放在`~/.config/fcitx/pinyin`下面即可；
-   额外的输入法支持（目前只有fcitx-sunpinyin）；
-   基于gtk的图形配置工具fcitx-config（并不包含在fcitx源码包中）；
-   右键的菜单支持。

一些其他的**小功能以及bugfix**：

-   拼音支持ng/gn的混用，例如输入ying/yign都可以辨认；
-   可以配置快速切换英文时将已有文字上屏；
-   快捷键支持禁用；
-   系统托盘和tint2，trayer等兼容性问题；
-   整体采用utf-8而不是gbk编码；
-   更多的调试信息；
-   更方便的码表配置。（分散的配置文件，而不是集中在`tables.conf`当中）；
-   scel2org，将sogou细胞词库转为原始的fcitx词库文件；
-   避免僵尸进程。

[源代码下载](http://code.google.com/p/fcitx/downloads/detail?name=fcitx-4.0_rc1.tar.gz)

*消息来源：*[csslayer.tk](http://csslayer.tk/wordpress/fcitx%e5%bc%80%e5%8f%91/fcitx-4-0-rc1/)
