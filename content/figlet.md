Title: figlet：ASCII 艺术字生成器
Date: 2006-09-08 21:44
Author: toy
Category: Apps
Slug: figlet

以前在逛论坛，或收邮件时，常看到有些朋友使用 ASCII
艺术字所作的签名，当时就觉得既好看，又非常神奇，羡慕不已。现在自己也可以尝试制作了，因为通过
figlet 这个小工具就能够直接生成 ASCII 艺术字，使用简单而方便。

figlet（如果没有的话，可以通过 sudo apt-get install figlet
进行安装）是命令行程序，使用方法为：

`figlet linuxtoy`

这样就会产生如下的 ASCII 艺术字：

![linuxtoy](http://i.linuxtoy.org/i/figlet.png)

另外，figlet 还有几个有用的选项：-w 为显示的宽度（字符），-f
可以定义不同的字体样式，-c 使生成的 ASCII 艺术字居中显示。

（Via [Inside Open
Source](http://opensource.apress.com/article/122/command-line-gems-figlet),
thanks!）
