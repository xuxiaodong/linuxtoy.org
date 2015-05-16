Title: Mozilla & OTOY ORBX.js 
Date: 2013-05-07 13:10
Author: lovenemesis
Category: Videos
Slug: mozilla-and-otoy-orbx-js

Mozilla 在 HTML5 的道路上马不停蹄，上个月[刚刚将 Unreal 引擎带到了 HTML5
的世界](http://linuxtoy.org/archives/mozilla-and-epic-games-ported-unreal-engine-to-web.html)，本月又和
OTOY 实现了无插件、完全使用 JavaScript 实现的高清视频编解码器
ORBX.js，允许在任意 HTML5 浏览器中远程运行原生 PC 应用程序。

ORBX.js 允许用户在 HTML5 兼容浏览器中远程运行位于另一台 Linux、OS X 或
Win 主机或云端上任意原生 PC
应用程序，而无需安装任何插件或本地扩展，完全使用 JavaScript 和 WebGL
实现。

使用 ORBX.js，您可以在 Macbook 游玩在另一台配备强劲显卡 Win PC 中的 Left
4
Dead，而无需担忧本本孱弱的显卡特效或者过热问题。[视频演示](https://www.youtube.com/watch?v=FRtBuP2-_pA&feature=player_embedded)（[朝内镜像](http://v.youku.com/v_show/id_XNTUzMjg0NTQ0.html)）

使用 ORBX.js，您可以不再购置昂贵的高端显卡，使用基于 GPU
的云端渲染服务可以更经济的达到将 3DS Max 渲染时间缩短的目标，其良好的
HTML5
兼容性甚至允许您在平板和智能手机上完成渲染工作。[视频演示](https://www.youtube.com/watch?v=YUsCnWBK8gc&feature=player_embedded)（[朝内镜像](http://v.youku.com/v_show/id_XNTUzMjgwOTY4.html)）

ORBX.js 远程桌面的视频流并非使用 H264 或 VP8 编码的`video`
标签，而是使用自身所创建的完全使用 JavaScript
从零开始设计的编解码器。该编解码可以实现 1080p60
超低延迟的回放，观看高清视频毫无压力。[视频演示](https://www.youtube.com/watch?v=eOY2U_i2fuc&feature=player_embedded)（[朝内镜像](http://v.youku.com/v_show/id_XNTUzMjc3NjEy.html)）

纯粹的 JavaScript 的远程视频流带来了以下几个额外的好处：

-   允许将**远程桌面的内容和本地的内容混合**起来。
-   不再依靠有专利限制的视频编码格式，也**不再依赖于浏览器所附带的解码包**。
-   可以在服务器端就对视频加上水印，**无需依赖客户端 HTML5 的 DRM
    实现**。

此项工作超越了 Chrome Remote Desktop 依赖平台相关 NaCl
的局限，将远程桌面及云端游戏推广到任意 HTML5 浏览器以及移动终端设备上。

[OTOY](http://render.otoy.com/) 得到了 Autodesk
的资金和技术支持，未来可能会看到 Autodesk 推出使用该技术的 GPU
渲染云服务。

[OTOY 官方发布公告 (PDF
格式)](http://www.otoy.com/130501_OTOY_release_FINAL.pdf)

[来自 JavaScript
创始人的博客](https://brendaneich.com/2013/05/today-i-saw-the-future/)
