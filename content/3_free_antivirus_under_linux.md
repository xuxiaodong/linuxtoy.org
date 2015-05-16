Title: 三款 Linux  下的免费桌面级杀毒软件
Date: 2008-10-08 23:05
Author: lovenemesis
Category: Apps, Featured
Tags: antivirus
Slug: 3_free_antivirus_under_linux

由于 Linux 良好的用户权限管理体系，病毒往往是 Linux
系统管理员最后才需要考虑的问题。以往，Linux
上的杀毒软件主要是为企业的邮件和文件服务器所设计的。如今，随着 Linux
桌面用户数量的增长，桌面用户在受益于 Linux
系统对病毒较强的天然免疫力的同时，也需要杀毒软件清理从网络或U盘带来的WIndows病毒。尽管那些病毒根本无法给
Linux 系统带来任何影响，但是阻止病毒的进一步传播，也未尝不是一件好事。

这里为大家介绍三款适用于桌面用户使用的杀毒软件。何谓“适合”？一个标准是可以免费使用，另一个标准是具有图形化操作界面。对于他们，将从安装配置、杀毒性能、图形界面三个项目进行简单的测试评分，每个单项最高5分。  
所有测试均在2008年10月7日系统更新后的 Fedora 9 i686\_PAE GNOME 2.22.3
上进行，病毒库也采用当天更新的。  

为避免由于图形界面实现方式差异带来的性能影响，杀毒测试均调用相应杀毒软件的命令行版本执行，递归扫描并扫描压缩文档，最后记录杀毒软件自身反馈的统计结果。  

杀毒效果测试一时选用的是笔者位于Ext3分区下存放个人文档的目录，该目录中包含了
JPEG/PNG 图片、MP3/OGG/WMA 音乐、DOC/ODT/TXT 文档、CHM/PDF
电子书、7Z/RAR/ZIP 压缩档案，共16.8G，无病毒。  

杀毒效果测试二时选用的是笔者位于Ext3分区下存放下载文件的目录，该目录中包含了
RPM/GZ/BZ2 软件包、EXE/MSI Windows可执行文件、MKV/RMVB/MP4/WMV电影、ISO
光盘镜像、7Z/RAR/ZIP 压缩档案，共17.6G，包含一个keygen。  

由于手头未有最新的病毒测试样本包，无法进行杀毒准确性测试。望有此样本的朋友与我联系，以便弥补这一遗憾。  
为更接近桌面用户的实际情况，图形界面测试全部以普通用户权限执行。

**[Avira AntiVir Personal - FREE
Antivirus](http://www.free-av.de/en/download/download_servers.php)**

Avira AntiVir Personal - FREE
是一款来自德国的免费杀毒软件，国内俗称“小红伞”，以较低的系统占用率著称。该产品的
Windows 版本陪伴笔者走过了将近10年的时光，所以完全转向 Linux
系统后我也一直选用它。 Avira 同时也是
[Dazuko](http://www.dazuko.org/indexold.shtml)
项目的创立者和赞助商，于是 Avira AntiVir Personal - FREE
也是本次参加评测的杀毒软件中惟一一款内置实时病毒检测的杀毒软件。做为一款商业软件，个人用户可以免费使用，安装完成后可以通过自动更新获得新的证书。

*安装配置：2分 － 体积庞大，无软件包方式，涉及手动编辑配置文件。*  
AntiVir Personal - FREE 的 Unix 版本支持32位 Linux / FreeBSD / OpenBSD
/ Solaris 操作系统，打包在一个45MB 大的 TAR.GZ 文件中，未提供 RPM/DEB
安装包。安装采用的是 Bash
脚本的方式，全英文，期间会提供关于实时病毒检测、邮件病毒提醒、更新代理服务器等配置向导，依照提示即可完成。尽管内置了实时病毒检测功能，但未包含
Dazuko 的源代码包，所以若要真正使用实时病毒检测功能，还需要另行下载
Dazuko 源代码包并编译成内核模块。安装后依据要求还需要添加 "-b
/usr/lib/AntiVir" 到 /etc/prelink.conf 文件中。另外还需将使用 AntiVir
Personal - FREE 的普通用户添加到新创建的 antivir 用户组中。

*杀毒性能：5分 － 杀毒速度最快，压缩文档支持较好。*

以下是 antivir 命令行版本信息。

    antivir -V
    7.8.1.34
    operating system: Linux (glibc 2.2)
    product version:  2.1.12-68
    engine version:   7.8.1.34
    packlib version:  7.6.1.7 (supports 34 formats)
    vdf version:      7.0.7.7

    product:          AntiVir Workstation
    key file:         hbedv.key
    registered user:  Avira AntiVir PersonalEdition Classic
    serial number:    0000149996-PXWSE-0001
    key expires:      01 Nov 2008
    run mode:         PERSONAL

    product:          AntiVir (command line scanner)
    key file:         hbedv.key
    registered user:  Avira AntiVir PersonalEdition Classic
    serial number:    0000149996-PXWSE-0001
    key expires:      01 Nov 2008
    run mode:         PERSONAL

以下是杀毒测试一统计结果。

    antivir -s -z
    ------ scan results ------
    directories:      285
    scanned files:     9440
    alerts:        0
    suspicious:        0
    scan time: 00:03:55
    --------------------------

以下是杀毒测试二统计结果。

    antivir -s -z
    ------ scan results ------
    directories:       41
    scanned files:   111809
    alerts:        1
    suspicious:        0
    repaired:        0
    deleted:        0
    renamed:        0
    quarantined:        0
    warnings:        2
    scan time: 00:15:59
    --------------------------

速度是最快的，同时对于RAR档案内的文件也能进行扫描。

*图形界面：1分 － 外表美观，无实际意义。*

[![](http://i.linuxtoy.org/i/2008/10/screenshot-antivir-unix-300x220.png)](http://i.linuxtoy.org/i/2008/10/screenshot-antivir-unix.png)

由于涉及到多个 Unix 分支系统， AntiVir Personal - FREE 的图形界面是采取
Java 方式实现的，所以要求至少 Sun JRE 1.4.2 。经测试 Fedora 9 预置的
OpenJDK 6 亦可运行。安装后 AntiVir Personal - FREE
并未在应用程序菜单中装创建启动器，所以图形界面需要打开终端使用
antivir-gui 命令启动。Java 实现的图形界面保持了和 Windows
版本一致精美的外观和操作方式，但是仅提供了基本的设置和扫描操作。其中更改的设置由于没有根用户权限是无法生效的，而扫描仅能选择扫描整个本地磁盘，无法指定具体某个目录，而且一但开始扫描就无法停止，只能通过系统监视器停止。类似的，更新病毒库操作由于没有根用户权限依然无法生效。估计这个图形界面的主要为了配合
Dazuko 的实时病毒监控而设计的，除此之外没什么用途。

**[Free avast! Linux Home
Edition](http://www.avast.com/eng/avast-for-linux-workstation.html)**

Free avast! Linux Home Edition 是一款来自捷克的免费杀毒软件，它的
Windows 版本因为较强的脱壳能力和精美的外表而著称。它的 Linux
版本采用于Windows版本相似的杀毒内核，自2003年起已经连续五年获得 VB100%
认证，可谓久负盛名。另外我发现 avast! PDA Edition 中竟然还有 Palm OS
平台的（只有30KB大！），足见
avast!杀毒内核的可移植性。做为一款商业软件，它的家庭版本也是可以免费使用的，但是需要每年通过注册的电子邮件获得新的证书。

*安装配置：4分 － 简单快速，每年更新证书稍显麻烦。*

Free avast! Linux Home Edition 提供32位 RPM/DEB/TAR.GZ 三种安装形式，约
11
MB。在笔者的系统下使用RPM包安装十分方便，下载完成后直接双击即可，除了GTK2
外没有特殊的依赖关系，之后会在应用程序菜单中找到相应的启动器。首次运行时会询问你证书，此时需要通过[官方网站](http://www.avast.com/eng/home-registration.php)注册，并在邮箱中找到你的证书，将其复制至此即可。整个过程中并未涉及更新用代理服务器的内容。

*杀毒性能：4分 － 速度一般，压缩档案支持很好。*

以下是 avast 命令行版本信息。

    avast -V
    avast: avast v1.0.8
    VPS: 081007-0 (date: 07.10.2008)
    Copyright(C) 2003-2007. ALWIL Software. All rights reserved.

以下是杀毒测试一统计结果。

    avast -t A
    #
    # Statistics:
    #
    # scanned files:    10654
    # scanned directories:  285
    # infected files:   0
    # total file size:  22.7 GB
    # virus database:   081007-0 07.10.2008
    # test elapsed:     13m:13s 438ms
    #

以下是杀毒测试二统计结果。

    avast -t A
    #
    # Statistics:
    #
    # scanned files:    120009
    # scanned directories:  41
    # infected files:   11
    # total file size:  25.2 GB
    # virus database:   081007-0 07.10.2008
    # test elapsed:     59m:50s 318ms
    #

扫描速度只能说一般，但是avast!解压缩能力是相当出众，对于多种 EXE
加壳手段都能检测出来。不过也因此导致了含有大量压缩档案的测试二用时较长。

*图形界面：4分 － 简洁明快，功能丰富*

[![](http://i.linuxtoy.org/i/2008/10/screenshot-avast-antivirus-261x300.png)](http://i.linuxtoy.org/i/2008/10/screenshot-avast-antivirus.png)

Free avast! Linux Home Edition 虽然没有保持 Windows
版本精美的操作界面，但是在简洁的外观下蕴涵了最为丰富的功能。包括排除目录、邮件提醒、报告格式等全部设置都可以在图形界面下完成，遗憾的是没有更新代理服务器的设置。值得一提的是
Free avast! Linux Home Edition
提供了本地的病毒百科全书，方便用户查阅。在图形界面下可以进行病毒库更新、查看日志、设置隔离区的操作，对于桌面用户来讲十分方便。病毒扫描也可以选择多个不同的目录，并且可以方便在快速、标准、深入三种方式中切换，也可以自由选择是否扫描压缩档案。按下F1可以打开内置帮助，采用的是GTK2的帮助组件。惟一遗憾的是目前还没有中文版本。

**[ClamTk Virus Scanner](http://clamtk.sourceforge.net/)**

ClamTk Virus Scanner 是著名的开放源代码杀毒软件 ClamAV
的图形前端，采用的是 GTK2-Perl
脚本制作，可以在32位/64位系统上运行。ClamTk Virus Scanner
同样是一款开放源代码，所以可以在包括商业公司、盈利机构等在内的任何场所免费使用。与采用KDE组件构造的
[Klamav](http://klamav.sourceforge.net/klamavwiki/index.php/Main_Page)
相比，ClamTK 更适合以 GNOME 为桌面环境的用户。

*安装配置：3分 － 依赖较多，涉及手动编辑配置文件。*

ClamTk Virus Scanner 提供了适合于多个发行版的软件包，包括
Debian、Fedora、CentOS、SuSE、Mandriva，印象中也被包含在Ubuntu
的资源仓库里，只有大约97KB，十分小巧。本人下载好适合 Fedora 的 RPM
包后双击开始安装，由于需要 ClamAV 和 GTK2-Perl 较多，又安装了共 21M
的相关支持包。安装过后需要注释掉 /etc/freshclam.conf 文件中的 Example
标示行才能更新病毒库。关于代理服务器和更新镜像的设置也只能手动修改配置文件完成。

*杀毒性能：2分 － 速度缓慢，压缩文档支持一般。*

以下是 clamscan 版本信息。

    clamscan -V
    ClamAV 0.93.3/8387/Tue Oct  7 23:37:07 2008

以下是杀毒测试一统计结果。

    clamscan -r
    ----------- SCAN SUMMARY -----------
    Known viruses: 438891
    Engine version: 0.93.3
    Scanned directories: 285
    Scanned files: 8360
    Infected files: 1
    Data scanned: 10691.21 MB
    Time: 1713.473 sec (28 m 33 s)

以下是杀毒测试二统计结果。

    clamscan -r
    ----------- SCAN SUMMARY -----------
    Known viruses: 438891
    Engine version: 0.93.3
    Scanned directories: 41
    Scanned files: 654
    Infected files: 1
    Data scanned: 2179.51 MB
    Time: 562.355 sec (9 m 22 s)

速度慢的出奇，很难想象这个还是和本地 Glibc
连接优化过的程序。在测试一中出现误报的情况。由于无法处理 RAR
格式的压缩档案，clamscan 会直接跳过测试二中大量的 RAR
档案，于是用时会比其余两款要短。

*图形界面：4分 － 美观，支持右键杀毒，充分本地化。*

[![](http://i.linuxtoy.org/i/2008/10/screenshot-clamtk-virus-scanner-300x189.png)](http://i.linuxtoy.org/i/2008/10/screenshot-clamtk-virus-scanner.png)

ClamTk Virus Scanner 充分发挥了开放源代码软件的优势，它的图形化界面与的
GNOME
风格协调统一，可以正确使用全局设置中图标集和字体。安装后不仅会在应用程序菜单汇中创建启动器，还会和
Nautilus
文件管理器集成，添加右键杀毒功能，十分方便。除此之外，还可以通过快捷键快速切换
ClamTk Virus Scanner
提供的各种设置选项。遗憾的是，由于权限设置问题，普通用户不能使用图形化方式更新病毒库（不知此瑕疵可否通过把普通用户添加到clamav用户组中解决）。感谢
Tao Wei 和 Aron Xu 两位翻译者，ClamTk Virus Scanner 中文化非常的高。

**总结**

经过之上的简单测试，**个人意见**：Avira AntiVir Personal - FREE
适合在意扫描速度和各种高级功能的技术性用户使用，但是憋足的图形化界面会严重影响桌面用户的接受度。ClamTk
Virus Scanner
做为开放源代码软件，体现了其与其他程序的高度协同性，而且拥有最好的中文本地化界面，但是其所用后端ClamAV的扫描准确度和速度需要改善(ClamAV
已经更新到 0.94 版本了，本文未采用由于 Fedora
仓库尚未更新到此版本)。相比之下，Free avast! Linux Home Edition
以其简单的安装和完备的图形化界面更容易征服 Linux 初学者的心，而连续五年
VB100% 的成绩也足以证明其的确具有强大的实力。

所以，**Free avast! Linux Home Edition** 获得本次 Linux
免费桌面级杀毒软件推荐奖(Toy奖？哎呦，番茄飞啊飞……)～

**PS:**关于 Linux
下到底有没有必要杀毒软件的问题，我只能说尚未见过没有杀毒软件的 Linux
邮件服务器。对于桌面用户来言，是不是有必要就看个人需要了。反正 Linux
下的杀毒软件又不带实时病毒检测功能，安装下来也就10MB左右，装一个完全不影响系统性能。另外对于双系统的用户来言，在
Linux 下查杀 Windows 分区的病毒是个很明智的手段。

强调一点，**Linux
不是完全对病毒免疫**，[这个链接](http://en.wikipedia.org/wiki/List_of_Linux_computer_viruses)指向了维基百科上关于
Linux 系统病毒的内容。
