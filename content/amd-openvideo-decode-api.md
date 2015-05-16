Title: AMD OpenVideo Decode API
Date: 2011-02-20 10:51
Author: lovenemesis
Category: News
Tags: AMD, ovd
Slug: amd-openvideo-decode-api

AMD 公开了适用于闭源 Linux Catalyst 驱动的 OpenVideo Decode 高清硬件解码
API。

不像 NVIDIA 对于 VDPAU 的推广，AMD 在 Linux 平台下的高清硬件解码方案
XvBA
需要来自第三方的闭源组件支持才可实现。这样子不仅增加了最终用户的使用难度，并且也影响了在各大开源播放器中的接受程度。

最近 AMD 对外公开了称为 [OpenVideo Decode (OVD) 的高清解码
API](http://developer.amd.com/gpu/AMDAPPSDK/assets/OpenVideo_Decode_API.PDF)文档，理论上讲，社区播放器的开发者可以依据该
API 在 Linux 平台上调用 UVD 引擎实现硬件解码。

[![](http://linuxtoy.org/img/2011/02/ovd.png)](http://linuxtoy.org/img/2011/02/ovd.png)

初步搜索显示，已经有[ffmpeg
的开发者根据该文档着手进行研究](http://www.devcomments.com/Adding-AMD-OpenVideo-Decode-acceleration-at1086837.htm)。
