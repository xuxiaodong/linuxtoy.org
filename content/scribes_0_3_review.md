Title: Scribes 0.3 点评
Date: 2006-11-05 18:04
Author: toy
Category: Apps
Slug: scribes_0_3_review

[Scribes](http://scribes.sourceforge.net)
这个文本编辑器之前我曾作过[介绍](http://linuxtoy.org/archives/scribes.html)。最近，Scribes
在经历了连续三次的 beta 之后，于昨日推出了 0.3
正式版。今天我在本机编译了 Scribes
的最新版，并进行了短期的试用。感觉诚如作者所言，0.3
是一次具有里程碑意义的重要发布。Scribes 0.3 不仅仅是扫除了以往版本中的
bug，更是实现了诸多的新特性，而且还包括某些细节方面的增强和性能方面的优化。

-   编辑远程文件

    Scribes 现在可以直接通过 ssh、ftp、sftp、webdav、webdavs、samba
    等协议访问远程的文件，并执行编辑操作。这项新功能需要使用 Ctrl + l
    来激活。

    ![scribes ftp](http://i.linuxtoy.org/i/2006/11/scribes_ftp.png)

-   导入／输出模板

    Scribes
    的模板是类似代码片断的东西，使用模板能够减少很多重复的工作。新的
    Scribes 允许输出或者导入这些模板，以方便用户之间共享劳动成果。

    ![scribes
    template](http://i.linuxtoy.org/i/2006/11/scribes_template.png)

-   书签操作

    在 Scribes 中能够将某些行设置为书签，方便以后返回这些行。使用 Ctrl +
    d 来定义书签，而用 Ctrl + b 可以打开书签浏览器。

    ![scribes
    bookmark](http://i.linuxtoy.org/i/2006/11/scribes_bookmark.png)

-   文档切换

    有用户向 Scribes 的开发者提议考虑加入 Tab
    分页功能。虽然作者没有采纳，但是在新版本中增添了文档切换功能。在编辑多文档时，足可应付的了。文档切换窗口可以按
    F9 键打开。

    ![scribes
    document](http://i.linuxtoy.org/i/2006/11/scribes_document.png)

-   智能的自动完成
    虽然 Scribes
    之前的版本便已实现了这方面的功能，但是现在已经加强了改进。对于如
    []、{}、""、'' 等配对的符号，Scribes 会自动帮你完成。另外，在
    Scribes 中，重复的单词它也会帮你自动输入。
-   性能的优化
    Scribes 使用 Psyco 来优化程序的性能，减少内存占用上的不必要消耗。

总的说来，Scribes 0.3
在各个方面所作出的努力都是十分明显的。在灵活性、智能性、平滑性上都有所提升。对于仍然在使用
Scribes 0.2.x 的用户来说，升级是显得非常有必要的。但 Scribes
到底是否适合你，还得亲自试用一番才知道。
