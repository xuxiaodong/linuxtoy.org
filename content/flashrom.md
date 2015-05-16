Title: 使用 Flashrom 在 Linux 下备份或刷写 BIOS
Date: 2009-01-22 11:33
Author: toy
Category: Apps, Featured
Tags: BIOS, Flashrom
Slug: flashrom

Flashrom 这款工具来自于 [Coreboot](http://www.coreboot.org/)
项目（即著名的 LinuxBIOS）。借助该工具，我们可以在 Linux
下轻松、方便的备份或刷写 BIOS。

**安装 Flashrom**

在使用 Flashrom 之前，首先你需要安装它。目前，一些流行的 Linux
发行版都可以通过自身的包管理器来安装 Flashrom。例如，Debian/Ubuntu
用户可执行如下命令：

`$ sudo apt-get install flashrom`

Fedora 用户需执行：

`$ sudo yum install flashrom`

如果你不能通过所使用 Linux 发行版的包管理器安装
Flashrom，那么可选择手动编译安装。只需执行以下命令：  

` $ svn co svn://coreboot.org/repos/trunk/util/flashrom $ cd flashrom $ make $ sudo make install`

注意，你将需要编译工具、Subversion、依赖包 pciutils 和 zlib 等东东。

**Flashrom 用法**

除了通过 [Flashrom 官方主页](http://www.coreboot.org/Flashrom)查询
Flashrom 是否支持你目前的主板、芯片之外，你也可以直接使用 Flashrom
工具来检测。使用 root 用户权限执行 `flashrom` 指令后，Flashrom
将输出类似下面的信息：

    Calibrating delay loop... OK.
    No coreboot table found.
    Found chipset "Intel ICH7/ICH7R", enabling flash write... OK.
    Found chip "Winbond W39V040B" (512 KB) at physical address 0xfff80000.
    No operations were specified.

如果你想把当前的 BIOS 映像备份下来，那么可执行：

`# flashrom -r bios_image.bin`

同样的，Flashrom 也将提供输出信息供参考：

    Calibrating delay loop... OK.
    No coreboot table found.
    Found chipset "Intel ICH7/ICH7R", enabling flash write... OK.
    Found chip "Winbond W39V040B" (512 KB) at physical address 0xfff80000.
    Reading flash... done.

刷写新的 BIOS 则可以执行：

`# flashrom -wv new_bios.bin`

某些芯片驱动需要先擦除后方能正常写入：

`# flashrom -E`

**警告：刷写 BIOS
是一项危险的操作，除非你清楚的知道自己在干什么，否则请勿轻易尝试。**

[Flashrom](http://www.coreboot.org/Flashrom)
