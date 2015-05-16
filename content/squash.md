Title: Squash — 批量调整图片大小
Date: 2008-04-11 18:10
Author: toy
Category: Apps
Tags: Qt, Squash
Slug: squash

[Squash](http://code.google.com/p/squash/)
以批处理模式同时对多幅图片调整大小，对经常需要处理大量图片的用户来说十分方便。在使用
Squash 时，个人感觉它处理图片的速度非常快，这得益于 Squash
支持多线程的特性。另外，Squash 还支持跨平台，无论是 Linux 用户，还是
Windows 和 Mac 用户，都可以使用它。

**安装 Squash**

Squash 目前提供有 deb 二进制包及源码包。如果你使用
Debian/Ubuntu，那么可以在[下载 deb
包](http://code.google.com/p/squash/downloads/list)后执行以下命令来安装：

`sudo dpkg -i squash*.deb`

其他 Linux 用户可以[下载 Squash
的源代码](http://code.google.com/p/squash/downloads/list)编译：  
` ./configure make`

需要注意的是，如果在安装 Squash 时出现了问题，请确认在你的 Linux
系统中已经安装了相应的 Qt4 库。

**使用 Squash**

当 Squash 安装成功后，从终端中执行 squash 就可以调出如下图所示的 Squash
用户界面了：

[![Squash](http://i.linuxtoy.org/i/2008/04/squash-300x208.png "squash")](http://i.linuxtoy.org/i/2008/04/squash.png)

Squash 的界面十分简洁，点击 Add Images
按钮添加要处理的图片，然后分别设置好要调整的百分比及保存目录，单击
Resize Images
即可。此外，你也可以根据自己需要设置其他选项，如文件名后缀、是否覆盖源文件等。
