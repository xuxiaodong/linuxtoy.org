Title: mp3tagiconv
Date: 2010-08-04 06:04
Author: lovenemesis
Category: Music Player
Tags: id3, MP3
Slug: mp3tagiconv

目前 Linux 中的 mp3 标签处理工具虽能使 MP3 文件在 Linux
中被正确识别，但由于以 ID3v1 标签写入方式不对，致使其无法被 Windows 及
Windows  
Media Player 识别，导致在 Windows 资源管理器中无法正确显示 mp3
文件的中文标签。

惟一可能正确处理中文标签的
easytag，不能在多种文本编码中猜测，且不适于用写脚本进行大批量处理，而且要正确写入编码需要配置的，默认设置不行。*感谢
Chen Xing 来稿*

这个小工具，mp3tagiconv，可以方便地处理MP3文件的标签（主要面向中英文），使其在Linux和Windows的多数软件中都不会出现乱码。代码托管在
[Google  
Code](http://code.google.com/p/mp3tagiconv) 上。

程序基于 mutagen 使用 python 语言写成，系统安装了 mutagen
后程序即可直接运行。使用方法简单，如：

`mp3tagiconv 一个或多个MP3文件路径`

程序不会影响编码已经完全正确的文件。

为了避免破坏文件，默认情况下在修改标签前会先把解码后的标签显示出来，待用户确定。

与 mid3iconv 的不同：

1.  写 id3v1 时默认使用 gbk 而非 latin-1 编码，确保其可被 Windows Media
    Player 识别。
2.  读标签时综合 ID3v1 和 ID3v2，避免丢失标签中的信息
3.  处理标签时可猜测 mp3 文件现在使用的编码
4.  默认不写文件，避免误操作

程序在我自己的很多MP3文件上正常，但没有做太大规模的测试，如果大家感兴趣，可以帮忙测试一下~

*PS：*
[MP3乱码问题的详细背景](http://www.linux-wiki.cn/index.php/Mp3%E6%A0%87%E7%AD%BE%E4%B9%B1%E7%A0%81%E9%97%AE%E9%A2%98%E5%88%86%E6%9E%90%E4%B8%8E%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
。

以Wiki模式创建Linux中文文档，欢迎加入 [Linux
Wiki](http://www.linux-wiki.cn/) 。
