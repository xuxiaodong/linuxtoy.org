Title: 短信息：Radeon 开源驱动支持相关
Date: 2014-08-26 13:33
Author: lovenemesis
Category: Drivers
Tags: AMD, radeon
Slug: briefing-radeon-oss-driver-support-related

短消息三则，均与 Radeon 开源驱动的支持硬件相关。

老用户们，使用 **初代 UVD 的 R600 系列显卡亦可以通过 VDPAU
实现硬件解码**了，支持的设备包括 HD 3000 系列独立显卡、HD 3000 及 HD4200
系列的集成显卡、基于 RV770 核心的 HD 4800
系列显卡。所需支持的代码已经提交，不过由于已经过了 Kernel 3.17
的窗口，需要等到 3.18
版本才能合并入主线。值得注意的是，由于硬件局限，早期版本无法实现 VDPAU
与 OpenGL 的互操作性（部分播放器字幕及 OSD
显示要求此）。[原邮件列表](http://lists.freedesktop.org/archives/dri-devel/2014-August/066738.html)
[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTc3MTc)

壕们，**R9 290 Hawaii
现在终于可以在开源驱动下跑了**，不过性能由于频率调整部分尚未完善，还欠佳。在此之前
R9 290 仅能使用闭源 Catalyst
驱动，开源驱动完全无法启动。由于尚未完善，R9 290
开源驱动在有限的测试中有的力压 HD 7950，有的则还不如 HD 5770。拥有此卡的
Linux 不妨留心即将发布的 Mesa10.3。
[消息来源](http://www.phoronix.com/scan.php?page=article&item=amd_290_opens#=1)

展望未来，**HSA 异构计算架构的 Linux
平台开源支持将在今年内完成**，该实现在用户态还将同时支持开源 Radeon
及闭源 Catalyst 驱动。届时配合 Kaveri 架构的 APU
即可实现异构计算。此外，Radeon 开源驱动团队也在考虑邀请 OpenCL
组的成员协助加快开源 radeon 驱动的 OpenCL
的实现。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTc3MTk)
