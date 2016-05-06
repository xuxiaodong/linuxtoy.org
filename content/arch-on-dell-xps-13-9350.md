Title: Dell XPS 13 9350 安装 Arch Linux
Date: 2016-05-06 10:56:48
Authors: toy
Category: Tips
Tags: dell, archlinux
Slug: arch-on-dell-xps-13-9350
Via: Arch Linux|https://wiki.archlinux.org/index.php/Beginners%27_guide

拿到一台 Dell XPS 13 9350，在安装 Arch Linux 时总体顺利，但有一些小问题，在此记一下备忘。

<!-- PELICAN_END_SUMMARY -->

1. 制作引导优盘

    将下载的 Arch Linux ISO 镜像文件 archlinux-2016.05.01-dual.iso 校验无误后，使用 `dd` 写到优盘。因我的优盘在系统识别为 `/dev/sdb`，故其命令为：

        dd if=archlinux-2016.05.01-dual.iso of=/dev/sdb bs=4M status=progress && sync

2. 引导 Arch Linux

    在引导之前按 `F12` 进入 BIOS 设置，关掉 Secure Boot，否则会报找不到 loader.efi 的错误。同时，将 SATA Operation 设置为 AHCI，若不然则无法识别 SSD 磁盘。

3. 连接 WiFi

    当引导完毕进入 shell 后，执行以下命令来连接 WiFi：

        wifi-menu

4. 对磁盘分区

    鉴于 GPT 分区表比 MBR 更有优势，在此选择 UEFI/GPT 的引导及分区方案。使用 `parted` 可以对磁盘进行分区操作：

        parted /dev/nvme0n1

    先删掉原分区，然后根据需要创建新的分区。我的分区方案如下，第一个分区用于 UEFI 引导，第二个作为 / 分区，最后一个用于 /home。

        Device            Start       End   Sectors  Size Type
        /dev/nvme0n1p1     2048   1050623   1048576  512M EFI System
        /dev/nvme0n1p2  1050624  84934655  83884032   40G Linux filesystem
        /dev/nvme0n1p3 84934656 500117503 415182848  198G Linux filesystem

    创建完后别忘了将第一分区设置 boot 标志。

        mkpart ESP fat32 1MiB 513MiB
        set 1 boot on
        mkpart primary ext4 513MiB 40.5GiB
        mkpart primary ext4 40.5GiB 100%

5. 格式化分区

    分别将三个分区格式化需要的文件系统类型：

        mkfs.fat -F32 /dev/nvme0n1p1
        mkfs.ext4 /dev/nvme0n1p2
        mkfs.btrfs /dev/nvme0n1p3

    完成后再挂载：

        mount /dev/nvme0n1p2 /mnt
        mkdir -p /mnt/{boot,home}
        mount /dev/nvme0n1p1 /mnt/boot
        mount /dev/nvme0n1p3 /mnt/home

6. 安装基础包

    使用 `pacstrap` 脚本来安装基础系统：

        pacstrap -i /mnt base base-devel

7. 生成 fstab

    使用 `genfstab` 来生成 fstab 文件：

        genfstab -U /mnt >> /mnt/etc/fstab

8. chroot

    为了进行后续配置，需要 chroot：

        arch-chroot /mnt /bin/bash

9. 设置区域和时区

    从 `/etc/locale.gen` 选取需要的区域，去掉开头的注释即可，然后使用 `locale-gen` 来生成。同时，创建 `/etc/locale.conf` 文件，并将 `LANG` 设为跟所选区域一致。

    使用 `tzselect` 来设置时区。

10. 设置 hostname

    将 `/etc/hostname` 的内容设置为喜欢的主机名。

11. 安装引导程序

    这里选择使用 `systemd-boot` 来完成 UEFI 引导：

        bootctl install

    同时，创建 `/boot/loader/entries/arch.conf` 引导条目：

        title   Arch Linux
        linux   /vmlinuz-linux
        initrd  /initramfs-linux.img
        options root=PARTUUID=06d1a377-976d-47db-a907-9bf03bb8519b rootfstype=ext4 rw pcie_aspm=force i915.enable_rc6=7

    其中 PARTUUID 可通过 `blkid` 获得。

    另外，`/boot/loader/loader.conf` 包含内容为：

        timeout 3
        default arch

12. 设置 root 密码

    使用 `passwd` 来设置 root 密码。

13. 重启

    执行 `exit` 退出 chroot 环境，同时卸载分区并重启系统：

        umount -R /mnt
        reboot

14. 安装其它包及配置环境

    为了避免手动操作，我利用 Ansible 将安装各种常用软件及配置环境的过程自动化，只需执行：

        ansible-playbook site.yml

    可通过 GitHub 获取 [archstrap][a]。

[a]: https://github.com/xuxiaodong/archstrap
