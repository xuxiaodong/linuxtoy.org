Title: NVIDIA 发布 Maxwell 系列 GPU 可用签名固件
Author: lovenemesis
Date: 2016-02-16
Category: Drivers
Tags: nvidia, nouveau
Slug: nvidia-releases-signed-firmware-for-maxwell-gpu
Summary: 在 GTX 900 系列显卡发布 18 月后，NVIDA 终于发布了可供开源驱动使用的签名固件。

按照 NVIDIA 的说法，为了安全 GTX 900 “Maxwell” 系列显卡将仅能引导由 NVIDIA 签名的固件。这意味着开源驱动 nouveau 一直以来即时生成固件指令的方式将无法在 GTX 900 系列上工作。缺失固件，除了简单的引导外和设备识别外，什么也做不了，这也是当下 Linux 系统 nouveau 驱动在 GTX 900 系列上的现状。

在新 GPU 发布前夕，NVIDIA 终于兑现了当初对于开源社区的承诺：释出了用于 GM200/GM204 GPU （GTX 970 及更高端）的签名固件。有了这个固件，开源驱动开发者便可以启用包括 3D 加速在内 GPU 功能，nouveau 终于在 GTX 900 系列上可用了。

注意本次发布的固件仅支持 GTX 970 及更高端的 GPU，入门级别的 GM206 则尚需等待。此外初代 Maxwell 产品（GTX750Ti）不在其中。

若一切顺利，新的签名固件将合并入 Linux 4.6 内核的发布，有望在下半年的发行版和最终用户见面。

消息来源：[Phoronix](https://www.phoronix.com/scan.php?page=news_item&px=NVIDIA-Releases-Signed-Blobs)
