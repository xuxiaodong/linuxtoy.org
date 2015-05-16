Title: 木词——Exaile 的歌词插件
Date: 2009-02-18 11:39
Author: toy
Category: Apps
Tags: Exaile, Plugins
Slug: mumulrc

[撰文/nowhere]

Linux 下的播放器与 Win 比较，除了对镜象 +CUE
的支持不好外，最让人头痛的，就是歌词问题。

试过 mlrc、lrcdis 等通用型的 bash
脚本。最不满意的是不支持本地歌词文件，硬盘上明明有，它偏要去网上下，找半天还找不到，急死人了。

[![mumulrc](http://i.linuxtoy.org/images/2009/02/muci-thumb.jpg)](http://i.linuxtoy.org/images/2009/02/muci.jpg)  
*木词插件截图*

木木开发的这个 [Exaile 插件](http://mumuhere.blogbus.com/)，我最喜欢的：

1.  歌词搜索能力很强，不太生僻的，它都能找到。
2.  支持本地歌词，我稍微度了一下，本地歌词取名“歌手-标题”，它马上就能发现。“歌手 -标题”（中间有空格），我没试，说不定也能。

刚刚放出的测试版，基本功能是做好了，小毛病还有一些，不过作者会改进。

1.  开启插件后，退出 Exaile 时，不先关闭插件的话，得按两遍退出才能关闭
    Exaile。
2.  歌词显示时，在不太好的机器上会有闪烁（比如现在流行的上网本）。主流的双核
    CPU 机器没这个问题。
3.  歌词显示时，过渡不太自然，老觉得一跳一跳的。作者说现在的设计是 1
    秒刷新一次窗口，正在考虑换一种显示方式。
4.  播放过程中，如果关闭了插件，再想开启的话，必须得重启 Exaile。

Ubuntu 8.10 中，用如下方法安装：

1.  [下载附件](http://mumuhere.blogbus.com/logs/35256231.html)，解压。
2.  依赖 wxPython，需要装上相应的文件。  

    `sudo aptitude install libwxbase2.6-0 libwxgtk2.6-0 python-wxgtk2.6 python-wxversion`
3.  把附件中除说明以外的文件，全部 copy 到 .exaile/plugins 中，运行
    Exaile，在编辑-插件中，会看到 mumulrc，启用即可。

