Title: GRUB 2 安装及配置笔记
Date: 2008-11-30 11:07
Author: toy
Category: Tutorials
Tags: Debian, GRUB
Slug: grub-2-installation-and-configuration

[作者/yjwork]

传说 GRUB 2 支持很多格式的背景，比如 JPEG、PND、TGA 等格式，支持 24
色，支持
800x600、1024x768，支持中文菜单显示。于是，受诱惑，安装了一下，但由于网上资料少，自己配置找的比较辛苦。不过还好，基本搞定了。写下来，做个笔记。

1.  安装 GRUB 2。我用的是 Debian Lenny，安装相当简单，直接执行：

    `apt-get install grub2`

    系统依赖装上 grub-pc 和 grub-common，安装过程中提示：

    GRUB upgrade scripts have detected a GRUB Legacy setup in
    /boot/grub.  
    In order to replace the Legacy version of GRUB in your system, it
    is  
    recommended that /boot/grub/menu.lst is adjusted to chainload GRUB
    2  
    from your existing GRUB Legacy setup. This step may be
    automaticaly  
    performed now.

    It's recommended that you accept chainloading GRUB 2 from menu.lst,
    and  
    verify that your new GRUB 2 setup is functional for you, before
    you  
    install it directly to your MBR (Master Boot Record).

    In either case, whenever you want GRUB 2 to be loaded directly from
    MBR,  
    you can do so by issuing (as root) the following command:  
    upgrade-from-grub-legacy

    ***小解释***：这个提示是说装 GRUB 2 时侦测到你有旧的 GRUB
    设置，系统将采用旧的设置来引导，新的 GRUB 2 暂时会成为旧 GRUB
    的一个项目引导，当你确定 GRUB 2 可以正常使用后，运行
    upgrade-from-grub-legacy，旧的 GRUB 会消失，只留 GRUB 2 的菜单。

    Chainload from menu.lst?

    将 GRUB 2 用旧的配置 menu.lst 引导？这里建议使用。

    The following Linux command line was extracted from the `kopt'
    parameter │  
    │ in GRUB Legacy's menu.lst. Please verify that it is correct, and
    modify  
    │ it if necessary.  
    │ Linux command line:  
    │ │

    这里不大了解，不过我是没输入任何东西自己确定的。

2.  安装完成后，重启。你会发现 GRUB 菜单有点不同了，上面有 GRUB 2
    的项目，在中间还有段提示，当你确定 GRUB 2 能正常使用后，使用
    upgrade-from-grub-legacy。不能引导的话，下面保留有原来的 GRUB
    设置，可以直接使用。
    使用 `upgrade-from-grub-legacy` 命令后，将删除原来的 menu.lst 项目。
3.  GRUB 2 的设置有所变化，不是原来的 menu.lst，而是
    /boot/grub/grub.cfg。
4.  看看 grub.cfg，学习下这个文件（注意，默认情况下 /boot/grub/grub.cfg
    为只读文件，修改的话，请先 `chmod +w /boot/grub/grub.cfg`）

    #  
    # DO NOT EDIT THIS FILE  
    #  
    # It is automatically generated by /usr/sbin/update-grub using
    templates  
    # from /etc/grub.d and settings from /etc/default/grub  
    #

    ### BEGIN /etc/grub.d/00\_header ###

    set default=0  
    #默认为 0，就是排第一个的项目。

    set timeout=5  
    #等待时间

    set root=(hd0,7)  
    #设置 root 分区

    search --fs-uuid --set 15d9bbc2-a1be-400c-883b-0b038a8174e0

    if font /usr/share/grub/ascii.pff ; then  
    #这里的 ascii.pff 为默认的字体，不支持中文，如果  
    #要中文支持，请改为 unicode.pff

    set gfxmode=1024x768 #默认为 640x480  
    #设置分辨率，这个建议跟你想设定的图片大小一致

    insmod gfxterm  
    #插入模块 gfxterm，当你前面设置为 unicode.pff
    后，这个终端支持中文显  
    #示，它还支持 24 位图像

    insmod vbe  
    #插入 vbe 模块，GRUB 2
    引入很多模块的东西，要使用它，需要在这里加入

    insmod png  
    #比如我们要想他显示 png 的图像做 GRUB 2 的背景，需要添加前面这行

    insmod jpeg  
    #添加 jpg 支持。在 /boot/grub 下可查看模块，带 .mod 的文件

    insmod tga  
    #如果要使用 tga 的图片做背景的话，gurb2-themes 里就是这种文件

    terminal gfxterm  
    #设置 GRUB 2 终端为 gfxterm

    background\_image /boot/grub/111.png  
    #设置背景图片

    fi

    ### END /etc/grub.d/00\_header ###

    ### BEGIN /etc/grub.d/05\_debian\_theme ###

    set menu\_color\_normal=cyan/blue  
    set menu\_color\_highlight=white/blue  
    #这两行为 Debian 下的菜单颜色设置，如果默认的话  
    #你会发现背景完全被蓝色挡住了，你需要修改 blue  
    #你可以改为 black，这样背景就会出现

    ### END /etc/grub.d/05\_debian\_theme ###

    ### BEGIN /etc/grub.d/10\_hurd ###

    ### END /etc/grub.d/10\_hurd ###

    ### BEGIN /etc/grub.d/10\_linux ###

    set root=(hd0,7)

    search --fs-uuid --set 15d9bbc2-a1be-400c-883b-0b038a8174e0

    menuentry "Debian GNU/Linux, linux 2.6.26-1-amd64" {

    linux /boot/vmlinuz-2.6.26-1-amd64
    root=UUID=15d9bbc2-a1be-400c-883b-0b038a8174e0 ro  
    initrd /boot/initrd.img-2.6.26-1-amd64

    }  
    #这里的 root=xxxx 也可以使用 /dev/hdax 来代替。  
    #当你的系统无法启动，而又不想打那么长的话。  
    #在 GRUB 2 启动时的命令行里，使用 (hd 加 tab 键可以看到分区和 uuid
    号

    menuentry "Debian GNU/Linux, linux 2.6.26-1-amd64 (single-user
    mode)" {

    linux /boot/vmlinuz-2.6.26-1-amd64
    root=UUID=15d9bbc2-a1be-400c-883b-0b038a8174e0 ro single  
    initrd /boot/initrd.img-2.6.26-1-amd64

    }  
    #默认的 GRUB 2 好像没添加 Windows 的项目，这样添加

    menuentry "启动 Windows"  
    #菜单名字  
    {

    set root=(hd0,1)  
    #设置 Windows 分区，这里要注意 GRUB 2 是硬盘从 0，分区从 1 开始

    chainloader +1  
    #原来的 GRUB 是 hd0,0 开始

    }

    ### END /etc/grub.d/10\_linux ###

    ### BEGIN /etc/grub.d/30\_os-prober ###

    ### END /etc/grub.d/30\_os-prober ###

    ### BEGIN /etc/grub.d/40\_custom ###

    # This file is an example on how to add custom entries

    ### END /etc/grub.d/40\_custom ###

5.  以上只是我在 Debian Lenny 上安装 GRUB 2 的一点心得，高中毕业，E
    文不太好，具体英文的话，可能理解有点偏差。如果哪里有错误，请指出，谢谢。

**更新**

增加截图如下：

[![GRUB
2](http://i.linuxtoy.org/images/2008/11/grub2-thumb.jpg)](http://i.linuxtoy.org/images/2008/11/grub2.jpg)  
*（点击可放大）*

使用手机拍摄，效果不好，只好拍个局部，请见谅。
