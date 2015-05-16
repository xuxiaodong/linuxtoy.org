Title: FVWM 多国文字渲染补丁
Date: 2009-02-17 16:56
Author: toy
Category: Apps
Tags: FVWM, Patch
Slug: fvwm-mix-display-patch

[撰文/kemean]

FVWM 虽支持 Xft2 &
Fontconfig，却无法支持对多语文字采用多种字体来渲染，单一字体渲染往往不尽人意，不是中文乱码就是英文非常难看。因此，我写了这个补丁，实现了类似
Pango 的国际化文本渲染功能。

[![FVWM](http://i.linuxtoy.org/images/2009/02/fvwm-mix-display-thumb.png)](http://i.linuxtoy.org/images/2009/02/fvwm-mix-display.png)

打上这个补丁之后，FVWM 便跟其它 GTK 程序一样，只需设置为 Sans
即可，它会根据具体的文字来匹配合适的字体，完全遵循
Fontconfig，渲染效果非常好。

你可以从 [Ubuntu
中文论坛](http://forum.ubuntu.org.cn/download/file.php?id=56775)下载此补丁。

**2009.2.19 更新**

粗斜体的问题已经修复， 而且补丁也基本重写，很大程度上重用了 FVWM
的代码， 性能更高了，代码也简洁许多。除了粗斜体外，
还支持了旋转字体（FVWM 自身支持的，不过我不会设置）。

[下载链接已更新]
