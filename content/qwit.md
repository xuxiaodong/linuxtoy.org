Title: Qwit，一个小巧且功能强大的 Twitter 客户端
Date: 2008-10-16 10:08
Author: toy
Category: Apps
Tags: Qwir, Twitter
Slug: qwit

[撰文/[彭嘉佑](http://pengjiayou.com/blog/)]

昨天在 Planet Fedora 上看到一个叫做 Qwit
的客户端的介绍，界面简洁，功能强大，可以查看你自己和朋友的 Twitter
消息，公共消息，别人回复你的消息，并可以直接回复（有回复按钮），支持手动刷新，可以设置更新时间间隔，有系统托盘图标及消息提示等基本功能，而且感觉
UI 设计的很不错的，虽然 Linux 下的 Twitter 客户端没有 Windows
下那么丰富，但也是很多的，我曾经介绍过 Twitux 这个 Twitter 客户端，虽然
Twitux 安装非常方便，但是其 UI 设计方面很不爽，发布消息的时候，非得按
Ctrl+N 在新窗口中输入消息不可，而 Qwit
直接将新消息窗口整合到了主界面中，很方便，这和 gTwitter 差不多，而且
Linux 下还有一个支持多微博客系统的客户端 Gwibber （支持 Twitter 和
identi.ca 等），但无论是 gTwitter 还是 Gwibber
我无论如何都搞不定依赖，只好作罢，另外，大量基于 Adobe Air 的 Twitter
客户端在 Linux 下都有问题，而 Qwit 是我最近发现的功能最强大的 Twitter
客户端了。

[![Qwit](http://i.linuxtoy.org/i/2008/10/qwit1-thumb.png)](http://i.linuxtoy.org/i/2008/10/qwit1.png)

听了上面的介绍，以及上面的截图，动心了吧，哈哈，那就下载吧，Qwit 基于
QT4 开发，在 Fedora 9 （Gnome）下安装需要如下环境 Linux 2.6.25, QT
4.3.3, GCC 4.1.2。

最新版本特性：

1.  头像图片缓存
2.  消息中的链接可点击
3.  显示别人回复你的消息
4.  http-proxy 代理支持
5.  KDE 原生界面
6.  公共消息，回复好友消息及自定义Twitter用户的时间线
7.  日志

Linux 下安装及编译说明：

-   解压源码包
-   进入解压后的目录，执行 qmake 命令，然后执行 make，最后 make install
-   输入 qwit 回车启动 Qwit 吧

你也可以直接下载可执行文件包，下载解压之后，双击即可运行了…我不想编译，我就这么懒
“smile”

另外说说 Qwit 不足的地方吧。先上图：

[![Qwit](http://i.linuxtoy.org/i/2008/10/qwit2-thumb.png)](http://i.linuxtoy.org/i/2008/10/qwit2.png)

上方的消息提示窗口感觉有点不爽，上图显示的只是一个消息，如果刷新之后有大量消息，整个屏幕都被占满了，可不可以改进一下做成像
Network Manager
连接成功之后的提示窗口那样呢？可以显示好友的头像和他的消息，消息窗口美化一下，如果有多个好友的消息，则轮流显示，窗口大小固定下来，不至于占用太多屏幕空间。

在设置界面加入更多自定义功能，比如可以设置是否显示消息提示功能，等等（更多[截图](http://linux.softpedia.com/progScreenshots/Qwit-Screenshot-41834.html)）。

总的来说，Qwit 已经是一个非常不错的 Twitter 客户端了，作者说是因为要学习
QT4 编程而开发，不知道有没有熟悉 QT4 编程的朋友，希望可以参与进去。

已经将 Qwit 设置成开机自启动程序了，以后默认的 Twitter
客户端，就是它了。

Qwit 项目主页：<http://code.google.com/p/qwit/>

[[原文链接](http://pengjiayou.com/blog/qwit-a-lightweighted-but-powerful-twitter-client-for-linux)]
