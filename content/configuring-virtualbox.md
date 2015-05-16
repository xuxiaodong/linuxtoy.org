Title: VirtualBox 中共享文件夹的设置
Date: 2007-05-23 21:12
Author: toy
Category: Tips
Slug: configuring-virtualbox

如果你需要从 VirtualBox
的客户机中使用主机里面的文件，那么通过共享文件夹的方式可以达成此目的。就以我的实际情况为例（VirtualBox
主机为 Linux，客户机为 Windows XP），说说设置的过程。

1.  在 VirtualBox 的主机（即 Linux 系统中）执行下列命令：

    `VBoxManage sharedfolder add "VM name" -name "sharename" -hostpath "\test"`

    该命令中的 VM name 指定要使用共享文件夹的虚拟机名称，如
    WinXP；sharename 为共享的文件夹名称，可任意设置，如
    sharedfolder；\\test
    为主机上需要共享的文件夹。下面给出一个该命令的实例：

    `VBoxManage sharedfolder add "WinXP" -name "downloads" -hostpath "\home\xu\downloads"`

2.  启动虚拟机（本例为 Windows XP），点击开始菜单中的“运行”，并输入
    cmd，然后执行以下指令：

    `net use x: \\vboxsvr\sharename`

    这个指令中的 x: 为映射的驱动器符号；sharename
    为上一步中所设置的共享文件夹名称。同样，我们给出一个实例供参考：

    `net use Z: \\vboxsvr\downloads`

    在命令成功执行后，通过资源管理器你便可以使用共享文件夹中的所有文件了。

    ![VirtualBox Shared
    Folder](http://i.linuxtoy.org/i/2007/05/vbox-sharedfolder.png)

在配置共享文件夹时，有几点需要注意：一是在配置时，不能开启或挂起虚拟机；二是要为客户机安装
VirtualBox Guest Additions 程序；三是共享文件夹只能用于 Windows 2000/XP
和 Linux 2.4/2.6 的客户机中。

另外，如果你的 VirtualBox 主机为 Windows，客户机为
Linux，也可按此法配置。不同的是，在执行第二个步骤时换成 mount 即可。

**更新**

Huahua 提供了一个 GUI 工具，可以很方便的为 VirtualBox
虚拟机设置共享文件夹。在安装之后，敲入 `VBoxSharedfolder`
即可打开如下图所示的设置对话框。

[![VirtualBox
Sharedfolder](http://i.linuxtoy.org/i/2007/05/vbox-sharedfolder-gui_s.png)](http://i.linuxtoy.org/i/2007/05/vbox-sharedfolder-gui.png)

你可以从[这儿下载](http://forum.ubuntu.org.cn/viewtopic.php?t=41759)该
GUI 工具。
