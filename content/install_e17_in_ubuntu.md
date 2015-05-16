Title: 在 Ubuntu 中安装 E17
Date: 2006-12-23 21:44
Author: toy
Category: Tutorials
Slug: install_e17_in_ubuntu

[E17](http://www.enlightenment.org) 即 Enlightenment
窗口管理器的最新开发版。与 GNOME、KDE 等主流的桌面环境相比，E17
的优点是更加轻快。同时，E17
的外观也是相当漂亮，具有下拉阴影以及许多动态效果。如果你想完全感受 E17
的魅力，那么不如亲自去体验一番。

[![E17](http://i.linuxtoy.org/i/2006/12/e17_s.jpg)](http://i.linuxtoy.org/i/2006/12/e17.jpg)  
*E17 窗口管理器的外观*

E17 在 Ubuntu 6.10 中的安装过程如下：

1.  使用文本编辑器打开 /etc/apt/sources.list 文件，并添加下列内容：  
    `deb http://edevelop.org/pkg-e/ubuntu edgy e17`
2.  执行 `wget http://lut1n.ifrance.com/repo_key.asc`，这将下载
    repo\_key.asc 文件。然后，使用 `sudo apt-key add repo_key.asc`
    添加密匙信息。
3.  更新源，可执行 `sudo apt-get update` 指令。
4.  安装 E17，在终端中执行 `sudo apt-get install e17`。

E17 已经安装就绪，现在注销系统，在会话中选择 Enlightenment 即可登录进入
E17 环境。
