Title: SMPlayer 0.6.6 发布
Date: 2009-01-04 16:19
Author: lovenemesis
Category: Movie Player
Tags: mplayer, Qt
Slug: smplayer-066-release

基于 Qt4 的 MPlayer 图形前端 SMPlayer 今日发布了 0.6.6 版本。

0.6.6 版本相对于以前版本有如下变化:

-   增加了一个生成视频预览(缩略图)的选项。
-   增加了一个由 Matthias Petri 开发的模仿 media player classic 的界面。
-   增加了一些缩放选项，用来在不加黑色边框时显示视频。
-   实现了一个新的可选的保存文件设置的方法。该方法对于每一个播放过的文件使用一个
    ini 文件。该方法比旧方式要快。
-   在选项->视频中添加了一个新选项，在全屏播放时添加黑色边框。如果启用该选项，在全屏模式时将向图像添加黑色边框。这样就使得字幕可以在黑色边框上显示。
-   提高播放进度条的分辨率，允许更精确的搜索。
-   为“置顶”添加三种模式：总是、从不和在播放时。
-   为打开的 URL 增加历史功能。
-   增加了一个可以遍历所有观察比例的动作，默认指派到按键“A”上。
-   可以在每个文件载入前执行一些操作。
-   可以设置互联网代理(用于下载字幕)。

英文原文及下载见[这里](http://www.qt-apps.org/content/show.php/SMPlayer?content=61041)。  
本人已经用官方源代码打包了 RPM for Fedora 10 i386， Dropbox
下载地址见[这里](http://dl.getdropbox.com/u/464139/smplayer-0.6.6-rvm.i386.rpm)。

2009年1月18日更新为本人中文完全汉化版，欢迎下载测试！  
已安装原先版本的朋友在终端使用以下命令覆盖安装：  

`su -c 'rpm -Uvh --replacepkgs --replacefiles smplayer-0.6.6-rvm.i386.rpm'`  
注意：以上链接经测试复制可用！先前留言中的代码被“污染”……
