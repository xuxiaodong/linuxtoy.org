Title: 在 Linux 下玩《英雄无敌 3》
Date: 2009-11-12 11:11
Author: jiqingwu
Category: Games
Slug: heroes-of-might-and-magic-3-for-linux

{ 撰文/[吴吉庆](http://hi.baidu.com/jiqing0925) }

**介绍**

英雄无敌 2 和 3 都是英雄无敌系列的经典，你知道吗，英雄无敌 3 有 Linux
版的啊。  
先来几张截图看看吧。

[![Heroes](http://i.linuxtoy.org/images/2009/11/thumb-heroes1.jpg)](http://i.linuxtoy.org/images/2009/11/heroes1.jpg)

[![Heroes](http://i.linuxtoy.org/images/2009/11/thumb-heroes2.jpg)](http://i.linuxtoy.org/images/2009/11/heroes2.jpg)

[![Heroes](http://i.linuxtoy.org/images/2009/11/thumb-heroes3.jpg)](http://i.linuxtoy.org/images/2009/11/heroes3.jpg)

怎么样？和 Windows 版的一样吗？  
不过，这个 Linux 版并不是原公司做的，这个是可敬的洛基(loki)公司做的。

洛基公司是个致力于开发 Linux 游戏的公司，目标是增加 Linux 的竞争力。  
无疑，他们都是非常喜欢 Linux 的一批人了。  
可惜，公司已经倒闭，无法赢利公司就无法生存。  
怎么 Linux 的游戏市场就是打不开呢？是因为当时 Linux 用户还少吧？
那么现在呢？

**下载和安装**

国内的用户可以到这里下载：

感谢 Ubuntu 中文论坛提供的服务。

下载完 Heroes.of.Might.and.Magic.3.Linux.[mulek.info].iso
后，按以下步骤安装：

sudo mount -o loop Heroes.of.Might.and.Magic.3.Linux.[mulek.info].iso
/mnt  
cd /mnt  
sudo bash setup.sh

将会启动安装的图形界面，有的机器也会启动文字安装界面。  
安装的默认目录是 /usr/local/games/Heroes3，你也可以更改。  
安装的大小是可以定制的，如果你不安装声音、音乐和视频，安装大小都不到
100 兆。

安装迅速完成， 这时在命令行运行 `heroes3`，就启动游戏了。  
进去体验一下吧，很流畅吧，CPU 占用非常之低，看来是基于 Timer
实现的啊，  
我喜欢这样的游戏。

**安装全屏补丁**

怎么回事？不能全屏。即使加了 `-f` 选项，也是在 800x600 的窗口中运行。

运行一下 `heroes3 -v`，现在的版本号是 1.2。

我们打一个 1.3.1 的补丁就可以了。

就在我们上面提到的  
中，有一个 heroes3-1.3.1a-x86.run 文件，大概两兆多大小，这个就是补丁。  
不过据说这个不行，要 Google 下载另一个 heroes3-1.3.1-x86.run，  
注意到差别了吗，这个文件名中少一个 a。另外这个大小只有 1 兆左右。

现在运行 `sudo sh heroes3-1.3.1-x86.run`，却发现以下错误：

    Verifying archive integrity...tail: cannot open `+6' for reading: No such file or directory
    Error in check sums 2268731580 1601210390

下面就是我要讲的主要部分，怎么对补丁进行 hack。

用 Vim 打开 heroes3-1.3.1-x86.run，搜索 +6 ，发现是作为 tail 的参数。  
表示从文件第六行的内容。但是这样使用参数是错误的，正确的使用方法是
`tail  
--lines=+6`。 所以把 +6 的部分都改正为 --lines=+6 。 这样 `tail:
cannot open  
`+6' for reading: No such file or directory` 的错误就消除了。

再次运行 `sudo sh heroes-1.3.1-x86.run`，仍然有如下错误

    Error in check sums 2268731580 1601210390

在 heroes-1.3.1-x86.run 中搜索，找到那个地方。

大概是 102 行，注释掉以下部分。

    #[ $sum1 -ne $CRCsum ] && {
    #  $echo Error in check sums $sum1 $CRCsum
    #  eval $finish; exit 2;
    #}

再次 `sudo sh heroes3-1.3.1-x86.run`，结果如下：

    Verifying archive integrity...OK
    Uncompressing Heroes of Might & Magic III for Linux: patch 1.3.1
    trap: 126: cd /tmp; /bin/rm -rf $tmpdir; exit $res: bad trap

搜索 trap，只在一个地方出现，

    [ "$keep" = y ] || trap 'cd /tmp; /bin/rm -rf $tmpdir; exit $res'

trap 什么意思，我不太明白，因为下面还有一行

    [ "$keep" = y ] || { cd /tmp; /bin/rm -rf $tmpdir; }

所以我认为 trap 这行没有实际作用，注释掉

    #[ "$keep" = y ] || trap 'cd /tmp; /bin/rm -rf $tmpdir; exit $res'

保存，运行 `sudo ./heroes3-1.3.1-x86.run --keep`。成了！

    Verifying archive integrity...OK
    Uncompressing Heroes of Might & Magic III for Linux: patch 1.3.1.....
    ***********************************************************************
    This script will install the 1.3.1 patch for Heroes of Might & Magic III
    You need an exiting installation of the game and sufficient
    write access permissions to proceed.

    This patch is for a x86 system
    You are running a x86 system

    OK !
    Please enter the Heroes III installation directory [/usr/local/games/Heroes3]
    :
    Patching heroes3 ...

    Successfully upgraded Heroes III to version 1.3.1 !
    Please read the file README.patch13 in /usr/local/games/Heroes3 for details
    about this patch.
    Enjoy the game !

检验一下，`heroes3 -v`：

    Heroes of Might and Magic III Linux 1.3.1
    - Mar  7 2000
    Built with flags:
    -DUNIX
    Built with glibc-2.1

OK，升级成功！运行
`heroes3`，不加参数，默认是全屏的。如果要在窗口内运行，就  
`heroes3 -w`。

Enjoy the game!

更新：  

想省事的朋友可以在[这里](http://code.google.com/p/girl-sword/downloads/list)下载我修改过的全屏补丁。

{
[Source](http://hi.baidu.com/jiqing0925/blog/item/08f1de445ddb5846510ffe94.html).
Thanks jiqing. }
