Title: Firefox 23 Beta
Date: 2013-06-28 10:06
Author: lovenemesis
Category: Android
Tags: Firefox, Mozilla
Slug: firefox-23-beta

依照步伐，Firefox 23 Beta 发布，带来了 Linux 平台下的 Gstreamer
整合和新平整化图标。

**桌面版**变化有：

-   支持 OS X 10.7+ 版本的滚动条。
-   在 HTTPS
    页面上将[阻止混杂的非加密内容显示](https://blog.mozilla.org/security/2013/05/16/mixed-content-blocking-in-firefox-aurora/)并弹出安全警告
    。
-   改善 `about:memory` 页面的布局，更方便执行操作。
-   为 HTML5 视频回放在 Vista 以上系统中启用 DXVA2 硬件解码。
-   更新 Firefox 图标，引入平整风。
-   从首选项中移除“自动载入图片”、“启用 JavaScript” 和
    “总是显示标签页工具栏”的选项。
-   简化插件安装的消息提示框。
-   用户现在可以自由切换全局搜索引擎，而不限于搜索框。
-   CSP 策略使用标准语法，并强制符号使用。
-   为开发者引入全局浏览器终端。
-   可以开发社交共享功能。
-   实现 HTML5 `range` 输入类型。
-   使用新的 ARIA 规则可以在触屏界面上更好的实现辅助按键事件。
-   增加无前缀的 `requestAnimationFrame`
-   为控制台增加[流量监控](https://hacks.mozilla.org/2013/05/firefox-developer-tool-features-for-firefox-23/)功能，方便的指导站点载入所用流量及时间。
-   移除文字闪烁属性 `text-decoration: blink`，并移除 `blink` 标签。

尽管未在发布公告中明说，针对 [Linux 桌面的版本已经打开了 gstreamer
支持](http://www.phoronix.com/scan.php?page=news_item&px=MTM5NzU)，但默认未启用。进入
`about:config` 将 `media.gstreamer.enabled` 开启即可，享受 gstreamer
带来的包括 HTML5 视频硬件解码等功能。注意本次启用的是 gstreamer-0.10
的支持，尚未启用 gstreamer-1.0，不过目前大多数发行版都是并行安装的。

[英文发布公告](https://www.mozilla.org/firefox/23.0beta/releasenotes/)

[全语言多平台下载](https://www.mozilla.org/firefox/beta/)

**附图：**访问 [12306](https://dynamic.12306.cn/otsweb/)
时即可看到混合内容保护的提示：

[![mixed-content-protector](http://lt-file.b0.upaiyun.com/files/2013/06/mixed-content-protector-300x157.png)](http://lt-file.b0.upaiyun.com/files/2013/06/mixed-content-protector.png)

**Android 版本**变化有：

-   向下滚动页面时将动态隐藏顶部地址栏。
-   实现基本的 RSS/Atom 订阅功能，长按地址栏触发。
-   允许在无法访问阅读模式的设备上添加文章至阅读列表(?)。
-   增加可选项，允许[在地址栏中显示 URL
    而非标题](https://blog.mozilla.org/ux/2013/05/polish-all-the-things1/)。
-   用户可以指定默认搜索引擎。
-   实现切换至标签页功能。
-   为阅读模式增加衬线/无衬线字体切换。
-   长按阅读模式按钮即可将文章添加入待阅读列表。
-   初始界面将记住用户的搜索关键词。
-   CSP 策略使用标准语法，并强制符号使用。
-   使用新的 ARIA 规则可以在触屏界面上更好的实现辅助按键事件。
-   增加无前缀的 `requestAnimationFrame`
-   移除文字闪烁属性 `text-decoration: blink`，并移除 `blink` 标签。

[英文发布公告](https://www.mozilla.org/en-US/mobile/23.0beta/releasenotes/)

[移动平台下载](https://www.mozilla.org/mobile/beta/)
