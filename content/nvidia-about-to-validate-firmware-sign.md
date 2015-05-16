Title: NVIDIA 即将验证 GPU 固件签名
Date: 2014-09-28 15:41
Author: lovenemesis
Category: Drivers
Tags: nouveau, NVIDIA
Slug: nvidia-about-to-validate-firmware-sign

NVIDIA 以“安全性”为名的一项新举动至少在短时间内将给 Nouveau
开源驱动的开发带来麻烦。

从 Maxwell 系列核心 GPU 开始 NVIDIA
将对固件实行签名，并在硬件层面执行签名验证工作。若是通过验证发现固件并非来自
NVIDIA 官方，则会禁用部分 GPU 功能。以初代 Maxwell 核心的 750Ti
为例，非官方签名固件将无法访问温度传感器，而第二代 Maxwell 核心的 GTX980
则不允许非官方签名固件访问物理内存。将这个消息传达至 NOUVEAU
开发者列表的 NVIDIA Linux 工程师 Andy Ritger
表示越来越多的功能都将要求官方签名的固件才能访问。

如果您对于 Nouveau 的开(xue)发(lei)史还不太了解的话，容我多说下。Nouveau
源自逆向工程，早先需要用户从闭源驱动中提取出 GPU
固件，才能使得开源驱动工作。随着对于硬件的熟悉，Nouveau 的 DRM
驱动已经可以自行生成部分硬件的 GPU
固件，免去了提取的步骤。不过对于刚刚新出的显卡，还是需要这个过程的。NVIDIA
在 Maxwell 开始的固件官方签名限制意味着现有的 Nouveau
工作模式将难以为继。

不过 Andy Ritger 表示他的团队正在试图效仿 AMD，允许 Nouveau
开发团队使用包含 NVIDIA 官方签名的 GPU 固件。目前 AMD
随着开源驱动一并分发闭源固件并提交至内核，这也是有些 radeon
开源驱动功能的实现依赖内核的部分原因。这个想法究竟能否实现（read:
能否通过法律部门审核）？尚不可知。

对于 Nouveau 开源驱动的忠实用户来说，暂时别想着换 Maxwell 核心的显卡了……

*消息来源*：[Phoronix](http://www.phoronix.com/scan.php?page=news\_item&px=MTc5ODA)

**PS：**另一方面，AMD 果真在[研究统一 radeon 开源驱动和 Catalyst
闭源驱动的内核模块](http://www.phoronix.com/scan.php?page=news\_item&px=MTc5ODE)，若实现，则意味着
AMD
闭源驱动显卡用户再也不用担心新内核更新，且可以非常便捷的切换用户态驱动实现。

**PSS：**
有[网友戏虐](http://www.phoronix.com/forums/showthread.php?107015-NVIDIA-Alerts-Nouveau-They-re-Starting-To-Sign-Validate-GPU-Firmware-Images&p=442796#post442796)说
NVIDIA 打算按功能卖 GPU 固件 DLC 了，支持应用（固件）内购买。
