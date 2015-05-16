Title: Mozilla Firefox 10
Date: 2012-02-01 09:40
Author: lovenemesis
Category: Web Browser
Tags: Firefox
Slug: mozilla-firefox-10

Mozilla 发布 Firefox 10 正式版本，带来了 **WebGL 抗锯齿**和 **CSS 3D
变换**支持。

对于**桌面用户及 Android 平台用户**来言，Firefox 10 的主要变化是提供了
[WebGL
抗锯齿功能](https://bugzilla.mozilla.org/show_bug.cgi?id=615976)，WebGL
渲染画面将更为平缓。此外桌面版本将**默认启用来自 Mozilla Add-on
站点且针对 Firefox 4
以上版本的附加组件**，而不是先前的默认禁用，改善附加组件兼容性问题。Android
原生版本为对 Flash 提供了初步支持，计划将**在下个版本切换到原生 Android
界面**。详情参考[本站先前报道](http://linuxtoy.org/archives/firefox-10-beta.html)。

对于**开发者**来言：

-   首个两位数版本号的发布，请留心[站点对于 User Agent
    的检查](http://hacks.mozilla.org/2012/01/firefox-goes-2-digit-time-to-check-your-ua-sniffing-scripts/)。
-   不能在 ECMAScript 5 Strict 模式使用
    [E4X](https://developer.mozilla.org/en/E4X)了。
-   增加了 [Page
    Visibility](https://developer.mozilla.org/en/DOM/Using_the_Page_Visibility_API)、[Full
    Screen](https://developer.mozilla.org/en/DOM/document.mozFullScreenEnabled)
    和
    [Battery](https://developer.mozilla.org/en/DOM/window.navigator.mozBattery)
    API。
-   增加了新的 [WebGL
    除错和调试工具](https://developer.mozilla.org/en/WebGL#WebGL_debugging_and_testing)，新的
    [Page
    Inspector](https://developer.mozilla.org/en/Tools/Page_Inspector)
    工具(值得推荐)。
-   移除了 --disable-rdf 和 --disable-smil 编译参数，打包者请留意

[完整开发者变化列表](https://developer.mozilla.org/en/Firefox_10_for_developers)

[桌面版本下载](http://firefox.com.cn/download/#other-download)

[移动版本下载](http://www.mozilla.org/en-US/m/)
