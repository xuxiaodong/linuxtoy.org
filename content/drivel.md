Title: Drivel — 离线 Blog 客户端
Date: 2006-08-04 20:25
Author: toy
Category: Tutorials
Slug: drivel

在 Linux 中找离线 Blog 客户端真的很难，之前有试过
BloGTK，但那已经是很遥远的事情了。直到最近，我对于
[Drivel](http://www.dropline.net/drivel/)
的发现，仿佛又重新燃起了希望。Drivel
虽然目前还算不上完美，但至少能够满足我的部分需要了。联想到在 Firefox
中写时的冒险，这总聊胜于无吧。

[![Drivel](http://i.linuxtoy.org/i/drivel_s.png)](http://i.linuxtoy.org/i/drivel.png)

**Drivel 的主要功能**

-   Drivel 现在支持的 Blog 系统包括：Movable Type、WordPress、Drupal
    等。同时，Drivel 也支持 LiveJournal、Blogger 等服务。
-   在 Drivel 中，可以投递、编辑、删除及查看最近的 Blog 条目。
-   集成了拼写检查和 HTML 语法高亮显示功能。
-   支持离线撰写和编辑。
-   能够在崩溃事件后自动恢复。
-   其他日志系统的扩展功能，如 LiveJournal 安全组和 Movable Type 类别。
-   此外，Drivel
    还支持大多数格式化操作，如：给文字加粗，上标下标，引用内容，插入列表、链接、图像、投票等等。

**Drivel 的安装**

以 Ubuntu 系统为例，直接在终端中执行指令 `sudo apt-get install drivel`
即可。其他系统请自行阅读安装说明。

**Drivel 的使用**

1.登录 Blog 系统

因为我目前使用的 Blog 系统为 WordPress，所以这里以 WordPress
为例。在安装完成后，通过“Application - Internet -Drivel Journal
Editor”菜单命令可以启动 Drivel。此时，Blog
系统登录窗口将会出现。现在要做的就是填写各种选项，像 Username、Password
这些。其中值得注意的是，Journal type 要选择 Movable Type（因为没有
WordPress 的选项，所以只有选相近的啰），而 Server address 则需要填入
xmlrpc.php
文件的正确地址（比如：http://www.xyz.com/xmlrpc.php）。然后点击“Log
In”就可以了。

2.撰写日志

这个就要靠各人自由发挥啰。不过，在这里还是提点一下，菜单下面的 Subject
即日志的标题，而 Show more options 则会提供有关类别的选项。在“Journal -
Recent
Entries”中则是你最近投递的日志，点击即可进行相关的编辑操作。“Format”菜单提供的是有关格式化的操作。

3.投递日志

看到右下角那个“Post”按钮了吗？点击它吧。

**Drivel 的不足**

就我的使用来看，当前 Drivel
仍然有诸多方面的不足。比如，无法选择多个类别，不支持
Tag，不支持引用等等。这些只有期待 Drivel 的后续版本加以改进了。

你使用离线 Blog 客户端吗？欢迎与我分享！

PS.这篇主题即由 Drivel 投递，效果非常不错。
