Title: png2ico－实用的图标转换器
Date: 2007-05-10 18:54
Author: toy
Category: Apps
Slug: png2ico

[png2ico](http://www.winterdrache.de/freeware/png2ico/)
是一个十分小巧的程序，但是却很实用。其主要功能是将 .png 格式的文件转换为
.ico 图标文件。该程序对于 Linux
系统仅提供了源代码，在使用之前需要自行编译，以下是编译、安装及使用过程。

为了完成 png2ico 的编译，你需要准备 libpng 库和 g++
编译器。在解开打包的源代码存档文件之后，执行 `make`
指令即可。然后，你只需将已编译好的二进制文件 png2ico 复制到
/usr/local/bin/ 目录就可以开始使用了。

png2ico
是命令行程序，它没有图形用户界面，所以其操作需要在命令行界面下完成。假设你有一个名为
logo.png 的文件，现将其转换为 favicon.ico 文件，可以执行以下指令：  
`png2ico favicon.ico logo.png`

有个人网站的朋友，可以使用此程序方便的制作收藏夹图标（一般其名称为“favicon.ico”）。

- [Download png2ico
source](http://www.winterdrache.de/freeware/png2ico/data/png2ico-src-2002-12-08.tar.gz)
