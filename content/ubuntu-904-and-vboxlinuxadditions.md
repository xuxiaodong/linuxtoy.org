Title: 在 Ubuntu 9.04 中安装 VBoxLinuxAdditions 时遇到错误的解决办法
Date: 2009-04-24 16:54
Author: toy
Category: Tips
Tags: Ubuntu 9.04, VirtualBox
Slug: ubuntu-904-and-vboxlinuxadditions

{撰文/[Leniy](http://eot-lug.blogspot.com/)}

昨天下完更新包后寝室要熄灯，于是今天才安装更新。重启后却提示我 ABI major
version(4) doesn't match the server's version(5)，另外还有 vboxadd
的模块错误。其解决办法如下：

先在提示的错误框中选择第一个，进入 Simple 模式。进入 GNOME
后，建立一个文件夹 ~/leniytemp 备用。接着在命令行输入：

sudo ./VBoxLinuxAdditions-x86.run --target ~/leniytemp

amd64 的类似。这次安装会提示 X Server 因为版本不匹配安装失败。然后进入
~/leniytemp，修改 install.sh 文件：

sudo gedit install.sh

在第 415 行（Ctrl+I 可以查找行号），把 1.5.99.* | 1.6 中的 1.6 换成
1.6.0 然后保存。

sudo ./install.sh

再安装一次，重启。解决问题。

{[原文链接](http://eot-lug.blogspot.com/2009/04/ubuntu904vboxlinuxadditions.html)}
