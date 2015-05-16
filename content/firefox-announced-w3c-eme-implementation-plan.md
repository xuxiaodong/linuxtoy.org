Title: Firefox 宣布 W3C EME 实现方案
Date: 2014-05-15 13:49
Author: lovenemesis
Category: News
Tags: drm, Firefox, html5, Mozilla
Slug: firefox-announced-w3c-eme-implementation-plan

Mozilla Hacks 博客公布了在 Firefox 中实现 W3C EME
扩展的计划，为了满足最终用户和厂商 HTML5 视频的版权控制需求(DRM)。

内容要点如下：

-   将使用来自 Adobe 的 CDM (Content Decryption Module 内容解密模块)
    来实现客户端的 DRM 需求。
-   尽管遭到[包括 Mozilla
    等组织的反对](https://www.eff.org/deeplinks/2013/03/defend-open-web-keep-drm-out-w3c-standards)，但是
    W3C EME 扩展中的 **CDM 将是二进制闭源的**，Mozilla
    使用的此款也不例外。不过 Adobe 承诺**此 CDM 会支持 Win、OS X 和
    Linux 平台**。移动版支持尚未确认。
-   该**闭源二进制 CDM 将不会随着 Firefox
    分发**，仅会在访问需要的网站的时提醒下载，且用户可以选择拒绝（不过当然也就看不成视频了），安装后也仅在用户允许下启用。Mozilla
    亦将提供编译时选项关闭 CDM 下载。
-   为了保护用户隐私，Firefox 将包含一个**特殊设计的开源的沙箱，限制该
    CDM 的访问权限**。和其他浏览器中直接绑定的 CDM
    不同，该沙箱将为每一个网站生成唯一的设备标识符，从而**阻止内容提供商通过
    CDM 返回的设备标识符追踪用户的跨站点浏览行为**。

实际上自从去年反对 W3C EME 暨 HTML DRM
的行动失败后，[其他浏览器已经“悄悄的”捆版闭源 CDM
默认分发](http://html5test.com/compare/feature/video-drm.html)了。Firefox
显然晚了不少，但是提出来实现方案相对更灵活，对于用户隐私性也有更多考虑。

[更多详情参加 Mozilla Hacks
博客原文](https://hacks.mozilla.org/2014/05/reconciling-mozillas-mission-and-w3c-eme/comment-page-1/#comment-2160761)
