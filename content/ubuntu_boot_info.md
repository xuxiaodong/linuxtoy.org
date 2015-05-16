Title: Ubuntu 引导信息的显示
Date: 2006-10-29 11:51
Author: toy
Category: Tutorials
Slug: ubuntu_boot_info

最近升级到 Ubuntu 6.10
后，发现开机引导系统时只有屏幕图像，没有显示引导的文本信息了。表面上看，似乎更加简单了。但对于需要了解
Ubuntu 引导过程的话，就显得不够方便。以下提示可以让 Ubuntu
在引导时重新显示文本信息。

方法是编辑 `/boot/grub/menu.lst` 文件，将包含 kernel 那行中的 quiet
去掉就可以了。比如，在我的系统中，修改之前为：  

`kernel /vmlinuz-2.6.17-10-386 root=UUID=af1ddd4e-df24-4f75-8fe9-12771182dddc ro quiet splash vga=791`

修改后是这个样子：  

`kernel /vmlinuz-2.6.17-10-386 root=UUID=af1ddd4e-df24-4f75-8fe9-12771182dddc ro splash vga=791`

重启系统可以看到修改后的效果。注意在修改之前备份。

查了一点资料，原来这个 quiet 参数的作用是阻止输出所有正常的文本信息。

(via [Ubuntu
Forums](http://ubuntuforums.org/showthread.php?t=286971&goto=newpost),
thanks!)
