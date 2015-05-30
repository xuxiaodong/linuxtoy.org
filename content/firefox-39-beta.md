Title: Firefox 39 Beta
Author: lovenemesis
Date: 2015-05-30
Category: Browser
Tags: mozilla, firefox
Slug: firefox-39-beta
Status: draft
Summary: 这一次和往常不同，Mozilla 在 Firefox 38 推送稳定渠道的一周后多后，才发布 Firefox 39 的 Beta 版本，为 Linux 平台启用了恶意软件检测，同时也带来了 Win 64 位版本。

本次**桌面版本**的更新有：

* 支持 Unicode 8.0 的肤色系 Emoji 表情
* 为 OS X 及 Linux 平台启用[恶意软件侦测](https://support.mozilla.org/en-US/kb/how-does-phishing-and-malware-protection-work)
* 支持 Web 辅助特性 [ARIA 1.1](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* 移除对于不安全的 SSLv3 网络通讯的支持
* 实现[异步初始化](http://dblohm7.ca/blog/2014/06/17/asynchronous-plugin-initialization-an-introduction/)，改善 NPAPI 插件性能
* 除了临时白名单站点以外，全局禁用 RC4
* 支持 CSS 滚动快照点
* [List-style-type](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type)现在支持字符串数值
* CSS 变换及动画层级与当前标准匹配
* 实现 `<link rel="preconnect">` 类型
* 为专用及共享网络请求和 Service Workers 启用 [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* 在蒙板视图中支持拖放节点
* 允许永久性保存 Web Console 的输入历史，哪怕已经关闭了开发工具
* 对于 WebSocker 连接来说可以在离线时访问本地主机
* 改善从 IPV6 退回到 IPV4 的性能
* 通过侦测损坏的 HTTP1.1 传输的方式解决部分未完成下载被标示为完成的问题
* 修复偶尔 Firefox Hello 窗口无法打开的问题

[官方英文发布摘要](https://www.mozilla.org/en-US/firefox/39.0beta/releasenotes/)

[官方多语言全平台下载，包括 Win 64 位版本](https://www.mozilla.org/en-US/firefox/beta/all/)

本次**Android 版本**的变化有：

* 允许[粘贴 Android 系统剪切版内容到可编辑的网页内容](https://miketaylr.com/posts/2015/03/contenteditable-paste.html)中
* 支持 Web 辅助特性 [ARIA 1.1](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* 除了临时白名单站点以外，全局禁用 RC4
* 默认启用 [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* 在开发者版本默认启用[竖排文本模式](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode)
