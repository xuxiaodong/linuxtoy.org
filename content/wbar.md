Title: wbar：Fluxbox 中的 Dock 应用
Date: 2006-10-21 17:40
Author: toy
Category: Tutorials
Slug: wbar

wbar 是一个相当小的 Dock 应用，与 Fluxbox
搭配使用，还算不错，既能保证有较好的速度，又不缺少适当的 eye candy
效果。

![wbar](http://i.linuxtoy.org/i/wbar.png)

在我的系统中，通过以下几个步骤可以让 wbar 良好的运行起来。

1.  到[这里](http://www.tecapli.com.ar/rodolfo/)抓取 1.0 的源代码。
2.  准备编译依赖：
    `sudo apt-get install libimlib2-dev`
3.  解包后，使用 make 开始编译，成功后在其目录生成 wbar 执行文件。
4.  使用 `sudo make config` 生成配置文件。
5.  通过 `sudo make install` 进行安装。

现在，执行 wbar 可以启动程序。如果不满意程序默认的配置和图标，那么可修改
/usr/local/share/wbar/dot.wbar 文件。
