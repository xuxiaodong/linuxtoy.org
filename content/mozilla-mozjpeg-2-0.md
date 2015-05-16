Title: Mozilla mozjpeg 2.0
Date: 2014-07-17 11:05
Author: lovenemesis
Category: Desktop Stuff
Tags: Mozilla, mozjpeg
Slug: mozilla-mozjpeg-2-0

mozjpeg 是一款 Mozilla 开发的 **JPEG 编码器**，衍生自
libjpeg-turbo，目标是在提高编码效率的同时与当前解码器保持兼容。

与 libjpeg-turbo 的编码器相比，包含棚格量化（trellis quantization）的
mozjpeg 2.0 在 baseline 和 progressive 模式下生成的 JPEG 体积平均减少
5%。体积的减少意味着网页加载速度的提升。

目前脸谱网已经对此项目捐助 6 万美金开发 mozjpeg 3.0
版本，评估其未来在其网站使用的可行性。

此外，Mozilla
也公布了新一轮的[有损图像压缩格式的对比研究报告](http://people.mozilla.org/~josh/lossy_compressed_image_study_july_2014/)，覆盖了
JPEG、WebP、JPEG XR 和 HEVC-MSP 四种格式。从结果看来并没有充足的证据表明
WebP 和/或 JPEG XR 相比 JPEG 有统计上显著的优势。当然，这不代表 Mozilla
不会增加对这几种格式的支持。

**注意：**这是一个 JPEG 编码器，对于 JPEG 解码，Mozilla
仍将继续支持并推荐使用 libjpeg-turbo。

[英文官方公告](https://blog.mozilla.org/research/2014/07/15/mozilla-advances-jpeg-encoding-with-mozjpeg-2-0/)
