Title: StartUp Manager－Grub 启动管理器
Date: 2007-04-21 16:02
Author: toy
Category: Apps
Slug: startup-manager

大家知道，Grub 的配置文件在
/boot/grub/menu.lst。虽然文本配置文件有解释说明，但是编辑起来比较麻烦。如果对
Grub 不太了解的话，那么可以使用图形配置界面的
[SUM](http://web.telia.com/~u88005282/sum/)——StartUp Manager。

警告：此软件尚不稳定可能导致 Grub 损坏，不过已经在 Debian Etch、Ubuntu
及 Kubuntu（包括 Breezy、Dapper、Edgy 和 Feisty
等版本）下进行了测试。建议在修改之前备份原始的配置文件。

此程序的使用过程如下：

1.  下载：选择 .deb 包进行下载。
2.  安装：进入下载目录后执行：  
    `$ sudo aptitude install startupmanager_*_all.deb -y`

    aptitude 会自动解决包依赖问题。

    然后再执行：  
    `$ sudo aptitude install grub-splashimages`

    这将安装 Grub 的闪屏文件。

3.  使用：点击“系统 → 管理工具 → StartUp-Manager”菜单命令。

下面是 SUM 的使用截图：

[![SUM](http://i.linuxtoy.org/i/2007/04/sum1_s.png)](http://i.linuxtoy.org/i/2007/04/sum1.png)

[![SUM](http://i.linuxtoy.org/i/2007/04/sum2_s.png)](http://i.linuxtoy.org/i/2007/04/sum2.png)

[![SUM](http://i.linuxtoy.org/i/2007/04/sum3_s.png)](http://i.linuxtoy.org/i/2007/04/sum3.png)

[![SUM](http://i.linuxtoy.org/i/2007/04/sum4_s.png)](http://i.linuxtoy.org/i/2007/04/sum4.png)

Download [StartUp Manager
1.0.3](http://web.telia.com/~u88005282/sum/downloads.html)

[撰文/rainofchaos]
