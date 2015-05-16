Title: 试用 FileZilla 3.0.0 beta1
Date: 2006-10-07 10:50
Author: toy
Category: Apps, FTP Client
Slug: try_filezilla_3_beta_1

[FileZilla](http://filezilla-project.org) 这个 FTP
客户端想来大家不会陌生，以前在 Windows
平台时，就没少用过它。现在，FileZilla 3 已经开始支持 Linux、MAC OS X
等系统，从而成为了一款真正跨平台的 FTP 传输软件。我只是针对正式发布的
[FileZilla 3.0.0
beta1](http://sourceforge.net/project/showfiles.php?group_id=21558&package_id=206762)
进行试用，你也可以尝试它的 [Nighly
builds](http://filezilla-project.org/nightly.php)
版，说不定会有新的发现哦。

[![filezilla](http://i.linuxtoy.org/i/filezilla_s.png)](http://i.linuxtoy.org/i/filezilla.png)

试用之后，个人认为 FileZilla 比较令人满意的地方主要有以下几个方面：

-   安装很简单。使用提供的 FileZilla 3 二进制包（注：FileZilla 提供了
    Windows、Debian Linux、OS X 和 FreeBSD
    等系统的二进制包），解开即可执行，不用担心安装依赖问题。
-   使用颇方便。FileZilla
    在界面操作上支持流行的双窗口，以及树状查看模式，无论是本地目录及文件，还是远程目录及文件，都一览无余。
-   快速连接及站点管理器。如果有需要马上连接的 FTP 站点，则可以使用
    FileZilla 所提供的快速连接工具直接连接到 FTP 站点。而 FileZilla
    的站点管理器能够把频繁使用的 FTP
    站点进行收集，并分类管理起来，为用户以后使用这些 FTP
    站点提供方便之门。
    [![filezilla site
    manager](http://i.linuxtoy.org/i/filezilla_site_manager_s.png)](http://i.linuxtoy.org/i/filezilla_site_manager.png)
-   远端命令执行器。FileZilla 包含一个执行远程服务器端 FTP
    命令的窗口，在此可以使用 FTP 命令执行相应操作。
    ![filezilla custom
    command](http://i.linuxtoy.org/i/filezilla_custom_command.png)
-   可视更改目录及文件属性。经常建站的朋友都知道，在安装某些 Web
    应用时，需要给目录及文件以可写或其他权限。FileZilla
    提供可视化的操作方式，来对目录及文件的权限进行更改。
    ![filezilla change file
    attributes](http://i.linuxtoy.org/i/filezilla_change_file_attributes.png)
-   此外，FileZilla
    所具有的目录列表过滤功能、默认的文件存在操作规则、动态更换远程服务器编码集（使中文支持无忧）、多线程传输及断点续传、工具栏自由切换各操作窗口等等，都很不错。

但当前 FileZilla 仍然需要不断加以改进：

-   由于 FileZilla 才刚刚开始公开测试，所以使用时需要承担潜在的 Bug
    所造成的风险。
-   站点管理器的数据需要与其他的 FTP
    客户端进行交换的话，导入／输出功能是必不可少的。
-   个人还希望在切换本地或远程目录时有一个书签功能，这样可以把经常使用的目录收藏起来。
-   遗憾的是，现在上传、下载尚不支持拖拉操作。这对已经习惯于傻瓜化操作的用户来说多少有些不便。
-   我发现在使用本地站点的地址栏时，支持自动补完功能，这点确实很方便。但同样的特性为什么不在远端的地址栏中也加以实现呢？

总结：如果在你所用的系统中缺少满意的 FTP 解决方案，FileZilla
是个不错的选择。但期待更加完善且好用的 FileZilla，仍需时日。
