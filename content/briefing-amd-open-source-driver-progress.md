Title: 短消息：AMD 开源显卡驱动进展
Date: 2011-12-13 12:48
Author: lovenemesis
Category: Drivers
Tags: AMD, hdmi, OpenCL
Slug: briefing-amd-open-source-driver-progress

短消息三则，覆盖最近 AMD 开源显卡驱动方面的进展。

尽管 AMD 的官方 HDMI 音频文档尚在审核开放中，但 **HD 5000 系列显卡的
HDMI 音频输出支持已经提前由社区开发者 Rafał Miłecki
完成**，对其的支持最晚将于 Linux Kernel 3.3
时面世。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTAyNDY)

即将发布的 **AMD HD 7000 系列显卡由于显卡架构上的差异将会用新的 R700G
Gallium3D 驱动**，注意这特指 HD 7900 系列，预期将在 2012
年夏季实现。因为目前已知的其他 HD 7000 显卡将是采用改良 28nm
工艺和部分优化的 Northen Islands 和 Caymen 核心，简单的扩展现有 R600G
Gallium3D
即可。[消息来源](http://www.phoronix.com/scan.php?page=news_item&px=MTAyNTA)
[AMD 7000
系列扩展阅读](http://www.brightsideofnews.com/news/2011/11/30/radeon-hd-7000-revealed-amd-to-mix-gcn-with-vliw4--vliw5-architectures.aspx)

开源驱动的 OpenCL GPU 通用高性能计算有了意义显著的一步，**AMD 先后开源了
R600G Gallium3D LLVM 2.9 后端(TGSI 至 LLVM ) 和 AMDIL LLVM 2.9
后端(AMDIL 至 LLVM)**，特别是前者的 TGSI 至 LLVM
转换器将会被用于其他开源显卡驱动的 OpenCL 支持。不过目前在完善针对 [LLVM
3.0](http://linuxtoy.org/archives/llvm-30.html)
的支持前暂不会合并入主线。[消息来源1](http://www.phoronix.com/scan.php?page=news_item&px=MTAyNTg)
[消息来源2](http://www.phoronix.com/scan.php?page=news_item&px=MTAyNjk)
