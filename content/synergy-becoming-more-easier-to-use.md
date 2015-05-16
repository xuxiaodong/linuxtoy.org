Title: Synergy 变得越来越易用
Date: 2011-10-29 09:56
Author: shuge.lee
Category: Apps, Desktop Stuff
Tags: Synergy
Slug: synergy-becoming-more-easier-to-use

[Synergy](http://synergy-foss.org)
是一个能帮助您共享鼠标键盘的软件，它支持 Linux、Mac 和
Windows。它正在变得越来越易用。

你有两台以上的机器 ，但是只有一套键盘鼠标，如何能在多台机器间共用？

Synergy 的应用场景

    路由/交换机 +--- A Mac --- 插上鼠标、键盘，作为 Synergy server
                |
                +--- B Linux --- 作为 Synergy client
                |
                +--- C Windows --- 作为 Synergy client
                |
                + .....

分别在不同机器上启动 Synergy
的服务端和客户端后，就可以设置快捷键来切换控制。  
比如，可以配置为，现在鼠标键盘控制着 A Mac ，按 C-M-1
后鼠标和键盘就控制 B Linux，按 C-M-2 就控制 C Windows。

在 1.3 版本以前，配置界面和方式都是纯文本或者提供不太人道的 GUI
（在不同平台上甚至也有差异），截至本文发表时候，unstable 1.4 版本的 GUI
被重写，它变得更加易于配置和易用。

真相

[![](http://linuxtoy.org/img/2011/10/synergy-14-1.png)](http://linuxtoy.org/img/2011/10/synergy-14-1.png)

主界面

[![](http://linuxtoy.org/img/2011/10/synergy-14-2.png)](http://linuxtoy.org/img/2011/10/synergy-14-2.png)

终于支持 DND 了

[![](http://linuxtoy.org/img/2011/10/synergy-14-3.png)](http://linuxtoy.org/img/2011/10/synergy-14-3.png)

配置快捷键切换

**注意**： 1.4 并不兼容 1.3，你如果通过 PMS(Package management
system)
来安装，可能会有兼容性问题，请到[官网下载](http://synergy-foss.org/download/)
unstable 1.4。

(完)
