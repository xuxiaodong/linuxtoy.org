Title: 调校 Nook GlowLight Plus 电子书阅读器 (1)
Date: 2016-04-11 21:41:35
Authors: toy
Category: Tips
Tags: nook
Slug: nook-glowlight-plus-1

关注 Twitter 的朋友可能知道去年底我入了一台电子书阅读设备 [Nook GlowLight Plus][n]。这款设备由书商 Barnes & Noble（巴诺）出品，经过调校后我颇为喜欢，时至今日已用它看了不少好书，中文英文皆有。最近稍为得闲，遂把调校过程记述如下，兴许对他人或有帮助也说不定。

<!-- PELICAN_END_SUMMARY -->

[![chinese]({filename}/images/chinese.thumb.png)]({filename}/images/chinese.png)[![input]({filename}/images/input.thumb.png)]({filename}/images/input.png)

Nook GlowLight Plus（下称“NGP”）为 6 寸 300 PPI 高清 E Ink 屏（支持 1080 x 1430 分辨率），带背光，能防水。可能有朋友会问为会啥不选 Kindle？毕竟当下它最为流行。除了硬件方面的原因之外，NGP 支持开放的 ePub 电子书格式，搭载的 Android 4.4 系统经 Root 后非常具有可玩性。经过权衡，NGP 最终获胜。

正所谓世上没有完美的设备，可惜 NGP 毕竟主要面向的是西文读者，所以对于中文的支持就比较糟糕。没有英汉字典，也没有中文输入法，对 ePub 的中文支持也是乏善可陈。好在 Android 系统本身并没有这些问题，只要动动手其实不难解决。

在接下来的这一系列文章中，我将介绍如何 Root NGP、制作英汉字典、安装中文输入法、以及对 ePub 添加中文多字体支持等内容。

**Root 过程**

1. 开启 USB 调试模式

   进入 Settings &rarr; ABOUT &rarr; Software，连续快点 N 图标三次将展开详细设置选项。之后点击 Development Options，开启 Developer options 并勾选 USB debugging 即可。

   [![software]({filename}/images/software.thumb.png)]({filename}/images/software.png)[![devel]({filename}/images/devel.thumb.png)]({filename}/images/devel.png)
   [![usb]({filename}/images/usbdebug.thumb.png)]({filename}/images/usbdebug.png)

2. 将 NGP 与电脑相连

   通过执行命令 `adb devices` 确认连接，此时将显示 NGP 的序列号。

3. [下载 Root 脚本][r]

   在解包后，直接执行：

        unzip rootGLP-3.zip
        chmod a+x rootnook.sh
        ./rootnook.sh

   脚本输出如下：

        push: files/supolicy -> /data/local/tmp/.nookrooter/supolicy
        push: files/su -> /data/local/tmp/.nookrooter/su
        push: files/libsupol.so -> /data/local/tmp/.nookrooter/libsupol.so
        push: files/install-recovery.sh -> /data/local/tmp/.nookrooter/install-recovery.sh
        push: files/eu.chainfire.supersu_preferences.xml -> /data/local/tmp/.nookrooter/eu.chainfire.supersu_preferences.xml
        push: files/eu.chainfire.supersu.apk -> /data/local/tmp/.nookrooter/eu.chainfire.supersu.apk
        push: files/doroot.sh -> /data/local/tmp/.nookrooter/doroot.sh
        push: files/busybox -> /data/local/tmp/.nookrooter/busybox
        push: files/adbd -> /data/local/tmp/.nookrooter/adbd
        9 files pushed. 0 files skipped.
        1229 KB/s (7413987 bytes in 5.886s)
                pkg: /data/local/tmp/.nookrooter/eu.chainfire.supersu.apk
        Success

        Restarting adbd as root... 
        Rooted.

   Root 过程利用了 Android 4.4 的 [Vold ASEC][v] 漏洞，由此添加并更改了一些系统文件以及安装了 SuperSu 程序。

   [![supersu]({filename}/images/supersu.thumb.png)]({filename}/images/supersu.png)

此时，通过 `adb shell` 连接后，执行 `su` 按提示授权便得到了具有 root 权限的 shell。

    shell@ntx_6sl:/ $ su
    root@ntx_6sl:/ # 

[n]: http://www.barnesandnoble.com/w/nook-glowlight-plus-barnes-noble/1122314015
[r]: http://forum.xda-developers.com/showpost.php?p=64191791&postcount=153
[v]: http://retme.net/index.php/2014/10/08/vold-asec.html
