Title: KDEmod 4.1 出炉了！
Date: 2008-07-31 14:33
Author: Ning Bao
Category: Tips
Tags: Archlinux, KDE, kde4, kdemod
Slug: kdemod-41

Archlinux的卖点之一就是其精雕细琢的KDE环境，[KDEmod](http://kdemod.ath.cx/)。  
然而，当KDE4放出之后，KDE3系列就显得不夠High了。

TOY已经发布了[关于Archlinux [Testing] Repo里KDE
4.1的信息](http://linuxtoy.org/archives/archlinux-kde-41.html)。

KDEmod团队也不甘落后，他们在今天也正式发布了KDE
4.1的稳定Packages，KDEmod4。

要安装的话，请按照KDEmod[论坛里的说明](http://kdemod.ath.cx/bbs/viewtopic.php?id=891):

1.清除所有有关KDEmod4的包：pacman -Rcs kdemod4-complete

2.清除所有有关KDEmod3的包：pacman -Rcs kdemod-complete

3.清除所有有关KDE的包

4.检查是不是清除了所有有关KDE的包： pacman -Q |grep kde

5.修改/etc/pacman.conf中有关KDEmod的设置，去掉旧的[kdemod]、[kdemod-unstable]等

6.在/etc/pacman.conf中加上 [kdemod-core]：

i686平台

> [kdemod-core]  
>  Server = http://kdemod.ath.cx/repo/core/i686

X86\_64平台

> [kdemod-core]  
>  Server = http://kdemod.ath.cx/repo/core/x86\_64

7. pacman -Suy

8.要安装所有KDEmod4的内容的话：pacman -S kdemod-complete;

只要安装最基本的内容的话：pacman -S kdemod

9.安装本地化软件，中文的话：pacman -S kdemod-kde-l10n-zh\_cn
kdemod-kde-l10n-zh\_tw

10.如果要完全清除KDEmod4的话：pacman -Rcs kdemod-uninstall

与KDEmod3不大一样的是，KDEmod4把Repo分成了几个部分，比如[kdemod-extragear]和[kdemod-playground]等。

我没有安装Archlinux [testing]
Repo里的KDE4.1，所以无法比较。但是经过一天，我发现KDEmod4真的是非常酷，比KDEmod3更上了一个台阶，而且感觉比较稳定。我个人对KDE4华丽的界面和Plasma、Widgets等技术不感兴趣（我一直在用dwm、wmii、awsome、xmonad之类的WMs）。不过，KDE4中的Semantic
Search技术（strigi,nepomuk...）还是很吸引我的还有就是KDE4中通用的脚本框架（kross）也很有趣，我有时间会写一些这方面的东西。
