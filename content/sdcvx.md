Title: sdcvx：轻量级的词典工具
Date: 2006-11-10 10:50
Author: toy
Category: Apps
Slug: sdcvx

xwindow 下最好的词典工具是什么？我会毫无疑问的回答是 Stardict。terminal
下最好的词典工具是什么？我认为是 Stardict 的同门兄弟 sdcv。sdcv 是
Stardict 的命令行工具，它使用 Stardict 的字典。

**为什么要使用 sdcv?**

当 Stardict
在增加更多更强大的功能时，它的体积在膨涨，它的系统资源占用在增长，它的移植性和灵活性在下降。因而导致了越来越多的旧机器，越来越多的老系统渐渐离它远去。而轻量级的桌面环境，和精选的配搭软件，却给你的旧机器老系统，带来了新的曙光。因
sdcv 不包含 gui
部分，所以它拥有极好的移植性，极低的系统资源占用。同时也显得更加高效、灵活。

**sdcvx?**

sdcv 在各方面都具有优势，然而它却显现出一个弊端：它没有配搭一个轻量级的
GUI。这个 GUI 也要像 sdcv
一样具有良好的移植性，极低的系统资源使用率，也一样的高效灵活。那么 sdcvx
就应运而生，sdcvx 是 sdcv 的 X 环境下的 GUI，也可以看作是 sdcv
的一个功能扩展。

sdcvx 的目标是作轻量级的 X 桌面环境下的词典工具，它拥有和 Stardict
相似的使用习惯：

-   通配符查词：“？”代表任一单字符，“＊”代表更多的字符
-   模糊查词：在预查的单词前加上“/”号来查询更多的近义词
-   键盘快捷键：复制（ctrl+c）、粘贴（ctrl+v）、清屏（alt+c）、退出（ctrl+q）、快速返回查询输入框（空格键）、快速清除查询输入框（ESC）、快速查询输入框内的单词（回车键）
-   它拥有和 gdict、xfce-dict-plugins 相似的更简洁易用的界面

sdcvx 的安装方法是先安装 sdcv，然后再安装 GUI，即
`tar jxvf sdcvx.tar.bz2 -C /usr/bin`。

[![sdcvx](http://i.linuxtoy.org/i/2006/11/sdcvx_s.jpg)](http://i.linuxtoy.org/i/2006/11/sdcvx.jpg)

相关下载：

-   [sdcv](http://prdownloads.sourceforge.net/sdcv/sdcv-0.4.2.tar.bz2?download)
-   [sdcvx](http://linuxtoy.org/dls/sdcvx.tar.bz2)

[撰文/[crown.hg](http://www.kw-gift.com/blog/)]
