Title: Firefox 44 Beta
Date: 2015-12-21
Author: lovenemesis
Category: Browser
Tags: firefox, mozilla
Slug: firefox-44-beta
Summary: Firefox 44 正式推送至 Beta 频道，引入 Push API，允许网页应用发送异步通知，哪怕页面已经被关闭。

**桌面版**变化有：

* 改善对于证书错误和不可信站点的错误提示
* 在不支持 MP4/H264 的系统上启用 WebM/VP9 支持
* 如果系统解码器可用的话允许开启 H264 支持
* 强化现有网页通知系统，引入 [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)，允许网页应用发送异步通知，哪怕页面已经被关闭
* 为准备在 Firefox 45 [移除的标签页组功能](https://support.mozilla.org/en-US/kb/tab-groups-removal)，并提供[迁移方案](https://addons.mozilla.org/firefox/addon/tab-groups-panorama/)
* 当 RC4 是唯一的加密措施时给出错误提示
* 不再信任 Equifax Secure 和 UTN - DATACorp SGC 颁发的 1024位根证书
* 在 Linux 平台上应用的和其他平台相同的网页字体映射机制
* 在终端中右键点击一个记录对象将会以全局变量形式保存
* 改善对于[动画的支持](http://devtoolschallenger.com/)，包括：在 Inspector 中直接以帧形式查看和修改 CSS 动画；直接修改立方贝塞尔曲线图来调整动画随着时间的变化规律；一次性[发现并抓取](https://www.youtube.com/watch?v=T2jykykN3yc)页面上的所有 CSS 动画。
* [布局和样式工具强化](http://devtoolschallenger.com/)，包括：在视图中显示尺子及各种测量工具；允许使用 CSS 滤镜实现诸如背景阴影等实时效果。
* 新的内存审查工具
* 引入 [Web Debugger API](https://hacks.mozilla.org/2015/11/developer-edition-44-creative-tools-and-more/) 和 [Service Workers API](https://developer.mozilla.org/docs/Web/API/Service_Worker_API/Using_Service_Workers)
* 新增 JSON 内置阅读器，方便无需扩展实现直观的查看、搜索复制和保存数据。

[多平台多语言下载](https://www.mozilla.org/en-US/firefox/beta/all/)

[完整英文发布公告](https://www.mozilla.org/en-US/firefox/44.0beta/releasenotes/)


**Android 版** 变化有：

* 当在隐私标签页打开系统 Intent URI 时给出提示
* 改善手机界面下标签页托盘的展示
* 显示历史搜索结果建议
* 以网页形式展示 Firefox 账户
* 在搜索时更方便的访问搜索设定
* 支持打开 MMS 协议的 URI
* 在快速搜索栏上点击将会有指向“自定义搜索提供商”的链接
* 允许使用 Android 打印服务启用云打印
* 允许用户在启动 Firefox 时设定主页面

[Play Store 官方下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox_beta&referrer=utm_source%3Dmozilla%26utm_medium%3DReferral%26utm_campaign%3Dmozilla-org)

[完整英文发布公告](https://www.mozilla.org/en-US/firefox/android/44.0beta/releasenotes/)


