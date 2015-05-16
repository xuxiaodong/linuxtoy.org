Title: FreeMind 在 Ubuntu Edgy Eft 中的安装
Date: 2006-11-21 18:37
Author: toy
Category: Tutorials
Slug: freemind_on_ubuntu_edgy_eft

[FreeMind](http://freemind.sourceforge.net)
的安装是要讲究技巧的，对于某些用户来说，按照常规办法安装的 FreeMind
可能难以正常运行。下面，我们就给出 FreeMind 0.8.0 在 Ubuntu Edgy Eft
中的安装过程。

[![FreeMind](http://i.linuxtoy.org/i/2006/11/freemind_s.png)](http://i.linuxtoy.org/i/2006/11/freemind.png)  
*（成功安装后的 FreeMind 运行截图）*

1.  安装 libcommons-lang-java：  
    `sudo apt-get install libcommons-lang-java`
2.  安装 librelaxng-datatype-java：  
    `sudo apt-get install librelaxng-datatype-java`
3.  安装
    [libforms-java](http://sourceforge.net/project/showfiles.php?group_id=7118&package_id=161831&release_id=355162)（需要下载）。  
    `sudo dpkg -i libforms-java_1.0.5-2_all.deb`
4.  以上三步的安装主要是为了解决 FreeMind
    的依赖问题。现在我们可以开始安装 [FreeMind
    0.8.0](http://sourceforge.net/project/showfiles.php?group_id=7118&package_id=161831&release_id=355162)
    了（同样需要下载）。  
    `sudo dpkg -i freemind_0.8.0-1_all.deb`
5.  如果上面所有的安装都没有问题，那么现在试着启动
    FreeMind。若正常，则说明 FreeMind 已经成功安装。

值得注意的是，FreeMind 的正常运行需要预先装好 Java
运行环境。另外，关于在 FreeMind
中正常显示中文的问题，可参考本站[之前所写的文章](http://linuxtoy.org/archives/java_chinese.html)。
