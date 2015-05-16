Title: 在 Eee PC 上安装 Archlinux
Date: 2008-04-05 13:10
Author: toy
Category: Featured
Tags: Archlinux, Eee PC
Slug: installing-archlinux-on-eee-pc

新入手一台 Eee PC 701 版本，稍微把玩了下内置的 Linux
系统，感觉很一般，于是决定干掉它安装用惯了的
Archlinux，过程还算顺利，不过有些地方要提一下，以便其他 Eee PC
用户参考。

最基本的安装指南在这里：<http://wiki.archlinux.org/index.php/Installing_Arch_Linux_on_the_Asus_EEE_PC>

1：安装过程与一般电脑无异，不过最好用 ext2 文件系统，不要使用 swap，关闭
log（直接 daemon 里面 !syslog-ng 就可以了），加上 noatime 参数，也就是说
fstab 的 ／ 那行是这样的：

`/dev/sda1 / ext2 noatime 0 1`

2：安装结束后，先安装 dkite 的
eeemodules-2.6.22.9-1-i686.pkg.tar.gz，确保网卡工作正常，然后我强烈推荐使用
toofish 源里的 kerneleee，源地址是：  
` [eee] Server = http://code.toofishes.net/packages/eee`

然后 `pacman -Sy kernel-eee linux-uvc-eee-svn madwifi-ng-eee`

再编辑 /boot/grub/menu.lst，添加下面的启动项目：  

` # (2) Arch Linux title  Arch Linux EEE kernel root   (hd0,0) kernel /boot/vmlinuzeee root=/dev/sda1 ro`

重启后使用这个内核，网卡、摄像头都 ok 了，非常方便。

3：显卡驱动这块，推荐
`pacman -Sy synaptics xf86-video-intel`，如果你希望使用 Compiz
Fusion（顺便说句，Eee PC 跑 cf
非常流畅，没有任何问题），那么可以使用我的
[xorg.conf](http://cid-3aa064832e7aee2e.skydrive.live.com/self.aspx/public/xorg.conf)
文件，这是在自带 Linux 系统的 xorg.conf
基础上改的，经过实际使用，触摸板功能完整，显卡也能够正常驱动。

4：对于热键支持，推荐使用 ighea's acpi-eee（地址见安装指南，需要自己
makepkg 安装），这个 acpi 模块相对 dkite
的有几个好处，最棒的是可以自定义 osd
的位置，不至于像原版一样总是在左上角出现，此外，还支持在不同电源模式下掩上屏幕的不同动作，比如在电源模式下，关上屏幕盖板可以设定为无动作；而在电池模式下则是挂起到内存，非常方便！睡眠键也可以自行定义动作。

5：加快启动速度，因为用了
ssd，所以这小玩意的启动速度本来就很快，不过么人心不足，还可以从其他几个方面加快速度：首先，bios
打开 boot boost，这就不会有 asus 那破
logo，自检也大大加快；然后，使用上面所说的 kernel-eee，这个内核要比 arch
官方内核启动速度更快；最后，grub 干脆不要等待时间，设定为 0s，不要使用
dm，或者让 dm 自动登陆。这么折腾下来，开机到 Xfce 启动完成，能控制在 25
秒左右，应该说差不多是即开即用了：）。

其他的东西基本上 Wiki 那篇文章都有，有什么问题照着做就可以，Eee PC
的所有功能，包括热键、休眠、开关 wifi 什么的都可以被 Archlinux
完美支持，没注意过裸系统的大小，我装完全部应用软件，包括 Netbeans6
和永中 Office，内置 4G ssd 硬盘还剩下 600M 剩余空间 (pacman 的 cache
挪到 sd 卡上去了），还有安装软件的余地。

ps：劝败，这玩意不错，挺好玩的，虽然 7' 屏幕较小，一般应用足够，配上 2G
内存，速度令人满意，Netbeans 都跑得挺欢，关键是轻巧，相比 2kg 的 12'
本本，这个 900 克的小玩意好带太多了。

[撰文/Matri Ning]
