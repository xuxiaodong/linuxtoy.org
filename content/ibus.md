Title: 下一代输入法框架 ibus
Date: 2008-08-03 07:33
Author: toy
Category: Apps
Tags: ibus, Python, scim-python
Slug: ibus

[撰文/[zhuli](http://www.zhuli.name)]

ibus 是一个下一代的输入法框架，作者是
[scim-python](http://linuxtoy.org/archives/scim-python.html) 的作者
Shawn.P.Huang，看样子以后是要取代 scim 的。

![ibus\_2.png](http://i.linuxtoy.org/i/2008/08/ibus_2.png)

ibus 主要采用 python
开发，现在还没有正式发布，不过据作者说就快发布了，现在主要在进行测试和完善设置。其主要亮点在于架构上，采用
cs
结构，所有输入引擎都是单独的进程，可以防止引擎之间互相影响，同时可以轻松实现引擎的随时加载和卸载。

现在已经有了拼音引擎，是移值的
[scim-python](http://linuxtoy.org/archives/scim-python.html)
的拼音，目前还没有形码输入法，m17n 可以用了，anthy 完成了大部分。

![ibus\_1.png](http://i.linuxtoy.org/i/2008/08/ibus_1.png)

相对而言另外两个下一代输入法引擎 imbus 和 scim2 却没有什么进展。

项目网址:
[http://code.google.com/p/ibus/](http://code.google.com/p/ibus/%20)
