Title: 打造完美的 Linux 桌面 — Arch Linux 2007.08-2 (1)
Date: 2007-12-17 19:30
Author: toy
Category: Featured
Slug: the-perfect-linux-desktop-arch-linux-2007-08-2-1

本文详细描述 [Arch Linux](http://archlinux.org/) 2007.08-2
的安装过程，包括基本系统、X Window
System、桌面环境、中文支持、常用软件等等。通过此文，你将最终获得一个轻快、灵活、最新的完美
Linux 桌面。

### 为什么要选择 Arch Linux

我不是一个 Arch Linux 老手，使用 Arch Linux
我才不过一个月时间，但我已经喜欢上了这个很有个性的 Linux
发行版。为什么要选择 Arch Linux？我基于以下理由：

-   简单。Arch Linux 信奉的哲学是 KISS，即保持简单。安装和配置 Arch
    Linux 比我预想的要容易。Arch Linux
    的文件系统结构布局清晰，让人一目了然。
-   轻快。Arch Linux 为 i686
    进行优化，无论是系统的启动，还是运行程序，都感觉比较轻快。
-   灵活。不象其他的 Linux 发行版，为你默认安装一些不想要的东西。Arch
    Linux
    给你一个最基本的系统，是在此基础上搭积木，还是耍魔方，随你怎么玩。这体现了
    Arch Linux 的灵活。
-   保持最新。几乎每个人都有喜新厌旧的心理。Arch Linux
    总能尽快满足你及时获取最新的软件。
-   Pacman 和 ABS。Pacman 是 Arch Linux 的包管理工具，与 Apt-get
    类似，使用同样简单。ABS 作为 Arch Linux
    的编译系统，使程序从源代码编译是如此容易。Arch Linux 还包括 AUR，让
    Arch Linux 用户彼此分享各种流行的包。

### 安装 Arch Linux 基本系统

看到 Arch Linux
的优点，是不是有一种跃跃欲试想要马上安装的感觉？不要着急，在安装 Arch
Linux 之前，还有一些准备工作需要作：

-   备份数据。首先，你应该备份现有系统中的重要数据，以做到有备无患。
-   收集信息。有些硬件的信息应当提前进行收集，在后面的系统配置中将会用到。
-   选择映像。Arch Linux 当前最新版本是
    [2007.08-2](http://archlinux.org/download/)，包括 CORE 和 FTP 安装
    ISO 映像。你需要根据自己的实际情况进行选择，本文将以 CORE
    为例，从光盘进行安装。Arch Linux CORE ISO 映像文件大小为 158
    MB，下载后刻盘备用。

**使用光盘引导**

当使用 Arch Linux 安装光盘引导后，将出现以下画面：

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux01.png)

Arch Linux
提供几种不同的引导选项，你可根据自己需要选择。一般情况下，按回车即可。

**启动 Arch Linux 安装程序**

稍等片刻，Arch Linux 即引导进入这个画面：

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux02.png)

该画面包括一些有用的安装信息，如安装日志的记录、文档的查看、键盘映射的更改等。我们直接在命令提示符后输入下列指令，以便启动
Arch Linux 安装程序：

`/arch/setup`

**选择安装源**

在经过一段欢迎信息之后，我们将来到下一个画面：

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux04.png)

因为我们是从光盘直接安装，所以保留默认选择即可。如果你是从 FTP/HTTP
安装，那么可以选择第二项。

**准备硬盘**

接着，我们会进入 Arch Linux
的安装主菜单。首先是要求我们准备硬盘，即对硬盘分区和挂载文件系统。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux05.png)

1. 对硬盘分区

如果你的硬盘上什么也没有，那么可以选择 Arch Linux
安装程序的自动分区方案。不过，我们并不建议这样做。我们推荐在分区之前，根据自己的硬盘容量及实际需要来确定一个合理的分区方案。本文拟分四个区：

-   /boot：引导分区
-   swap：交换区
-   /：根分区
-   /home：用户目录区

现在，分区方案已经确定。因此，我们选择第二项进行手动分区。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux06.png)

Arch Linux
安装程序会自动检测硬盘类型及容量，要求你选择分区的硬盘，并带你进入硬盘分区程序
cfdisk。

根据我们确定的分区方案，按 Tab 切换到 New 上，创建第一个分区
sda1。然后，依次建立余下的分区。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux10.png)

分区创立完成后，我们还需要做两件事：

1\) 设置可引导标志。先选择 sda1，再切换到 Bootable 来完成。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux16.png)

2\) 保存创建的分区。通过切换到 Write 来写入分区。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux17.png)

最后，切换到 Quit 退出 cfdisk 分区程序。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux19.png)

2. 挂载文件系统

在建立分区后，选择 DONE 条目返回准备硬盘画面。接着，我们选择 Set
Filesystem Mountpoints 来将已建立的分区挂载到文件系统上。

Arch Linux 同样会自动检测硬盘容量，并首先要求你挂载 swap 区，我们选择
/dev/sda2。然后依次挂载 /、/boot 和 /home 区。与挂载 swap
区不同的是，挂载后几个分区会要求你选择一个文件系统类型。我们为 / 和
/home 选择 ext3，/boot 选择 ext2。你也可以选择其他的类型。另外，挂载
/boot 和 /home 时，需要自己输入挂载点，按原名输入即可。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux23.png)

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux26.png)

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux30.png)

完成后，返回 Arch Linux 安装程序主菜单。

**选择包**

接下来，我们进行第五项任务：选择要安装的包。Arch Linux
首先会要求选择安装介质，因为我们是从 CD-ROM
进行安装，所以保持默认。然后，我们选择 CD
驱动器，仍然默认。最后，选择包：

-   base：Arch Linux 中所包含的最基本的包。
-   devel：包含一些软件编译工具。
-   lib：包含应用程序所需的库文件。
-   support：包含一些在网络和文件系统方面有用的包。

我们将选择以上四个分类的包，使用空格键可以完成选择过程。当 Arch Linux
安装程序提示你是否默认选中所有的包时，按 Yes
后会进入具体的包选择画面。在此，你可以选择哪些包安装，哪些包不安装。完成后，按
OK 确认。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux45.png)

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux47.png)

**安装包**

在安装包前，Arch Linux 安装程序将提示你是否保存 Pacman 缓存，我们选择
No，即不保存 Pacman 缓存的包。Arch Linux
将花一会儿时间来安装你所选择的包，你可以稍微休息一下。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux52.png)

**配置系统**

现在，我们将进入 Arch Linux
安装过程中的一个重要环节，即配置系统文件。Arch Linux
安装程序先会询问是否使用 hwdetect，按推荐选择 Yes，并回答是否需要支持从
usb、firewire、pcmcia
等设备引导。之后，我们需要选择所用的文本编辑器，可选 nano 和
vim，我们选择后者。然后，我们就到了如下的配置画面：

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux66.png)

该画面包括需要配置的系统文件，主要有：

-   /etc/rc.conf
-   /etc/fstab
-   /etc/mkinitcpio.conf
-   /etc/mkinitcpio.d/kernel26-fallback.conf
-   /etc/modprobe.conf
-   /etc/resolv.conf
-   /etc/hosts
-   /etc/hosts.deny
-   /etc/hosts.allow
-   /etc/locale.gen

其中，有些配置文件可以暂时不管它，需要重点关注的是：

1. /etc/rc.conf

该文件中，你需要首先配置区域、时区、主机名、网络接口等内容。

1\) LOCALE

LOCALE 定义系统的语言，默认为
en\_US.utf8，即为英文。作为我们中文用户，可以将其设置为
zh\_CN.utf8。方法是，在进入 vim 编辑环境后，移动光标到该位置，按 i
进行编辑。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux67.png)

2\) TIMEZONE

TIMEZONE 设置你所在的时区，由于我在中国西部，所以将其设置为
Asia/Chongqing。中文用户还可以设置成 Asia/Shanghai。由你所在的位置决定。

3\) HOSTNAME

HOSTNAME 即设置主机名，我设置为 linuxtoy。

4\) INTERFACES

INTERFACES
这部分设置你的网络接口参数。因为我是通过路由连接上网，所以我将 eth0
设置为 dhcp，即通过 DHCP
获得网络地址。你需要根据自己的实际情况来修改这些参数。

在编辑完成后，按 :wq 保存并退出 vim 编辑环境。

2. /etc/fstab

该文件确定文件系统设置及挂载点，可以不用编辑，不过查看一下是否正确还是有必要的。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux68.png)

3. /etc/locale.gen

这个文件包含系统所支持的区域及字符集。对我们中文用户来说，你需要去掉包括
zh\_CN 这几行行首的注释符 #。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux76.png)

4. 设置 root 密码

为 root 帐号设置一个密码，需要重复输入以便确认。

5. 设置 Pacman 镜像

给 Pacman 包管理器设置镜像，选择较快的地址即可。

**安装引导程序**

系统配置完成后，回到主菜单。进入下一步，安装系统引导程序。我们选择 GRUB
条目。此时，Arch Linux 安装程序让你查看 /boot/grub/menu.lst
的内容。接着，要求选择安装的位置，我们选 MBR，即主引导记录，第一项。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux82.png)

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux85.png)

**退出安装**

还好，我们顺利完成了 Arch Linux
安装程序的所有步骤。现在是时候退出了。按提示我们在命令行输入下列指令，以便重启系统：

`reboot`

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux89.png)

**新建用户**

重启系统后，输入 root 帐号和密码登录系统。

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux90.png)

![Arch Linux
安装截图](http://i.linuxtoy.org/i/archlinux/archlinux91.png)

首先要做的一件事情是，建立一个普通的帐号。可以通过以下命令完成：

`useradd -m -s /bin/bash xiaodong`

这将添加一个名为 xiaodong 的用户。接着，为该帐号设置密码：

`passwd xiaodong`

至此，Arch Linux 的基本系统算是安装完成了。(待续)

[声明：本系列文章尚需完善，谢绝转载]
