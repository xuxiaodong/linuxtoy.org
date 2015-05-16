Title: 在 Ubuntu 中安装 Quod Libet 0.24
Date: 2006-12-14 18:11
Author: toy
Category: Tutorials
Slug: install_quod_libet_in_ubuntu

[Quod Libet](http://www.sacredchao.net/quodlibet) 0.24
推出已经有好长一段时间了，但目前的 Ubuntu Edgy Eft 官方源中仍然保留的是
0.23。对于喜欢追新的朋友而言，可能有点等不及了。想要在你的 Ubuntu
中无痛安装 Quod Libet 最新版吗？那么，跟我来吧。

1.  添加 GPG 加密信息：  

    `wget http://malteo.homelinux.net/B54820BC.gpg -O- | sudo apt-key add -`
2.  在 /etc/apt/sources.list 中添加下列内容：  

    ` deb http://malteo.homelinux.net edgy-malteo all deb-src http://malteo.homelinux.net edgy-malteo all`
3.  更新源，并安装 Ex Falso、Quod Libet、以及 Quod Libet 插件：  

    ` sudo apt-get update sudo apt-get install exfalso quodlibet quodlibet-ext`
    如果你先前安装过 Quod Libet，那么可以直接升级：  
    `sudo apt-get upgrade`

安装好的 Quod Libet，如下图所示：

[![Quod
Libet](http://i.linuxtoy.org/i/2006/12/quodlibet_s.jpg)](http://i.linuxtoy.org/i/2006/12/quodlibet.jpg)  
*Quod Libet 主界面*

![Quod Libet
About](http://i.linuxtoy.org/i/2006/12/quodlibet_about.jpg)  
*Quod Libet 关于窗口*

希望以上内容能够给你带来一些帮助。
