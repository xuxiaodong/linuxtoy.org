Title: NVIDIA 显示驱动更新至 180.29
Date: 2009-02-12 20:22
Author: toy
Category: Apps, Drivers
Tags: NVIDIA
Slug: nvidia-display-driver-18029

NVIDIA 针对 Linux 平台提供的显示驱动已从
[180.27](http://linuxtoy.org/archives/nvidia-release-18027-opengl3-officially-supported.html)
更新至
[180.29](http://www.nvidia.cn/object/linux_display_ia32_180.29_cn.html)。NVIDIA
180.29 主要包括以下变化：

-   添加了针对 GeForce 9300 GE 及 Quadro NVS 420 的 GPU 支持。
-   在 GeForce 8 系列和之后发布的 GPU 上添加针对 OpenGL 3.0 的支持。
-   修正了一处漏洞，在交织状态下使用基于覆盖的展示队列时，该漏洞导致
    VDPAU 显示绿屏。
-   修正了一处漏洞，在某些 GPU 上重启 X 服务器后该漏洞导致 VDPAU
    运行错误。
-   改进了 VDPAU
    模式调换能力；消除了一项由于模式调换恢复代码引起的崩溃，以及一项基于
    Blit 展示队列引起的系统停滞。
-   修正了一处漏洞，当使用 DisplayPort 设备时该漏洞导致 VDPAU 崩溃。
-   修正了非 SLI 模式下在多 GPU 系统上使用基于 Blit 的展示队列时 VDPAU
    中一个潜在的问题。
-   对 VDPAU 的 VdpVideoMixerRender 函数的层数据进行了遗漏错误检查。
-   改进了 VDPAU 对 GPU 因资源限制而无法得到支持时多 GPU 设置的处理。
-   改进了 NVIDIA X 驱动和 VDPAU 之间 GPU 视频存储器管理的协调。
-   修正了覆盖正在使用时 VDPAU 中的一个潜在问题。
-   改进了工作站 Open GL 的性能。
-   修正了一个在 GeForce 6 和 7 系列 GPU 中造成 Xid 错误的 X
    驱动器加速错误。
-   升级了 X 驱动程序，以支持不被该驱动程序识别为“支持”的
    GPU，这样驱动程序就可以驱动原来无法驱动的 GPU。
-   添加运行来自“nvidia-installer”的安装前/后的分散程序；详情请请参阅“nvidia-installer”手册
-   更新了 X 驱动上的 metamode 剖析器，由此模式命名可由周期而定（譬如
    “.”）。
-   修改了一处 VDPAU
    上的错误，该错误导致交织状态下使用基于覆盖的显示线无法在由组建视频链接的显示器上使用。
-   修改了一些 VDPAU 上的错误，当对特定的 MPEG-2
    视频进行解码时这些错误导致屏幕显示崩溃。
-   修改了一处 VDPAU 上的崩溃，在某些 GPU 上使用 64 位驱动时产生无效的
    MPEG-2 数据流可导致崩溃出现。
-   在集成 GPU 上修改了一处 X 驱动性能问题。
-   修改了一处稳定性错误，使用 FSAA 时该错误在 OpenGL 应用上发生。
-   修改了一处初始化错误，该错误导致某些 AGP GPU 在调整成 PCI
    兼容模式时出错。
-   修正了一处漏洞，在使用 Coolbits
    界面对频率选项进行调整后，该漏洞导致系统稳定性出错。
-   改进了在某些新发布的移动 GPU 上的热键转换问题。
-   改进了一处功耗管理程序的衰退，并改进了对新发布的 Linux 2.6
    核心的兼容性。

NVIDIA 180.29 支持 [32
位](ftp://download.nvidia.com/XFree86/Linux-x86/180.29/)及 [64
位](ftp://download.nvidia.com/XFree86/Linux-x86_64/180.29/)平台，可从其
FTP 站点下载。
