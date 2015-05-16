Title: Firefox 31 Beta
Date: 2014-06-16 13:27
Author: lovenemesis
Category: Web Browser
Tags: Firefox, Mozilla
Slug: firefox-31-beta-2

在刚刚过去的(世界杯)周末(前)，Mozilla 工程师将 Firefox 31 推送至 Beta
频道，整合分代垃圾回收机制并支持 HTML5 视频字幕。

**桌面版本**的变化有：

-   为新空白标签页增加搜索框。
-   整合[分代垃圾回收机制](https://blog.mozilla.org/nnethercote/2014/03/31/generational-gc-has-landed/)，改善在部分评测中的性能。
-   OdinMonkey 将为 asm.js 风格的代码启用回溯分配器。
-   mozilla::pkix 将是默认的证书验证者。
-   在 Win 平台上若音视频 OGG 和 PDF 文件没有程序关联的话，Firefox
    将关联成为打开工具。
-   部分实现 [OpenType MATH
    表](https://developer.mozilla.org/en-US/docs/Mozilla/MathML_Project/Fonts)。
-   移除通过 `capability.policy.*` 方式指定站点权限的 CAPS
    基础架构，最显著的变化将不再能通过此方法获得剪贴板访问权限。不过
    checkloaduri 权限依然生效，提供 `file://` URI访问功能。
-   实现 HTML5 视频字幕
    [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/Web_Video_Text_Tracks_Format)
    并默认启用。
-   实现 CSS3 变量(?)
-   默认启用 `navigator.sendBeacon`。
-   新的 Array
    内建方法：[Array.prototype.fill()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)
-   新的 Object
    内建方法：[Object.setPrototypeOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
-   默认启用 CSP 1.1 nonce-source 和 hash-source。
-   通过 `onbeforeunload`
    事件生成的对话框不再阻止对浏览器其余功能的访问。
-   大量开发者工具改善：[为颜色选择器加入滴管（颜色拾取工具）](https://developer.mozilla.org/en-US/docs/Tools/Eyedropper)；[可编辑箱型模式(model)](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector#Box_model_view)；在
    Vim 和 Emacs 风格快捷键的基础上，为代码编辑器[增加 sublime
    风格快捷键](https://developer.mozilla.org/en-US/docs/tools/Keyboard_shortcuts#Source_editor)；终端增加[栈追溯](https://developer.mozilla.org/en-US/docs/Tools/Web_Console#Error_messages)功能；允许将网络请求[按照
    cURL
    格式复制](https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor#Copy_as_cURL)；终端日志支持[风格定义](https://developer.mozilla.org/en-US/docs/Tools/Web_Console#Styling_messages)；引入新的[附加组件调试工具](https://developer.mozilla.org/en-US/Add-ons/Add-on_Debugger)；引入新的
    [Canvas
    调试工具](https://hacks.mozilla.org/2014/03/introducing-the-canvas-debugger-in-firefox-developer-tools/)。

[完整英文发布公告](https://www.mozilla.org/en-US/firefox/31.0beta/releasenotes/)

[官方全平台多语言下载](https://www.mozilla.org/en-US/firefox/channel/#beta)

Android 版本的变化有：

-   在标签页同步页面支持下拉即刷新。
-   在 `about:home` 主屏幕支持重新排序已有内容面板。
-   整合[分代垃圾回收机制](https://blog.mozilla.org/nnethercote/2014/03/31/generational-gc-has-landed/)，改善在部分评测中的性能。
-   OdinMonkey 将为 asm.js 风格的代码启用回溯分配器。
-   mozilla::pkix 将是默认的证书验证者。
-   部分实现 [OpenType MATH
    表](https://developer.mozilla.org/en-US/docs/Mozilla/MathML_Project/Fonts)。
-   移除通过 `capability.policy.*` 方式指定站点权限的 CAPS
    基础架构，最显著的变化将不再能通过此方法获得剪贴板访问权限。不过
    checkloaduri 权限依然生效，提供 `file://` URI访问功能。
-   实现 [Firefox HUB
    API](https://developer.mozilla.org/en-US/Add-ons/Firefox_for_Android/Firefox_Hub_Walkthrough)（[代码样例](https://addons.mozilla.org/en-US/android/collections/leibovic/home-panels/)）。
-   实现 HTML5 视频字幕
    [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/Web_Video_Text_Tracks_Format)
    并默认启用。
-   实现 CSS3 变量(?)
-   默认启用 `navigator.sendBeacon`。
-   新的 Array
    内建方法：[Array.prototype.fill()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)
-   新的 Object
    内建方法：[Object.setPrototypeOf()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)
-   默认启用 CSP 1.1 nonce-source 和 hash-source。

[完整英文发布公告](https://www.mozilla.org/en-US/mobile/beta/notes/)

[Play Store
官方下载](https://play.google.com/store/apps/details?id=org.mozilla.firefox_beta&utm_source=mozilla&utm_medium=Referral&utm_campaign=mozilla-org)
