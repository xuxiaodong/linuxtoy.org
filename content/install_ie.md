Title: 在 Ubuntu 中安装 Internet Explorer
Date: 2006-08-06 20:55
Author: toy
Category: Tutorials
Slug: install_ie

在 Ubuntu 中安装 Internet Explorer 很麻烦？试试 IEs 4 Linux
吧，使用它，只需简单回答几个问题就可以了。

[![IE](http://i.linuxtoy.org/i/ie_s.png)](http://i.linuxtoy.org/i/ie.png)

**1.安装准备**

目前，要在 Ubuntu 中运行 IE，Wine 是免不了的。所以，你需要首先安装
Wine。另外，在使用 IEs 4 Linux 过程中，会用到 cabextract
这个解包小工具。安装指令如下：

`sudo apt-get install wine cabextract`

**2.安装 IE**

在下载
[IEs4Linux](http://www.tatanka.com.br/ies4linux/downloads/ies4linux-2.0.tar.gz)
后，使用 `tar xvzf ies4linux-2.0.tar.gz` 解包。然后，运行脚本
`./ies4linux`。

(1)IE 6 will be installed automatically.Do you want to install IE 5.5
SP2 too? [ y / n ]

如果你不需要安装 IE 5.5 SP2，则选“n”。

(2)And do you want to install IE 5.01 SP2? [ y / n ]

询问是否安装 IE 5.01 SP2。默认为“n"。

(3)IEs can be installed using one of the following locales:  
　　EN-US PT-BR DE FR ES IT NL SV JA KO NO  
　　DA CN TW FI PL HU AR HE CS PT RU EL TR  
　　Default is EN-US. Hit enter to keep it or choose a different one:

此处，输入“CN”，以便安装 IE 中文版。

(4)By default, I will install everything at /home/xxd/.ies4linux  
　　I will also install Flash 9 plugin and create Desktop shortcuts.  
　　Is that ok for you? (To configure advanced options type n) [ y / n
]

默认是安装在 /home/user/.ies4linux 中，同时安装 Flash 9
插件，并在桌面上创建快捷方式，按“y”继续。

现在，安装程序会自动连接到 Microsoft
的网站下载所需文件，请耐心等候。假如看到“IEs 4 Linux installations
finished!”，就说明 IE 已经成功安装了。
