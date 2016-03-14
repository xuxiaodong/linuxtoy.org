Title: Firefox 46 Beta
Author: lovenemesis
Date: 2016-03-14
Category: Browser
Tags: mozilla, firefox
Slug: firefox-46-beta
Summary: Firefox 46 如约尔至 Beta 频道，带来了 JS `W^X` 保护和 Android 6.0 运行时权限请求支持。

**桌面版**的变化有：

* [密码提交并非用 HTTPS 协议时](https://hacks.mozilla.org/2016/01/login-forms-over-https-please/)将被标示为不安全
* 为 JIT 引擎启用 [W^X 保护](http://jandemooij.nl/blog/2015/12/29/wx-jit-code-enabled-in-firefox/) 支持，意味至页面中包含的 JIT 将不可同时可写及可执行
* 继续完善 Linux 平台上的 GTK3 整合
* 将 CDM 用作处理 H264/AAC 媒体的最后被选方案（笔者注：已然优先使用内置或系统解码器）
* 修复并提高了 [WebRTC](https://wiki.mozilla.org/Media/WebRTC/ReleaseNotes/46) 性能和错误
* 内存工具想显示[支配树的内存占用情况](https://developer.mozilla.org/en-US/docs/Tools/Memory/Dominators_view)
* 内存分配和垃圾回收将暂停 Profiling 生成过程
* 可以从样式编辑器侧边栏中快速启动并调试系统主题
* 增加对 [documents.elementsFromPoint](https://developer.mozilla.org/en-US/docs/Web/API/Document/elementsFromPoint) 支持
* [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) 增加了 HKDF 支持

[官方发布日志](https://www.mozilla.org/en-US/firefox/46.0beta/releasenotes/)

[官方多语言全平台下载](https://www.mozilla.org/en-US/firefox/beta/all/)

**Android版**的变化有：

* 在[后台打开标签页的提示](https://support.mozilla.org/en-US/kb/open-links-background-later-viewing-firefox-android)现在包含 URL
* 在 Android 6.0 上支持[按需请求所必要的权限](https://support.mozilla.org/en-US/kb/how-firefox-android-use-permissions-it-requests)
* 当离线时将显示已经缓存的页面
* 首页快捷方式图标更清晰
* 自动补全时将包含默认域名
* 在菜单中增加书签和历史项目
* 移除 [Firefox Sync 1.1 支持](https://blog.mozilla.org/services/2015/07/31/shutting-down-the-legacy-sync-service/)
* 移除 Android 3.X 支持
* 首选站点将显示最流行的站点

[官方发布日志](https://www.mozilla.org/en-US/firefox/android/46.0beta/releasenotes/)

[Play Store 官方下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox_beta&referrer=utm_source%3Dmozilla%26utm_medium%3DReferral%26utm_campaign%3Dmozilla-org)
