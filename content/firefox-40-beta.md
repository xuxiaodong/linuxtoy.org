Title: Firefox 40 Beta
Author: lovenemesis
Date: 2015-07-04
Category: Browser
Tags: mozilla, firefox
Slug: firefox-40-beta
Summary: 在美国独立日假期前一天，Mozilla 按时将 Firefox 40 推送至 Beta 频道，为 Linux 平台默认启用了 OMTC 渲染支持，且支持即将发布的 Win10。

本次**桌面版本**的变化有：

* 支持即将发布的 Win10，包括平板模式
* 提供对于可能有威胁的文件的下载保护
* 针对浏览习惯在[推荐列表](https://support.mozilla.org/kb/how-do-tiles-work-firefox#w_suggested-tiles)列出您可能感兴趣的站点
* 在 Firefox Hello 对话中增加指向附件内容的 URL
* 依据首选项的风格重新改良了附件组件管理器
* 实现 [CSS 动画](https://wiki.mozilla.org/Platform/GFX/OffMainThreadCompositing#CSS_Animations)异步渲染，提高稳定性且更加平缓
* 为 GNU/Linux 平台启用主线程外混成模式（OMTC），改善视频和渲染的稳定性和可靠度
* 在安装未经 Mozilla 签名的附件组件时将会弹出安全警告
* 为 Win 平台启用硬件垂直同步，提供更加平台的滚动体验
* 降低 JPEG 图像的内存占用，并提升绘制速度
* 支持新的 Unicode 8.0 肤色风格表情
* [IndexedDB 事务](https://developer.mozilla.org/docs/Web/API/IndexedDB_API/Basic_Concepts_Behind_IndexedDB#durable)默认将是非持久性的。
* 实现[AudioBufferSourceNode.detune](https://developer.mozilla.org/docs/Web/API/AudioBufferSourceNode/detune)从而可以模块化处理音频回放比率（？）
* 提升开发者工具中的[性能调优器](https://hacks.mozilla.org/?p=28808)
* 新的[规则查看悬浮提示](http://youtu.be/t3NKmmWfklU)将方便调试 CSS 过滤器值
* SharedWorker 和 ServiceWorker 的 Console API 消息将显示在 Web 终端中
* Inspector 的搜索范围扩展到整个内容帧
* 废弃 Places Keywords API，引入[异步关键字 API](https://developer.mozilla.org/docs/Mozilla/Tech/Places/Using_the_Places_keywords_API)
* 移除扩展中对于二进制 XPCOM 的支持，转向使用 Add-on SDK 中的 "system/child_process" 管道机制调用原生二进制组件

[完整英文发布公告](https://www.mozilla.org/en-US/firefox/40.0beta/releasenotes/)

[官方多语言全平台下载](https://www.mozilla.org/en-US/firefox/channel/#beta)


本次 **Android 版本**的变化有：

* 支持 Android Presentation API 实现屏幕投射
* 提供对于可能有威胁的文件的下载保护
* 长按前进和后退按钮将弹出浏览历史记录
* 实现 [CSS 动画](https://wiki.mozilla.org/Platform/GFX/OffMainThreadCompositing#CSS_Animations)异步渲染，提高稳定性且更加平缓
* 在安装未经 Mozilla 签名的附件组件时将会弹出安全警告
* 降低 JPEG 图像的内存占用，并提升绘制速度
* 支持新的 Unicode 8.0 肤色风格表情
* [IndexedDB 事务](https://developer.mozilla.org/docs/Web/API/IndexedDB_API/Basic_Concepts_Behind_IndexedDB#durable)默认将是非持久性的。
* 实现[AudioBufferSourceNode.detune](https://developer.mozilla.org/docs/Web/API/AudioBufferSourceNode/detune)从而可以模块化处理音频回放比率（？）
* 移除扩展中对于二进制 XPCOM 的支持，转向使用 Add-on SDK 中的 "system/child_process" 管道机制调用原生二进制组件

[Play Store 官方下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox&referrer=utm_source%3Dmozilla%26utm_medium%3DReferral%26utm_campaign%3Dmozilla-org)