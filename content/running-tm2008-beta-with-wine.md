Title: Linux 下使用 Wine 安装运行 TM2008 Beta 及乱码、与 Windows 共享聊天记录等相关问题的解决
Date: 2008-12-08 18:10
Author: toy
Category: Tips
Tags: Wine
Slug: running-tm2008-beta-with-wine

[撰文/[Rainux](http://www.rainux.org/)]

**前言**

腾讯已经发布了官方的 QQ for Linux，虽然有很多问题，例如没有 amd64
版本，功能太弱，聊天记录格式与 Windows 下的 QQ/TM
格式不一致等等，但无疑是 Linux 里使用 QQ/TM
最简单的方案。如果它已经能满足你的需求了，那么不必浪费时间看本文。

**精简版本**

如果你没时间看我唠叨，精简的版本是：TM2008 Beta 运行需要 Unicode 版本的
IE6、rpcrt4.dll、Visual C++ 2005 SP1 运行库，安装程序需要
GDI+。不可以使用
[IEs4Linux](http://www.tatanka.com.br/ies4linux/page/Main_Page)，因为它安装的
IE6 及相关运行库是 Win9x 的 ANSI 版本。必须使用 CrossOver Games 里的
[rpcrt4.dll](http://www.rainux.org/stuff/rpcrt4.dll.gz)，然后用
[winetricks](http://www.kegel.com/wine/winetricks) 安装 msxml3 gdiplus
riched20 riched30 ie6 vcrun6 vcrun2005sp1 即可安装运行 TM2008 Beta。

**详细版本**

只看精简版没搞定？请看详细的（唠叨的）版本：

安装 Wine，运行一下 winecfg，让它生成一个干净的 ~/.wine
目录。如果要使用已有的 ~/.wine，请先将其备份。同时确保 winecfg 里设置的
Windows 版本至少是 Windows 2000（我用的是 Wine 1.x 默认的 Windows XP）。

获取一份 CrossOver Games 里的
[rpcrt4.dll](http://www.rainux.org/stuff/rpcrt4.dll.gz)，将其复制为
~/.wine/drive\_c/windows/system32/rpcrt4.dll（覆盖已有的文件），运行
winecfg，在 Libraries -> DLL Overrides 里将 rpcrt4 设置为 Native
(Windows)。

下载 [winetricks](http://www.kegel.com/wine/winetricks)，使用它安装 IE6
和一些重要的运行库。如果这个过程失败，删除 ~/.wine（或者恢复备份的
~/.wine）并从头再来。

`sh winetricks msxml3 gdiplus riched20 riched30 ie6 vcrun6 vcrun2005sp1`

此时如果你有 Windows 上安装好的
TM2008，它已经可以运行了，但是无法登录，会提示“网络连接失败，请检查网络。”。所以还是老老实实用安装程序装一次吧。这里有个很莫名的问题，如果直接使用
Wine 运行 TM2008
安装程序，它很可能会直接崩溃，看不到任何图形界面的提示。而使用 Wine
运行一个其它的程序，例如 cmd.exe 或者 Total
Commander，再用这个程序去启动 TM2008 安装程序则不会有任何问题。

**中文乱码（空心方框）问题**

好吧，终于看到 TM2008
的安装界面了，不过很可能你又会头大了——所有的中文全是空心方框。原因是安装程序界面的字体是被指定为
Tahoma 的，而实际上 Tahoma 字体并不包括中文字符。有两个办法解决，都是
Windows 的技术，把 Tahoma
字体替换成某个中文字体，或者把某个中文字体链接到 Tahoma
上。照这两个片段修改
~/.wine/system.reg，只需要其中一个。别忘了把中文字体名改成你自己需要的。

[Software\\\\Microsoft\\\\Windows
NT\\\\CurrentVersion\\\\FontSubstitutes]  
"MS Shell Dlg"="Microsoft YaHei"  
"MS Shell Dlg 2"="Microsoft YaHei"  
"Tahoma"="Microsoft YaHei"

[Software\\\\Microsoft\\\\Windows
NT\\\\CurrentVersion\\\\FontLink\\\\SystemLink]  
"Tahoma"=str(7):"SimSun.TTC,SimSun\\0"

最后还必须把你改的中文字体文件符号链接到 ~/.wine/drive\_c/windows/Fonts
目录下，不这么做其它软件都没问题，就 QQ 或 TM 会乱码，该死的硬编码。

**查看聊天记录时的性能问题**

好了，现在不会有什么问题阻挡你了，TM2008 Beta
安装和启动都非常顺利，使用也很稳定。甚至 QQ2009 Preview4
都可以安装并启动，不过使用时很容易崩溃。但是如果你像我这样疯狂地保存了七八年的聊天记录，你会发现：

-   每次启动 TM2008 后第一次给任何人发消息都会导致 TM2008 失去响应将近
    20
    秒钟，之后继续发消息则不会有问题。第一次接收到某人的消息也会同样如此。
-   任何试图查看聊天记录的操作都会导致 TM2008 消耗 100% CPU
    并且很长时间没有反应，等待足够长的时间后才可以看到聊天记录。

这是由于 TM2008 的聊天记录数据库使用了 Windows 的 Structured Storage
技术，而其 API 库 ole32.dll 的 Wine
实现还不完善或者可能性能太低。虽然可以用 winetricks 安装 dcom98
来获取一个 Win9x 的 ANSI 版本的 ole32.dll，但它没法让 Unicode 版本的
TM2008 运行起来。搜遍了网络也找不到在 Wine 里使用 Win2k 以上系统的
ole32.dll
的方法。没办法，为了保持聊天记录的一致性，只有两个选择。要么不在 Linux
里看聊天记录；要么把聊天记录数据库 Msg2.0.db 备份并从 QQ Profile
目录（我的文档\\QQ Files\\QQ 号码）里删除，让 TM2008 自己生成一个空白的
Msg2.0.db，暂时抛弃历史包袱，以后再到 Windows
下把新的记录导出为备份文件后合并到老的数据库里。

**与 Windows 共享聊天记录**

如果你还像我这样偶尔会切换到 Windows，希望跟 Windows 下的 TM2008
共享聊天记录数据库，那么有两个办法：

-   直接在 Linux 里使用 [ntfs-3g](http://www.ntfs-3g.org/) 读写存放
    TM2008 聊天记录的 NTFS 分区。虽然 ntfs-3g
    已经号称非常稳定可靠了，但对于聊天记录这种极度个人化的数据我还是宁可保守一些。
-   创建一个 ext2 分区用来和 Windows 共享数据，在 Windows 下可以用 [Ext2
    IFS](http://www.fs-driver.org/) 驱动来访问它。比起私有文件系统 NTFS
    的 Linux 版开源驱动来说，当然是开源的 ext2 文件系统的 Windows
    版驱动更值得信赖。

用这两种办法都需要在 Linux 和 Windows 里创建 QQ Files
目录的符号链接，Linux 里不必说，ln -s 即可。Windows Vista
以前的版本可以用
[Junction](http://technet.microsoft.com/en-us/sysinternals/bb896768.aspx)
来创建 NTFS 上的符号链接，Windows Vista 可以用自带的 MKLINK。

对于我这种非笔记本用户来说使用日志文件系统来抵御意外断电是必须的。按照
Ext2 IFS 的 FAQ，它也可以读写 ext3 分区。不过比较新的 Linux 发行版的
mkfs.ext3 创建的 ext3 分区 Ext2 IFS 是无法访问的，可能是 ext3
文件系统格式发生了变化。而 Windows 下一些分区工具如 Paragon Partition
Manager 或 Acronis Disk Director 创建的 ext3 分区则没有问题。

**参考资料**

-   [Howto: Office 2007 on Linux with
    Wine](http://mediakey.dk/~cc/howto-office-2007-on-linux-with-wine/)
-   [Microsoft Office 2007
    Update](http://www.wine-reviews.net/microsoft/microsoft-office-2007-update.html)

[[原文连接](http://www.rainux.org/2008/12/08/240)]
