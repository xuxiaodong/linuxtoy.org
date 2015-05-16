Title: 使用 Gobby 协作文本编辑
Date: 2006-11-11 12:12
Author: toy
Category: Apps
Tags: Gobby
Slug: collaborative_text_editing_with_gobby

随着网络的逐渐发展，多人协同工作的模式正在变得越来越流行。从某种程度上说，这正是利用网络的便利优势的最好体现。作为需要通过网络来协作的朋友，恐怕不仅仅是具备即时通讯软件就能够满足的。有时候，面对大量的文本、代码交流，即时通讯工具显得十分有限。在这个意义上，[Gobby](http://darcs.0x539.de)
这个协作文本编辑中的佼佼者将弥补上述方面的不足。

**Gobby 简介**

基于 Gobby
在多人协作方面的定位，不仅可以通过它完成多文档的文本编辑任务，而且协同工作的用户也能够使用它进行互相交流。

[![Gobby for
Linux](http://i.linuxtoy.org/i/2006/11/gobby_s.png)](http://i.linuxtoy.org/i/2006/11/gobby.png)  
Gobby 在 Linux 上

**Gobby 的主要特性**

1.  跨平台。Gobby 能够在 Linux、Mac OS X、Windows、以及其他的 UNIX
    等系统上运行。这就保证了无论用户身处什么系统环境，都可以圆满地进行协同工作。
2.  保密性。Gobby
    在实时协作时通过加密的通道传输信息，这样确保了用户的数据内容安全。同时，Gobby
    也支持对会话进行加密保护。
3.  易用性。Gobby
    支持多文档的编辑，能够直接拖拉操作，在请求时同步文档。另外，也支持
    Zeroconf 和 Unicode。
4.  身份标识。每个参与协作的用户都可以设置自己的身份标识颜色，以此来达到区分用户的目的。
5.  聊天风格。Gobby 具有类似 IRC
    一样的聊天风格，与编码最大程度的保持一致。
6.  语法着色。在 Gobby 中编辑文本时，支持大多数程序语言的语法着色显示。

**Gobby 的安装及使用**

Gobby 的最新稳定版为 0.4.1。在 Linux 中的安装以 Ubuntu
为例，只需在终端中输入 `sudo apt-get install gobby` 指令即可。其他的
Linux 系统可以参见 Gobby
网站上的[安装指南](http://darcs.0x539.de/trac/obby/cgi-bin/trac.cgi/wiki/InstallationGuide)。Windows
系统需要在安装 [GTK +](http://gladewin32.sourceforge.net) 和
[GTKMM](http://www.pcpm.ucl.ac.be/~gustin/win32_ports/binaries/gtkmm-runtime-2.8.8-2.exe)
这两个运行环境之后，再下载 Gobby 的二进制文件来完成整个安装过程。Mac OS
X 系统可通过 DarwinPorts 方式来安装 Gobby。

在使用 Gobby 时，首先需要一方创建
Session，然后另一方再加入该会话，就可以开始协作过程了。Gobby
的使用并不复杂，相信通过短暂的摸索就可以上手。

[![Gobby for
Windows](http://i.linuxtoy.org/i/2006/11/gobby_win_s.png)](http://i.linuxtoy.org/i/2006/11/gobby_win.png)  
Gobby 在 Windows 上

附：[Gobby
的下载页面](http://darcs.0x539.de/trac/obby/cgi-bin/trac.cgi/wiki/Download)。
