Title: Unarchiver: FREE RARv3 解压工具
Date: 2011-05-11 17:07
Author: lovenemesis
Category: File Manager
Tags: unar
Slug: unarchiver-free-rarv3-extraction-tools

今天，Free Software Foundation 宣布 RARv3 解压工具的开源实现 Unarchiver
完成。

[Unarchiver](http://code.google.com/p/theunarchiver/) 由 Dag Ågren
开发，是一款适用于 OS X 平台的开源多格式解压软件。其解压缩引擎核心
`lsar`(读取压缩文档) 和 `unar`(释放压缩文档) 支持包括 Linux 和 Windows
在内的多个平台。

unar 支持的[众多压缩文档格式（Zip, Tar, Gzip, Bzip2, 7-Zip, Rar, LhA,
StuffIt）中](http://code.google.com/p/theunarchiver/wiki/SupportedFormats)(甚至支持
NDS 格式)，就包含被 Free Software Foundation 列为高优先级自由软件实现的
RARv3 格式。

RARv3
是一种在媒体文件压缩中应用普遍的压缩文件格式，尤其常见于天朝地区，本人猜测与大量盗版
WinRAR 用户有密切关系。  
在 Linux
平台下，作者提供可以免费使用的命令行版本，一般可以在发行版的闭源软件仓库找到。

目前 `lsar` 和 `unar`
尚未被打包整合进绝大多数发行版，希望有志之士可以在这方面做出自己的贡献，将其和
Linux 平台下常见的图形化前端 File Roller 和 Ark 整合。

*消息来源：*[Free Software
Foundation](http://www.fsf.org/blogs/licensing/free-rarv3-extraction)
