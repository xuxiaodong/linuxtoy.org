Title: RPMFusion Testing 增加适用于 Fedora 10 的ATi fglrx 驱动(2009.1.21更新)
Date: 2008-12-30 10:48
Author: lovenemesis
Category: Drivers
Tags: Fedora, fglrx, rpmfusion
Slug: rpmfusion-testing-added-fglrx-for-fedora10-added-uninstall

使用 ATi 显卡的 Fedora 10 用户们终于在年末等来了 rpmfusinon 版本的 fglrx
而无需降级 libdrm。（2009年1月21日更新)目前已经结束 testing
状态，推荐各位朋友们使用。

以下内容翻译自
[FedoraForum](http://forums.fedoraforum.org/showthread.php?t=155503) 的
[leigh123@linux](http://forums.fedoraforum.org/member.php?u=78273)
大人最新修订的 Howto，有问题的话欢迎进入讨论。

1. 安装驱动  

`su - rpm -Uvh http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm yum install akmod-fglrx xorg-x11-drv-fglrx xorg-x11-drv-fglrx-libs.i386`
（译者注: fglrx 已经从 testing 移至 update 了）

2.编辑 xorg.conf  
首先调用ati显示配置做初步工作  
`su aticonfig --initial -f`  
然后手动编辑 xorg.conf  
`su gedit /etc/X11/xorg.conf`

添加以下字段：  
`Section "Extensions" Option "Composite" "Enable" EndSection`

`Section "ServerFlags" Option "AIGLX" "on" EndSection`

`Section "DRI" Mode 0666 EndSection`

然后在 Device 字段添加如下内容：  
`Option        "OpenGLOverlay" "off" Option      "VideoOverlay" "on"`

4.备份已有的 initrd
（译者注：这个文件记录了内核模块的位置信息，修改它是为了禁止载入已有的
radeon 驱动）  

`` su mv /boot/initrd-`uname -r`.img /boot/initrd-`uname -r`.img.backup ``

重新生成新的 initrd，使 radeon 模块不会被强行载入  
`` su mkinitrd -v /boot/initrd-`uname -r`.img  `uname -r` ``

5.编辑grub.conf  
`su gedit /boot/grub/grub.conf`  
在内核所在行的最后添加 `nopat`参数。  
可选：如果工作不正常的话再添加 `nomodeset` 参数。

6.重新启动计算机  
这步是必须的，否则fglrx的内核模块不会编译。

*翻译结束*

如果**严格参照**以上方法施行后 fglrx 工作异常，想要换回原先的开源驱动。  
目前 FedoraForum 上面的卸载方法还是针对老的需要降级 libdrm
的方式，新方式的 leigh123@linux 大人尚未更新。  
不过从以上安装过程来看，因为不涉及 libdrm
了，要简单的多，本人推测如下：  
1. 卸载 fglrx 包  
通过 yum remove 的方式清理掉安装的 rpm 包  
2. 依然使用 KMS 方式进行显示设定  
删除 /etc/X11/xorg.conf 文件，卸载 system-config-display
（这个保留也可以）。  
3.恢复之前的 initrd 文件  
使用之前备份的 initrd 文件  
mv /boot/initrd-`uname -r`.img.backup /boot/initrd-`uname -r`.img  
4. 取消无用的内核引导参数  
删除掉 /boot/grub/grub.conf 文件中内核行的 nopat 参数。

希望使用 ATi 显卡的朋友们积极尝试下，将结果反馈给
[FedoraForum](http://forums.fedoraforum.org/showthread.php?t=155503)
。顺便BS下 AMD 慢半拍的驱动开发速度……
