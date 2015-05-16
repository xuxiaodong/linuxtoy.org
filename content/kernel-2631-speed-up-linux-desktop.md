Title: Kernel 2.6.31 - 加速 Linux 桌面
Date: 2009-09-07 14:11
Author: toy
Category: News
Tags: Kernel
Slug: kernel-2631-speed-up-linux-desktop

{ 文/Rodney Gedda 译/Shawn |  

[原文](http://www.techworld.com.au/article/317416/kernel\_2\_6\_31\_speed\_up\_linux\_desktop)
}

随着 Kernel 2.6.31 即将发布，Linux 桌面用户可以期待更快的速度，以及对
USB  
3.0 的支持和新版的 Firewire 驱动。

从 2.6.30 六月份发布以来，Kernel
开发者们一直致力于提高桌面的交互性能，特别  
是在内存使用存在压力的状况之下。

如果程序执行到的代码没有缓存在内存里，那就需要从硬盘里读出这部分程序，所以  

速度相对就慢了点，作为桌面程序则会让人感觉到一些延迟。但是，上一个版本的
Kernel 内存占用管  
理很容易导致上面所说情况的发生。据 Kernelnewbies.org 说，新的版本，加  
入了一些新的优化，使得从 active pages 列表中很难移出“mapped executable  

pages”。“这就意味着桌面使用效能的提升，内存使用紧张和错误会减少百分之五  
十，内存从硬盘读写会减少三分之一，在高内存占用时，X 桌面的响应会  
是原来速度的两倍。

更近一步的提高是，在百分之十缓存热读写的过程中，在文件服务的闪存效能的错  
误会从 50 降到 3。

Linux 最初的开发者，Linus
Torvalds，最初为自己的桌面而开发的操作系统很明显  
是作为 Unix 服务器的方式。但是近些年来，Linux 在台式机和笔记本的应用与  
Windows 相比仍然保持着一定的份额，并作为一个主流操作系统替代品的方式出  
现。现在有多少用户使用 Linux 桌面，各方的估计差别很大，据 Net  
Applications 在 2009 年五月的统计是百分之 1.17，但是到八月份却下降了
0.94。  
Windows 7
在十月份的上市会使这一份额继续下降。这对“企鹅”来说不是全部黯淡  
的，也不是完全光明的。但是随着 Kernel 内存管理，X.org
显示的发展，以及显卡驱  
动的更新和提高，GNOME 和 KDE 这两个主流桌面都在不断的提高 Linux
桌面的使用效  
率。

另外一个随着 2.6.31 而来的提升是 Kernel mode-setting 对 ATI Radeon
显卡的支  
持。

Kernel mode-setting 使得显示方式的初始化从 X server 的启动改变为 Kernel
的启  

动，于是无缝启动更加流畅并且使得更换用户更快捷。新版中并口的开发包括了最  
新的 USB 3.0 和最新的 Firewire 的支持。

英特尔已经开始了 USB 3.0 的开发，他把 xHCI 0.95 应用其中。USB
3.0，或者称之  
为超高速 USB，理论上数据传输是 4Gbps，目前还没有应用 xHCI 的硬件，但是
Kernel 的  
驱动已经在 Fresco Logic host controller prototype 做了测试。

对于 Firewire，2.6.31 提高了 fine-grained 进入的许可，IP
网络的新驱动，以  
及大于两个 TB 的 Firewire 硬盘的支持。

根据项目所介绍，“这已经不是实验性质的了，我们鼓励提供老的 ieee 1394
驱动的开  
发商应用新的驱动。”

最新的 Kernel 2.6.31-rc8 已于 8 月 28 日发布。

{ Thanks Shawn. }
