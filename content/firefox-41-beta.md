Title: Firefox 41 Beta
Author: lovenemesis
Date: 2015-08-14
Category: Web Browser
Tags: firefox, mozilla
Slug: firefox-41-beta
Summary: Mozilla 携 Firefox 41 版本至 Beta 通道，默认禁用了未签名扩展，且重新设计了进程恢复页面，以及一大堆 HTML5 方面的改善。

**桌面版本**的变化有：

* 允许使用 SVG 作为 Favicon
* 支持 TSF 文本服务框架
* 新设计的进程恢复及欢迎回来界面
* 允许给 Firefox 账户添加一个头像
* Firefox Hello 现在支持即时消息聊天
* 未经 Mozilla 签名的扩展将[被默认禁用](https://support.mozilla.org/kb/add-on-signing-in-firefox)
* 修复了一些[长达 14 年的老 Bug](https://bugzilla.mozilla.org/show_bug.cgi?id=77999)，从而大幅度降低了[使用 ABP 及其他扩展时的内存消耗](https://blog.mozilla.org/nnethercote/2015/07/01/firefox-41-will-use-less-memory-when-running-adblock-plus/)
* WebRTC 现在要求[实现 Perfect Forward Secrecy 以提高安全性](https://hacks.mozilla.org/2015/02/webrtc-requires-perfect-forward-secrecy-pfs-starting-in-firefox-38/)
* 在 Win7 下禁用了 WARP （？）
* 改善了图像解码的速度，在部分设备上特别是滚动时甚至达到2倍的提升
* 通过异步渲染的方式提供更可靠及稳定的 [CSS 动画](https://wiki.mozilla.org/Platform/GFX/OffMainThreadCompositing#CSS_Animations)
* 默认启用 [CSS 字体加载 API](http://dev.w3.org/csswg/css-font-loading/)
* 允许通过[使用 JavaScript 实现剪切粘贴](https://developer.mozilla.org/docs/Web/API/Document/execCommand)
* 默认启用 [MessageChannel](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel) 及 [MessagePort](https://developer.mozilla.org/docs/Web/API/MessagePort) API
* 在 Win 及 OS X 平台上[Navigator.onLine ](https://developer.mozilla.org/docs/Web/API/NavigatorOnLine/onLine)状态会随着实际互联网状态改变
* 增加对 SVG 格式的 [transform-origin 属性](https://developer.mozilla.org/docs/Web/CSS/transform-origin)支持
* 实现 [CacheAPI](https://developer.mozilla.org/docs/Web/API/CacheStorage)支持，可以查询命名缓存供 Worker 及 ServiceWorker 使用
* 在页面元素的上下文菜单中增加**截图功能**
* 在 Inspector 的 Copy Rule Declaration 上下文菜单中允许复制 CSS 规则声明
* 网络请求可以按照 [HAR 格式](http://www.softwareishard.com/blog/har-12-spec/)导出
* 允许在[新的标签页打开页面源代码](https://hacks.mozilla.org/2015/07/developer-edition-41-view-source-in-a-tab-screenshot-elements-har-files-and-more/)
* 可以在 Inspector 里快速[添加 CSS 规则](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Examine_and_edit_CSS#Add_rules)
* 修复图片对于改变大小没有响应的问题

[官方多语言全平台下载](https://www.mozilla.org/en-US/firefox/beta/all/)

[英文完整发布摘要](https://www.mozilla.org/en-US/firefox/41.0beta/releasenotes/)

**Android 版本**的变化有：

* 允许在搜索面板快速变更搜索引擎提供商
* 在平板界面上亦支持滑动关闭
* 在登录站点时可以选在所需要的账户信息
* 允许使用 SVG 作为 Favicon
* 增加重复书签检查
* 允许网页使用 [Intent URI](https://developer.chrome.com/multidevice/android/intents)打开本地应用程序
* 改善了图像解码的速度，在部分设备上特别是滚动时甚至达到2倍的提升
* UA 信息中现在包含 Android 系统版本
* 通过异步渲染的方式提供更可靠及稳定的 [CSS 动画](https://wiki.mozilla.org/Platform/GFX/OffMainThreadCompositing#CSS_Animations)
* 默认启用 [CSS 字体加载 API](http://dev.w3.org/csswg/css-font-loading/)
* 允许通过[使用 JavaScript 实现剪切粘贴](https://developer.mozilla.org/docs/Web/API/Document/execCommand)
* 默认启用 [MessageChannel](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel) 及 [MessagePort](https://developer.mozilla.org/docs/Web/API/MessagePort) API
* 增加对 SVG 格式的 [transform-origin 属性](https://developer.mozilla.org/docs/Web/CSS/transform-origin)支持
* [JavaAddonManager](https://developer.mozilla.org/Add-ons/Firefox_for_Android/API/JavaAddonManager.jsm)现在支持发送、接受及相应来自的 Gecko 的消息
* 引入试验性的快速拨号 API（[API样例程序](https://github.com/pocmo/speed-dial)）

[官方 Play Store 下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox_beta&referrer=utm_source%3Dmozilla%26utm_medium%3DReferral%26utm_campaign%3Dmozilla-org)

[英文完整发布摘要](https://www.mozilla.org/en-US/firefox/android/41.0beta/releasenotes/)
