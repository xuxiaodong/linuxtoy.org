Title: Firefox 38 Beta
Date: 2015-04-06 10:33
Author: lovenemesis
Category: Web Browser
Tags: Firefox, Mozilla
Slug: firefox-38-beta

Mozilla 按部就班的发布了 Firefox 38 Beta
版本，带来了标签页式首选项及阅读列表试验，同时该版本也将是下个 ESR
版本。

**桌面版本**的变化有：

* 新的标签页风格首选项  
* 允许在基于 Firefox Hello 的对话中分享正在浏览的标签页或窗口  
* 带来阅读视图模式，且允许将网页添加到带阅读列表  
* 支持 [Ruby
标示](https://hacks.mozilla.org/2015/03/ruby-support-in-firefox-developer-edition-38/)（注音符号）  
* 在用户名和密码区域不再支持 `autocomplete=off`  
* 当设定 `Fragment` URL 时分析器不进行编码，同样的仅在行间的
`Fragment` 符合 URL 标准时才进行解码（？）  
* 对于空的正则表达式 `RegExp.prototype.source` 返回 `(?:)`
而不再是空字符串  
* 通过连接预载入的方式改善页面加载时间  
* 可以在 Web Workers 中使用 WebSocket  
* 为响应式图片实现 `srcset` 属性和 `picture` 元素  
* 实现 `KeyboardEvent.code` DOM3 事件  
* 实现 [BroadcastChannel
API](https://hacks.mozilla.org/2015/02/broadcastchannel-api-in-firefox-38/)  
* 在 OS X 上实现部分 MSE 从而允许 YouTube 原生 HTML5 回放  
* 实现了 [EME](https://support.mozilla.org/en-US/kb/enable-drm)
从而允许回放加密的 HTML5 音视频  
* 同时为了实现 EME 功能，会自动在播放加密视频时下载 [Adobe Primetime
Content Decryption
Module](https://support.mozilla.org/en-US/kb/enable-drm)  
* 可以在调试工具中看到在优化过程中移除的变量  
* 在 Web 终端中 XMLHttpRequest 日志将被单独归类显示  
* 在 Web 终端中增加了 `copy` 命令  
* WebRTC 增加了多媒体流及重协商支持

[完整英文发布公告](https://www.mozilla.org/en-US/firefox/38.0beta/releasenotes/)

[官方多平台全语言下载](https://www.mozilla.org/en-US/firefox/channel/#beta)

**移动版本**的变化有：

* 支持 [Ruby
标示](https://hacks.mozilla.org/2015/03/ruby-support-in-firefox-developer-edition-38/)（注音符号）  
* 在用户名和密码区域不再支持 `autocomplete=off`  
* 当设定 `Fragment` URL 时分析器不进行编码，同样的仅在行间的
`Fragment` 符合 URL 标准时才进行解码（？）  
* 对于空的正则表达式 `RegExp.prototype.source` 返回 `(?:)`
而不再是空字符串  
* 通过连接预载入的方式改善页面加载时间  
* 可以在 Web Workers 中使用 WebSocket  
* 为响应式图片实现 `srcset` 属性和 `picture` 元素  
* 实现 `KeyboardEvent.code` DOM3 事件  
* 实现 [BroadcastChannel
API](https://hacks.mozilla.org/2015/02/broadcastchannel-api-in-firefox-38/)  
* WebRTC 增加了多媒体流及重协商支持

[完整英文发布公告](https://www.mozilla.org/en-US/mobile/38.0beta/releasenotes/)

[官方 Play Store
下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox&referrer=utm\_source%3Dmozilla%26utm\_medium%3DReferral%26utm\_campaign%3Dmozilla-org)
