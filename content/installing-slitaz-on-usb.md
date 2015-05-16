Title: 在 U 盘上安装 slitaz 系统
Date: 2008-09-25 13:38
Author: toy
Category: Tips
Tags: SliTaz
Slug: installing-slitaz-on-usb

[撰文/ideal]

slitaz是一个非常小的linux发行版（使用了BusyBox)。可以方便的装在U盘上。

然后就可以在其他机器上启动啦。

台湾的penk对其进行了改进，加入了中文输入法（不过好像是繁体的）。

下载地址：<ftp://mirror.nttu.edu.tw/livecd/PUD/slitaz/slitaz.tw-04222008.iso>

首先保证U盘上已经装了个grub。没有的话可以马上装一个。

在U盘上建个boot文件夹，然后在boot下建个grub文件夹，把/boot/grub下的文件复制到U盘上相应的位置。

进入grub的命令行（在shell中输入grub，或者开机进入grub是按c），然后setup(fd0)就可以了。（fd0根据实际情况修改，使用TAB键提示。）

然后把slitaz的那个iso的文件解压出来放到U盘上（可以在U盘上建个文件夹，如slitaz，然后把解压出来的文件放到这个文件夹下），然后修改menu.lst，加入如下内容（假定解压的文件放在slitaz下）：  

` title        SliTaz GNU/Linux kernel    /slitaz/boot/bzImage root=/dev/ram0 vga=771 ramdisk_size=100000 initrd      /slitaz/boot/rootfs.gz`

保存，重启，选择从U盘启动即可。
