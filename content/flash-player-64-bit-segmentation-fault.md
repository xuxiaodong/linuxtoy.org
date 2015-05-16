Title: 遭遇 Flash Player 64 位插件段错误
Date: 2009-02-08 14:13
Author: toy
Category: Tips
Tags: Debian, Flash Player
Slug: flash-player-64-bit-segmentation-fault

[撰文/yjwork]

看到 Debian Lenny RC 2 登场，正好捡一硬盘，忍不住装了下。用 netinst
安装了 gnome-core、Iceweasel，将 64 位的 Flash Player 插件放入
/usr/lib/iceweasel 后，运行 Iceweasel，输入 about:plugins
后看到可爱的插件了。

但是可怜的是，一打开带 Flash
的网站，浏览器自动关闭，换浏览器，也同样故障。

在终端运行，报“段错误”。而同样在我的另一个 Debian
系统，一直升级的系统里没问题。

一星期来，一直比较郁闷，重装系统 N 次，Google 无数次无法找到答案。

今天偶然试试装了
GNOME，居然没问题了，看来是缺少依赖。然后，一个个的软件删除，删除一个打开一次
Flash 网站，终于发现了该死的依赖文件
libcurl3-gnutls，装上这个后一切解决。

唉，如果正好有人也遇到这样的问题的话，看看吧；如果那位老大给解释解释最好不过了。
