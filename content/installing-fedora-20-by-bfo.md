Title: 使用 BFO 方式安装 Fedora 20
Date: 2013-12-27 13:14
Author: lovenemesis
Category: Tutorials
Tags: Fedora
Slug: installing-fedora-20-by-bfo

你是不是还在使用传统的下载-安装的方式进行 Fedora
的安装呢？是不是觉得每次下载不仅花费时间，而且镜像文件还占用了不少硬盘空间（虽说目前主流配置都是
T
级别的）呢？下面为你介绍一种长久以来低调存在，但非常高效的安装方法：BFO。*感谢
[tiansworld](https://fedoraproject.org/wiki/User:Tiansworld) 来稿*

**什么是 BFO？**

BFO 即
[boot.fedoraproject.org](http://boot.fedoraproject.org)，是一种能够引导主机，通过网络进行安装或运行其它介质的方式。它与
`pxeboot `环境的工作方式很像。详细介绍可以[参考官方说明](http://boot.fedoraproject.org)。

**怎样使用 BFO？**

BFO 拥有提供了用于分别能够用于 DVD/CD、U 盘、软盘和 lkrn
镜像的文件。文件体积非常的小，因此老式小容量的 U
盘便可胜任。点击[此下载各种介质引导文件](http://boot.fedoraproject.org/en/download)。

以 U 盘版本为例，在下载对应的 U 盘版本镜像 (`bfo.usb`) 后，可使用 DD
命令将镜像写至 U 盘。

`>dd if=/pathto/bfo.usb of=/dev/sdb`

其中 *pathto* 是下载的 `bfo.usb` 文件所处的目录。 `/dev/sdb`
是你要使用的 U 盘设备名。  
写好之后，便可以使用它来安装 Fedora 了。

**通过 BFO 安装 Fedora**

**前提**：计算机能够连接到稳定的互联网；计算机可以从 U
盘、光盘、软盘等引导，并可将引导顺序设为这些设备优先。

以下还是以 U 盘为例：

1.  插入 U 盘，开机。正常情况下，你会看到如图 1
    的界面，再此之后会出现类似图 2 的界面（如果你不幸的只看到黑屏
    `boot：` 那也不要着急，请看后文）。
2.  选择
    `Install currently supported Fedora releases`，然后回车，这时你会看到如图
    3 一样的目前仍受支持的 Fedora
    发行版列表。在这里，你可以直接选择你要安装的 Fedora
    版本，然后回车，此后将进入 Fedora 的安装过程，如图 5,6。
3.  当然你也可以在选中要安装的版本后，按 Tab
    键，显示或编辑选项。在这里可以将预设的内核、内核镜像、源的地址改为其它你需要的地址。比如可以修改为速度更快的源地址。同时也可以加上
    kickstart 文件的路径，以便实现自动化安装。

前面说如果你不幸只看到黑屏 **boot:**
提示符，那么只要在提示符后面输入这些内容然后回车就可以了。这种情况下最好要有耐心，同时还要仔细，因为不小心输入错误，就需要完全重新输入。你也许会说，这么长串的东西，谁会记得住呢！其实这里面并不复杂，只是三个
URL 而已。第一个是 `vmlinuz` 所在的位置，第二个是 `initrd.img`
的位置，还有一个是 `repo` 的位置。这三个 URL
一般都指向一个源，因此也不是特别复杂。当然出现黑屏 `boot:`
提示符的机率并不大。

后面的过程就是 Fedora 的安装过程了，无需多说。

**总结**

BFO
安装方式总体简单方便，省去下载文件的时间。由于它依赖网络，因此对于网络状况良好的环境值得使用。对于网络较差的环境，则可根据情况，适当减少初次安装的软件包，以缩短安装时间。在完成安装后再使用包管理程序陆续安装其它软件包。

**配图**

[![bfo\_1](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_1.png)](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_1.png)

图片一

[![bfo\_2](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_2.png)](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_2.png)

图片二

[![bfo\_3](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_3.png)](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_3.png)

图片三

[![bfo\_4](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_4.png)](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_4.png)

图片四

[![bfo\_5](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_5.png)](http://lt-file.b0.upaiyun.com/files/2013/12/bfo_5.png)

图片五
