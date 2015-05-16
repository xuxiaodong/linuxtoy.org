Title: locate 和 find：两个查找文件的命令
Date: 2007-02-09 15:49
Author: toy
Category: Tutorials
Slug: locate-and-find

对于初次切换到 Linux
系统的朋友来说，如果想要从命令行界面执行查找文件的任务的话，那么，locate
和 find
是两个需要了解的命令。虽说这两个命令都可以满足查找文件的操作，不过却是各有所长，在选择上不妨兼而用之。

1.  locate：该命令在运行时需要后台索引的数据库作为支撑，在 Ubuntu
    中这个数据库文件位于
    /var/cache/locate/locatedb。一般来说，这个数据库文件每天是通过 cron
    自动更新的。如果不幸没有得到更新，那么可以执行 `sudo updatedb`
    来手动更新。
    假如我想要在系统中查找一个名为 linux.html
    的文件，那么可以这样执行命令：`locate linux.html`。locate
    搜索文件的速度很快，一会儿就会把结果列出来。locate
    有一个十分有用的选项 -r，它可以让你在搜索文件时使用正则表达式。
2.  find：这是另一个 Linux 系统中重要的文件查找命令。find
    命令的功能很强大，其一般使用方法为：`find 位置 -name 文件名称`。例如，我要在
    / 这个根目录中查找 linux.html 文件，可以执行
    `find / -name linux.html`。你除了可以按文件名称来使用 find
    查找文件外，也可以根据文件大小（通过 -size n
    选项指定）、时间（如 -atime n 表示查找 n
    天前访问过的文件）来搜索文件。
    此外，find 命令同样支持在搜索文件时使用正则表达式，你只需指定 -regex
    选项即可。

值得注意的是，对于 locate 与 find
这两个命令的解说远非这篇小文所能满足。关于这两个命令的更加详细的用法，你可能需要通过
man locate 或 man find 查询。
