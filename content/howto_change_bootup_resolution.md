Title: 如何更改引导屏幕的分辨率
Date: 2006-09-17 16:41
Author: toy
Category: Tutorials
Slug: howto_change_bootup_resolution

1.  打开 menu.list 文件
    `sudo vim /boot/grub/menu.lst`
2.  查找类似下列内容的行
    `kernel /boot/vmlinuz-2.6.15-26-386 root=/dev/hda5 ro quiet splash`
3.  在行尾追加 `vga=` 选项，如果所用为 16 位色的 1024x768
    分辨率，则让“vga=0x317”，具体数值可通过下表获取

        Colours   640x400 640x480 800x600 1024x768 1152x864 1280x1024 1600x1200
        --------+--------------------------------------------------------------
         4 bits |    ?       ?     0x302      ?        ?        ?         ?
         8 bits |  0x300   0x301   0x303    0x305    0x161    0x307     0x31C
        15 bits |    ?     0x310   0x313    0x316    0x162    0x319     0x31D
        16 bits |    ?     0x311   0x314    0x317    0x163    0x31A     0x31E
        24 bits |    ?     0x312   0x315    0x318      ?      0x31B     0x31F
        32 bits |    ?       ?       ?        ?      0x164      ?

    另外，0x317 本身是作为十六进制表示，换算成十进制为
    791，所以，以上参数也可用“vga=791”代替。

4.  保存更改，重启后生效。

（Via
[Ubuntuforums](http://ubuntuforums.org/showthread.php?p=1505142#post1505142),
thanks!）
