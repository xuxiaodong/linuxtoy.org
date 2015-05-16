Title: 清理 Ubuntu 系统的 5 个提示
Date: 2007-02-01 22:47
Author: toy
Category: Tips
Slug: 5-tips-for-cleaning-up-ubuntu

岁末将至，为了辞旧迎新，进行大扫除总是应该的。对于爱机而言，经过一年的辛苦工作，是否也到了该清理的时候呢？如果你是一位
Ubuntu 系统用户，那么以下介绍的 5 个提示，可能会对你有所帮助。

提示 1：清理残余的配置文件

一般而言，当我们从 Ubuntu
系统中删除了一个软件之后，该软件的残余配置文件并没有被删除。如果你确信以后不再使用该软件，那么保留其配置文件实在没有必要，所以我们大可一并删除之。

要删除某个软件的残余配置文件，可以执行下面的操作：

1.  在终端中执行 `sudo synaptic`，以便启动 Synaptic 包管理工具。
2.  点击 Synaptic 右下角的 Status 按钮进行切换。
3.  现在，你应该能够在 Synaptic 的左边看到 Not installed (residual
    config)。选择它即可在右边看到包含有残余配置文件的包，你可以在此选择删除该包。

提示 2：清理下载的缓存包

我们在 Ubuntu 中通过 `sudo apt-get install`
安装软件时，其下载的包都缓存在 /var/cache/apt/archives/
目录中。如果要清理掉这些已下载的缓存包，那么可以执行命令：  
`sudo apt-get autoclean`  
`sudo apt-get clean`

提示 3：清理不再需要的包

我们知道，在 Ubuntu
系统中安装软件时，该软件的依赖通常也会自动安装上。那么，在我们删除该软件后，其依赖可能需要我们手动删除之。你可以运行
`sudo apt-get autoremove` 命令来解决这个问题。

提示 4：清理无用的语言文件

Ubuntu 与其他 Linux
发行版一样，是一个支持多语言界面的系统。其实，对使用自己母语的我们来说，通常保留中文即可，你也可以保留自己所需要使用的语言，如英文。其他的语言文件于我们而言则没有必要保留。

为了清理这些无用的语言文件，你需要在 Ubuntu 系统中安装一个名为
localepurge 的小工具。你可以从本站读到 [localepurge
这个工具的具体用法](http://linuxtoy.org/archives/localepurge.html)。

提示 5：清理无用的翻译内容

你可以使用 trans-purge 这组小工具来清理 *.desktop、mime-database、gconf
schema
中的无用翻译内容。该[工具组的详细使用](http://linuxtoy.org/archives/trans_purge.html)本站同样曾经介绍过。

经过这一系列的清理之后，不仅可以节省大量的硬盘占用空间，而且能够使
Ubuntu 系统获得更加快速的运行效率。何乐而不为呢？
