Title: 全志 Allwinner A20 机顶盒刷入原生 Debian
Date: 2015-09-09 13:09:27
Authors: yang
Category: Tips
Tags: debian
Slug: allwinner-debian

花费 60 大洋购买了一台天敏电视精灵 3 安卓机顶盒。买来的目的就是为了刷入原生的 Debian 或其他发行版本。

<!-- PELICAN_END_SUMMARY -->

查看了一下具体的硬件：全志 Allwinner A20 双核 CPU，Cortex-A7 架构；内存 1G；闪存 4G；两个 USB，一个 HDMI，一个 AV。大体看了一下 Sunxi 的 Wiki，发现可以按照以下的办法来刷入。最好有一根 ttl 线来接入盒子的 UART 接口查看输出信息。

下面是操作步骤：

**第一部分：**

进入默认的安卓系统，通过 ttl，使用 root 账户直接挂载 nanda 分区，获取其中的 script.bin。如果你没有 ttl 线，可以先尝试用 adb 连接盒子，然后用 root 大师来获取 root 权限，之后顺序操作即可：先把盒子连接上 Wifi，然后 `adb connect IPADDRESS`，root。总之，就是为了获取 script.bin。

获取 script.bin方法：

    # mkdir /sdcard/nanda
    # mount -t vfat /dev/block/nanda /sdcard/nanda
    # exit
    # adb pull /sdcard/nanda/script.bin

取得 script.bin 后，如果要修改其中的节点，那么需要 sunxi-tools：

    # git clone https://github.com/linux-sunxi/sunxi-tools
    # make
    ./bin2fex script.bin script.fex

编辑 fex 文件，编辑后，重新生成二进制文件：

    ./fex2bin script.fex script.bin

script.bin 文件是 fex 文件的二进制实现，fex 文件定义 SoC 是如何工作的，它配置 GPIO 引脚并设置 DRAM、显示（如 HDMI、VGA、分辨率）等参数。

**第二部分：**

1、编译 uboot

这边的编译环境为 Linux version 3.16.0-4-686-pae (debian-kernel@lists.debian.org) (gcc version 4.8.4 (Debian 4.8.4-1) ) #1 SMP Debian 3.16.7-ckt11-1+deb8u3 (2015-08-04)，默认的编译工具为 gcc-arm-linux-gnueabihf，在“deb http://emdebian.org/tools/debian/ jessie main”源中可以找到。

因为我这边没有也找不到盒子的 uboot 源码，我尝试用了 cubieboard2 的 uboot 源码，编译后可以正常使用。

    git clone https://github.com/linux-sunxi/u-boot-sunxi -b wip/a20
    make cubieboard2 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf-

找一个 SD 卡，用来引导，全志盒子默认为 SD 卡引导。用 fdisk 给 SD 卡分两个区，第一个为 fat，第二个为 ext4 格式，具体不再赘述。按照我的是 sdb1、sdb2。

将编译好的 uboot 写入到 sdcard：

    # dd if=spl/sunxi-spl.bin of=/dev/sdb bs=1024 seek=8
    # dd if=u-boot.bin of=/dev/sdb bs=1024 seek=32

新建一个 boot.cmd 文件，输入以下内容：

    setenv bootargs console=ttyS0,115200 root=/dev/mmcblk0p2 rootwait
    panic=10 ${extra}
    fatload mmc 0 0x48000000 uImage
    bootm 0x48000000

使用 cmd 文件来生成 scr 文件：

    mkimage -C none -A arm -T script -d boot.cmd boot.scr 

2、编译内核

依旧使用 cubieboard2 的内核，因为我使用 Sunxi 的内核编译后无法启动，本人菜鸟折腾了几天没精力了。直接使用 cubieboard2 的内核可以启动，但是需要添加盒子的 PHY 网卡驱动。天敏电视精灵 3 的 PHY 为 ICplus 芯片。如下操作：

    # git clone https://github.com/cubieboard2/linux-sunxi
    # make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- sun7i_defconfig
    # make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig

进入 menuconfig 状态，添加 ICplus 网卡的支持：

    # make -j$(nproc) ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- uImage modules
    # make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- INSTALL_MOD_PATH=output modules_install

生成的内核和模块路径：

    arch/arm/boot/uImage
    output/lib/

制作 Debian rootfs：

    # debootstrap --verbose --arch=armhf --foreign jessie debian http://ftp.cn.debian.org/debian
    # cd debian
    # cp /usr/bin/qemu-arm-static usr/bin/
    # LC_ALL=C LANGUAGE=C LANG=C chroot . /debootstrap/debootstrap --second-stage
    # LC_ALL=C LANGUAGE=C LANG=C chroot . dpkg --configure -a

chroot 并部署 rootfs：

    passwd
    echo "a20" > etc/hostname
    echo "127.0.0.1 a20" >> etc/hostname
    echo T0:2345:respawn:/sbin/getty -L ttyS0 115200 vt100 >> etc/inittab
    echo deb http://ftp.cn.debian.org/debian/ jessie main contrib non-free > etc/apt/sources.list
    echo deb http://security.debian.org/ jessie/updates main contrib non-free >> etc/apt/sources.list
    apt-get update
    apt-get dist-upgrade
    apt-get install openssh-server
    apt-get install locales
    echo "en_US.UTF-8 UTF-8" > etc/locale.gen
    echo "zh_CN.UTF-8 UTF-8" >> etc/locale.gen
    locale-gen

需要修改 rootfs 下的两个文件 /etc/network/interfaces 和 /etc/ssh/sshd_config，开启静态 ip 地址和支持 root 登录。

所有的制作完成了，下面拷贝文件到 SD 卡相应分区：

拷贝到 sdb1 下的文件：

uImage script.bin boot.scr

然后将 Debian 的 rootfs 文件拷贝到 sdb2，内核模块拷贝到 /lib 下。

插入 SD 卡到盒子，通电后等待片刻即可用 ssh 登录盒子了，一个完整原生的 Debian 系统跑起来了。

目前先研究到这里，使用 /dev/fb0 应该可以继续启动 Xorg，跑跑 LXDE 应该没什么问题。

目前存在的问题：盒子上的两个 USB 接口无法使用！因为是套用的 cubieboard2 的源码和 uboot，具体到底是 script.bin 的缘故还是源码的缘故，我折腾了几天，依然搞不定。希望有精通嵌入式的朋友帮我看下能否解决该问题，谢谢大家！
