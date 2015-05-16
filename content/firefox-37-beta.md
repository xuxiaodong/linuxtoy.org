Title: Firefox 37 Beta
Date: 2015-02-26 15:41
Author: lovenemesis
Category: Web Browser
Tags: Firefox, Mozilla
Slug: firefox-37-beta

包含 HTTP/2 完整支持的 Firefox 36 刚刚发布，Firefox 37 Beta
就如约而至，包含带来强化安全的特性，且集成了可在 Firefox 中调试 Chrome
及 Safari 的工具 Valence。

**桌面版本** 的变化有：

* 集成[新的 Heartbeat
反馈系统](https://wiki.mozilla.org/Advocacy/heartbeat)，方便用户及时反馈意见。  
* Bing 搜索默认使用 HTTPS。  
* 支持 OneCRL 集中式证书撤销。  
* 移除证书和 TLS 中的 DSA 支持。  
* 支持证书中的电子邮件限定条件。  
* 实现 HTTP/2 AltSvc 非认证加密（opportunistic encryption）。  
* 前半 Beta 阶段启用新的首选项界面。  
* 禁用不安全的 TLS 备选加密方案。  
* 扩展 SSL 错误信息报告机制，可以汇报非证书导致的错误。  
* TLS False Start 优化需要一个使用 AEAD 的加密套件（？）。  
* Web Workers 中现在可以使用 WebSocket。  
* 允许在 Worker 线程中访问 IndexedDB。  
* 支持 CSS
[display:contents](https://developer.mozilla.org/en-US/docs/Web/CSS/display)  
* 支持[在 Firefox 中调试 Chrome 桌面及 Android 版、Safari iOS
版](https://developer.mozilla.org/en-US/docs/Tools/Valence)。  
* 新的 [Inspector
动画面板](https://hacks.mozilla.org/2015/01/web-animation-tools-network-security-insights-font-inspector-improvements-and-more-firefox-developer-tools-episode-37/)，用来审阅元素的动画效果。  
*
在网络面板中增加[安全面板](https://hacks.mozilla.org/2015/01/web-animation-tools-network-security-insights-font-inspector-improvements-and-more-firefox-developer-tools-episode-37/)。  
* 调试器面板支持 `chrome://` 和 `about://` 两种风格。  
* 在网络终端中增加对于弱加密口令的日志。

[英文发布摘要](https://www.mozilla.org/en-US/firefox/37.0beta/releasenotes/)

[全平台多语言下载](https://www.mozilla.org/en-US/firefox/beta/all/)

截至发稿时其 **Android 版本**尚未公布。
