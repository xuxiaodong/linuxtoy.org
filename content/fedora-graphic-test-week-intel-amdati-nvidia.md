Title: Fedora 显卡驱动测试周：Intel,AMD/ATi 和 nVidia
Date: 2009-09-10 14:29
Author: lovenemesis
Category: Drivers
Tags: Fedora, graphic
Slug: fedora-graphic-test-week-intel-amdati-nvidia

近日， [Fedora QA 负责人 Adam Williamson 在
FedoraForum](http://forums.fedoraforum.org/showthread.php?t=229794)
宣布了本周的9号至11号为 Intel, AMD/ATi 和 nVidia
的显卡驱动测试日。由于本次测试的显卡驱动不仅对于预计12月初发布的 Fedora
12 意义重大，同时对于下一步的 Kernel 2.6.32 也具有重要影响，如他所言：
What's in Fedora's drivers today will be in everyone else's
tomorrow。在此希望诸位朋友多多参与测试。

**所有测试都可以通过为此定制的 Fedora Rawhide 免安装 LiveCD
完成，测试过程不会影响硬盘上已有的任何系统和文件。**

[AMD/ATi
测试详细说明](https://fedoraproject.org/wiki/Test_Day:2009-09-09_Radeon)

[nVidia
测试详细说明](https://fedoraproject.org/wiki/Test_Day:2009-09-10_Nouveau)

[Intel
测试详细说明](https://fedoraproject.org/wiki/Test_Day:2009-09-11_Intel)

**测试 LiveCD 下载：**

[Test LiveCD
i686](http://adamwill.fedorapeople.org/20090909_test_day_images/testday-20090909-i686.iso)
MD5SUM:4e09b55dcf898038d6959aa5893b3d35

[Test LiveCD
x86\_64](http://adamwill.fedorapeople.org/20090909_test_day_images/testday-20090909-x86_64.iso)
MD5SUM:6b1b617a7dd1ef42ee0cbb9fcd14a162

**注意：Live USB Bug**

目前有一个已知与 Dracut 有关的 Live USB Bug。当使用以上的 LiveCD 制作
LiveUSB 后，启动时会出现 *No root device found. Boot has failed,
sleeping forever.* 的错误提示。此时需要手动指定 Live USB root
分区卷标。在从 U 盘引导后出现 GRUB 界面时连续按两次 Tab
键，进入内核引导参数编辑模式，将 *root=* 区域修改成
*root=live:LABEL=(label)* ，其中 (label) 代表
U盘的卷标，之后回车即可开始引导。

一个简单的查看U盘卷标的方法是观察插入U盘后在 GNOME
桌面显示的U盘名称（默认会以卷标名称挂载）。比如本人U盘插入后在GNOME
桌面显示为 Thumb ，那么卷标名就是 Thumb 。
