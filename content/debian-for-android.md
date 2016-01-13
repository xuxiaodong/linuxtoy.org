Title: 安卓设备运行原生 Debian（非 chroot）
Date: 2016-01-13 18:44:42
Authors: yang
Category: Tips
Tags: debian
Slug: debian-for-android

最近在折腾安卓盒子的过程中发现，通过修改安卓内核的 initramfs 文件，添加一个自己的 BusyBox 来 switch\_root 进入 Debian 是可行的。而且在 BusyBox 下就可以直接 `insmod *.ko` 内核模块了，所以驱动不是问题。如此，则市面上大部分安卓设备都可以原生运行 Debian 系统了？

<!-- PELICAN_END_SUMMARY -->

原理：利用安卓内核来引导 Debian 的 rootfs。

拆解与打包 boot.img。

boot.img 包含了 zImage 和 initramfs 等文件，现在需要修改 initramfs 来 switch\_root 进入 Debian。

利用 mkbootimg 和 unpackbootimg：<https://github.com/osm0sis/mkbootimg>

编译后，先提取安卓默认 boot.img：

    dd if=/dev/block/nandX of=boot.img

拆分：

    unpackbootimg boot.img

会提取出若干文件。

制作自己的 initramfs：

    mkdir initramfs
    cd initramfs

创建一个 init 文件：

    #!/bin/sh
    mkdir -p /root
    mkdir -p /proc
    mkdir -p /sys
    mkdir -p /dev
    mkdir -p /tmp
    mount -t proc none /proc
    mount -t sysfs none /sys
    mount -t ramfs none /dev
    mount -t tmpfs none /tmp
    insmod /ko/disp.ko
    insmod /ko/lcd.ko
    insmod /ko/hdmi.ko
    insmod /ko/nand.ko
    insmod /ko/gpio-sunxi.ko
    insmod /ko/ump.ko
    insmod /ko/mali.ko
    insmod /ko/videobuf-core.ko
    insmod /ko/videobuf-dma-contig.ko
    insmod /ko/uvcvideo.ko
    insmod /ko/rtl8150.ko
    echo /sbin/mdev > /proc/sys/kernel/hotplug
    mdev -s

    echo -e "Waiting 5 seconds for removable devices to stablize"
    i=0
    while [ $i -lt 5 ]; do
        sleep 1
        echo -n "."
        i=$(($i+1))
    done
    echo
    blkid | grep 4cc77658-b809-4894-b6a7-c5f15d8b00fe > /tmp/mountdev

    #/bin/sh
    mount $(cat /tmp/mountdev | cut -d ':' -f 1) -o noatime,nodiratime /root
    exec switch_root /root /sbin/init

这里 4cc77658-b809-4894-b6a7-c5f15d8b00fe 为 rootfs 设备的 UUID。

    chmod u+x init

编译 BusyBox（不再赘述）。

将编译好的 BusyBox 目录拷贝到 initramfs 下，进行打包：

    find . | cpio -H newc -o > ../initramfs.cpio.gz

重新制作 boot.img

    mkbootimg --base 0x00200000 --kernel zImage --ramdisk initramfs.cpio.gz -o my-boot.img

`--base` 为解包后查看里面的 base 参数。

以上只是一个大体的架构步骤，具体到某些盒子可能不太一样，另外要准备好 ttl 线以便查看引导错误。如此，一个陈旧的、吃灰的安卓盒子可以跑原生的 Debian 系统，然后随意使用 apt 来安装自己的服务当小型服务器来用了，何乐不为？而且目前市面上的安卓盒子内存基本都是 1G 左右，功耗且低，在家里跑服务是非常不错的。
