Title: Mozilla WebAPI
Date: 2011-08-30 15:48
Author: lovenemesis
Category: News
Tags: Mozilla, WebAPI
Slug: mozilla-webapi

Mozilla 前几日表明要开发 WebAPI，那么它到底是什么呢？

**WebAPI 的目的是为 Web 程序提供：**

-   **设备硬件的访问接口**，比如相机、蓝牙和 NFC。
-   **存储数据的读写支持**，比如联系人和日历信息。

**安全和隐私**

这些接口目前尚未存在的主要原因就是安全隐私。

对于其中一些安全问题，可以采取类似现在地理位置信息的方式：弹出窗口询问请求。

对于另外一些更为敏感的信息如联系人，**需要一个更好的安全框架，目前还处在讨论中**。

Robert
提供了一些[参考想法](http://robert.ocallahan.org/2011/06/permissions-for-web-applications_30.html)。

**标准化**

WebAPI 目的是**成为可供不同浏览器和设备使用的通用 API**，并非 Mozilla
特有的。由于 WebAPI 尚处于研究阶段，所以主要开发工作将在 Mozilla
以公开的方式进行。

当接近完成时，将提交给 W3C 的 [Device API](http://www.w3.org/2009/dap/)
进行标准化工作。

**High Level 和 Low Level**

针对设备硬件控制来讲，当下的目标是**开发一系列的 Low Level
API**，使得开发者可以更早的利用这组 API 实现有创造性的 Web 应用。

随着时间推移，将会把这些 Low Level API 封装起来提供更为便捷使用的 High
Level API。

**如何加入**

[邮件列表](https://lists.mozilla.org/listinfo/dev-webapi)

[Wiki 页面](https://wiki.mozilla.org/WebAPI)

*消息来源：*[Mozilla
Hacks](http://hacks.mozilla.org/2011/08/more-details-about-the-webapi-effort/)
