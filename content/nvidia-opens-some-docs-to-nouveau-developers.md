Title: NVIDIA 开放部分文档给 Nouveau 开发者
Date: 2013-09-25 13:44
Author: lovenemesis
Category: Drivers
Tags: NVIDIA
Slug: nvidia-opens-some-docs-to-nouveau-developers

没有人会忘记 [Linus 本人给 NVIDIA
手势](http://linuxtoy.org/archives/briefing-about-nvidia.html)的事情，不过似乎
NVIDIA 有意不再做他口中最差的公司了。

NVIDIA 的 Andy Ritger 在刚刚过去的几天里向 Nouveau 开发者活跃的
FreeDesktop 邮件列表中公布了 NVIDIA 显卡 BIOS 的 DCB (Device Control
Block) 文档，希望能为逆向工程的 Nouveau 驱动开发者提供一些帮助。

众所周知由于得不到任何 NVIDIA 方面的支持，Nouveau
的驱动状况一直处于喜忧参半的状况，依据型号不同，最终用户时不时还要进行从闭源驱动提取固件的
Hack 行为才能让其工作。对于本次 NVIDIA 的举措，开发者表示尽管 DCB
文档本身对于改善当前驱动现状不大，不过这算是一个开端。

Andy Ritger 进一步表示说依据社区的反馈，将逐步开放更多的 BIOS
文档。NVIDIA 希望 Nouveau 最终能达到一个合理的开箱体验，包括 GPU
初始化、显示配置和基本的 2D 和 3D 渲染。

相比社区相对较为积极的反馈，Linus 本人对此的态度可谓保守乐观，毕竟本次
DCB 文档的信息相比整个 GPU 信息来讲太微不足道了，不过 NVIDIA 在 ARM
领域的合作态度已经比传统 GPU
领域进步不少了，或许未来他有机会能仅就那个手势给 NVIDIA 致歉。

*消息来源：*[Ars
Technica](http://arstechnica.com/information-technology/2013/09/nvidia-seeks-peace-with-linux-pledges-help-on-open-source-driver/)

**编者点评：**毫无疑问这是个好事，特别对于比较杯具的 Nouveau
驱动来说（本人最近在使用一块二手 GeForce 560Ti）。不过 NVIDIA
此番的诚意相比 Intel 和 AMD 差距还是非常大的：

1.  自身依然没有员工直接参与开源驱动开发 ；
2.  仅计划公布 VBIOS 文档，更为关键和有用的 Shader 等信息依然封闭。
3.  依旧不提供允许自由分发的 Atomic Bios (最简
    BIOS)，未来有部分型号仍然需要从闭源驱动提取。

